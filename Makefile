filename-doc=doc
filename-beamer=presentation
directory-doc=doc/
directory-beamer=beamer/

.PHONY: all doc beamer clean

all: doc beamer

doc:
	cd ${directory-doc} && latexmk -pdf -xelatex -use-make ${filename-doc}.tex

beamer:
	cd ${directory-beamer} && latexmk -pdf -xelatex -shell-escape -use-make ${filename-beamer}.tex

clean:
	cd ${directory-doc} && latexmk -c
	cd ${directory-beamer} && latexmk -c
	rm -f ${directory-doc}${filename-doc}.{ps,log,aux,out,dvi,bbl,blg,toc,fls,fdb_latexmk}
	rm -f ${directory-beamer}${filename-beamer}.{ps,log,aux,out,dvi,bbl,blg,toc,fls,fdb_latexmk,nav,snm,vrb}
	rm -rf **/*.{ps,log,aux,out,dvi,bbl,blg,toc,fls,fdb_latexmk,nav,snm,vrb}
