
%define		_state		stable
%define		_ver		3.4
%define		_snap		%{nil}
%define		_lang		pl

Summary:	K Desktop Environment - Polish support
Summary(pl):	KDE - wsparcie dla j�zyka polskiego
Name:		kde-i18n-%{_lang}
Version:	%{_ver}.0
Release:	1
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/kde-i18n/%{name}-%{version}.tar.bz2
# Source0-md5:	666b27c705a8117ab99082e9f4cddc0c
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
