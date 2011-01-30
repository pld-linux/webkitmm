Summary:	A C++ interface for the Webkit/GTK+
Name:		webkitmm
Version:	1.1.6
Release:	1
License:	LGPL v2.1
Group:		X11/Libraries
Source0:	http://gitorious.org/webkitmm/jeremy-fixes/archive-tarball/5767d552
# Source0-md5:	e3d6fe2ec250a5b41a01100cdc3b1a8d
URL:		http://gitorious.org/webkitmm
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	glibmm-devel >= 2.16.0
BuildRequires:	gtk-webkit-devel >= 1.1.7
BuildRequires:	gtkmm-devel >= 2.10.0
BuildRequires:	libtool
BuildRequires:	mm-common
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The webkitmm project provides C++ bindings for Webkit/GTK+. This gives
you a comfortable C++ API and allows webkit to be integrated
seamlessly with gtkmm.

%package devel
Summary:	webkitmm header files
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm-devel >= 2.16.0
Requires:	gtk-webkit-devel >= 1.1.7
Requires:	gtkmm-devel >= 2.10.0

%description devel
Header files for webkitmm library.

%package doc
Summary:	Reference documentation for webkitmm
Group:		Documentation
Requires:	devhelp

%description doc
Reference documentation for webkitmm.

%prep
%setup -q -n %{name}-jeremy-fixes

%build
mm-common-prepare --force --copy
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-maintainer-mode

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libwebkitmm-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwebkitmm-1.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwebkitmm-1.0.so
%{_libdir}/libwebkitmm-1.0.la
%{_libdir}/webkitmm-1.0
%{_includedir}/webkitmm-1.0
%{_pkgconfigdir}/webkitmm-1.0.pc

%files doc
%defattr(644,root,root,755)
%{_docdir}/webkitmm-1.0
%{_datadir}/devhelp/books/webkitmm-1.0
