Summary:	Japanese input method for GTK2
Summary(pl):	Metoda wprowadzania znaków japoñskich dla GTK2
Name:		im-ja
Version:	1.3
Release:	1
License:	LGPL
Group:		Applications/Editors
Source0:	http://im-ja.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	20ceb957496d84f854e379f40b0e704a
BuildRequires:	Canna-devel
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	gnome-panel-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 1:2.2.0
BuildRequires:	pkgconfig
BuildRequires:	libglade2-devel >= 1:2.0
Requires(post,postun):	/sbin/ldconfig
Requires(post):	GConf2
Requires(post,postun):	gtk+2
Requires:	gtk+2 >= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
im-ja is a Japanese input module for GTK2. Currently supports
hiragana, katakana, half-width katakana, zenkaku, canna, wnn and
kanji character recognition inputs. Hotkeys can be configured via a
GUI configurator.

%description -l pl
im-ja to modu³ wej¶ciowy do wprowadzania znaków japoñskich dla GTK2.
Aktualnie obs³uguje metody rozpoznawania znaków hiragana, katakana,
katakana po³ówkowej szeroko¶ci, zenkaku, canna, wnn i kanji. Klawisze
mog± byæ konfigurowane narzêdziem z graficznym interfejsem.

%prep
%setup -q

%build
%configure \
	--disable-anthy \
	--disable-wnn

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/immodules/*.la

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
%doc README COPYING TODO AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/gtk-2.0/*/immodules/im-ja.so
%dir %{_libdir}/im-ja
# -gnome?
%attr(755,root,root) %{_libdir}/im-ja/im-ja-applet
%attr(755,root,root) %{_libdir}/im-ja/kpengine
%{_libdir}/bonobo/servers/*.server
%{_datadir}/%{name}
%{_datadir}/control-center-2.0/capplets/*.desktop
%{_datadir}/gnome-2.0/ui/*.xml
%{_pixmapsdir}/*.jpg
%{_pixmapsdir}/*.png
%{_mandir}/man1/*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
