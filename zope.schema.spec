#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.schema
Version  : 4.5.0
Release  : 5
URL      : https://pypi.debian.net/zope.schema/zope.schema-4.5.0.tar.gz
Source0  : https://pypi.debian.net/zope.schema/zope.schema-4.5.0.tar.gz
Summary  : zope.interface extension for defining data schemas
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.schema-legacypython
Requires: zope.schema-python3
Requires: zope.schema-python
Requires: Sphinx
Requires: setuptools
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
===============

%package legacypython
Summary: legacypython components for the zope.schema package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the zope.schema package.


%package python
Summary: python components for the zope.schema package.
Group: Default
Requires: zope.schema-legacypython
Requires: zope.schema-python3

%description python
python components for the zope.schema package.


%package python3
Summary: python3 components for the zope.schema package.
Group: Default
Requires: python3-core

%description python3
python3 components for the zope.schema package.


%prep
%setup -q -n zope.schema-4.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512080935
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1512080935
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
