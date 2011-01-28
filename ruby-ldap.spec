Summary:	LDAP API (RFC1823) library module for Ruby
Summary(pl.UTF-8):	Moduł języka Ruby dostępu do bibliotek API LDAP (RFC1823)
Name:		ruby-ldap
Version:	0.9.10
Release:	1
License:	Redistributable
Group:		Development/Libraries
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
# Source0-md5:	99b0bad43d31d67e3c6c9605bd48c168
URL:		http://github.com/alexey-chebotar/ruby-ldap
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	openssl-devel
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby/LDAP is an extension module for Ruby. It provides the interface
to some LDAP libraries (for example, OpenLDAP, UMich LDAP, Netscape
SDK and ActiveDirectory). The common API for application development
is described in RFC1823 and most libraries comply with it. Ruby/LDAP
supports those libraries.

%description -l pl.UTF-8
Ruby/LDAP jest modułem rozszerzającym dla języka Ruby. Dostarcza on
interfejs do niektórych bibliotek LDAP (np. OpenLDAP, Netscape SDK i
ActiveDirectory). Wspólne API dla rozwoju aplikacji jest opisane w
RFC1823 i większość bibliotek go przestrzega. Ruby/LDAP wspiera te
biblioteki.

%package rdoc
Summary:	HTML documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{name}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{name}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{name}.

%package ri
Summary:	ri documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{name}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{name}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{name}.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README -o -print | xargs touch --reference %{SOURCE0}

%build
ruby extconf.rb --with-openldap2
%{__make}

rdoc --ri --op ri lib
rdoc --op rdoc lib
# rm -r ri/NOT_THIS_MODULE_RELATED_DIRS
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitelibdir=$RPM_BUILD_ROOT%{ruby_rubylibdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog FAQ NOTES README TODO test
%attr(755,root,root) %{ruby_archdir}/ldap.so
%{ruby_rubylibdir}/ldap*

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/LDAP
