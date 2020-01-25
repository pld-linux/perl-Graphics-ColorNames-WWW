#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Graphics
%define		pnam	ColorNames-WWW
Summary:	WWW color names and equivalent RGB values
Summary(pl.UTF-8):	Nazwy kolorów WWW i ich wartości RGB
Name:		perl-Graphics-ColorNames-WWW
Version:	1.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Graphics/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c518859fd8797927481e2318bff362e0
URL:		http://search.cpan.org/dist/Graphics-ColorNames-WWW/
BuildRequires:	perl-Graphics-ColorNames
BuildRequires:	perl-Module-Load
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW color names and equivalent RGB values.

%description -l pl.UTF-8
Nazwy kolorów WWW i ich wartości RGB.

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
%{perl_vendorlib}/Graphics/ColorNames/*.pm
%{_mandir}/man3/*
