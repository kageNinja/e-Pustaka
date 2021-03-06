%define name ePustaka.ign
%define release 1
%define version Beta1
%define license GPL2
%define url http://http://github.com/havied2
%define group System Environment/Base

Summary:IGOS Nusantara SDK Application
Name:%{name}
Version:%{version}
Release:%{release}
License:%{license}
Group:%{group}
URL:%{url}
Source0:%{name}.tar.gz
Source1:%{name}.txt
BuildRoot:%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:ignsdk
BuildArch:noarch
%description
%{description}
Aplikasi untuk memberikan kemudahan bagi para putakawan utuk menyimpan data buku dan mencarinya.

%prep
%setup -q -n %{name}

%install
%include %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir
%config %attr(0755,root,root) 
/opt/ignsdk/*
/usr/share/applications/*

%changelog

* Mon Feb 18 2013 foo <foo@bar.org>
- First Build
