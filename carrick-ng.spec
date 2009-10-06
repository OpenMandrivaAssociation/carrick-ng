%define version 1.1.4
%define rel 1
%define snapshot git20091002
%define release %mkrel 0.%{snapshot}.%{rel}
%define sversion %{version}%{snapshot}

Name: carrick-ng
Summary: Connection management panel for Moblin
Group: Networking/Other
Version: %{version}
License: GPL 2
URL: http://www.moblin.org
Release: %{release}
Source0: %{name}-%{sversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: connman-devel
BuildRequires: libgtk+2-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libnotify-devel
BuildRequires: nbtk-devel
BuildRequires: intltool
BuildRequires: gnome-common
BuildRequires: moblin-panel-devel

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
%{_datadir}/carrick/icons/*
%{_datadir}/carrick/theme/*
%{_datadir}/locale/*
