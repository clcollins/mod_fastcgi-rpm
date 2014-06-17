#
# spec file for package mod_fastcgi (Version 2.4.6)
#
# Copyright (c) 2014 Chris Collins <collins.christopher@gmail.com>

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

BuildRequires: autoconf automake httpd httpd-devel apr-devel
Requires: httpd apr libtool

Summary:        FastCGI module for Apache

%description
This  module provides support for the FastCGI protocol.
FastCGI is a language independent, scalable, open extension to CGI
that provides high performance and persistence without the limitations
of server specific APIs.

%prep
%setup -n %{name}-%{version}

%build
cp Makefile.AP2 Makefile
%{__make} top_dir="%{_libdir}/httpd"
%{__cat} << EOF > mod_fastcgi.conf
# This is the Apache server configuration file for global fastcgi support.
# Some options can be overridden in the virtual host context.
# See <URL:http://www.fastcgi.com/mod_fastcgi/docs/mod_fastcgi.html>

# Required here because fastcgi.conf loads before httpd.conf
User apache
Group apache

LoadModule fastcgi_module modules/mod_fastcgi.so

# global FastCgiConfig can be overridden by FastCgiServer options in vhost config
FastCgiConfig -idle-timeout 20 -maxClassProcesses 1
EOF


%install
%{__rm} -rf %{buildroot}
%{__make} install top_dir="%{_libdir}/httpd" DESTDIR="%{buildroot}"
%{__install} -Dp -m0644 mod_fastcgi.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/fastcgi.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root, 0775)
%attr(0644,root,root) %{_libdir}/httpd/modules/%{name}.so
%attr(0644,root,root) %{_sysconfdir}/httpd/conf.d/fastcgi.conf
%doc docs/LICENSE.TERMS docs/%{name}.html CHANGES

%changelog
* Fri Jun 13 2014 Chris Collins <collins.christopher@gmail.com> 2.4.6-1
- First package
