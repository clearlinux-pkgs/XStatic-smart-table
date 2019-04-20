#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-smart-table
Version  : 1.4.13.2
Release  : 17
URL      : http://pypi.debian.net/XStatic-smart-table/XStatic-smart-table-1.4.13.2.tar.gz
Source0  : http://pypi.debian.net/XStatic-smart-table/XStatic-smart-table-1.4.13.2.tar.gz
Summary  : smart-table 1.4.13 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-smart-table-python3
Requires: XStatic-smart-table-python
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
XStatic-smart-table
        -------------------
        
        smart-table javascript library packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package
        `XStatic`.

%package python
Summary: python components for the XStatic-smart-table package.
Group: Default
Requires: XStatic-smart-table-python3
Provides: xstatic-smart-table-python

%description python
python components for the XStatic-smart-table package.


%package python3
Summary: python3 components for the XStatic-smart-table package.
Group: Default
Requires: python3-core

%description python3
python3 components for the XStatic-smart-table package.


%prep
%setup -q -n XStatic-smart-table-1.4.13.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532216117
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
