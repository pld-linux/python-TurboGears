
%define	module	TurboGears

Summary:	The rapid web development megaframework
Summary(pl):	Wielkie ¶rodowisko do szybkiego tworzenia serwisów WWW
Name:		python-TurboGears
Version:	0.8a5
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://www.turbogears.org/download/eggs/TurboGears-0.8a5.tar.gz
# Source0-md5:	ff1c1737fac46eb7ec931c05c461bc68
URL:		http://www.turbogears.org/
%pyrequires_eq	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	unzip
Requires:	python-FormEncode
Requires:	python-TestGears
Requires:	python-cElementTree
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TurboGears is the rapid web development megaframework you've been
looking for.

%description -l pl
TurboGears to wielkie ¶rodowisko do szybkiego tworzenia serwisów WWW.

%prep
%setup  -q -c

%install
rm -rf $RPM_BUILD_ROOT

%{_bindir}/easy_install \
        --no-deps \
        --script-dir="$RPM_BUILD_ROOT%{_bindir}" \
        --install-dir="$RPM_BUILD_ROOT%{py_sitescriptdir}" \
        --always-unzip \
        %{SOURCE0}

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

echo '%{module}-%{version}-py%{py_ver}.egg' > $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}.pth

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{module}*
