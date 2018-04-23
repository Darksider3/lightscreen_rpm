specfile=lightscreen.spec

all: build

build: $(specfile)
	cd ..;spectool -g -R SPECS/$(specfile)
	rpmbuild -ba $(specfile)
clean:
	cd ..;rm -rf SOURCES/*
