%define	pdir	Silly
%define	pnam	StringMaths
%include	/usr/lib/rpm/macros.perl
Summary:	Silly-StringMaths perl module
Summary(pl):	Modu� perla Silly-StringMaths
Name:		perl-Silly-StringMaths
Version:	0.13
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Silly-StringMaths provides support for basic integer mathematics,
using strings rather than numbers.

%description -l pl
Silly-StringMaths umo�liwia wykonywanie operacji matematycznych na
liczbach ca�kowitych, zamiast liczb wykorzystuj�c �a�cuchy.

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
