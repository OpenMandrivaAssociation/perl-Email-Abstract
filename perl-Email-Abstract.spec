%define upstream_name    Email-Abstract
%define upstream_version 3.004

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Unified interface to mail representations
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(MIME::Entity) >= 5.501.0
BuildRequires:	perl(Email::Simple)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Class::Accessor::Grouped)
BuildRequires:	perl-devel
BuildArch:		noarch

%description
Email::Abstract provides module writers with the ability to write
representation-independent mail handling code. For instance, in the cases of
Mail::Thread or Mail::ListDetector, a key part of the code involves reading the
headers from a mail object. Where previously one would either have to specify
the mail class required, or to build a new object from scratch, Email::Abstract
can be used to perform certain simple operations on an object regardless of its
underlying representation.

Email::Abstract currently supports Mail::Internet, MIME::Entity, Mail::Message,
Email::Simple and Email::MIME. Other representations are encouraged to create
their own Email::Abstract::* class by copying Email::Abstract::EmailSimple. All
modules installed under the Email::Abstract hierarchy will be automatically
picked up and used.

For this reason, the tedious process of looking for a valid date has been
encapsulated in this software. Further, the process of creating RFC compliant
date strings is also found in this software.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 3.4.0-4mdv2012.0
+ Revision: 765192
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 3.4.0-2
+ Revision: 667124
- mass rebuild

* Fri Mar 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.4.0-1
+ Revision: 646417
- new version

* Mon Nov 15 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.3.0-1mdv2011.0
+ Revision: 597671
- update to new version 3.003

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 3.2.0-2mdv2011.0
+ Revision: 564733
- rebuild for perl 5.12.1

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 3.2.0-1mdv2011.0
+ Revision: 552699
- update to 3.002

* Sun Feb 14 2010 Jérôme Quelin <jquelin@mandriva.org> 3.1.0-4mdv2010.1
+ Revision: 505730
- rebuild using %%perl_convert_version

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.001-3mdv2010.0
+ Revision: 426443
- rebuild

* Thu Dec 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.001-2mdv2009.1
+ Revision: 315963
- new version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.13.4-2mdv2009.0
+ Revision: 223661
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Nov 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.13.4-1mdv2008.1
+ Revision: 110400
- new version (upstream version 2.134)

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.13.2-1mdv2008.0
+ Revision: 48057
- update to new version 2.132


* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.13.1-1mdv2007.0
+ Revision: 111269
- fix build dependencies
- Import perl-Email-Abstract

* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.13.1-1mdv2007.1
- first mdv release

