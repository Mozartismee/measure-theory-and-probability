# Offline LaTeX compilation

Keep every file in this directory at the same level. No external course file, web page, image, bibliography, or custom style file is required.

## Student handout

Compile `main.tex` with pdfLaTeX:

```text
pdflatex main.tex
```

The student handout contains the three-session plan, self-contained lecture notes, exercises, and work record. It does not load or contain the solutions file.

## Independent solutions

Compile `solutions_main.tex` with pdfLaTeX:

```text
pdflatex solutions_main.tex
```

This produces a separate solution document whose exercise numbering matches the student handout.

Both entry points have also been compile-verified with Tectonic/XeTeX. The source is ASCII-clean and remains intended for ordinary pdfLaTeX compilation as specified above.

## File roles

- `01_session_plan.tex`: three-session schedule and completion contract.
- `02_lecture_notes.tex`: all theory and proof interfaces required by the packet.
- `03_exercises.tex`: Exercises 0--5 and closed-book reconstruction.
- `04_work_record.tex`: rupture record and representation ledger.
- `05_solutions.tex`: complete independent solutions.
- `main.tex`: student entry point.
- `solutions_main.tex`: solution entry point.

## Format and boundary

Both documents use the 14 July packet as their typographic reference: Latin Modern text and mathematics, A4 geometry with 14 mm left/right margins, 12 mm top and 14 mm bottom margins, and approximately 9.8 pt text with 11.8 pt leading. Paragraph spacing is 0.36 em; section spacing is 1.0 em above and 0.36 em below; display spacing is 6 pt, reduced to 4 pt for short displays. Lists and tables remain compact without reducing ledger text below footnote size.

Microtypographic protrusion is enabled for every supported engine; font expansion is additionally enabled under pdfLaTeX and disabled under XeTeX, where it is unsupported. Widow, orphan, display-widow, and cross-page hyphen controls are strict. Standard LaTeX section penalties preserve heading attachment without forcing the excessive white space produced by blanket section-level page reservations; packet titles alone reserve five following baselines. The documents use no headers or page numbers. Ordinary A4 printing is intended; borderless printing is neither required nor desirable.

The three deployment problems in Exercise 5 are original mechanism-equivalent exercises. The labels Q50, Q386, and Q370 are structural anchors only; no official problem statement is reproduced.

The packet is self-contained for the 17--19 July study cycle. The full Hahn-first proof of Radon--Nikodym and general conditional kernels or densities remain explicit deferred proof debts.
