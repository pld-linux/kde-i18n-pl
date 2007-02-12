
%define		_state		unstable
%define		_ver		3.4.0
%define		_snap		%{nil}
%define		_lang		pl

Summary:	K Desktop Environment - Polish support
Summary(pl.UTF-8):   KDE - wsparcie dla języka polskiego
Name:		kde-i18n-%{_lang}
Version:	%{_ver}
Release:	0.rc1.1
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
#Source0:	ftp://ftp.pld-linux.org/software/kde/%{name}-%{_snap}.tar.bz2
#Source0:	ftp://ftp.kde.org/pub/kde/unstable/%{_ver}/src/kde-i18n/%{name}-%{version}.tar.bz2
Source0:	ftp://ftp.kde.org/pub/kde/unstable/%{_ver}-rc1/src/kde-i18n/%{name}-%{version}-rc1.tar.bz2
# Source0-md5:	03288300721806ba3e3faf3e37725b8d
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.1.93
BuildRequires:	libxml2-progs >= 1:2.6.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_messagesdir	%{_datadir}/locale/%{_lang}/LC_MESSAGES
%define		__unsermake	%{_datadir}/unsermake/unsermake

%description
K Desktop Environment - Polish support.

%description -l pl.UTF-8
KDE - wsparcie dla języka polskiego.

%prep
#%setup -q -n %{name}-%{_snap}
%setup -q

%build

%configure \
	--disable-rpath \
	--enable-final

%{__unsermake}

%install
rm -rf $RPM_BUILD_ROOT

%{__unsermake} install \
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
