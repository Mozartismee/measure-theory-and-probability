# Preparing the polycopié

The Markdown files two directories above are the mathematical source of truth. These files only assemble the printable student handout and independent Corrigé.

- `main.tex` builds the student packet.
- `solutions_main.tex` builds the independent corrigé.
- `build_packets.py` converts the five canonical Markdown files to temporary LaTeX fragments, compiles both entry points, then uses ReportLab and pypdf to add stable page labels.
- Temporary fragments and raw PDFs are written under `tmp/pdfs/`.
- Final PDFs are written under the module's `Polycopiés/` directory.

The build must be run from the repository environment with Pandoc, Tectonic, ReportLab and pypdf available. No official SOA problem statement is embedded in either PDF.
