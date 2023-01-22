Summary:        Software version control visualization tool
Name:           gource
Version:        0.54
Release:        1
License:        GPLv3
Group:          Monitoring
URL:            http://gource.io
Source0:	https://github.com/acaudwell/Gource/releases/download/gource-%{version}/gource-%{version}.tar.gz
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  ftgl-devel
BuildRequires:  pcre-devel
BuildRequires:  png-devel
BuildRequires:  jpeg-devel
BuildRequires:	pkgconfig(glew)
BuildRequires:	boost-devel
BuildRequires:	glm-devel

%description
Software projects are displayed by Gource as an animated tree with the root
directory of the project at its centre. Directories appear as branches with
files as leaves. Developers can be seen working on the tree at the times they
contributed to the project.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%doc ChangeLog README THANKS COPYING INSTALL
%{_bindir}/gource
%{_datadir}/gource
%{_mandir}/man1/gource.1*
