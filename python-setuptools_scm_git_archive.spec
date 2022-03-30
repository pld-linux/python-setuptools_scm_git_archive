#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	setuptools_scm plugin for git archives
Summary(pl.UTF-8):	Wtyczka setuptools_scm do archiwów gita
Name:		python-setuptools_scm_git_archive
Version:	1.1
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/setuptools_scm_git_archive/
Source0:	https://files.pythonhosted.org/packages/source/s/setuptools_scm_git_archive/setuptools_scm_git_archive-%{version}.tar.gz
# Source0-md5:	1c9351fa5cebd12e76488737a7c78f2e
URL:		https://pypi.org/project/setuptools_scm_git_archive/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a setuptools_scm plugin that adds support for git archives
(for example the ones GitHub automatically generates).

%description -l pl.UTF-8
Ten moduł to wtyczka setuptools_scm, dodająca obsługę archiwów git
(np. takich, jak automatycznie generowane przez GitHuba).

%package -n python3-setuptools_scm_git_archive
Summary:	setuptools_scm plugin for git archives
Summary(pl.UTF-8):	Wtyczka setuptools_scm do archiwów gita
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-setuptools_scm_git_archive
This is a setuptools_scm plugin that adds support for git archives
(for example the ones GitHub automatically generates).

%description -n python3-setuptools_scm_git_archive -l pl.UTF-8
Ten moduł to wtyczka setuptools_scm, dodająca obsługę archiwów git
(np. takich, jak automatycznie generowane przez GitHuba).

%prep
%setup -q -n setuptools_scm_git_archive-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/setuptools_scm_git_archive
%{py_sitescriptdir}/setuptools_scm_git_archive-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-setuptools_scm_git_archive
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/setuptools_scm_git_archive
%{py3_sitescriptdir}/setuptools_scm_git_archive-%{version}-py*.egg-info
%endif
