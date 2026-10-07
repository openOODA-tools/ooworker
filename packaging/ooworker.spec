Name:           ooworker
Version:        0.1.0
Release:        1%{?dist}
Summary:        Micro-task scheduling worker communicating over stdio pipes with capability constraints.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooworker
Source0:        ooworker-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooworker is a sovereign, capability-bounded TASK RUNNER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooworker
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooworker-uninstall

%files
/usr/bin/ooworker
/usr/bin/ooworker-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
