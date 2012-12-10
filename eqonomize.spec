%define name    eqonomize          
%define version 0.6                
%define release %mkrel 3
 
Name:           %name
Version:        %version
Release:        %release
Source0:        http://ovh.dl.sourceforge.net/sourceforge/eqonomize/%name-%version.tar.gz
Patch0:         eqonomize-0.6-fix-desktopfile-typo.patch
Patch1:		eqonomize-0.6-fix-docs.patch
Summary:        Personal finance program for KDE                                         
License:        GPLv2+                                                                   
Group:          Office                                                                   
Url:            http://eqonomize.sourceforge.net/                                        
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
%apply_patches
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


%changelog
* Thu Sep 10 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.6-3mdv2010.0
+ Revision: 437482
- rebuild

* Sat Feb 21 2009 Nicolas Lécureuil <neoclust@mandriva.org> 0.6-2mdv2009.1
+ Revision: 343532
- Fix a typo in the desktop file

* Wed Jan 28 2009 Anne Nicolas <anne.nicolas@mandriva.com> 0.6-1mdv2009.1
+ Revision: 334751
- imported package eqonomize


