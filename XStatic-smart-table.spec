#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-smart-table
Version  : 1.4.13.2
Release  : 14
URL      : http://pypi.debian.net/XStatic-smart-table/XStatic-smart-table-1.4.13.2.tar.gz
Source0  : http://pypi.debian.net/XStatic-smart-table/XStatic-smart-table-1.4.13.2.tar.gz
Summary  : smart-table 1.4.13 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-smart-table-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
XStatic-smart-table
-------------------
smart-table javascript library packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-smart-table package.
Group: Default
Provides: xstatic-smart-table-python

%description python
python components for the XStatic-smart-table package.


%prep
%setup -q -n XStatic-smart-table-1.4.13.2

%build
export LANG=C
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
