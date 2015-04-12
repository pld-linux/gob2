Summary:	GOB2, The GObject Builder
Summary(pl.UTF-8):	GOB2 - budowniczy obiektów GObject
Name:		gob2
Version:	2.0.20
Release:	2
License:	GPL v2+
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gob2/2.0/%{name}-%{version}.tar.xz
# Source0-md5:	b97b5656362100f30755d09880f94608
URL:		http://www.jirka.org/gob.html
BuildRequires:	flex
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GOB is a simple preprocessor for making GObject objects (glib
objects). It makes objects from a single file which has inline C code
so that you don't have to edit the generated files. Syntax is somewhat
inspired by Java and yacc. It supports generating C++ code.

%description -l pl.UTF-8
GOB jest prostym preprocesorem służącym do tworzenia obiektów GObject
(obiektów glib). Tworzy obiekty z pojedynczego pliku zawierającego
wbudowany kod C, dzięki czemu nie trzeba modyfikować wygenerowanych
plików. Składnia jest do pewnego stopnia inspirowana Javą i yaccem.
Obsługuje generowanie kodu C++.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.generated-code ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gob2
%{_mandir}/man1/gob2.1*
%{_aclocaldir}/gob2.m4
%{_examplesdir}/%{name}-%{version}
