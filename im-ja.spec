Summary:	Japanese input method for GTK2
Name:		im-ja
Version:	0.6
Release:	2
License:	LGPL
Group:		Applications/Editors
Source0:	http://im-ja.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	aeb6e5454587fd7e7a3f41629d26b914
BuildRequires:	gtk+2-devel
BuildRequires:	Canna-devel
Requires:	gtk+2 >= 2.0.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
im-ja is a Japanese input module for GTK2. Currently supports
hiragana, katakana, half-width katakana, zenkaku, canna , wnn and
kanji character recognition inputs. Hotkeys can be configured via a
GUI configurator.


%prep
%setup -q

%build
%configure --disable-wnn
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
GCONF_CONFIG_SOURCE=`%{_bindir}/gconftool-2 --get-default-source` %{_bindir}/gconftool-2 --makefile-install-rule /etc/gconf/schemas/im-ja.schemas > /dev/null

%postun -p /sbin/ldconfig
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
GCONF_CONFIG_SOURCE=`%{_bindir}/gconftool-2 --get-default-source` %{_bindir}/gconftool-2 --makefile-install-rule /etc/gconf/schemas/im-ja.schemas > /dev/null

%files
%defattr(644,root,root,755)
%doc README COPYING TODO AUTHORS ChangeLog
%{_libdir}/gtk-2.0/*
%{_libdir}/im-ja/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/control-center-2.0/*
%{_datadir}/%{name}/*
%{_mandir}/man1/*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
