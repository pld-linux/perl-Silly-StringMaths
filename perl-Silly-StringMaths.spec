#
# Conditional build:
%bcond_without	tests	# don't perform "make test"

%define		pdir	Silly
%define		pnam	StringMaths
%include	/usr/lib/rpm/macros.perl
Summary:	Silly::StringMaths Perl module
Summary(cs.UTF-8):	Modul Silly::StringMaths pro Perl
Summary(da.UTF-8):	Perlmodul Silly::StringMaths
Summary(de.UTF-8):	Silly::StringMaths Perl Modul
Summary(es.UTF-8):	Módulo de Perl Silly::StringMaths
Summary(fr.UTF-8):	Module Perl Silly::StringMaths
Summary(it.UTF-8):	Modulo di Perl Silly::StringMaths
Summary(ja.UTF-8):	Silly::StringMaths Perl モジュール
Summary(ko.UTF-8):	Silly::StringMaths 펄 모줄
Summary(nb.UTF-8):	Perlmodul Silly::StringMaths
Summary(pl.UTF-8):	Moduł Perla Silly::StringMaths
Summary(pt.UTF-8):	Módulo de Perl Silly::StringMaths
Summary(pt_BR.UTF-8):	Módulo Perl Silly::StringMaths
Summary(ru.UTF-8):	Модуль для Perl Silly::StringMaths
Summary(sv.UTF-8):	Silly::StringMaths Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Silly::StringMaths
Summary(zh_CN.UTF-8):	Silly::StringMaths Perl 模块
Name:		perl-Silly-StringMaths
Version:	0.13
Release:	12
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2b3404284cdf68664ad8027aa223aad8
URL:		http://search.cpan.org/dist/Silly-StringMaths/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Silly::StringMaths provides support for basic integer mathematics,
using strings rather than numbers.

%description -l pl.UTF-8
Silly::StringMaths umożliwia wykonywanie operacji matematycznych na
liczbach całkowitych, zamiast liczb wykorzystując łańcuchy.

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
