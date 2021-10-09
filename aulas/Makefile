%.pdf: %.md
	pandoc -s -t beamer  $^ -o $@
	git commit -am"Modifiquei o ficheiro $^"
	git push
