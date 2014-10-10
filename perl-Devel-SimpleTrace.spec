%define	upstream_name	 Devel-SimpleTrace
%define	upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	See where you code warns and dies using stack traces
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module can be used to more easily spot the place where a program or a
module generates errors. Its use is extremely simple, reduced to just useing
it.

This is achieved by modifying the functions warn() and die() in order to
replace the standard messages by complete stack traces that precisely indicates
how and where the error or warning occurred. Other than this, their use should
stay unchanged, even when using die() inside eval().

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{perl_vendorlib}/Devel
%{_mandir}/*/*

%changelog
* Thu Feb 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 639634
- update to new version 0.08

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 403103
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.07-3mdv2009.0
+ Revision: 256636
- rebuild

* Thu Jan 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2008.1
+ Revision: 153983
- new version

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.06-1mdv2008.1
+ Revision: 135833
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Jan 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2007.0
+ Revision: 103019
- Import perl-Devel-SimpleTrace

* Mon Jan 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2007.1
- first mdv release

