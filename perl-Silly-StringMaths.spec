%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Silly-StringMaths perl module
Summary(pl):	Modu³ perla Silly-StringMaths
Name:		perl-Silly-StringMaths
Version:	0.13
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Silly/Silly-StringMaths-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Silly-StringMaths provides support for basic integer mathematics, using 
strings rather than numbers. 

%description -l pl
Silly-StringMaths umo¿liwia wykonywanie operacji matematycznych na liczbach
ca³kowitych, zamiast liczb wykorzystuj±c ³añcuchy.

%prep
%setup -q -n Silly-StringMaths-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

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
