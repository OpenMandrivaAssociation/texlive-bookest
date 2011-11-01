Name:		texlive-bookest
Version:	1.1
Release:	1
Summary:	Extended book class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bookest
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookest.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookest.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The class extends the standard book class, in the areas of
colour scheme management, document layout, headings and
footers, front page layout, and other minor items.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
