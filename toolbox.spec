Name:           toolbox-tweaked
Version:        0.0.99.5
Release:        1%{?dist}
Summary:        A tweaked toolbox binary

License:        Apache-2.0
URL:            https://github.com/firekind/toolbox
Source0:        %{name}-%{version}.tar.gz

Requires:       containers-common flatpak-session-helper glibc podman

%description
A tweaked toolbox binary

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/
cp -a * %{buildroot}

%files
%config /etc/containers/toolbox.conf
%config /etc/profile.d/toolbox.sh
/usr/share/man/man5/toolbox.conf.5.gz
/usr/share/man/man1/toolbox-init-container.1.gz
/usr/share/man/man1/toolbox-rmi.1.gz
/usr/share/man/man1/toolbox.1.gz
/usr/share/man/man1/toolbox-help.1.gz
/usr/share/man/man1/toolbox-create.1.gz
/usr/share/man/man1/toolbox-run.1.gz
/usr/share/man/man1/toolbox-list.1.gz
/usr/share/man/man1/toolbox-rm.1.gz
/usr/share/man/man1/toolbox-enter.1.gz
/usr/share/fish/vendor_completions.d/toolbox.fish
/usr/share/toolbox/test/meson.build
/usr/share/toolbox/test/system/meson.build
/usr/share/toolbox/test/system/001-version.bats
/usr/share/toolbox/test/system/201-ipc.bats
/usr/share/toolbox/test/system/libs/helpers.bash
/usr/share/toolbox/test/system/setup_suite.bash
/usr/share/toolbox/test/system/104-run.bats
/usr/share/toolbox/test/system/210-ulimit.bats
/usr/share/toolbox/test/system/105-enter.bats
/usr/share/toolbox/test/system/203-network.bats
/usr/share/toolbox/test/system/103-container.bats
/usr/share/toolbox/test/system/101-create.bats
/usr/share/toolbox/test/system/108-completion.bats
/usr/share/toolbox/test/system/107-rmi.bats
/usr/share/toolbox/test/system/102-list.bats
/usr/share/toolbox/test/system/206-user.bats
/usr/share/toolbox/test/system/002-help.bats
/usr/share/toolbox/test/system/220-environment-variables.bats
/usr/share/toolbox/test/system/README.md
/usr/share/toolbox/test/system/106-rm.bats
/usr/share/toolbox/test/system/211-dbus.bats
/usr/share/zsh/site-functions/_toolbox
/usr/share/bash-completion/completions/toolbox.bash
/usr/bin/toolbox
/usr/lib/tmpfiles.d/toolbox.conf
