specfile=lightscreen.spec
cleanfolders=SRPMS/* SOURCES/* RPMS/* BUILD/*

all: build

build: $(specfile)
	cd ..;spectool -g -R SPECS/$(specfile)
	rpmbuild -ba $(specfile)
clean:
	cd ..;rm -rf $(cleanfolders)
