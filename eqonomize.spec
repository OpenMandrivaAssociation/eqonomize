%define debug_package %{nil}

Name:           eqonomize
Version:        1.2
Release:        1
Source0:	https://github.com/Eqonomize/eqonomize/releases/download/v1.2.0/%{name}-%{version}.tar.gz
Summary:        Personal finance program for KDE                                         
License:        GPLv2+                                                                   
Group:          Office                                                                   
Url:            https://eqonomize.sourceforge.net/                                        
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
#--------------------------------------------------------------------
 
%prep
%setup -q -n %name-%version
%autopatch -p1
%build
%qmake_qt5 PREFIX=%{buildroot}%{_prefix}
%make
 
%install
%{makeinstall_std}
 
