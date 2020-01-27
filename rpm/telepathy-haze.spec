Name:       telepathy-haze

Summary:    A multi-protocol Libpurple connection manager for Telepathy
Version:    0.8.0
Release:    1
License:    GPLv2+
URL:        http://developer.pidgin.im/wiki/Telepathy
Source0:    http://telepathy.freedesktop.org/releases/telepathy-haze/%{name}-%{version}.tar.gz
Patch0:     0001-telepathy-haze-Reword-comment-for-Wimplicit-fallthro.patch
Patch1:     0001-Allow-build-with-glib2-2.62.4.patch
BuildRequires:  pkgconfig(purple)
BuildRequires:  pkgconfig(telepathy-glib)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  dbus-python
BuildRequires:  pygobject2
BuildRequires:  python-twisted

%description

telepathy-haze is a connection manager built around libpurple, the core of
Pidgin (formerly Gaim), as a Summer of Code project under the Pidgin umbrella.
Ultimately, any protocol supported by libpurple will be supported by
telepathy-haze; for now, XMPP, MSN and AIM are known to work acceptably, and
others will probably work too.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%reconfigure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%license COPYING
%{_libexecdir}/telepathy-haze
%{_datadir}/dbus-1/services/*.haze.service
%{_mandir}/man8/telepathy-haze.8*
