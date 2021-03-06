# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/projectdiscovery/mapcidr
%global goipath         github.com/projectdiscovery/mapcidr
Version:                0.0.8

%gometa

%global common_description %{expand:
Small utility program to perform multiple operations for a given subnet/CIDR
ranges.}

%global golicenses      LICENSE.MD
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Small utility program to perform multiple operations for a given subnet/CIDR ranges

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/projectdiscovery/blackrock)
BuildRequires:  golang(github.com/projectdiscovery/gologger)
BuildRequires:  golang(github.com/projectdiscovery/gologger/levels)
BuildRequires:  golang(github.com/projectdiscovery/ipranger)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE.MD
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Aug 30 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.0.8-1%{?dist}
- Initial package

