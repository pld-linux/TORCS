# ToDo:
# - make it compile - this one is horrible, it creates exports/include dir
#   in top source directory and puts symlinks to various *.h files there.
#   However, it does not put symlinks to plib/*.h or GL/*.h. Anyone knows
#   how to fix it? Or maybe this one should be removed from repo?
Summary:	The Open Racing Car Simulator
Summary(pl):	The Open Racing Car Simulator
Name:		TORCS
Version:	1.2.0
Release:	0.1
License:	GPL	
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src.tgz
Source1:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src-robots-base.tgz
Source2:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src-robots-berniw.tgz
Source3:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src-robots-K1999.tgz
Source4:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data.tgz
Source5:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-tracks-base.tgz
Source6:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-extra.tgz
Source7:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-Patwo-Design.tgz
Patch0:		%{name}-inc.patch
URL:		http://torcs.sourceforge.net/
BuildRequires:	plib >= 1.7.0-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix /usr/X11R6

%description

%description -l pl

%prep
%setup -q -n torcs-1.2.0 -a1 -a2 -a3 -a4 -a5 -a6
mv torcs-1.2.0/src/drivers/* src/drivers
rm -r torcs-1.2.0
%patch0 -p1

%build
CPPFLAGS="-I/usr/X11R6/include"; export CPPFLAGS
CFLAGS="-I/usr/X11R6/include"; export CFLAGS
%{__aclocal}
%{__autoconf}
%configure \
	--x-includes=%{_prefix}/include
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
cp -rf data cars categories tracks menu $RPM_BUILD_ROOT%{_datadir}/games/torcs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.html README.linux
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/games/torcs
%{_datadir}/games/torcs/cars/
%{_datadir}/games/torcs/categories/
%{_datadir}/games/torcs/config/
%{_datadir}/games/torcs/data/
%{_datadir}/games/torcs/drivers/
%{_datadir}/games/torcs/menu/
%{_datadir}/games/torcs/modules/
%{_datadir}/games/torcs/results/
%{_datadir}/games/torcs/telemetry/
%{_datadir}/games/torcs/tracks/
%{_datadir}/games/torcs/setup_linux.sh
%attr(755,root,root) %{_datadir}/games/torcs/torcs
%{_libdir}/lib*.so
