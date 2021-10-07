%.pdf: %.md
	pandoc -s -t beamer  $^ -o $@
	git commit -am"Modifiquei o ficheiro $^"
	git push
	cp $@ ../aasb2122.github.io
	(cd ../aasb2122.github.io; git commit -am"Modifiquei o ficheiro $@"; git push)

index.html: pagina.md
	pandoc -s $^ -o $@
	git commit -am"Modifiquei o ficheiro $^"
	git push
	cp $@ ../aasb2122.github.io
	(cd ../aasb2122.github.io; git commit -am"Modifiquei o ficheiro $@"; git push)
