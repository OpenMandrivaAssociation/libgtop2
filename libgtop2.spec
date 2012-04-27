%define pkgname		libgtop

%define api	2.0
%define major	7
%define libname	%mklibname gtop %{api} %{major}
%define girname %mklibname gtop-gir %{api}
%define develname %mklibname -d gtop %{api}

Summary:	The LibGTop library
Name:     	%{pkgname}2
Version:	2.28.4
Release:	3
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.gnome.org/
Source0: 	http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.xz

BuildRequires:  intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(xau)

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

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Summary:	Development files for %{pkgname}
Group:		Development/GNOME and GTK+
Provides:	%{pkgname}%{api}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{develname}
LibGTop is a library that fetches information about the running
system such as CPU and memory useage, active processes and more.

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
find %{buildroot} -name *.la | xargs rm
%{find_lang} %{pkgname}-%{api}

%post -n %{develname}
%_install_info %{name}.info

%postun -n %{develname}
%_remove_install_info %{name}.info

%files -f %{pkgname}-%{api}.lang
%doc NEWS README

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GTop-%{api}.typelib

%files -n %{develname}
%doc AUTHORS ChangeLog
%{_includedir}/%{pkgname}-%{api}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_infodir}/*.info*
%{_datadir}/gir-1.0/GTop-%{api}.gir
%doc %{_datadir}/gtk-doc/html/*

