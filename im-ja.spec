Summary:	Japanese input method for GTK2
Name:		im-ja
Version:	0.6
Release:	1
License:	LGPL
Group:		Applications/Editors
Source0:	http://im-ja.sourceforge.net/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gtk2 >= 2.0.6
BuildPrereq:	gtk2-devel

%description
im-ja is a Japanese input module for GTK2. Currently supports
hiragana, katakana, half-width katakana, zenkaku, canna , wnn and
kanji character recognition inputs. Hotkeys can be configured via a
GUI configurator.


%prep
%setup -q

%build
./configure \
--prefix=%{_prefix} \
	--mandir=%{_mandir} \
--sysconfdir=%{_sysconfdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
GCONF_CONFIG_SOURCE=`%{_bindir}/gconftool-2 --get-default-source`%{_bindir}/gconftool-2 --makefile-install-rule /etc/gconf/schemas/im-ja.schemas > /dev/null

%postun -p /sbin/ldconfig
%{_bindir}/gtk-query-immodules-2.0 > %{_sysconfdir}/gtk-2.0/gtk.immodules
GCONF_CONFIG_SOURCE=`%{_bindir}/gconftool-2 --get-default-source`%{_bindir}/gconftool-2 --makefile-install-rule /etc/gconf/schemas/im-ja.schemas > /dev/null

%files
%defattr(644,root,root,755)
%doc README COPYING TODO AUTHORS ChangeLog
%{_libdir}/gtk-2.0/*
%{_libdir}/im-ja/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/control-center-2.0/*
%{_datadir}/im-ja/*
%{_mandir}/man1/*
