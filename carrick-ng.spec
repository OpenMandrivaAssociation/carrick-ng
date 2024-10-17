Name: carrick-ng
Summary: Connection management panel for Moblin
Group: Networking/Other
Version: 1.1.13
Release: %mkrel 3
License: GPLv2+
URL: https://www.moblin.org
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
Patch0: carrick-ng-1.1.13-libnotify.patch
Patch1: carrick-ng-1.1.13-rest.patch
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
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang carrick

%clean
rm -rf %{buildroot}

%files -f carrick.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS NEWS README HACKING ChangeLog
%{_sysconfdir}/xdg/autostart/carrick-panel.desktop
%{_bindir}/carrick-connection-panel
%{_libdir}/carrick-3g-wizard
%{_datadir}/carrick
%{_datadir}/dbus-1/services/org.moblin.*.service
