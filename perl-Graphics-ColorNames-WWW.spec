#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Graphics
%define		pnam	ColorNames-WWW
Summary:	WWW color names and equivalent RGB values	
Name:		perl-Graphics-ColorNames-WWW
Version:	0.01
Release:	1
License:	same as perl
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/C/CF/CFAERBER/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://search.cpan.org/dist/Graphics-ColorNames-WWW/
BuildRequires:	perl-Module-Load
BuildRequires:	perl-Graphics-ColorNames
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW color names and equivalent RGB values.

%prep
%setup -q %{version}q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Graphics/*.pm
%dir %{perl_vendorlib}/Graphics/ColorNames/WWW
%{perl_vendorlib}/Graphics/ColorNames/WWW/*.pm
%{_mandir}/man3/*
