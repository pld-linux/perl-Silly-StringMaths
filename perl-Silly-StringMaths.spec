%include	/usr/lib/rpm/macros.perl
%define		pdir	Silly
%define		pnam	StringMaths
Summary:	Silly::StringMaths Perl module
Summary(cs):	Modul Silly::StringMaths pro Perl
Summary(da):	Perlmodul Silly::StringMaths
Summary(de):	Silly::StringMaths Perl Modul
Summary(es):	M�dulo de Perl Silly::StringMaths
Summary(fr):	Module Perl Silly::StringMaths
Summary(it):	Modulo di Perl Silly::StringMaths
Summary(ja):	Silly::StringMaths Perl �⥸�塼��
Summary(ko):	Silly::StringMaths �� ����
Summary(no):	Perlmodul Silly::StringMaths
Summary(pl):	Modu� Perla Silly::StringMaths
Summary(pt):	M�dulo de Perl Silly::StringMaths
Summary(pt_BR):	M�dulo Perl Silly::StringMaths
Summary(ru):	������ ��� Perl Silly::StringMaths
Summary(sv):	Silly::StringMaths Perlmodul
Summary(uk):	������ ��� Perl Silly::StringMaths
Summary(zh_CN):	Silly::StringMaths Perl ģ��
Name:		perl-Silly-StringMaths
Version:	0.13
Release:	9
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
Silly::StringMaths umo�liwia wykonywanie operacji matematycznych na
liczbach ca�kowitych, zamiast liczb wykorzystuj�c �a�cuchy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Silly
%{_mandir}/man3/*
