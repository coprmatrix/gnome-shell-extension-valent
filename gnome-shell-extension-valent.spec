Name:           gnome-shell-extension-valent
Version:        0
Release:        0
Summary:        GNOME Shell integration for Valent

License:        GPLv3+
URL:            https://github.com/andyholmes/gnome-shell-extension-valent/tree/main

Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  meson

Requires:       valent


%description
Valent is an implementation of the KDE Connect protocol, built on GNOME platform
libraries.

This GNOME Shell extension helps Valent integrate with the GNOME desktop.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
%meson_test

%files -f %{name}.lang
%doc README.md
%license LICENSE
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/extensions
%{_datadir}/gnome-shell/extensions/valent@andyholmes.ca/

%changelog
