# Overleaf compilation

Upload every file in this directory to one Overleaf project.

## Student handout

1. Choose **main.tex** as the main document.
2. Select **pdfLaTeX**.
3. Compile.

The handout contains the notes, exercises, and compact work record. It does not contain solutions.

## Independent solutions

1. Choose **solutions_main.tex** as the main document.
2. Select **pdfLaTeX**.
3. Compile again.

This produces a separate solution document containing complete solutions to every exercise.

Both documents use approximately 9.8 pt text with 11.8 pt leading, restrained mathematical spacing, no forced page breaks between sections, and no headers or page numbers. The A4 margins are 14 mm on the left and right, 12 mm at the top, and 14 mm at the bottom: compact lecture-note geometry, not full-bleed typesetting.

The optional course extract is stored in **03_lp_cours_extract.tex** and omitted from the student handout by default. To include it, replace

    \printcoursfalse

with

    \printcourstrue

in **main.tex**.

Ordinary A4 printing is intended. Borderless printer mode is neither required nor desirable.
