Summary:	WebRTC Audio Processing library
Name:		webrtc-audio-processing
Version:	0.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://freedesktop.org/software/pulseaudio/webrtc-audio-processing/%{name}-%{version}.tar.xz
# Source0-md5:	da25bb27812c8404060d4cc0dc712f04
Patch0:		%{name}-link.patch
URL:		http://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebRTC is an open source project that enables web browsers with
Real-Time Communications (RTC) capabilities via simple Javascript
APIs. The WebRTC components have been optimized to best serve this
purpose. WebRTC implements the W3C's proposal for video conferencing
on the web.

%package devel
Summary:	Header files for WebRTC Audio Processing library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files needed to develop programs
which make use of WebRTC Audio Processing library.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS PATENTS README
%attr(755,root,root) %ghost %{_libdir}/libwebrtc_audio_processing.so.0
%attr(755,root,root) %{_libdir}/libwebrtc_audio_processing.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwebrtc_audio_processing.so
%{_libdir}/*.la
%{_includedir}/webrtc_audio_processing
%{_pkgconfigdir}/webrtc-audio-processing.pc

