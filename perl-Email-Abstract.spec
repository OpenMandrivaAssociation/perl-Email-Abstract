%define modname	Email-Abstract
%define modver	3.004

Summary:	Unified interface to mail representations
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Email/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(MIME::Entity) >= 5.501.0
BuildRequires:	perl(Email::Simple)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Class::Accessor::Grouped)
BuildRequires:	perl-devel

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
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man3/*

