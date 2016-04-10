# .tex and .pdf files
TEXFILES=$(wildcard lab[0-9]*.tex) $(wildcard final_*.tex)
PDFFILES=$(TEXFILES:.tex=.pdf)

# three arguments to pdflatex:
# minted package (syntax highlighter) needs
# do not stop to show errors
# print where errors are found
PDFLATEX_ARGS=-shell-escape -interaction nonstopmode -file-line-error

all: $(PDFFILES)

# compile PDFs
# run LaTeX twice in order to get cross referencing content like the TOC
$(PDFFILES): $(TEXFILES)
	@echo Compiling lab to PDF.
	# dashes are Makefile syntax used to ignore non-zero exit codes
	- pdflatex $(PDFLATEX_ARGS) $(basename $@)
	- pdflatex $(PDFLATEX_ARGS) $(basename $@)

# remove supplementary LaTeX files
clean: .FORCE
	rm -rf _minted-*
	rm -f *.aux *.log *.loe *.toc

.FORCE:
