# build_example: Compiles example binaries as well
#	0 = no
#	1 = yes
%define build_example	0

# End of user configurable section

%{?_without_example: %{expand: %%define build_example 0}}
%{?_with_example: %{expand: %%define build_example 1}}

%define req_glib2_version	2.0.0

%define	pkgname		libgtop
%define api_version	2.0
%define lib_major	7
%define libname	%mklibname gtop %{api_version} %{lib_major}
%define libnamedev %mklibname -d gtop %{api_version}
%define last_abi_break_version 2.14.0

Summary:	The LibGTop library
Name:     	%{pkgname}2
Version: 2.28.4
Release: 4
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.gnome.org/

Source0: 	http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
BuildRequires:	glib2-devel >= %{req_glib2_version}
BuildRequires:	gobject-introspection-devel
BuildRequires:	libxau-devel
BuildRequires:	texinfo
BuildRequires:	gtk-doc
BuildRequires:  intltool

%description
LibGTop is a library that fetches information about the running
system such as CPU and memory useage, active processes and more.

On Linux systems, this information is taken directly from the /proc
filesystem while on other systems a server is used to read that
information from other /dev/kmem, among others.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}
Provides:	%{pkgname}%{api_version} = %{version}-%{release}
Requires:   %{name} >= %{version}
Requires:	glib2 >= %{req_glib2_version}

%description -n %{libname}
LibGTop is a library that fetches information about the running
system such as CPU and memory useage, active processes and more.

On Linux systems, this information is taken directly from the /proc
filesystem while on other systems a server is used to read that
information from other /dev/kmem, among others.

%package -n %{libnamedev}
Summary:	Development files for %{pkgname}
Group:		Development/GNOME and GTK+
Provides:	%{pkgname}%{api_version}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	glib2-devel >= %{req_glib2_version}
Conflicts:	%{pkgname}%{api_version}-devel < %{last_abi_break_version}
Obsoletes: %mklibname -d gtop %{api_version} %{lib_major}

%description -n %{libnamedev}
LibGTop is a library that fetches information about the running
system such as CPU and memory useage, active processes and more.

Install this package if you wish to develop applications that access
information on system statistics such as CPU and memory usage.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure2_5x \
%if %build_example
	--with-libgtop-examples
%endif

%make


%install
%makeinstall_std 
%{find_lang} %{pkgname}-%{api_version}


%files -f %{pkgname}-%{api_version}.lang
%defattr(-, root, root)
%doc NEWS README
%if %build_example
%dir %{_libdir}/%{pkgname}
%{_libdir}/%{pkgname}/first*
%{_libdir}/%{pkgname}/mountlist*
%{_libdir}/%{pkgname}/netload*
%{_libdir}/%{pkgname}/procmap*
%{_libdir}/%{pkgname}/second*
%{_libdir}/%{pkgname}/smp*
%{_libdir}/%{pkgname}/sysdeps*
%{_libdir}/%{pkgname}/timings*
%endif

%files -n %{libname}
%defattr(-, root, root)
%doc NEWS README
%{_libdir}/lib*.so.%{lib_major}*
%{_libdir}/girepository-1.0/GTop-%{api_version}.typelib

%files -n %{libnamedev}
%defattr(-, root, root)
%doc AUTHORS ChangeLog
%doc %_datadir/gtk-doc/html/*
%{_includedir}/%{pkgname}-%{api_version}
%{_libdir}/lib*.so
%attr(644,root,root) %{_libdir}/*a
%{_libdir}/pkgconfig/*
%{_infodir}/*.info*
%_datadir/gir-1.0/GTop-%{api_version}.gir


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.28.3-2mdv2011.0
+ Revision: 662374
- mass rebuild

* Fri Mar 25 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.3-1
+ Revision: 648515
- new version
- add introspection support

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 2.28.2-2
+ Revision: 640177
- update glib reqname

* Tue Sep 28 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.2-1mdv2011.0
+ Revision: 581731
- update to new version 2.28.2

* Tue Mar 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.1-1mdv2010.1
+ Revision: 529817
- update to new version 2.28.1

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.28.0-2mdv2010.1
+ Revision: 520866
- rebuilt for 2010.1

* Mon Sep 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446455
- update to new version 2.28.0

* Mon May 25 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.3-1mdv2010.0
+ Revision: 379685
- new version
- drop patch

* Mon May 11 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 374170
- new version

* Tue Apr 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 366956
- update to new version 2.26.1

* Mon Mar 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 346859
- update to new version 2.26.0

* Tue Feb 17 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 341274
- update to new version 2.25.91

* Tue Jan 20 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.4-1mdv2009.1
+ Revision: 331535
- update to new version 2.24.4

* Tue Jan 13 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.3-1mdv2009.1
+ Revision: 328859
- new version
- fix format strings

* Tue Sep 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287333
- new version

* Tue Aug 19 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 273558
- new version

* Thu Jul 03 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.4-1mdv2009.0
+ Revision: 230989
- new version

* Tue Jul 01 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.3-1mdv2009.0
+ Revision: 230464
- new version
- update license

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 27 2008 Funda Wang <fwang@mandriva.org> 2.22.2-1mdv2009.0
+ Revision: 211509
- New version 2.22.2

* Wed Apr 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.1-1mdv2009.0
+ Revision: 192447
- new version

* Mon Mar 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183774
- new version
- new version

* Mon Feb 25 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 175045
- new version

* Mon Jan 14 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.5-1mdv2008.1
+ Revision: 151899
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 16 2007 Frederic Crozat <fcrozat@mandriva.com> 2.21.1-3mdv2008.1
+ Revision: 109124
- Remove patch0, no longer useful
- Clean specfile
- Tag gtk-doc files as doc

* Tue Oct 30 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.1-2mdv2008.1
+ Revision: 103783
- fix buildrequires

* Tue Oct 30 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.1-1mdv2008.1
+ Revision: 103737
- new version

* Sun Sep 16 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 88487
- new version

* Mon Aug 27 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.92-1mdv2008.0
+ Revision: 71783
- new version

* Sun Aug 26 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.91-1mdv2008.0
+ Revision: 71582
- new version
- new devel name

* Tue Jul 10 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.5-1mdv2008.0
+ Revision: 50852
- new version

* Mon Jun 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.4-1mdv2008.0
+ Revision: 41018
- new version

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 2.19.3-2mdv2008.0
+ Revision: 36183
- rebuild with correct optflags

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - new version

* Wed May 09 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.9-1mdv2008.0
+ Revision: 25403
- new version


* Sun Feb 25 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.8-1mdv2007.0
+ Revision: 125667
- new version

* Mon Feb 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.7-1mdv2007.1
+ Revision: 118864
- new version

* Sun Jan 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.6-1mdv2007.1
+ Revision: 108926
- new version

* Tue Dec 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.5-1mdv2007.1
+ Revision: 90735
- fix buildrequires
- new version
- unpack patch
- add gtk-doc files
- rebuild
- rebuild
- Import libgtop2

* Thu Sep 21 2006 Götz Waschk <waschk@mandriva.org> 2.14.4-1mdv2007.0
- New version 2.14.4

* Thu Sep 07 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.3-1mdv2007.0
- New version 2.14.3

* Sat Aug 12 2006 Götz Waschk <waschk@mandriva.org> 2.14.2-2mdv2007.0
- fix buildrequires

* Sat Jul 29 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-1mdv2007.0
- New release 2.14.2

* Wed Apr 19 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.1-2mdk
- Fix conflicts to ease upgrade

* Sat Apr 15 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.1-1mdk
- Release 2.14.1

* Fri Feb 24 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.2-2mdk
- Use mkrel

* Tue Nov 29 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.2-1mdk
- New release 2.12.2

* Thu Oct 06 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.0-1mdk
- Release 2.12.0

* Wed Jun 15 2005 Götz Waschk <waschk@mandriva.org> 2.10.2-1mdk
- New release 2.10.2

* Thu Apr 21 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-1mdk 
- Release 2.10.1 (based on Götz Waschk package)

* Mon Feb 14 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.8.3-1mdk
- New release 2.8.3

* Tue Dec 07 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.8.2-1mdk
- New release 2.8.2

* Wed Oct 20 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.1-1mdk
- New release 2.8.1

* Thu Apr 08 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.0-2mdk
- Add conflicts to easy upgrade

* Thu Apr 08 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.0-1mdk
- new version

* Wed Apr 07 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.5.2-1mdk
- New release 2.5.2
- Remove patches 1, 2 (merged upstream)

* Wed Feb 25 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.8-4mdk
- Fix distlint error

