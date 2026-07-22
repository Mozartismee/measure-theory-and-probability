# Typesetting the polycopié

The five Markdown texts in the module directory are the reference texts. These LaTeX files provide an A4 polycopié and an independent Corrigé.

## Polycopié

1. Upload every file in this directory to one Overleaf project.
2. Choose **main.tex** as the main document.
3. Select pdfLaTeX and compile.

The polycopié contains the preparatory notes, the Feuille de travail, and the Carnet. It does not contain the Corrigé.

## Corrigé

1. In the same project, choose **solutions_main.tex** as the main document.
2. Compile with pdfLaTeX.

The result is a separate correction booklet.

The optional course extract is **03_lp_cours_extract.tex**. To include it in the polycopié, replace

    \printcoursfalse

with

    \printcourstrue

in **main.tex**.

The text is set at approximately 9.8 pt with 11.8 pt leading. The A4 margins are 14 mm on the left and right, 12 mm at the top, and 14 mm at the bottom. Ordinary A4 printing is intended; borderless mode is unnecessary.

The portable archive is [Overleaf Sources.zip](../../Polycopiés/Overleaf%20Sources.zip).
