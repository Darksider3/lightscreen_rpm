# lightscreen_rpm
![build](https://copr.fedorainfracloud.org/coprs/darksider3/lightscreen/package/Lightscreen/status_image/last_build.png)

(S)RPM Package for [Lightscreen](https://github.com/ckaiser/Lightscreen)

## How to install
just add the copr to your `dnf`:
```
dnf copr enable darksider3/lightscreen
```


## How to build?
It's pretty basic. Install every required devel package:

```
sudo dnf -y qt5-qtbase-devel qt5-qtdeclarative-devel \
qt5-qtxmlpatterns-devel qt5-qtmultimedia-devel qt5-qtx11extras-devel \
make cmake dos2unix \
xcb-util-keysyms-devel desktop-file-utils rpmbuild spectool
```

And create the Build-Tree:

```
rpmdev-setuptree
```

Change to it, and then to it's SPECS directory:

```
cd ~/rpmbuild/SPECS
```

get this git repository:

```
git clone https://github.com/Darksider3/lightscreen_rpm.git .
```

... and build it!


```
make
```

Afterwards you will find your rpm-File under `rpmbuild/RPMS/$(Architectur)/lightscreen-$(Version).rpm`
