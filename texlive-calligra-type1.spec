# revision 24302
# category Package
# catalog-ctan /fonts/calligra-type1
# catalog-date 2011-10-16 10:43:33 +0200
# catalog-license other-free
# catalog-version 001.000
Name:		texlive-calligra-type1
Version:	001.000
Release:	3
Summary:	Type 1 version of Caliigra
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/calligra-type1
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calligra-type1.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calligra-type1.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 001.000-2
+ Revision: 749952
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 001.000-1
+ Revision: 717996
- texlive-calligra-type1
- texlive-calligra-type1
- texlive-calligra-type1

