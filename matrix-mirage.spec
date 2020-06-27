%define oname mirage

Name:           matrix-mirage
Version:        0.5.2
Release:        1
Summary:        A fancy, customizable, keyboard-operable Matrix chat client written in Qt/QML + Python with nio.
License:        LGPLv3.0
URL:            https://github.com/mirukana/mirage
Source0:        https://github.com/mirukana/mirage/archive/v%{version}/%{oname}-%{version}.tar.gz

BuildRequires: qt5-devel
BuildRequires: qt5-qtbase-devel


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
