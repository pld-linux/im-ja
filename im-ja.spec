#
# Conditional build:
%bcond_without	anthy	# Anthy support
%bcond_without	canna	# Canna support
%bcond_with	wnn	# Wnn support (build error)
%bcond_with	gnome2	# GNOME 2.x panel applet

Summary:	Japanese input method for GTK2
Summary(pl.UTF-8):	Metoda wprowadzania znaków japońskich dla GTK2
Name:		im-ja
Version:	1.5
Release:	1
License:	LGPL v2+
Group:		Applications/Editors
Source0:	https://im-ja.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	8986574373d03e685730e16d8f15ade9
Patch0:		%{name}-link.patch
URL:		https://im-ja.sourceforge.net/
%{?with_canna:BuildRequires:	Canna-devel}
%{?with_wnn:BuildRequires:	FreeWnn-devel}
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
%{?with_anthy:BuildRequires:	anthy-devel}
BuildRequires:	gettext-tools
%{?with_gnome2:BuildRequires:	gnome-panel2-devel >= 2.0.0}
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	xorg-lib-libSM-devel
Requires(post,postun):	/sbin/ldconfig
Requires(post):	GConf2
Requires(post,postun):	gtk+2
Requires:	gtk+2 >= 2:2.4.0
Requires:	libglade2 >= 1:2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
im-ja is a Japanese input module for GTK2. Currently supports
hiragana, katakana, half-width katakana, zenkaku, canna, wnn and
kanji character recognition inputs. Hotkeys can be configured via a
GUI configurator.

%description -l pl.UTF-8
im-ja to moduł wejściowy do wprowadzania znaków japońskich dla GTK2.
Aktualnie obsługuje metody rozpoznawania znaków hiragana, katakana,
katakana połówkowej szerokości, zenkaku, canna, wnn i kanji. Klawisze
mogą być konfigurowane narzędziem z graficznym interfejsem.

%prep
%setup -q
%patch -P0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_anthy:--disable-anthy} \
	%{!?with_canna:--disable-canna} \
	%{!?with_gnome:--disable-gnome} \
	%{!?with_wnn:--disable-wnn}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	schemasdir=/etc/gconf/schemas

# useless
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/immodules/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
/sbin/ldconfig
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
%gconf_schema_install

%postun
umask 022
/sbin/ldconfig
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules

%files -f %{name}.lang
%defattr(644,root,root,755)
# COPYING contains only note about different licenses, not license text
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/im-ja-conf
%attr(755,root,root) %{_bindir}/im-ja-xim-server
%attr(755,root,root) %{_libdir}/gtk-2.0/*/immodules/im-ja.so
%dir %{_libexecdir}/im-ja
%attr(755,root,root) %{_libexecdir}/im-ja/im-ja-helper
%attr(755,root,root) %{_libexecdir}/im-ja/kpengine
%{_datadir}/%{name}
%{_sysconfdir}/gconf/schemas/im-ja.schemas
%{_desktopdir}/im-ja.desktop
%{_pixmapsdir}/im-ja-about.jpg
%{_pixmapsdir}/im-ja-capplet.png
%{_mandir}/man1/im-ja-conf.1*
%{_mandir}/man1/im-ja-xim-server.1*

# -gnome?
%if %{with gnome2}
%attr(755,root,root) %{_libexecdir}/im-ja/im-ja-applet
%{_libdir}/bonobo/servers/GNOME_ImJaApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_ImJaApplet.xml
%endif
