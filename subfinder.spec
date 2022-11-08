# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/projectdiscovery/subfinder
%global goipath         github.com/projectdiscovery/subfinder
Version:                2.5.3

%gometa

%global goname          subfinder

%global common_description %{expand:
Subfinder is a subdomain discovery tool that discovers valid subdomains for
websites. Designed as a passive framework to be useful for bug bounties and
safe for penetration testing.}

%global golicenses      LICENSE.md
%global godocs          THANKS.md README.md DISCLAIMER.md

Name:           %{goname}
Release:        %autorelease
Summary:        A subdomain discovery tool that discovers valid subdomains for websites

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

%build
%gobuild -o %{gobuilddir}/bin/subfinder %{goipath}/v2/cmd/subfinder/

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE.md
%doc THANKS.md README.md DISCLAIMER.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
