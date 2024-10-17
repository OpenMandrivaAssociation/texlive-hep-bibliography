Name:		texlive-hep-bibliography
Version:	67632
Release:	1
Summary:	An acronym extension for glossaries
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hep-bibliography
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-bibliography.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-bibliography.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-bibliography.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The hep-bibliography package extends the BibLaTeX package with
some functionality mostly useful for high energy physics. In
particular it makes full use of all BibTeX fields provided by
Discover High-Energy Physics. The package is loaded with
\usepackage{hep-bibliography}.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hep-bibliography
%{_texmfdistdir}/tex/latex/hep-bibliography
%doc %{_texmfdistdir}/doc/latex/hep-bibliography

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
