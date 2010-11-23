Summary:        Gource is a software version control visualization tool
Name:           gource
Version:        0.28
Release:        %mkrel 1
License:        GPLv3
Group:          Monitoring
URL:            http://code.google.com/p/gource/
Source0:        http://gource.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:  libSDL-devel
BuildRequires:  libSDL_image-devel
BuildRequires:  ftgl-devel
BuildRequires:  pcre-devel
BuildRequires:  png-devel
BuildRequires:  jpeg-devel
BuildRequires:	libglew-devel	
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Software projects are displayed by Gource as an animated tree with the root
directory of the project at its centre. Directories appear as branches with
files as leaves. Developers can be seen working on the tree at the times they
contributed to the project.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog README THANKS COPYING INSTALL
%{_bindir}/gource
%{_datadir}/gource
%{_mandir}/man1/gource.1*
