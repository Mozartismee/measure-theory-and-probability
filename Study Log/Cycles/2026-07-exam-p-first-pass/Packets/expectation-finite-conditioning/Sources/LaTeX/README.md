# LaTeX Sources

The directory contains two independent, self-contained editions of the 17–19 July module. No external course file, image, bibliography, or style file is required.

## Student edition

Compile from this directory:

```text
pdflatex main.tex
```

`main.tex` assembles the plan, notes, exercises, and Carnet. It does not load the solutions.

## Corrigé

Compile separately:

```text
pdflatex solutions_main.tex
```

The exercise numbering agrees with the student edition. Attempt and corrigé must remain separate.

## Printed copies

- [Student Handout](../../Polycopiés/Student%20Handout.pdf)
- [Independent Corrigé](../../Polycopiés/Independent%20Corrigé.pdf)
- [Overleaf Sources](../../Polycopiés/Overleaf%20Sources.zip)

Both entry points are intended for pdfLaTeX and have also been verified with Tectonic/XeTeX. The page is A4, compact, unnumbered, and set in Latin Modern. The deployment exercises are original mechanism-equivalent problems; Q50, Q386, and Q370 are structural anchors only.

The packet is self-contained for the 17–19 July cycle. The Hahn-first proof of Radon–Nikodym and general conditional kernels remain deferred.
