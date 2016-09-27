


all:doc

doc:
	pdflatex  template
	pdflatex  template
	pdflatex  template

view:	doc
	okular template.pdf

.PHONY:
cleanall:
	-rm -rf *.aux *.log *.tex~ *.pdf *out
clean:
	-rm -rf *.aux *.log *.tex~ *out
