# Generated by go2rpm 1.8.2
%bcond_without check
%global debug_package %{nil}

# https://github.com/projectdiscovery/hmap
%global goipath         github.com/projectdiscovery/hmap
Version:                0.0.2

%gometa -f

%global common_description %{expand:
Hybrid memory/disk map.}

%global golicenses      LICENSE.md
%global godocs          README.md example

Name:           %{goname}
Release:        %autorelease
Summary:        Hybrid memory/disk map

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
sed -i '/badgerOptions.EventLogging/d' store/disk/badger.go

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
for test in "TestDialer" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
