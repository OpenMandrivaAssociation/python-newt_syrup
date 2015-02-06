Summary:       Newt Syrup is an app framework built on top of Newt
Name:          python-newt_syrup
Version:       0.2.0
Release:       2
License:       LGPLv2+
Url:           http://newt-syrup.fedorahosted.org/
Source0:        http://mcpierce.fedorapeople.org/rpms/newt_syrup-%{version}.tar.gz
Group:         Development/Python
BuildArch:     noarch
Requires:      newt >= 0.52.11
BuildRequires: python-devel python-setuptools

%description
Newt Syrup is an app framework built on top of Newt. It provides a set of
classes for creating text-based applications. Developers can use the widgets
provided by Newt and the framework provided by Syrup to create full text-based
applications in Python.

%prep
%setup -q -n newt_syrup-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS ChangeLog COPYING
%{python_sitelib}/*


%changelog
* Fri May 25 2012 Guilherme Moro <guilherme@mandriva.com> 0.2.0-1
+ Revision: 800561
- imported package python-newt_syrup

