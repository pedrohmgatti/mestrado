pdflatex main.tex

# bibtex main.aux

pdflatex main.tex

pdflatex main.tex

mv main.pdf relatorio_atividade1.pdf 

rm *.aux *.log *.out *.toc *.bbl *.blg *.fdb_latexmk *.fls *.synctex.gz
