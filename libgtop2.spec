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
%define lib_name	%mklibname gtop %{api_version} %{lib_major}
%define last_abi_break_version 2.14.0

Summary:	The LibGTop library
Name:     	%{pkgname}2
Version: 2.19.3
Release: %mkrel 2
License:	GPL
Group:		System/Libraries
URL:		http://www.gnome.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

Source0: 	http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
# (fc) 2.0.2-1mdk fix autoconf/automake environment (rawhide)
Patch0:		libgtop-2.0.0-prog_as.patch

BuildRequires:	libglib2.0-devel >= %{req_glib2_version}
BuildRequires:	popt-devel
BuildRequires:	autoconf2.5 automake1.7 intltool
BuildRequires:	gtk-doc

%description
LibGTop is a library that fetches information about the running
system such as CPU and memory useage, active processes and more.

On Linux systems, this information is taken directly from the /proc
filesystem while on other systems a server is used to read that
information from other /dev/kmem, among others.

%package -n %{lib_name}
Summary:	%{summary}
Group:		%{group}
Provides:	%{pkgname}%{api_version} = %{version}-%{release}
Requires:   %{name} >= %{version}
Requires:	libglib2.0 >= %{req_glib2_version}

%description -n %{lib_name}
LibGTop is a library that fetches information about the running
system such as CPU and memory useage, active processes and more.

On Linux systems, this information is taken directly from the /proc
filesystem while on other systems a server is used to read that
information from other /dev/kmem, among others.

%package -n %{lib_name}-devel
Summary:	Development files for %{pkgname}
Group:		Development/GNOME and GTK+
Provides:	%{pkgname}%{api_version}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}
Requires:	libglib2.0-devel >= %{req_glib2_version}
Conflicts:	%{pkgname}%{api_version}-devel < %{last_abi_break_version}

%description -n %{lib_name}-devel
LibGTop is a library that fetches information about the running
system such as CPU and memory useage, active processes and more.

Install this package if you wish to develop applications that access
information on system statistics such as CPU and memory usage.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1 -b .prog_as

aclocal-1.7
automake-1.7 --add-missing --force-missing
WANT_AUTOCONF_2_5=1 autoconf
WANT_AUTOCONF_2_5=1 autoheader

%build
%configure2_5x \
%if %build_example
	--with-libgtop-examples
%endif

%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%{find_lang} %{pkgname}-%{api_version}

#remove unpackaged files
rm -rf $RPM_BUILD_ROOT%{_libdir}/libgnomesupport* \
 $RPM_BUILD_ROOT%{_bindir}/libgtop_daemon2 \
 $RPM_BUILD_ROOT%{_libdir}/libgtop/include

%clean
rm -rf %{buildroot}

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%post -n %{lib_name}-devel
%_install_info %{name}.info

%postun -n %{lib_name}-devel
%_remove_install_info %{name}.info

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

%files -n %{lib_name}
%defattr(-, root, root)
%doc NEWS README
%{_libdir}/lib*.so.%{lib_major}*

%files -n %{lib_name}-devel
%defattr(-, root, root)
%doc AUTHORS ChangeLog
%{_includedir}/%{pkgname}-%{api_version}
%{_libdir}/lib*.so
%attr(644,root,root) %{_libdir}/*a
%{_libdir}/pkgconfig/*
%{_infodir}/*.info*
%_datadir/gtk-doc/html/*


