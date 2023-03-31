Name:		texlive-bookest
Version:	15878
Release:	2
Summary:	Extended book class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bookest
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookest.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookest.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
