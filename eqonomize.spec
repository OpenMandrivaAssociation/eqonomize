%define debug_package %{nil}

Name:           eqonomize
Version:        1.5.6
Release:        1
Source0:	https://github.com/Eqonomize/eqonomize/releases/download/v%{version}/%{name}-%{version}.tar.gz
Summary:        Personal finance program for KDE                                         
License:        GPLv2+                                                                   
Group:          Office                                                                   
Url:            https://eqonomize.github.io
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Charts)
 
%description
Eqonomize! is a personal accounting software, 
with focus on efficiency and ease of use for  
the small household economy. 
 
%files 
%_bindir/eqonomize   
%_datadir/applications/eqonomize.desktop
%_datadir/icons/*/*/*/*.png
%_datadir/icons/*/*/*/*.svg
%_datadir/%{name} 
%_datadir/mime/packages/%{name}.xml
%_docdir/%{name} 
%{_mandir}/man1/%{name}.1.*
#--------------------------------------------------------------------
 
%prep
%autosetup -p1

%build
%qmake_qt5 PREFIX=%{buildroot}%{_prefix}
%make_build
 
%install
%make_install
 
