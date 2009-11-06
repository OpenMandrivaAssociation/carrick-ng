%define version 1.1.13
%define rel 1
%define snapshot 0
# git20091002

%if %{snapshot}
%define release %mkrel 0.%{snapshot}.%{rel}
%define sversion %{version}%{snapshot}
%else
%define sversion %{version}
%define release %mkrel %{rel}
%endif

Name: carrick-ng
Summary: Connection management panel for Moblin
Group: Networking/Other
Version: %{version}
Release: %{release}
License: GPL 2
URL: http://www.moblin.org
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{sversion}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: connman-devel
BuildRequires: libgtk+2-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libnotify-devel
BuildRequires: nbtk-devel
BuildRequires: intltool
BuildRequires: gnome-common
BuildRequires: moblin-panel-devel
BuildRequires: iso-codes
BuildRequires: librest-devel >= 0.6.1
BuildRequires: mobile-broadband-provider-info

Requires: mobile-broadband-provider-info

%description
Carrick is a connection management panel for Moblin.

%prep
%setup -q -n %{name}-%{sversion}

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%doc COPYING AUTHORS NEWS README HACKING ChangeLog
%{_sysconfdir}/xdg/autostart/carrick-panel.desktop
%{_bindir}/carrick-connection-panel
%{_libdir}/carrick-3g-wizard
%{_datadir}/carrick/icons/*
%{_datadir}/carrick/theme/*
%{_datadir}/locale/*
%{_datadir}/dbus-1/services/org.moblin.*.service
