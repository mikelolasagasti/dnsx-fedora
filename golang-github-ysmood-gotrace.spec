# Generated by go2rpm 1.8.2
%bcond_without check
%global debug_package %{nil}

# https://github.com/ysmood/gotrace
%global goipath         github.com/ysmood/gotrace
Version:                0.6.0

%gometa -f

%global common_description %{expand:
A lib for monitoring runtime goroutine stack.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        A lib for monitoring runtime goroutine stack

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
export GODEBUG="tracebackancestors=1000"
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
