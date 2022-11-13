Name:		texlive-latexfileinfo-pkgs
Version:	26760
Release:	1
Summary:	A comparison of packages showing LaTeX file information
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latexfileinfo-pkgs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexfileinfo-pkgs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexfileinfo-pkgs.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexfileinfo-pkgs.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an HTML file that lists and compares CTAN
packages that display LaTeX source file information from
\ProvidesClass, \ProvidesFile, and \ProvidesPackage commands in
the LaTeX file. Five packages of the author's, and several
other packages are discussed; revision control systems are
mentioned briefly.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/latexfileinfo-pkgs/latexfileinfo_pkgs.RLS
%doc %{_texmfdistdir}/doc/latex/latexfileinfo-pkgs/README
%doc %{_texmfdistdir}/doc/latex/latexfileinfo-pkgs/latexfileinfo_pkgs.htm
#- source
%doc %{_texmfdistdir}/source/latex/latexfileinfo-pkgs/SrcFILEs.txt
%doc %{_texmfdistdir}/source/latex/latexfileinfo-pkgs/latexfileinfo_pkgs.tex
%doc %{_texmfdistdir}/source/latex/latexfileinfo-pkgs/mkht_ltxfinfo_pkgs.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
