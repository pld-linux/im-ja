Summary:	Japanese input method for GTK2
Summary(pl):	Metoda wprowadzania znak�w japo�skich dla GTK2
Name:		im-ja
Version:	0.6
Release:	2
License:	LGPL
Group:		Applications/Editors
Source0:	http://im-ja.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	aeb6e5454587fd7e7a3f41629d26b914
BuildRequires:	Canna-devel
BuildRequires:	gtk+2-devel
Requires(post,postun):	/sbin/ldconfig
Requires(post):	GConf2
Requires(post,postun):	gtk+2
Requires:	gtk+2 >= 2.0.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
im-ja is a Japanese input module for GTK2. Currently supports
hiragana, katakana, half-width katakana, zenkaku, canna, wnn and
kanji character recognition inputs. Hotkeys can be configured via a
GUI configurator.

%description -l pl
im-ja to modu� wej�ciowy do wprowadzania znak�w japo�skich dla GTK2.
Aktualnie obs�uguje metody rozpoznawania znak�w hiragana, katakana,
katakana po��wkowej szeroko�ci, zenkaku, canna, wnn i kanji. Klawisze
mog� by� konfigurowane narz�dziem z graficznym interfejsem.

%prep
%setup -q

%build
%configure \
	--disable-wnn

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/immodules/*.la

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

%files
%defattr(644,root,root,755)
# COPYING contains only note about different licenses, not license text
%doc README COPYING TODO AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/gtk-2.0/*/immodules/*.so
%attr(755,root,root) %{_libdir}/im-ja
%{_datadir}/control-center-2.0/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
