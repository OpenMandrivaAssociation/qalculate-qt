%define bname qalculate

# qmake doesn't like debugsource
%undefine _debugsource_packages

Summary:	A very versatile desktop calculator
Name:		%{bname}-qt
Version:	5.8.0
Release:	1
License:	GPLv2+
Group:		Office
Url:		https://qalculate.github.io/
Source0:	https://github.com/Qalculate/qalculate-qt/releases/download/v%{version}/qalculate-qt-%{version}.tar.gz
BuildRequires:	desktop-file-utils
BuildRequires:	gmp-devel
BuildRequires:	glibc-devel
BuildRequires:	intltool
BuildRequires:	imagemagick
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libqalculate)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(mpfr)
BuildRequires:	qmake-qt6
BuildRequires:	qt6-qttools-linguist-tools
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
%{_datadir}/metainfo/io.github.Qalculate.qalculate-qt.metainfo.xml
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*/apps/%{name}.{svg,png}
%{_mandir}/man1/%{name}.1.*

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%{_qtdir}/bin/qmake \
	PREFIX=%{buildroot}%{_prefix}

%build
%make_build

%install
%make_install

# locales
%find_lang %{name} --with-qt
