Summary:	The Open Racing Car Simulator
Summary(pl):	The Open Racing Car Simulator - symulator wy¶cigów samochodowych
Name:		TORCS
Version:	1.2.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src.tgz
# Source0-md5:	5e43742b252f1e96f8d93da82b8f9fbb
Source1:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src-robots-base.tgz
# Source1-md5:	f21e4e88c2d6982efb28798d02b1c491
Source2:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src-robots-berniw.tgz
# Source2-md5:	df4588752f50eedee7aa0d6f5df74036
Source3:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src-robots-K1999.tgz
# Source3-md5:	ee6a5f0099723087585d1295a2d3b48d
Source4:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data.tgz
# Source4-md5:	b7c8729b122d1a3bc1fc563783828d12
Source5:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-tracks-base.tgz
# Source5-md5:	afb991a29f875e2030f2ad24d82d2c22
Source6:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-extra.tgz
# Source6-md5:	1b96f6f9eedda8d1857f9bd112664ab6
Source7:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-Patwo-Design.tgz
# Source7-md5:	dddb6ffec22c15a9f8c60d0c69a806cf
Source8:	%{name}.desktop
Source9:	%{name}.png
Patch0:		%{name}-inc.patch
Patch1:		%{name}-compile_fix.patch
URL:		http://torcs.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	plib-devel > 1.7.0-1
Requires:	%{name}-data = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Open Racing Car Simulator.

%description -l pl
The Open Racing Car Simulator - symulator wy¶cigów samochodowych.

%package data
Summary:	Data files for TORCS
Summary(pl):	Pliki z danymi dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}

%description data
Data files for TORCS.

%description data -l pl
Pliki z danymi dla TORCS.

%package data-tracks-base
Summary:	Base tracks data files for TORCS
Summary(pl):	Bazowe pliki z danymi o trasach dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}

%description data-tracks-base
Base tracks data files for TORCS.

%description data-tracks-base -l pl
Bazowe pliki z danymi o trasach dla TORCS.

%package data-cars-extra
Summary:	Extra cars data files for TORCS
Summary(pl):	Dodatkowe pliki z danymi o samochodach dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}

%description data-cars-extra
Extra cars data files for TORCS.

%description data-cars-extra -l pl
Bazowe pliki z danymi o trasach dla TORCS.

%package data-cars-Patwo-Design
Summary:	Patwo-Design cars data files for TORCS
Summary(pl):	Pliki z danymi o samochodach dla TORCS - Patwo-Design
Group:		X11/Applications/Games
Requires:	%{name} = %{version}

%description data-cars-Patwo-Design
Patwo-Design cars data files for TORCS.

%description data-cars-Patwo-Design -l pl
Pliki z danymi o samochodach dla TORCS - Patwo-Design.

%package robots-base
Summary:	Base robots files for TORCS
Summary(pl):	Podstawowe pliki komputerowych kierowców dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}

%description robots-base
Base robots files for TORCS.

%description robots-base -l pl
Podstawowe pliki komputerowych kierowców dla TORCS.

%package robots-berniw
Summary:	Berniw robots files for TORCS
Summary(pl):	Pliki komputerowych kierowców dla TORCS - Berniw
Group:		X11/Applications/Games
Requires:	%{name} = %{version}

%description robots-berniw
Berniw robots files for TORCS.

%description robots-berniw -l pl
Pliki komputerowych kierowców dla TORCS - Berniw.

%package robots-K1999
Summary:	K1999 robots files for TORCS
Summary(pl):	Pliki komputerowych kierowców dla TORCS - K1999
Group:		X11/Applications/Games
Requires:	%{name} = %{version}

%description robots-K1999
K1999 robots files for TORCS.

%description robots-K1999 -l pl
Pliki komputerowych kierowców dla TORCS - K1999.

%prep
%setup -q -n torcs-%{version} -a1 -a2 -a3 -a4 -a5 -a6 -a7
mv torcs-%{version}/src/drivers/* src/drivers
rm -r torcs-%{version}
%patch0 -p1
%patch1 -p1

%build
CPPFLAGS="-I/usr/X11R6/include"; export CPPFLAGS
CFLAGS="-I/usr/X11R6/include"; export CFLAGS
%{__aclocal}
%{__autoconf}
%configure \
	--x-includes=/usr/X11R6/include
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Racing,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf data cars categories tracks menu $RPM_BUILD_ROOT%{_datadir}/games/torcs
install %{SOURCE8} $RPM_BUILD_ROOT%{_applnkdir}/Games/Racing
install %{SOURCE9} $RPM_BUILD_ROOT%{_pixmapsdir}

find $RPM_BUILD_ROOT%{_datadir}/games/torcs -name "Makefile" -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.html README.linux
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_datadir}/games/torcs
%{_datadir}/games/torcs/config
%{_datadir}/games/torcs/modules
%{_datadir}/games/torcs/setup_linux.sh
%attr(755,root,root) %{_datadir}/games/torcs/torcs
%{_applnkdir}/Games/Racing/*
%{_pixmapsdir}/*

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/games/torcs/cars
%{_datadir}/games/torcs/cars/360-modena
%{_datadir}/games/torcs/cars/clkdtm
%{_datadir}/games/torcs/categories
%{_datadir}/games/torcs/data
%dir %{_datadir}/games/torcs/drivers
%{_datadir}/games/torcs/drivers/human
%{_datadir}/games/torcs/menu
%dir %{_datadir}/games/torcs/results
%{_datadir}/games/torcs/telemetry
%dir %{_datadir}/games/torcs/tracks
%dir %{_datadir}/games/torcs/tracks/dirt
%dir %{_datadir}/games/torcs/tracks/oval
%dir %{_datadir}/games/torcs/tracks/road
%{_datadir}/games/torcs/tracks/road/g-track-3
%{_datadir}/games/torcs/tracks/road/wheel-1

%files data-tracks-base
%defattr(644,root,root,755)
%{_datadir}/games/torcs/tracks/dirt/dirt-[1-6]
%{_datadir}/games/torcs/tracks/dirt/mixed-[1-2]
%{_datadir}/games/torcs/tracks/oval/a-speedway
%{_datadir}/games/torcs/tracks/oval/e-track-5
%{_datadir}/games/torcs/tracks/oval/g-track-1
%{_datadir}/games/torcs/tracks/oval/michigan
%{_datadir}/games/torcs/tracks/road/aalborg
%{_datadir}/games/torcs/tracks/road/alpine-1
%{_datadir}/games/torcs/tracks/road/e-track-[1-4]
%{_datadir}/games/torcs/tracks/road/e-track-6
%{_datadir}/games/torcs/tracks/road/eroad
%{_datadir}/games/torcs/tracks/road/g-track-2

%files data-cars-extra
%defattr(644,root,root,755)
%{_datadir}/games/torcs/cars/155-DTM
%{_datadir}/games/torcs/cars/acura-nsx-sz
%{_datadir}/games/torcs/cars/baja-bug
%{_datadir}/games/torcs/cars/buggy
%{_datadir}/games/torcs/cars/cg-nascar-rwd
%{_datadir}/games/torcs/cars/gt40
%{_datadir}/games/torcs/cars/lotus-gt1
%{_datadir}/games/torcs/cars/mclaren-f1
%{_datadir}/games/torcs/cars/porsche-gt1
%{_datadir}/games/torcs/cars/porsche-gt3rs
%{_datadir}/games/torcs/cars/viper-gts-r
%{_datadir}/games/torcs/cars/xj-220

%files data-cars-Patwo-Design
%defattr(644,root,root,755)
%{_datadir}/games/torcs/cars/206W10
%{_datadir}/games/torcs/cars/306W61
%{_datadir}/games/torcs/cars/CORW61
%{_datadir}/games/torcs/cars/EVOWRC61
%{_datadir}/games/torcs/cars/FOCW61
%{_datadir}/games/torcs/cars/SWRC62

%files robots-base
%defattr(644,root,root,755)
%{_datadir}/games/torcs/drivers/cylos1
%{_datadir}/games/torcs/drivers/damned
%{_datadir}/games/torcs/drivers/inferno*
%{_datadir}/games/torcs/drivers/lliaw
%{_datadir}/games/torcs/drivers/tanhoj
%{_datadir}/games/torcs/drivers/tita

%files robots-berniw
%defattr(644,root,root,755)
%{_datadir}/games/torcs/drivers/berniw*

%files robots-K1999
%defattr(644,root,root,755)
%{_datadir}/games/torcs/drivers/K1999
