%include	/usr/lib/rpm/macros.perl
Summary:	Silly-StringMaths perl module
Summary(pl):	Modu³ perla Silly-StringMaths
Name:		perl-Silly-StringMaths
Version:	0.13
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Silly/Silly-StringMaths-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Silly-StringMaths provides support for basic integer mathematics,
using strings rather than numbers.

%description -l pl
Silly-StringMaths umo¿liwia wykonywanie operacji matematycznych na
liczbach ca³kowitych, zamiast liczb wykorzystuj±c ³añcuchy.

%prep
%setup -q -n Silly-StringMaths-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Silly/StringMaths.pm
%{_mandir}/man3/*
