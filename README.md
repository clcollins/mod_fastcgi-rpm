mod_fastcgi-rpm
===============

Mod_fastcgi is an excellent way to run PHP applications with Apache and PHP-FPM.  Unfortunately it can be somewhat hard to find in official repositories for RHEL-based servers.  I made this to make it easier to build inside of [Docker](http://docker.io) images.


##Building##

1. `git clone https://github.com/clcollins/mod_fastcgi-rpm.git`
2. `yum install rpm-build rpmdevtools autoconf automake httpd httpd-devel apr-devel`
3. `./build.sh mod_fastcgi`
4. `sudo yum install ~/rpmbuild/RPMS/*/*.rpm`
5. PROFIT!

##To Do##

* Add Selinux support a la the Repoforge spec.

##Acknowledgements##

Thanks to:

* Ian Meyer [https://github.com/imeyer](https://github.com/imeyer) for giving me the idea to do this (check out his awesome Runit rpm spec file and build script for RHEL-based systems).
* Repoforge [https://github.com/repoforge](https://github.com/repoforge) for some guidance with their [https://github.com/repoforge/rpms/blob/master/specs/mod_fastcgi/mod_fastcgi.spec](.spec) file.

##Copyright Information##

Copyright (C) 2014 Chris Collins

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.

