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
Release: %mkrel 1
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.gnome.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

Source0: 	http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.xz
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
Requires:	libglib2.0 >= %{req_glib2_version}

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
rm -rf %{buildroot}
%makeinstall_std 

%{find_lang} %{pkgname}-%{api_version}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%post -n %{libnamedev}
%_install_info %{name}.info

%postun -n %{libnamedev}
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
