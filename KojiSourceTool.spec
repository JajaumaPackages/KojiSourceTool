Name:           KojiSourceTool
Version:        1.0.0
Release:        1%{?dist}
Summary:        A source fetching tool for my build system

License:        MIT
Source0:        KojiSourceTool
Source1:        KojiSourceTool.Makefile

BuildArch:      noarch
Requires:       make
Requires:       rpmdevtools
Requires:       rpm-build

%description
%{Summary}.


%prep


%build


%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_bindir}
install -m755 %{SOURCE0} %{buildroot}%{_bindir}/KojiSourceTool
install -d -m755 %{buildroot}%{_datadir}/KojiSourceTool
install -m644 %{SOURCE1} %{buildroot}%{_datadir}/KojiSourceTool/Makefile


%files
%{_bindir}/KojiSourceTool
%dir %{_datadir}/KojiSourceTool
%{_datadir}/KojiSourceTool/Makefile


%changelog
* Sun Aug 06 2017 Jajauma's Packages <jajauma@yandex.ru> - 1.0.0-1
- Initial release
