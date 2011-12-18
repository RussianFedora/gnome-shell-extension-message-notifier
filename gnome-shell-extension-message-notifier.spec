Name:           gnome-shell-extension-message-notifier
Version:        0.0.0
Release:        0.2.e97f54acaf9git%{?dist}.R
Summary:        Empathy notifier for GNOME Shell
Group:          User Interface/Desktops
License:        GPLv2+ 
URL:            http://cgit.collabora.com/git/user/bari/shell-message-notifier.git/

Source0:        shell-message-notifier.tar.bz2
Source1:        message-notifier
Source2:        message-notifier.desktop

Requires:       gnome-shell
BuildArch:      noarch


%description
This is a simple hack to avoid missing IM messages.


%prep
%setup -q -n shell-message-notifier


%build


%install
rm -rf $RPM_BUILD_ROOT
install -dD $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/message-notifier@shell-extensions.barisione.org
install -m 644 extension.js metadata.json notification-icon.jpg stylesheet.css \
    $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/message-notifier@shell-extensions.barisione.org

install -dD $RPM_BUILD_ROOT%{_bindir}
install -dD $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart

install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README COPYING AUTHORS
%{_sysconfdir}/xdg/autostart/*.desktop
%{_bindir}/message-notifier
%{_datadir}/gnome-shell/extensions/*


%changelog
* Sun Dec 18 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.0.0-0.2.e97f54acaf9git.R
- added autostart restart script to place extension extreme to the left

* Fri Dec 16 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.0.0-0.1.e97f54acaf9git.R
- initial build
