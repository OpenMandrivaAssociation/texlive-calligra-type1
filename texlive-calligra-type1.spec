%global tl_name calligra-type1
%global tl_revision 24302
%global tl_version 001.000

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Type 1 version of Calligra
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/calligra-type1
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/calligra-type1.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/calligra-type1.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This is a conversion (using mf2pt1) of Peter Vanroose's handwriting
font.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from calligra-type1:
Map calligra.map
TL_DROPIN_EOF
