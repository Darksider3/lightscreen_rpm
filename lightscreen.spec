Name: lightscreen
Version: 2.4.git7782bd5
Release: 1%{?dist}
Summary: Simple tool to automate the tedious process of saving and cataloging screenshots
URL: https://lightscreen.com.ar/
License: GPLv2

Source0: https://github.com/ckaiser/Lightscreen/archive/7782bd5d68a0c14b06873d3a04929816e337c8a3.zip
Source1: https://github.com/ckaiser/UGlobalHotkey/archive/231b10144741b29037f0128bb7a1cd7176529f74.zip
Source2: https://github.com/ckaiser/SingleApplication/archive/c6378eec45a5fdf699b4d27fb4be22a190b2a184.zip
Source3: https://gist.github.com/Darksider3/6db935d8a54f67061f0841add8f392b9/archive/6feb4628124f90f197886623c56278a1ab11ab91.zip

BuildRequires: qt5-qtbase-devel qt5-qtdeclarative-devel qt5-qtxmlpatterns-devel qt5-qtmultimedia-devel qt5-qtx11extras-devel
BuildRequires: make cmake
Requires: qt5-qtbase qt5-qtdeclarative qt5-qtxmlpatterns qt5-qtmultimedia qt5-qtx11extras

%description
Lightscreen is a simple tool to automate the tedious process of saving and cataloging screenshots.

%prep
	cd %_sourcedir
	unzip "6feb4628124f90f197886623c56278a1ab11ab91.zip"
	unzip "7782bd5d68a0c14b06873d3a04929816e337c8a3.zip"
	unzip "231b10144741b29037f0128bb7a1cd7176529f74.zip"
	unzip "c6378eec45a5fdf699b4d27fb4be22a190b2a184.zip"
	cp -r Lightscreen-7782bd5d68a0c14b06873d3a04929816e337c8a3 %{_builddir}
	cp UGlobalHotkey-231b10144741b29037f0128bb7a1cd7176529f74/* "%{_builddir}"/"Lightscreen-7782bd5d68a0c14b06873d3a04929816e337c8a3/tools/UGlobalHotkey"
	cp SingleApplication-c6378eec45a5fdf699b4d27fb4be22a190b2a184/* "%{_builddir}"/"Lightscreen-7782bd5d68a0c14b06873d3a04929816e337c8a3/tools/SingleApplication"
	cd "%{_builddir}"/"Lightscreen-7782bd5d68a0c14b06873d3a04929816e337c8a3"

%build
	cd "%{_builddir}/Lightscreen-7782bd5d68a0c14b06873d3a04929816e337c8a3"
	cp "%{_sourcedir}/6db935d8a54f67061f0841add8f392b9-6feb4628124f90f197886623c56278a1ab11ab91/undef_success_x11.patch" "%{_builddir}/Lightscreen-7782bd5d68a0c14b06873d3a04929816e337c8a3/tools/"
	cd tools
	unix2dos undef_success_x11.patch
	patch --ignore-whitespace --binary screenshot.cpp < undef_success_x11.patch
	cd "%{_builddir}/Lightscreen-7782bd5d68a0c14b06873d3a04929816e337c8a3"
	qmake-qt5
	make

%install
	mkdir -p %{buildroot}/%{_bindir}
	mkdir -p %{buildroot}/usr/share/pixmaps
	install -p -m 0755 "%{_builddir}/Lightscreen-7782bd5d68a0c14b06873d3a04929816e337c8a3/lightscreen" "%{buildroot}/%{_bindir}/lightscreen"
	install -p -m 0775 "%{_builddir}/Lightscreen-7782bd5d68a0c14b06873d3a04929816e337c8a3/images/LS.ico" "%{buildroot}/usr/share/pixmaps/lightscreen.ico"
	#install -Dm775 "%{_builddir}/lightscreen.desktop" "%{buildroot}/usr/share/applications/lightscreen.desktop"

%files
	/usr/bin/lightscreen
	/usr/share/pixmaps/lightscreen.ico
%changelog
* Sun Apr 22 2018 darksider3 <github@darksider3.de> - 2.4.git-1
- initial package release
