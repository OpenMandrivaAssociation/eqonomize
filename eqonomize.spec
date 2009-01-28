%define name    eqonomize          
%define version 0.6                
%define release %mkrel 1           
 
Name:           %name
Version:        %version
Release:        %release
Source0:        http://ovh.dl.sourceforge.net/sourceforge/eqonomize/%name-%version.tar.gz
Summary:        Personal finance program for KDE                                         
License:        GPLv2+                                                                   
Group:          Office                                                                   
Url:            http://eqonomize.sourceforge.net/                                        
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot                      
BuildRequires:  kdelibs4-devel                                                           
 
%description
Eqonomize! is a personal accounting software, 
with focus on efficiency and ease of use for  
the small household economy. 
 
%files -f %name.lang
%defattr(-,root,root)
%_bindir/eqonomize   
%_datadir/applications/kde4/eqonomize.desktop
%_datadir/apps/eqonomize/eqonomizeui.rc      
%_datadir/icons/hicolor/128x128/apps/eqonomize.png
%_datadir/icons/hicolor/128x128/mimetypes/eqz.png 
%_datadir/icons/hicolor/16x16/apps/eqonomize.png
%_datadir/icons/hicolor/16x16/mimetypes/eqz.png
%_datadir/icons/hicolor/22x22/apps/eqonomize.png
%_datadir/icons/hicolor/22x22/mimetypes/eqz.png
%_datadir/icons/hicolor/32x32/apps/eqonomize.png
%_datadir/icons/hicolor/32x32/mimetypes/eqz.png
%_datadir/icons/hicolor/48x48/apps/eqonomize.png
%_datadir/icons/hicolor/48x48/mimetypes/eqz.png
%_datadir/icons/hicolor/64x64/apps/eqonomize.png
%_datadir/icons/hicolor/64x64/mimetypes/eqz.png
%_datadir/mimelnk/application/x-eqonomize.desktop
 
 
#--------------------------------------------------------------------
 
%prep
%setup -q -n %name-%version
 
%build
%cmake_kde4
%make
 
%install
rm -rf %{buildroot}
%{makeinstall_std} -C build
 
rm -f %buildroot%_datadir/applications/kde/*.desktop
 
%find_lang %name --with-html
 
%clean
rm -rf %{buildroot}
 
%post
%update_icon_cache hicolor
 
%postun
%clean_icon_cache hicolor
