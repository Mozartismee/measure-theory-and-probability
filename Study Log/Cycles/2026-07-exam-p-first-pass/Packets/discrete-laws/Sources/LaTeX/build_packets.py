from __future__ import annotations

import io
import shutil
import subprocess
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PACKET = HERE.parents[1]
TEMP = ROOT / "tmp" / "pdfs"
OUTPUT = PACKET / "Polycopiés"

PANDOC = shutil.which("pandoc") or "/usr/local/bin/pandoc"
TECTONIC = shutil.which("tectonic") or "/opt/homebrew/bin/tectonic"


def run(command: list[str], *, cwd: Path | None = None) -> None:
    subprocess.run(command, cwd=cwd, check=True)


def normalized_markdown(source: Path, target: Path) -> Path:
    lines = source.read_text(encoding="utf-8").splitlines()
    output: list[str] = []
    math_lines: list[str] = []
    math_prefix = ""
    in_display = False

    for line in lines:
        if line.strip() == "$$":
            if not in_display:
                in_display = True
                math_prefix = line[: len(line) - len(line.lstrip())]
                math_lines = []
            else:
                body = " ".join(part.strip() for part in math_lines if part.strip())
                output.append(f"{math_prefix}$$ {body} $$")
                in_display = False
            continue
        if in_display:
            math_lines.append(line)
        else:
            output.append(line)

    if in_display:
        raise ValueError(f"Unclosed display-math block in {source}")

    target.write_text("\n".join(output) + "\n", encoding="utf-8")
    return target


def markdown_to_latex(source: Path, target: Path) -> None:
    normalized = normalized_markdown(
        source,
        TEMP / f"{source.stem}.normalized.md",
    )
    run(
        [
            PANDOC,
            "--from=gfm+tex_math_dollars",
            "--to=latex",
            "--wrap=none",
            str(normalized),
            "-o",
            str(target),
        ]
    )


def compile_tex(entry: str) -> Path:
    run(
        [
            TECTONIC,
            "--keep-logs",
            "--outdir",
            str(TEMP),
            entry,
        ],
        cwd=HERE,
    )
    return TEMP / f"{Path(entry).stem}.pdf"


def footer_overlay(page_count: int, label: str) -> PdfReader:
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, _ = A4
    for index in range(1, page_count + 1):
        pdf.setStrokeColorRGB(0.78, 0.78, 0.78)
        pdf.setLineWidth(0.35)
        pdf.line(40, 25, width - 40, 25)
        pdf.setFillColorRGB(0.28, 0.28, 0.28)
        pdf.setFont("Helvetica", 7.2)
        pdf.drawString(40, 14, label)
        pdf.drawRightString(width - 40, 14, f"p. {index} / {page_count}")
        pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return PdfReader(buffer)


def stamp(raw: Path, final: Path, label: str, title: str) -> None:
    source = PdfReader(str(raw))
    overlay = footer_overlay(len(source.pages), label)
    writer = PdfWriter()
    for page, footer in zip(source.pages, overlay.pages):
        page.merge_page(footer)
        writer.add_page(page)
    writer.add_metadata(
        {
            "/Title": title,
            "/Author": "ENS to Exam P Discrete Distribution Cycle",
            "/Subject": "Measure-theoretic discrete probability and Exam P deployment",
        }
    )
    final.parent.mkdir(parents=True, exist_ok=True)
    with final.open("wb") as handle:
        writer.write(handle)


def main() -> None:
    TEMP.mkdir(parents=True, exist_ok=True)
    OUTPUT.mkdir(parents=True, exist_ok=True)

    markdown_to_latex(PACKET / "00_Overview.md", TEMP / "discrete_overview.tex")
    markdown_to_latex(PACKET / "01_Preparatory Notes.md", TEMP / "discrete_notes.tex")
    markdown_to_latex(PACKET / "02_Feuille de travail.md", TEMP / "discrete_exercises.tex")
    markdown_to_latex(PACKET / "03_Carnet.md", TEMP / "discrete_carnet.tex")
    markdown_to_latex(PACKET / "04_Corrigé.md", TEMP / "discrete_solutions.tex")

    student_raw = compile_tex("main.tex")
    solutions_raw = compile_tex("solutions_main.tex")

    stamp(
        student_raw,
        OUTPUT / "Student Handout.pdf",
        "Discrete Distributions - Student Packet",
        "Discrete Distributions - One-Week Student Packet",
    )
    stamp(
        solutions_raw,
        OUTPUT / "Independent Corrigé.pdf",
        "Discrete Distributions - Corrige",
        "Discrete Distributions - One-Week Corrige",
    )


if __name__ == "__main__":
    main()
