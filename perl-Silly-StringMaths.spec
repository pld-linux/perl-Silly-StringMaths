%include	/usr/lib/rpm/macros.perl
Summary:	Silly-StringMaths perl module
Summary(pl):	Modu³ perla Silly-StringMaths
Name:		perl-Silly-StringMaths
Version:	0.13
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Silly/Silly-StringMaths-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
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

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Silly/StringMaths
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Silly/StringMaths.pm
%{perl_sitearch}/auto/Silly/StringMaths

%{_mandir}/man3/*
