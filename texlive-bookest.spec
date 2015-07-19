# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/bookest
# catalog-date 2008-08-17 01:00:50 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-bookest
Version:	1.1
Release:	10
Summary:	Extended book class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bookest
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookest.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookest.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class extends the standard book class, in the areas of
colour scheme management, document layout, headings and
footers, front page layout, and other minor items.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bookest/bookest.cls
%doc %{_texmfdistdir}/doc/latex/bookest/README
%doc %{_texmfdistdir}/doc/latex/bookest/bookestdoc-en.pdf
%doc %{_texmfdistdir}/doc/latex/bookest/bookestdoc-en.tex
%doc %{_texmfdistdir}/doc/latex/bookest/bookestdoc-it.pdf
%doc %{_texmfdistdir}/doc/latex/bookest/bookestdoc-it.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 749810
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 717964
- texlive-bookest
- texlive-bookest
- texlive-bookest
- texlive-bookest
- texlive-bookest

