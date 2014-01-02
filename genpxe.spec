%define	_source_filedigest_algorithm	md5
%define	_binary_filedigest_algorithm	md5

Summary: Generate pxe configs and ethers from nodes.conf
Name: genpxe
Version: 1.0
Release: 1%{?dist}
Group: Applications/System
Source0: genpxe
Source1: pxe-template.conf
BuildRoot: %{_tmppath}/%{name}-%{version}-root
License: Modified BSD
BuildArch: noarch
Packager: ben@lanl.gov
Prefix: %{_bindir}
Prefix: %{_sysconfdir}

%description
genpxe generates the appropriate tftp pxe files based off of definitions
in the /etc/nodes.conf file.  The configuration file defines the template
for generating the files.  This will also generate the /etc/ethers file 
for dnsmasq.

# no prep required
#%setup

# no build required
#%build

%install
umask 022
%{__rm} -rf $RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 0750 %SOURCE0 $RPM_BUILD_ROOT%{_bindir}/genpxe

%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}
%{__install} -m 0644 %SOURCE1 $RPM_BUILD_ROOT%{_sysconfdir}/pxe-template.conf

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(0750,root,root) %{_bindir}/genpxe
%config %{_sysconfdir}/pxe-template.conf

%changelog
* Fri Oct 4 2013 Ben McClelland <ben@lanl.gov> 1.0-1
- First cut.
