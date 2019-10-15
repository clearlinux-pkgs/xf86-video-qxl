#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA9D8C21429AC6C82 (teuf@gnome.org)
#
Name     : xf86-video-qxl
Version  : 0.1.5
Release  : 26
URL      : http://xorg.freedesktop.org/releases/individual/driver/xf86-video-qxl-0.1.5.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/driver/xf86-video-qxl-0.1.5.tar.bz2
Source99 : http://xorg.freedesktop.org/releases/individual/driver/xf86-video-qxl-0.1.5.tar.bz2.sig
Summary  : Xorg X11 qxl video driver
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

%description
The QXL virtual GPU is found in the RedHat Enterprise
Virtualisation system, and also in the spice project.

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
%setup -q -n xf86-video-qxl-0.1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557105316
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1557105316
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-video-qxl
cp COPYING %{buildroot}/usr/share/package-licenses/xf86-video-qxl/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/drivers/qxl_drv.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xf86-video-qxl/COPYING
