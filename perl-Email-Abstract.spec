%define module      Email-Abstract
%define name        perl-%{module}
%define version     2.13.4
%define up_version  2.134
%define release     %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Unified interface to mail representations
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{up_version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Email::Simple)
BuildRequires:  perl(Module::Pluggable)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{up_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*


