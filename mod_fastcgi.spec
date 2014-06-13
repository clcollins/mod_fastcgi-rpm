#
# spec file for package mod_fastcgi (Version 2.4.6)
#
# Copyright (c) 2014 Chris Collins <collins.christopher@gmail.com>

%ifarch x86_64
%define fcgi_libdir  %{buildroot}/usr/lib64/httpd
%else
%define fcgi_libdir  %{buildroot}/usr/lib/httpd
%endif

Name:           mod_fastcgi
Version:        2.4.6
Release:        1

Group:          Web
License:        OpenSource

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Url:            http://www.FastCGI.com
Source:         http://www.FastCGI.com/dist/%{name}-%{version}.tar.gz

Obsoletes: mod_fastcgi <= %{version}-%{release}
Provides: mod_fastcgi = %{version}-%{release}

BuildRequires: make gcc httpd-devel apr-devel
Requires: httpd apr libtool

Summary:        FastCGI module for Apache 

%description
This  module provides support for the FastCGI protocol.
FastCGI is a language independent, scalable, open extension to CGI
that provides high performance and persistence without the limitations
of server specific APIs.

%prep
%setup -q

%build
cp Makefile.AP2 Makefile
make top_dir=%{fcgi_libdir}

%install
rm -rf %{buildroot}
make install top_dir=%{fcgi_libdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0644,root,root) %{_libdir}/httpd/modules/%{name}.so
%doc docs/LICENSE.TERMS docs/%{name}.html CHANGES

%changelog
* Fri Jun 13 2014 Chris Collins <collins.christopher@gmail.com> 2.4.6-1
- First package
