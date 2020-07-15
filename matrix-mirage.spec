%define oname mirage

Name:           matrix-mirage
Version:        0.5.2
Release:        1
Summary:        A fancy, customizable, keyboard-operable Matrix chat client written in Qt/QML + Python with nio.
License:        LGPLv3.0
URL:            https://github.com/mirukana/mirage
Source0:        https://github.com/mirukana/mirage/archive/v%{version}/%{oname}-%{version}.tar.gz

BuildRequires: qmake5
BuildRequires: qt5-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5QuickWidgets)

BuildRequires: pkgconfig(python)
BuildRequires: pyotherside
BuildRequires: cmake(Olm)
BuildRequires: python-pillow-devel
BuildRequires: python3dist(pillow)
python3dist(aiofiles)
python3dist(appdirs)
#python3dist(blist)
python3dist(cairosvg)
#python3dist(filetype)
#python-html-sanitizer
python3.8dist(lxml)
#python-matrix-nio
python3dist(mistune)



%description
A fancy, customizable, keyboard-operable Matrix chat client for encrypted and decentralized communication.
Written in Qt/QML + Python with nio.
 
%prep
%autosetup -p1 -n %{oname}-%{version}
 
%build
%qmake_qt5 PREFIX=/usr
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
