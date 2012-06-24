Summary:	GOB2, The GObject Builder
Summary(pl):	GOB2, Budowniczy obiekt�w GObject
Name:		gob2
Version:	2.0.6
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://ftp.5z.com/pub/gob/%{name}-%{version}.tar.bz2
# Source0-md5:	ada2db09f3740858376429b5c7e98ada
URL:		http://www.5z.com/jirka/gob.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GOB is a simple preprocessor for making GObject objects (glib
objects). It makes objects from a single file which has inline C code
so that you don't have to edit the generated files. Syntax is somewhat
inspired by Java and yacc. It supports generating C++ code.

%description -l pl
GOB jest prostym preprocesorem s�u��cym do tworzenia obiekt�r GObject
(obiekt�w glib). Tworzy obiekty z pojedynczego pliku zawieraj�cego
wbudowany kod C, dzi�ki czemu nie trzeba modyfikowa� wygenerowanych
plik�w. Sk�adnia jest do pewnego stopnia inspirowana Jav� i yaccem.
Obs�uguje generowanie kodu C++.

%prep
%setup -q

%build
%configure

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
%doc README AUTHORS NEWS TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_aclocaldir}/*
%{_examplesdir}/%{name}-%{version}
