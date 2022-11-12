Name:		texlive-calligra-type1
Version:	24302
Release:	1
Summary:	Type 1 version of Caliigra
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/calligra-type1
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calligra-type1.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calligra-type1.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a converstion (using mf2pt1 of Peter Vanroose's
handwriting font.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/calligra-type1/callig15.afm
%{_texmfdistdir}/fonts/map/dvips/calligra-type1/calligra.map
%{_texmfdistdir}/fonts/type1/public/calligra-type1/callig15.pfb
%doc %{_texmfdistdir}/doc/fonts/calligra-type1/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
