%define	module	Devel-SimpleTrace
%define	name	perl-%{module}
%define	version 0.07
%define	release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	See where you code warns and dies using stack traces
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/Devel/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module can be used to more easily spot the place where a program or a
module generates errors. Its use is extremely simple, reduced to just useing
it.

This is achieved by modifying the functions warn() and die() in order to
replace the standard messages by complete stack traces that precisely indicates
how and where the error or warning occurred. Other than this, their use should
stay unchanged, even when using die() inside eval().

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{perl_vendorlib}/Devel
%{_mandir}/*/*


