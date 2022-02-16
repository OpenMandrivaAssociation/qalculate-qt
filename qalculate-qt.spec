%define bname qalculate

# ignore debugsource list
%global _empty_manifest_terminate_build 0

Summary:	A very versatile desktop calculator
Name:		%{bname}-qt
Version:	4.0.0
Release:	1
License:	GPLv2+
Group:		Office
Url:		https://qalculate.github.io/
Source0:	https://github.com/Qalculate/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	desktop-file-utils
BuildRequires:	gmp-devel
BuildRequires:	glibc-devel
BuildRequires:	intltool
BuildRequires:	imagemagick
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libqalculate)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(mpfr)
BuildRequires:	qmake5
BuildRequires:	qt5-linguist-tools
Requires:	gnuplot

%description
Qalculate! is a multi-purpose desktop calculator for GNU/Linux. It is small
and simple to use but with much power and versatility underneath

Features include customizable functions, units, arbitrary precision,
plotting, and a user-friendly interface.

This package provides the Qt frontend.

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*/apps/%{name}.{svg,png}
%{_mandir}/man1/%{name}.1.*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%qmake_qt5 \
	PREFIX=%{buildroot}%{_prefix}
%make_build

%install
%make_install

# locales
%find_lang %{name} --with-qt

