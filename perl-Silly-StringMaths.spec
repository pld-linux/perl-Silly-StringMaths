%include	/usr/lib/rpm/macros.perl
%define	pdir	Silly
%define	pnam	StringMaths
Summary:	Silly::StringMaths perl module
Summary(pl):	Moduł perla Silly::StringMaths
Name:		perl-Silly-StringMaths
Version:	0.13
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Silly::StringMaths provides support for basic integer mathematics,
using strings rather than numbers.

%description -l pl
Silly::StringMaths umożliwia wykonywanie operacji matematycznych na
liczbach całkowitych, zamiast liczb wykorzystując łańcuchy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
