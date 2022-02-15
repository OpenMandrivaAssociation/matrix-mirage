%define oname mirage

Summary:	A fancy, customizable, keyboard-operable Matrix chat client written in Qt/QML + Python with nio
Name:		matrix-%{oname}
Version:	0.7.2
Release:	1
License:	LGPLv3.0
Group:		Networking/Instant messaging
URL:		https://github.com/mirukana/mirage
Source0:	https://github.com/mirukana/mirage/archive/v%{version}/%{oname}-%{version}.tar.gz
# (debian)
Patch0:		2003_rename_app.patch
Patch1:		2006_avoid_simpleaudio.patch

BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	qt5-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtdeclarative
BuildRequires:	qt5-qtgraphicaleffects
BuildRequires:	qt5-qtimageformats
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libmediainfo)
BuildRequires:	pkgconfig(libopenjp2)
BuildRequires:	pkgconfig(libturbojpeg)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(aiofiles)
BuildRequires:	python3dist(appdirs)
BuildRequires:	python3dist(async-generator)
BuildRequires:	python3dist(blist)
BuildRequires:	python3dist(cairosvg)
BuildRequires:	python3dist(dataclasses)
BuildRequires:	python3dist(dbus-python)
BuildRequires:	python3dist(pyfastcopy)
BuildRequires:	python3dist(filetype)
BuildRequires:	python3dist(hsluv)
BuildRequires:	python3dist(html-sanitizer)
BuildRequires:	python3dist(lxml)
BuildRequires:	python3dist(matrix-nio)
BuildRequires:	python3dist(mistune)
BuildRequires:	python3dist(pillow)
BuildRequires:	python3dist(plyer)
BuildRequires:	python3dist(pymediainfo)
BuildRequires:	python3dist(pycryptodome)
##BuildRequires: python3dist(python-olm)
BuildRequires:	 python3dist(redbaron)
#BuildRequires:	python3dist(simpleaudio)
BuildRequires:	python3dist(sortedcontainers)
BuildRequires:	 python3dist(watchgod)
BuildRequires:	pkgconfig(olm)
##BuildRequires: pkgconfig(Qt5Qml)
##BuildRequires: pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5QuickControls2)
##BuildRequires: pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5Svg)
##BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pyotherside

Requires: pyotherside
Requires: python3dist(pip)
Requires: python3dist(matrix-nio)
Requires: python3dist(python-olm)
Requires: python3dist(filetype)
Requires: python3dist(pillow)
Requires: python3dist(aiofiles)
Requires: python-atomicwrites
Requires: python3dist(appdirs)
Requires: python3dist(blist)
Requires: python3dist(cairosvg)
Requires: python3dist(html-sanitizer)
Requires: python3dist(lxml)
Requires: python3dist(matrix-nio)
Requires: python3dist(mistune)
Requires: python3dist(async-generator)
Requires: python3dist(dataclasses)
Requires: python3dist(pyfastcopy)
Requires: python3dist(pymediainfo)

%description
A fancy, customizable, keyboard-operable Matrix chat client for encrypted and decentralized communication.
Written in Qt/QML + Python with nio.
 
%files
%{_bindir}/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/examples/%{oname}/settings.py
%{_iconsdir}/hicolor/*x*/apps/%{oname}.png

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}
 
%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

