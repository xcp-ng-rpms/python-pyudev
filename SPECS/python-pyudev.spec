%global package_speccommit fbd001d9ec9f7ae9db85640d211455005a917086
%global usver 0.21.0
%global xsver 2
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global srcname pyudev
Name:             python-%{srcname}
Version:          0.21.0
Release:          %{?xsrel}%{?dist}
Summary:          A libudev binding

License:          LGPLv2+
URL:              http://pypi.python.org/pypi/pyudev
Source0: pyudev-0.21.0.tar.gz

BuildArch:        noarch

%description
pyudev is a LGPL licensed, pure Python binding for libudev, the device
and hardware management and information library for Linux.  It supports
almost all libudev functionality, you can enumerate devices, query device
properties and attributes or monitor devices, including asynchronous
monitoring with threads, or within the event loops of Qt, Glib or wxPython.

The binding supports CPython 2 (2.6 or newer) and 3 (3.1 or newer), and
PyPy 1.5 or newer.  It is tested against udev 151 or newer, earlier
versions of udev as found on dated Linux systems may work, but are not
officially supported.

%if 0%{?xenserver} < 9
%package -n python2-%{srcname}
Summary:          A libudev binding
Provides:         python-%{srcname} = %{version}-%{release}

BuildRequires:    python2-devel
BuildRequires:    python2-setuptools

# Dependencies for libraries loaded through ctypes
# glibc is needed for pipe2. This is not needed in the python3 package.
Requires:         glibc

# Needed for libudev
Requires:         systemd-libs

# Used for python2/3 compatibility
Requires:         python-six

%description -n python2-%{srcname}
pyudev is a LGPL licensed, pure Python binding for libudev, the device
and hardware management and information library for Linux.  It supports
almost all libudev functionality, you can enumerate devices, query device
properties and attributes or monitor devices, including asynchronous
monitoring with threads, or within the event loops of Qt, Glib or wxPython.

The binding supports CPython 2 (2.6 or newer) and 3 (3.1 or newer), and
PyPy 1.5 or newer.  It is tested against udev 151 or newer, earlier
versions of udev as found on dated Linux systems may work, but are not
officially supported.
%endif

%package -n python3-%{srcname}
Summary:          A libudev binding
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:    python3-devel
BuildRequires:    python3-setuptools

# Needed for libudev, loaded through ctypes
Requires:         systemd-libs

# Used for python2/3 compatibility
Requires:         python3-six

%description -n python3-%{srcname}
pyudev is a LGPL licensed, pure Python binding for libudev, the device
and hardware management and information library for Linux.  It supports
almost all libudev functionality, you can enumerate devices, query device
properties and attributes or monitor devices, including asynchronous
monitoring with threads, or within the event loops of Qt, Glib or wxPython.

The binding supports CPython 2 (2.6 or newer) and 3 (3.1 or newer), and
PyPy 1.5 or newer.  It is tested against udev 151 or newer, earlier
versions of udev as found on dated Linux systems may work, but are not
officially supported.


%prep
%autosetup -n %{srcname}-%{version}
rm -rf pyudev.egg-info

%build
%if 0%{?xenserver} < 9
%py2_build
%endif
%py3_build

%install
%if 0%{?xenserver} < 9
%py2_install
%endif
%py3_install

%if 0%{?xenserver} < 9
%files -n python2-%{srcname}
%license COPYING
%doc README.rst CHANGES.rst
%{python2_sitelib}/pyudev/
%{python2_sitelib}/pyudev-%{version}-*.egg-info
%exclude %{python2_sitelib}/pyudev/glib.py*
%exclude %{python2_sitelib}/pyudev/pyqt4.py*
%exclude %{python2_sitelib}/pyudev/pyqt5.py*
%exclude %{python2_sitelib}/pyudev/pyside.py*
%exclude %{python2_sitelib}/pyudev/wx.py*
%endif

%files -n python3-%{srcname}
%license COPYING
%doc README.rst CHANGES.rst
%{python3_sitelib}/pyudev
%{python3_sitelib}/pyudev-%{version}-*.egg-info
%exclude %{python3_sitelib}/pyudev/glib.py
%exclude %{python3_sitelib}/pyudev/__pycache__/glib.*
%exclude %{python3_sitelib}/pyudev/pyqt4.py
%exclude %{python3_sitelib}/pyudev/__pycache__/pyqt4.*
%exclude %{python3_sitelib}/pyudev/pyqt5.py
%exclude %{python3_sitelib}/pyudev/__pycache__/pyqt5.*
%exclude %{python3_sitelib}/pyudev/pyside.py
%exclude %{python3_sitelib}/pyudev/__pycache__/pyside.*
%exclude %{python3_sitelib}/pyudev/wx.py
%exclude %{python3_sitelib}/pyudev/__pycache__/wx.*

%changelog
* Mon Mar 18 2024 Alex Brett <alex.brett@cloud.com> - 0.21.0-2
- CA-390424: Add missing version-release to the python-pyudev provide

* Thu Feb 01 2024 Fei Su <fei.su@cloud.com> - 0.21.0-1
- Downgrade version for py2+py3 compatible

* Wed Jul 12 2023 Lin Liu <lin.liu@citrix.com> - 0.23.2-1
- First imported release
