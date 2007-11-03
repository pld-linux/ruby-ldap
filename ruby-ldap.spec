Summary:	LDAP API (RFC1823) library module for Ruby
Summary(pl.UTF-8):	Moduł języka Ruby dostępu do bibliotek API LDAP (RFC1823)
Name:		ruby-ldap
Version:	0.9.7
Release:	1
License:	Redistributable
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/ruby-ldap/%{name}-%{version}.tar.gz
# Source0-md5:	373d07cb833fac6d907652f7c8ac7480
URL:		http://ruby-ldap.sourceforge.net/
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	openssl-devel
BuildRequires:	ruby
BuildRequires:	ruby-devel
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

%prep
%setup -q

%build
ruby extconf.rb --with-openldap2
%{__make}

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitelibdir=$RPM_BUILD_ROOT%{ruby_rubylibdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

%files
%defattr(644,root,root,755)
%doc ChangeLog FAQ README* TODO
%doc example/ test/
%attr(755,root,root) %{ruby_archdir}/ldap.so
%{ruby_rubylibdir}/ldap*
