
%define	module	TurboGears

Summary:	The rapid web development megaframework
Summary(pl):	Wielkie ¶rodowisko do szybkiego tworzenia serwisów WWW
Name:		python-TurboGears
Version:	0.8.8
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://www.turbogears.org/download/eggs/TurboGears-%{version}.tar.gz
# Source0-md5:	83be5f971d5c208c3e91e60b570cbcff
URL:		http://www.turbogears.org/
%pyrequires_eq	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools >= 0.6a9
BuildRequires:	unzip
Requires:	python-FormEncode
Requires:	python-TestGears
Requires:	python-elementtree
Requires:	python-cElementTree
Requires:	python-kid
Requires:	python-cherrypy >= 2.1.1
Requires:	python-SQLObject
Requires:	python-json-py
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TurboGears is the rapid web development megaframework you've been
looking for.

%description -l pl
TurboGears to wielkie ¶rodowisko do szybkiego tworzenia serwisów WWW.

%prep
%setup -q -n %{module}-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

install -d build/scripts-%{py_ver}
python ./setup.py install \
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
