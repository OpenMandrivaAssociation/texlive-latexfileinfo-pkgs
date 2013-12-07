# revision 26760
# category Package
# catalog-ctan /info/latexfileinfo-pkgs
# catalog-date 2012-05-30 14:24:48 +0200
# catalog-license lppl1.3
# catalog-version 0.22
Name:		texlive-latexfileinfo-pkgs
Version:	0.22
Release:	5
Summary:	A comparison of packages showing LaTeX file information
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latexfileinfo-pkgs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexfileinfo-pkgs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexfileinfo-pkgs.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexfileinfo-pkgs.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.22-2
+ Revision: 813600
- Update to latest release.
- Import texlive-latexfileinfo-pkgs
- Import texlive-latexfileinfo-pkgs

