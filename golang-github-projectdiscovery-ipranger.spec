# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/projectdiscovery/ipranger
%global goipath         github.com/projectdiscovery/ipranger
Version:                0.0.2

%gometa

%global common_description %{expand:
IP/FQDN data structure helper with randomization of hosts and ports based on
masscan internal logic.}

%global golicenses      LICENSE
Name:           %{goname}
Release:        1%{?dist}
Summary:        IP/FQDN data structure helper with randomization of hosts and ports based on masscan internal logic

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/projectdiscovery/hmap/store/hybrid)
BuildRequires:  golang(github.com/projectdiscovery/mapcidr)
BuildRequires:  golang(github.com/yl2chen/cidranger)

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
* Mon Aug 30 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.0.2-1
- Initial package

