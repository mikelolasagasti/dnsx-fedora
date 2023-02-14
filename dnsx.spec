# Generated by go2rpm 1.8.2
%bcond_without check

# https://github.com/projectdiscovery/dnsx
%global goipath         github.com/projectdiscovery/dnsx
Version:                1.1.2

%gometa -f

%global goname          dnsx

%global common_description %{expand:
Dnsx is a fast and multi-purpose DNS toolkit allow to run multiple DNS queries
of your choice with a list of user-supplied resolvers.}

%global golicenses      LICENSE.md
%global godocs          SECURITY.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Dnsx is a fast and multi-purpose DNS toolkit

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/dnsx %{goipath}/cmd/dnsx

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
%doc SECURITY.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
