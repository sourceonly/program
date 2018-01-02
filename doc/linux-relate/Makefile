target:	pdf
pdf:	*tex
	./create_all.sh
	latex main
	latex main
	latex main
	dvipdfmx main
.PHONY:
clean:
	-rm -rf *log *aux *dvi *pdf *~ main.tex *toc *out
