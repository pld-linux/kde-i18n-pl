#
# Conditional build:
# --with        subpackages             Builds subpackages
#

%define         _state          stable
%define         _ver		3.1.3

%define		_topic		i18n
%define		_lang		pl
%define		_part		%{_topic}-%{_lang}

%define		_p1		kdelibs
%define		_p2		kdeaddons
%define		_p3		kdeadmin
%define		_p4		kdeartwork
%define		_p5		kdebase
%define		_p6		kdebindings
%define		_p7		kdeedu
%define		_p8		kdegames 
%define		_p9		kdegraphics
%define		_p10		kdemultimedia
%define		_p11		kdenetwork
%define		_p12		kdepim
%define		_p13		kdesdk 
%define		_p14		kdetoys
%define		_p15		kdevelop

Summary:	K Desktop Environment - Polish support
Summary(pl):	KDE - wsparcie dla jêzyka polskiego
Name:		kde-%{_part}
Version:	%{_ver}
Release:	1
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
Source0:        ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-i18n/%{name}-%{version}.tar.bz2
Source1:	kde-i18n-splitmo
Source2:	kde-i18n-splitdoc
BuildRequires:	kdelibs >= %{version}
BuildRequires:	kdelibs-devel
BuildRequires:	libxml2-progs >= 2.4.2
BuildRequires:	gettext-devel
%if %{?_with_subpackages:0}1
Conflicts:	%{_p1}-%{_part}
Conflicts:	%{_p2}-%{_part}
Conflicts:	%{_p3}-%{_part}
Conflicts:	%{_p4}-%{_part}
Conflicts:	%{_p5}-%{_part}
Conflicts:	%{_p6}-%{_part}
Conflicts:	%{_p7}-%{_part}
Conflicts:	%{_p8}-%{_part}
Conflicts:	%{_p9}-%{_part}
Conflicts:	%{_p10}-%{_part}
Conflicts:	%{_p11}-%{_part}
Conflicts:	%{_p12}-%{_part}
Conflicts:	%{_p13}-%{_part}
Conflicts:	%{_p14}-%{_part}
Conflicts:	%{_p15}-%{_part}
%endif
Conflicts:	kde-%{_topic}
Obsoletes:	kde-%{_topic}-Polish
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        %{_docdir}/kde/HTML
%define         _messagesdir    %{_datadir}/locale/%{_lang}/LC_MESSAGES

%description
K Desktop Environment - Polish support.

%description -l pl
KDE - wsparcie dla jêzyka polskiego.

%package -n %{_p1}-%{_part}
Summary:	KDE - Polish support - %{_p1}
Summary(pl):	KDE - wsparcie dla jêzyka polskiego - %{_p1}
Group:		X11/Applications
Conflicts:	kde-%{_topic}
Conflicts:	kde-%{_part}

%description -n %{_p1}-%{_part}
K Desktop Environment - Polish support - translations for %{_p1}.

%description -n %{_p1}-%{_part} -l pl 
KDE - wsparcie dla jêzyka polskiego - t³umaczenia dla %{_p1}.

%package -n %{_p2}-%{_part}
Summary:	KDE - Polish support - %{_p2}
Summary(pl):	KDE - wsparcie dla jêzyka polskiego - %{_p2}
Group:		X11/Applications
Requires:	%{_p1}-%{_part} = %{version}
Conflicts:	kde-%{_topic}
Conflicts:	kde-%{_part}

%description -n %{_p2}-%{_part}
K Desktop Environment - Polish support - translations for %{_p2}.

%description -n %{_p2}-%{_part} -l pl 
KDE - wsparcie dla jêzyka polskiego - t³umaczenia dla %{_p2}.

%package -n %{_p3}-%{_part}
Summary:	KDE - Polish support - %{_p3}
Summary(pl):	KDE - wsparcie dla jêzyka polskiego - %{_p3}
Group:		X11/Applications
Requires:	%{_p1}-%{_part} = %{version}
Conflicts:	kde-%{_topic}
Conflicts:	kde-%{_part}

%description -n %{_p3}-%{_part}
K Desktop Environment - Polish support - translations for %{_p3}.

%description -n %{_p3}-%{_part} -l pl 
KDE - wsparcie dla jêzyka polskiego - t³umaczenia dla %{_p3}.

%package -n %{_p4}-%{_part}
Summary:	KDE - Polish support - %{_p4}
Summary(pl):	KDE - wsparcie dla jêzyka polskiego - %{_p4}
Group:		X11/Applications
Requires:	%{_p1}-%{_part} = %{version}
Conflicts:	kde-%{_topic}
Conflicts:	kde-%{_part}

%description -n %{_p4}-%{_part}
K Desktop Environment - Polish support - translations for %{_p4}.

%description -n %{_p4}-%{_part} -l pl 
KDE - wsparcie dla jêzyka polskiego - t³umaczenia dla %{_p4}.

%package -n %{_p5}-%{_part}
Summary:	KDE - Polish support - %{_p5}
Summary(pl):	KDE - wsparcie dla jêzyka polskiego - %{_p5}
Group:		X11/Applications
Requires:	%{_p1}-%{_part} = %{version}
Conflicts:	kde-%{_topic}
Conflicts:	kde-%{_part}

%description -n %{_p5}-%{_part}
K Desktop Environment - Polish support - translations for %{_p5}.

%description -n %{_p5}-%{_part} -l pl 
KDE - wsparcie dla jêzyka polskiego - t³umaczenia dla %{_p5}.

%package -n %{_p6}-%{_part}
Summary:	KDE - Polish support - %{_p6}
Summary(pl):	KDE - wsparcie dla jêzyka polskiego - %{_p6}
Group:		X11/Applications
Requires:	%{_p1}-%{_part} = %{version}
Conflicts:	kde-%{_topic}
Conflicts:	kde-%{_part}

%description -n %{_p6}-%{_part}
K Desktop Environment - Polish support - translations for %{_p6}.

%description -n %{_p6}-%{_part} -l pl 
KDE - wsparcie dla jêzyka polskiego - t³umaczenia dla %{_p6}.

%package -n %{_p7}-%{_part}
Summary:	KDE - Polish support - %{_p7}
Summary(pl):	KDE - wsparcie dla jêzyka polskiego - %{_p7}
Group:		X11/Applications
Requires:	%{_p1}-%{_part} = %{version}
Conflicts:	kde-%{_topic}
Conflicts:	kde-%{_part}

%description -n %{_p7}-%{_part}
K Desktop Environment - Polish support - translations for %{_p7}.

%description -n %{_p7}-%{_part} -l pl 
KDE - wsparcie dla jêzyka polskiego - t³umaczenia dla %{_p7}.

%package -n %{_p8}-%{_part}
Summary:	KDE - Polish support - %{_p8}
Summary(pl):	KDE - wsparcie dla jêzyka polskiego - %{_p8}
Group:		X11/Applications
Requires:	%{_p1}-%{_part} = %{version}
Conflicts:	kde-%{_topic}
Conflicts:	kde-%{_part}

%description -n %{_p8}-%{_part}
K Desktop Environment - Polish support - translations for %{_p8}.

%description -n %{_p8}-%{_part} -l pl 
KDE - wsparcie dla jêzyka polskiego - t³umaczenia dla %{_p8}.

%package -n %{_p9}-%{_part}
Summary:	KDE - Polish support - %{_p9}
Summary(pl):	KDE - wsparcie dla jêzyka polskiego - %{_p9}
Group:		X11/Applications
Requires:	%{_p1}-%{_part} = %{version}
Conflicts:	kde-%{_topic}
Conflicts:	kde-%{_part}

%description -n %{_p9}-%{_part}
K Desktop Environment - Polish support - translations for %{_p9}.

%description -n %{_p9}-%{_part} -l pl 
KDE - wsparcie dla jêzyka polskiego - t³umaczenia dla %{_p9}.

%package -n %{_p10}-%{_part}
Summary:	KDE - Polish support - %{_p10}
Summary(pl):	KDE - wsparcie dla jêzyka polskiego - %{_p10}
Group:		X11/Applications
Requires:	%{_p1}-%{_part} = %{version}
Conflicts:	kde-%{_topic}
Conflicts:	kde-%{_part}

%description -n %{_p10}-%{_part}
K Desktop Environment - Polish support - translations for %{_p10}.

%description -n %{_p10}-%{_part} -l pl 
KDE - wsparcie dla jêzyka polskiego - t³umaczenia dla %{_p10}.

%package -n %{_p11}-%{_part}
Summary:	KDE - Polish support - %{_p11}
Summary(pl):	KDE - wsparcie dla jêzyka polskiego - %{_p11}
Group:		X11/Applications
Requires:	%{_p1}-%{_part} = %{version}
Conflicts:	kde-%{_topic}
Conflicts:	kde-%{_part}

%description -n %{_p11}-%{_part}
K Desktop Environment - Polish support - translations for %{_p11}.

%description -n %{_p11}-%{_part} -l pl 
KDE - wsparcie dla jêzyka polskiego - t³umaczenia dla %{_p11}.

%package -n %{_p12}-%{_part}
Summary:	KDE - Polish support - %{_p12}
Summary(pl):	KDE - wsparcie dla jêzyka polskiego - %{_p12}
Group:		X11/Applications
Requires:	%{_p1}-%{_part} = %{version}
Conflicts:	kde-%{_topic}
Conflicts:	kde-%{_part}

%description -n %{_p12}-%{_part}
K Desktop Environment - Polish support - translations for %{_p12}.

%description -n %{_p12}-%{_part} -l pl 
KDE - wsparcie dla jêzyka polskiego - t³umaczenia dla %{_p12}.

%package -n %{_p13}-%{_part}
Summary:	KDE - Polish support - %{_p13}
Summary(pl):	KDE - wsparcie dla jêzyka polskiego - %{_p13}
Group:		X11/Applications
Requires:	%{_p1}-%{_part} = %{version}
Conflicts:	kde-%{_topic}
Conflicts:	kde-%{_part}

%description -n %{_p13}-%{_part}
K Desktop Environment - Polish support - translations for %{_p13}.

%description -n %{_p13}-%{_part} -l pl 
KDE - wsparcie dla jêzyka polskiego - t³umaczenia dla %{_p13}.

%package -n %{_p14}-%{_part}
Summary:	KDE - Polish support - %{_p14}
Summary(pl):	KDE - wsparcie dla jêzyka polskiego - %{_p14}
Group:		X11/Applications
Requires:	%{_p1}-%{_part} = %{version}
Conflicts:	kde-%{_topic}
Conflicts:	kde-%{_part}

%description -n %{_p14}-%{_part}
K Desktop Environment - Polish support - translations for %{_p14}.

%description -n %{_p14}-%{_part} -l pl 
KDE - wsparcie dla jêzyka polskiego - t³umaczenia dla %{_p14}.

%package -n %{_p15}-%{_part}
Summary:	KDE - Polish support - %{_p15}
Summary(pl):	KDE - wsparcie dla jêzyka polskiego - %{_p15}
Group:		X11/Applications
Requires:       %{_p1}-%{_part} = %{version}
Conflicts:	kde-%{_topic}
Conflicts:	kde-%{_part}

%description -n %{_p15}-%{_part}
K Desktop Environment - Polish support - translations for %{_p15}.

%description -n %{_p15}-%{_part} -l pl 
KDE - wsparcie dla jêzyka polskiego - t³umaczenia dla %{_p15}.

%prep
%setup -q -n %{name}

%build

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_htmldir}

install -d $RPM_BUILD_ROOT%{_htmldir}/%{_lang}

%if %{?_with_subpackages:1}0
touch {%{_p1},%{_p2},%{_p3},%{_p4},%{_p7},%{_p5},%{_p6},%{_p8},%{_p9},%{_p10},\
%{_p11},%{_p12},%{_p13},%{_p14},%{_p15}}.cont

grep -v '^#' < %{SOURCE1} | \
while read package file ; do                                                                                    
    if [ "$package" != "" -a "$file" != "" ] ; then
	if ls $RPM_BUILD_ROOT/%{_messagesdir} |grep -q $file; then
	    echo "%{_messagesdir}/$file" >> $package.cont                                     
	fi
    fi	     
done                                                                                                            
											                                                                                                                
grep -v '^#' < %{SOURCE2} | \
while read package directory ; do
    if [ "$package" != "" -a "$directory" != "" ] ; then
	if ls $RPM_BUILD_ROOT/%{_htmldir}/%{_lang} |grep -q $directory; then
	    echo "%{_htmldir}/%{_lang}/$directory" >> $package.cont
	fi
    fi
done    	          
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{?_with_subpackages:0}1
%files
%defattr(644,root,root,755)
%{_htmldir}/%{_lang}
%{_datadir}/locale/%{_lang}/charset
%{_datadir}/locale/%{_lang}/*.*
%{_messagesdir}/* 
%else
%files -n %{_p1}-%{_part} -f %{_p1}.cont 
%defattr(644,root,root,755)
%dir %{_htmldir}/%{_lang}
%{_datadir}/locale/%{_lang}/charset
%{_datadir}/locale/%{_lang}/*.*

%files -n %{_p2}-%{_part} -f %{_p2}.cont
%defattr(644,root,root,755)

%files -n %{_p3}-%{_part} -f %{_p3}.cont
%defattr(644,root,root,755)

%files -n %{_p4}-%{_part} -f %{_p4}.cont
%defattr(644,root,root,755)

%files -n %{_p5}-%{_part} -f %{_p5}.cont
%defattr(644,root,root,755)

%files -n %{_p6}-%{_part} -f %{_p6}.cont
%defattr(644,root,root,755)

%files -n %{_p7}-%{_part} -f %{_p7}.cont
%defattr(644,root,root,755)

%files -n %{_p8}-%{_part} -f %{_p8}.cont
%defattr(644,root,root,755)

%files -n %{_p9}-%{_part} -f %{_p9}.cont
%defattr(644,root,root,755)

%files -n %{_p10}-%{_part} -f %{_p10}.cont
%defattr(644,root,root,755)

%files -n %{_p11}-%{_part} -f %{_p11}.cont
%defattr(644,root,root,755)

%files -n %{_p12}-%{_part} -f %{_p12}.cont
%defattr(644,root,root,755)

%files -n %{_p13}-%{_part} -f %{_p13}.cont
%defattr(644,root,root,755)

%files -n %{_p14}-%{_part} -f %{_p14}.cont
%defattr(644,root,root,755)

%files -n %{_p15}-%{_part} -f %{_p15}.cont
%defattr(644,root,root,755)
%endif
