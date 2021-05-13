#!/bin/bash
set -e

MAINTEX="main"
default="light"
target=${1:-$default}

GREEN='\033[0;32m'
NC='\033[0m' # No Color

if [ "$target" = "all" ]; then
	if [ -e "out.bak" ]; then
		rm -R out/*
	else
		mv out out.bak
		mkdir out
	fi
	pdflatex -halt-on-error -output-directory out "$MAINTEX".tex
	bibtex "out/$MAINTEX"
	cd out
	makeglossaries "$MAINTEX"
	pythontex --interpreter python:python3 "$MAINTEX"
	cd -
	pdflatex -halt-on-error -output-directory out "$MAINTEX".tex
	pdflatex -halt-on-error -output-directory out "$MAINTEX".tex
elif [ "$target" = "light" ]; then
	pdflatex -halt-on-error -output-directory out "$MAINTEX".tex
fi

cp -pv out/"$MAINTEX".pdf .
echo -e "${GREEN}success${NC}"