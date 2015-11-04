filename-doc=doc
filename-beamer=presentation
directory-doc=p-doc/
directory-beamer=p-beamer/

.PHONY: all doc beamer clean

all: doc beamer

doc:
	cd ${directory-doc} && latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make ${filename-doc}.tex

beamer:
	cd ${directory-beamer} && latexmk -pdf -xelatex -shell-escape -use-make ${filename-beamer}.tex

clean:
	rm -f ${directory-doc}${filename-doc}.{ps,log,aux,out,dvi,bbl,blg,toc,fls,fdb_latexmk}
	rm -f ${directory-beamer}${filename-beamer}.{ps,log,aux,out,dvi,bbl,blg,toc,fls,fdb_latexmk,nav,snm,vrb}
