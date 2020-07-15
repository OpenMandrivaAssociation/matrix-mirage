%define oname mirage

Name:           matrix-mirage
Version:        0.5.2
Release:        1
Summary:        A fancy, customizable, keyboard-operable Matrix chat client written in Qt/QML + Python with nio.
License:        LGPLv3.0
URL:            https://github.com/mirukana/mirage
Source0:        https://github.com/mirukana/mirage/archive/v%{version}/%{oname}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: qt5-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5QuickWidgets)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: qt5-qtgraphicaleffects
BuildRequires: qt5-qtimageformats

BuildRequires: pkgconfig(python)
BuildRequires: python3dist(pip)
BuildRequires: pyotherside
# In unsupported repo for now, so disable it
#BuildRequires: pkgconfig(libmediainfo)

BuildRequires: cmake(Olm)
BuildRequires: python3dist(python-olm)
BuildRequires: python-pillow-devel
BuildRequires: python3dist(pillow)
BuildRequires: pkgconfig(libturbojpeg)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(libopenjp2)
BuildRequires: python3dist(aiofiles)
BuildRequires: python3dist(appdirs)
#python3dist(blist)
BuildRequires: python3dist(cairosvg)
#python3dist(filetype)
#python-html-sanitizer
BuildRequires: python3.8dist(lxml)
BuildRequires: python3dist(matrix-nio)
BuildRequires: python3dist(mistune)
#python3dist(pymediainfo)
#python3dist(async-generator)
#python3-dataclasses
#python-pyfastcopy

Requires: python3dist(matrix-nio)
Requires: python3dist(python-olm)


%description
A fancy, customizable, keyboard-operable Matrix chat client for encrypted and decentralized communication.
Written in Qt/QML + Python with nio.
 
%prep
%autosetup -p1 -n %{oname}-%{version}
 
%build
#%qmake_qt5 PREFIX=/usr
%qmake_qt5
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
