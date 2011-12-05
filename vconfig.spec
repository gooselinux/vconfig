Summary: Linux 802.1q VLAN configuration utility
Name: vconfig
Version: 1.9
Release: 8.1%{?dist}
License: GPLv2+
Group: System Environment/Base
Source: http://www.candelatech.com/~greear/vlan/vlan.%{version}.tar.gz
URL: http://www.candelatech.com/~greear/vlan.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%define _sbin /sbin

%description 
The vconfig program configures and adjusts 802.1q VLAN parameters.

%prep
%setup -q -n vlan

%build
make clean
rm -f vconfig
make CCFLAGS="%{optflags}" STRIP=/bin/true vconfig

%install
rm -rf ${RPM_BUILD_ROOT}
%{__install} -D -m755 vconfig ${RPM_BUILD_ROOT}%{_sbin}/vconfig
%{__install} -D -m644 vconfig.8 ${RPM_BUILD_ROOT}%{_mandir}/man8/vconfig.8
rm -rf contrib/CVS

%clean 
rm -rf ${RPM_BUILD_ROOT}

%files 
%defattr(-, root, root, 0755)
%doc CHANGELOG contrib README vlan.html vlan_test.pl
%{_sbin}/vconfig
%{_mandir}/man8/vconfig.8*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.9-8.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar 19 2008 Roman Rakus <rrakus@redhat.cz> - 1.9-6
- added STRIP=/bin/true for useful debuginfo

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.9-5
- Autorebuild for GCC 4.3

* Thu Aug 16 2007 Phil Knirsch <pknirsch@redhat.com> - 1.9-4
- License review and update

* Wed Jan 10 2007 Phil Knirsch <pknirsch@redhat.com> - 1.9-3
- Removed CVS cruft from documentation (#221161)
- Tiny specfile cleanups.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.9-2.1
- rebuild

* Fri Feb 17 2006 Phil Knirsch <pknirsch@redhat.com> - 1.9-2
- Fix build problems and cleaned up files in archive properly

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.9-1.1
- bump again for double-long bug on ppc(64)

* Fri Feb 10 2006 Phil Knirsch <pknirsch@redhat.com> - 1.9-1
- Updated to vconfig-1.9

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.8-7.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com> - 1.8-7.1
- rebuilt

* Mon Aug 15 2005 Phil Knirsch <pknirsch@redhat.com>
- Fixed license from LGPL to GPL (#163998)

* Wed Mar 02 2005 Phil Knirsch <pknirsch@redhat.com> 1.8-7
- bump release and rebuild with gcc 4

* Fri Feb 18 2005 Phil Knirsch <pknirsch@redhat.com> 1.8-6
- rebuilt

* Sun Feb 13 2005 Florian La Roche <laroche@redhat.com> 1.8-5
- remove kernel dep, kernel runtime deps should go into apps, #146151

* Mon Sep 27 2004 Phil Knirsch <pknirsch@redhat.com> 1.8-4
- Small specfile changes (#131487)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Oct 22 2003 Bill Nottingham <notting@redhat.com> 1.8-1
- update to 1.8 (#107761)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 22 2003 Jeremy Katz <katzj@redhat.com> 1.6-3
- fix to build with gcc 3.3

* Fri Jan 31 2003 Bill Nottingham <notting@redhat.com> 1.6-2
- adapt upstream package
- add patch for license

* Thu Jan 23 2003 Tuomo Soini <tis@foobar.fi> 1.6-6foo
- changes for new initscripts package

* Sun Sep 15 2002 Tuomo Soini <tis@foobar.fi> 1.6-5foo
- foobarize

* Tue Aug 06 2002 Tuomo Soini <tis@foobar.fi> 1.6-t4
- fix ifup-vlan to be able to set default route

* Tue Jun 25 2002 Tuomo Soini <tis@foobar.fi> 1.6-t3
- pgp sign, foobarize spec-file

* Thu May 30 2002 Tuomo Soini <tis@foobar.fi> 1.6-t2
- fix typo in ifup-vlan

* Thu May 30 2002 Tuomo Soini <tis@foobar.fi> 1.6-t1
- updated for redhat 7.3
- build doesn't require kernel-sources

* Fri Apr 05 2002 Dale Bewley <dale@bewley.net>
- update to 1.6
- add ifup scripts

* Tue Dec 11 2001 Dale Bewley <dale@bewley.net>
- initial specfile

# EOF
