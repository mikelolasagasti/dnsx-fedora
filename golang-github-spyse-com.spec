# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/spyse-com/go-spyse
%global goipath         github.com/spyse-com/go-spyse
Version:                1.2.4

%gometa

%global common_description %{expand:
The official wrapper for spyse.com API, written in Go, aimed to help developers
build their integrations with Spyse.}

%global golicenses      LICENSE.md
%global godocs          examples README.md

Name:           %{goname}
Release:        %autorelease
Summary:        The official wrapper for spyse.com API, written in Go, aimed to help developers build their integrations with Spyse

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
