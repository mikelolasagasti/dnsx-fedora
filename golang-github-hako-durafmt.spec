# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/hako/durafmt
%global goipath         github.com/hako/durafmt
Version:                1.0.0
%global tag             1.0.0
%global commit          5c1018a4e16b9db6718f25e524de025b1fc67303

%gometa

%global common_description %{expand:
Durafmt is a tiny Go library that formats time.Duration strings into a human
readable format.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md README.md

Name:           %{goname}
Release:        9%{?dist}
Summary:        Better time duration formatting in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Tue Aug 31 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.0.0-9.20210831git5c1018a
- Update to latest git

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 15:24:19 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-2
- Update to new macros

* Wed Feb 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- First package for Fedora
