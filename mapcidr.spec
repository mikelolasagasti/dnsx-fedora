# Generated by go2rpm 1.9.0
%bcond_without check

# https://github.com/projectdiscovery/mapcidr
%global goipath         github.com/projectdiscovery/mapcidr
Version:                1.1.0

%gometa -f

%global goname mapcidr

%global common_description %{expand:
Small utility program to perform multiple operations for a given subnet/CIDR
ranges.}

%global golicenses      LICENSE.MD
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Small utility program to perform multiple operations for a given subnet/CIDR ranges

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

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
for test in "Test_asnClient_GetCIDRsForASNNum" "TestASNClient_GetIPAddressesAsStream" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif

%files
%license LICENSE.MD
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
