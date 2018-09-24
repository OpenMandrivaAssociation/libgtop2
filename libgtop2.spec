%define url_ver %(echo %{version}|cut -d. -f1,2)

%define pkgname	libgtop
%define api	2.0
%define major	11
%define libname	%mklibname gtop %{api} %{major}
%define girname %mklibname gtop-gir %{api}
%define devname	%mklibname -d gtop %{api}

Summary:	The LibGTop library
Name:		%{pkgname}2
Version:	2.38.0
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgtop/%{url_ver}/%{pkgname}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(xau)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	gtk-doc
BuildRequires:	texinfo

%description
LibGTop is a library that fetches information about the running
system such as CPU and memory useage, active processes and more.

On Linux systems, this information is taken directly from the /proc
filesystem while on other systems a server is used to read that
information from other /dev/kmem, among others.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}
Provides:	%{pkgname}%{api} = %{version}-%{release}
Suggests:	%{name} = %{version}-%{release}

%description -n %{libname}
LibGTop is a library that fetches information about the running
system such as CPU and memory useage, active processes and more.

On Linux systems, this information is taken directly from the /proc
filesystem while on other systems a server is used to read that
information from other /dev/kmem, among others.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}gtop2.0_0 < 2.28.4-5

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Development files for %{pkgname}
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
Install this package if you wish to develop applications that access
information on system statistics such as CPU and memory usage.

%prep
%setup -qn %{pkgname}-%{version}

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std 
#find_lang %{pkgname}-%{api}

%files -f %{pkgname}-%{api}.lang
%doc NEWS README

%files -n %{libname}
%{_libdir}/libgtop-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GTop-%{api}.typelib

%files -n %{devname}
%doc AUTHORS ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/%{pkgname}-%{api}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_infodir}/*.info*
%{_datadir}/gir-1.0/GTop-%{api}.gir

