
Summary:	GOB2, The GObject Builder
Name:		gob2
Version:	2.0.4
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.0/%{name}-%{version}.tar.bz2
URL:		http://www.5z.com/jirka/linux.html#gob
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GOB is a simple preprocessor for making GObject objects (glib
objects). It makes objects from a single file which has inline C code
so that you don't have to edit the generated files. Syntax is somewhat
inspired by java and yacc. It supports generating C++ code

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS COPYING NEWS TODO ChangeLog
%doc examples
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*
%{_aclocaldir}/*
