#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : xf86-video-qxl
Version  : 0.1.6
Release  : 439
URL      : https://www.x.org/releases/individual/driver/xf86-video-qxl-0.1.6.tar.xz
Source0  : https://www.x.org/releases/individual/driver/xf86-video-qxl-0.1.6.tar.xz
Source1  : https://www.x.org/releases/individual/driver/xf86-video-qxl-0.1.6.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xf86-video-qxl-lib = %{version}-%{release}
Requires: xf86-video-qxl-license = %{version}-%{release}
BuildRequires : libXfont-dev
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(spice-protocol)
BuildRequires : pkgconfig(spice-server)
BuildRequires : pkgconfig(xfont2)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
1. Introduction
2. Building
2.1 Building from source on fedora
2.2 Building from source with your own Xserver
3. Running

%package lib
Summary: lib components for the xf86-video-qxl package.
Group: Libraries
Requires: xf86-video-qxl-license = %{version}-%{release}

%description lib
lib components for the xf86-video-qxl package.


%package license
Summary: license components for the xf86-video-qxl package.
Group: Default

%description license
license components for the xf86-video-qxl package.


%prep
%setup -q -n xf86-video-qxl-0.1.6
cd %{_builddir}/xf86-video-qxl-0.1.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1674573709
export GCC_IGNORE_WERROR=1
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1674573709
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-video-qxl
cp %{_builddir}/xf86-video-qxl-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xf86-video-qxl/4ab212b66c904975518d1ec36c463522202794e9 || :
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/drivers/qxl_drv.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xf86-video-qxl/4ab212b66c904975518d1ec36c463522202794e9
