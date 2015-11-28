
%define	module	TurboGears

Summary:	The rapid web development megaframework
Summary(pl.UTF-8):	Wielkie środowisko do szybkiego tworzenia serwisów WWW
Name:		python-TurboGears
Version:	1.0.1
Release:	4
License:	GPL
Group:		Development/Languages/Python
Source0:	http://files.turbogears.org/eggs/TurboGears-%{version}.tar.gz
# Source0-md5:	57580dce73ab2fc5c7f72e3e3cd804b1
URL:		http://www.turbogears.org/
%pyrequires_eq	python
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	python-setuptools >= 0.6a9
BuildRequires:	rpm-pythonprov
Requires:	python-FormEncode
Requires:	python-SQLObject >= 0.7.1-0.1457.0
Requires:	python-TestGears
Requires:	python-cElementTree
Requires:	python-cherrypy >= 2.1.1
Requires:	python-elementtree
Requires:	python-json-py
Requires:	python-kid
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TurboGears is the rapid web development megaframework you've been
looking for.

%description -l pl.UTF-8
TurboGears to wielkie środowisko do szybkiego tworzenia serwisów WWW.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

install -d build/scripts-%{py_ver}
%py_install \
        --single-version-externally-managed \
        --optimize 2 \
        --root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{module}*
%{py_sitescriptdir}/turbogears
