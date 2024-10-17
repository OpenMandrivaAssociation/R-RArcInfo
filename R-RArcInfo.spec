%global packname  RArcInfo
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.4_12
Release:          2
Summary:          Functions to import data from Arc/Info V7.x binary coverages
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-12.tar.gz
Requires:         R-RColorBrewer 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-RColorBrewer

%description
This package uses the functions written by Daniel Morissette
<danmo@videotron.ca> to read geographical information in Arc/Info V 7.x
format and E00 files to import the coverages into R variables.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/exampleData
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
