%global tl_name bookest
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Extended book class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bookest
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bookest.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bookest.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class extends the standard book class, in the areas of colour scheme
management, document layout, headings and footers, front page layout,
and other minor items.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bookest
%dir %{_datadir}/texmf-dist/tex/latex/bookest
%doc %{_datadir}/texmf-dist/doc/latex/bookest/README
%doc %{_datadir}/texmf-dist/doc/latex/bookest/bookestdoc-en.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookest/bookestdoc-en.tex
%doc %{_datadir}/texmf-dist/doc/latex/bookest/bookestdoc-it.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookest/bookestdoc-it.tex
%{_datadir}/texmf-dist/tex/latex/bookest/bookest.cls
