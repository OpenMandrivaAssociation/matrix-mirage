%define oname mirage

Name:           matrix-mirage
Version:        0.7.0
Release:        1
Summary:        A fancy, customizable, keyboard-operable Matrix chat client written in Qt/QML + Python with nio.
License:        LGPLv3.0
Group:          Networking/Instant messaging
URL:            https://github.com/mirukana/mirage
# For now use "git clone --recursive" to download all sources and submodules. Source code not contains submodules.
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
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xscrnsaver)

BuildRequires: pkgconfig(python)
BuildRequires: python3dist(pip)
BuildRequires: pyotherside

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
BuildRequires: python3dist(blist)
BuildRequires: python3dist(cairosvg)
BuildRequires: python3dist(filetype)
BuildRequires: python3dist(html-sanitizer)
BuildRequires: python3dist(lxml)
BuildRequires: python3dist(matrix-nio)
BuildRequires: python3dist(mistune)
BuildRequires: python3dist(async-generator)
BuildRequires: python3dist(dataclasses)
BuildRequires: python3dist(pyfastcopy)
BuildRequires: python3dist(pymediainfo)
BuildRequires: pkgconfig(libmediainfo)

Requires: python3dist(pip)
Requires: pyotherside
Requires: python3dist(matrix-nio)
Requires: python3dist(python-olm)
Requires: python3dist(filetype)
Requires: python3dist(pillow)
Requires: python3dist(aiofiles)
Requires: python-atomicwrites
Requires: python3dist(appdirs)
Requires: python3dist(blist)
Requires: python3dist(cairosvg)
Requires: python3dist(filetype)
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
 
%prep
%autosetup -p1 -n %{oname}-%{version}
 
%build
%qmake_qt5 PREFIX=/usr
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/mirage
%{_datadir}/applications/mirage.desktop
%{_iconsdir}/hicolor/*x*/apps/mirage.png
