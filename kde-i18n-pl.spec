
%define		_state		unstable
%define		_ver		3.3.92
%define		_snap		%{nil}
%define		_lang		pl

Summary:	K Desktop Environment - Polish support
Summary(pl):	KDE - wsparcie dla j�zyka polskiego
Name:		kde-i18n-%{_lang}
Version:	%{_ver}
Release:	1
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
#Source0:	ftp://ftp.pld-linux.org/software/kde/%{name}-%{_snap}.tar.bz2
Source0:	ftp://ftp.kde.org/pub/kde/unstable/%{_ver}/src/kde-i18n/%{name}-%{version}.tar.bz2
# Source0-md5:	afb1ccfc7f31d1d6462fc5a3b7253789
BuildRequires:	kdelibs-devel >= 9:3.1.93
BuildRequires:	libxml2-progs >= 1:2.6.2
BuildRequires:	gettext-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_messagesdir	%{_datadir}/locale/%{_lang}/LC_MESSAGES

%description
K Desktop Environment - Polish support.

%description -l pl
KDE - wsparcie dla j�zyka polskiego.

%prep
#%setup -q -n %{name}-%{_snap}
%setup -q

%build

%configure \
	--disable-rpath \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_kdedocdir}/%{_lang}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_kdedocdir}/%{_lang}
#%{_datadir}/locale/%{_lang}/entry.desktop
%{_datadir}/locale/%{_lang}/charset
%{_datadir}/locale/%{_lang}/*.*
%{_messagesdir}/*
