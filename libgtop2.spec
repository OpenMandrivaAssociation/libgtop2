%define pkgname		libgtop
%define api_version	2.0
%define lib_major	7
%define libname	%mklibname gtop %{api_version} %{lib_major}
%define girname %mklibname gtop-gir %{api_version}
%define develname %mklibname -d gtop %{api_version}

Summary:	The LibGTop library
Name:     	%{pkgname}2
Version:	2.28.4
Release:	2
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.gnome.org/

Source0: 	http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:  intltool
BuildRequires:	texinfo
BuildRequires:	pkgconfig(glib-2.0) >= 2.0.0
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
Provides:	%{pkgname}%{api_version} = %{version}-%{release}

%description -n %{libname}
LibGTop is a library that fetches information about the running
system such as CPU and memory useage, active processes and more.

On Linux systems, this information is taken directly from the /proc
filesystem while on other systems a server is used to read that
information from other /dev/kmem, among others.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Summary:	Development files for %{pkgname}
Group:		Development/GNOME and GTK+
Provides:	%{pkgname}%{api_version}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
LibGTop is a library that fetches information about the running
system such as CPU and memory useage, active processes and more.

Install this package if you wish to develop applications that access
information on system statistics such as CPU and memory usage.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure2_5x \
	--disable-static \

%make

%install
rm -rf %{buildroot}
%makeinstall_std 
find %{buildroot} -name *.la | xargs rm
%{find_lang} %{pkgname}-%{api_version}

%post -n %{develname}
%_install_info %{name}.info

%postun -n %{develname}
%_remove_install_info %{name}.info

%files -f %{pkgname}-%{api_version}.lang
%doc NEWS README

%files -n %{libname}
%{_libdir}/lib*.so.%{lib_major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GTop-%{api_version}.typelib

%files -n %{develname}
%doc AUTHORS ChangeLog
%doc %_datadir/gtk-doc/html/*
%{_includedir}/%{pkgname}-%{api_version}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_infodir}/*.info*
%_datadir/gir-1.0/GTop-%{api_version}.gir

