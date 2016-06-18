%define __conf_dir %{_sysconfdir}/nodeconductor/valimo

Name: nodeconductor-auth-valimo
Summary: NodeConductor Valimo authentication plugin
Group: Development/Libraries
Version: 0.1.0
Release: 1.el7
License: Copyright 2016 OpenNode LLC.  All rights reserved.
Url: http://nodeconductor.com
Source0: %{name}-%{version}.tar.gz

Requires: nodeconductor >= 0.96.0
Requires: python-lxml >= 3.2.0

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: python-setuptools

%description
NodeConductor plugin bringing OpenID-based authentication support.

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=INSTALLED_FILES

mkdir -p %{buildroot}%{__conf_dir}
echo "%{__conf_dir}" >> INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Mon May 9 2016 Juri Hudolejev <juri@opennodecloud.com> - 0.1.0-1.el7
- Initial version of the package
