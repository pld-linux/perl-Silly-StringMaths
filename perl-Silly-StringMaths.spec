#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Silly
%define		pnam	StringMaths
Summary:	Silly::StringMaths Perl module
Summary(cs):	Modul Silly::StringMaths pro Perl
Summary(da):	Perlmodul Silly::StringMaths
Summary(de):	Silly::StringMaths Perl Modul
Summary(es):	Módulo de Perl Silly::StringMaths
Summary(fr):	Module Perl Silly::StringMaths
Summary(it):	Modulo di Perl Silly::StringMaths
Summary(ja):	Silly::StringMaths Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Silly::StringMaths ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Silly::StringMaths
Summary(pl):	Modu³ Perla Silly::StringMaths
Summary(pt):	Módulo de Perl Silly::StringMaths
Summary(pt_BR):	Módulo Perl Silly::StringMaths
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Silly::StringMaths
Summary(sv):	Silly::StringMaths Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Silly::StringMaths
Summary(zh_CN):	Silly::StringMaths Perl Ä£¿é
Name:		perl-Silly-StringMaths
Version:	0.13
Release:	10
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2b3404284cdf68664ad8027aa223aad8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Silly::StringMaths provides support for basic integer mathematics,
using strings rather than numbers.

%description -l pl
Silly::StringMaths umo¿liwia wykonywanie operacji matematycznych na
liczbach ca³kowitych, zamiast liczb wykorzystuj±c ³añcuchy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Silly
%{_mandir}/man3/*
