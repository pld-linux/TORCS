Summary:	The Open Racing Car Simulator
Summary(pl.UTF-8):	The Open Racing Car Simulator - symulator wyścigów samochodowych
Name:		TORCS
Version:	1.3.0
Release:	2
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src.tgz
# Source0-md5:	915c89f9d3618d13dddd5bfb4d199539
Source1:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src-robots-base.tgz
# Source1-md5:	da007d61447f38fbdbd22aec029cc26c
Source2:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src-robots-berniw.tgz
# Source2-md5:	abeb72ba3913ef0bde727fdaa9699eef
Source3:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src-robots-bt.tgz
# Source3-md5:	ca8506aecc30bee308a5e198304b71b2
Source4:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src-robots-olethros.tgz
# Source4-md5:	227d47687b821298fe6b2f147071e73f
Source5:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data.tgz
# Source5-md5:	8bff8540f7994dce02d32ba8fb4ad8a8
Source6:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-tracks-dirt.tgz
# Source6-md5:	7c1d5dab87d6c06ac8e7ba8bab30f0b1
Source7:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-tracks-oval.tgz
# Source7-md5:	a27ce8b505dfbf2caba91ac6cc802bab
Source8:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-tracks-road.tgz
# Source8-md5:	8e30d3cc03dafb8392d690d96459f317
Source9:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-extra.tgz
# Source9-md5:	248ae5c165f703b22bd7224d7c2caed4
Source10:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-kcendra-gt.tgz
# Source10-md5:	02fb83162e78ac52c4d8ea829e34f8b3
Source11:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-kcendra-roadsters.tgz
# Source11-md5:	b4c3399c5dab66d41790f00eec2c6bd3
Source12:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-kcendra-sport.tgz
# Source12-md5:	d6b67de89c964fb42b27d6fb777549bd
Source13:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-nascar.tgz
# Source13-md5:	40de51f6a929d121f46dd47709d58b8b
Source14:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-Patwo-Design.tgz
# Source14-md5:	1b38279fb1e0c12ec256d26d6b17e1cc
Source15:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-VM.tgz
# Source15-md5:	c58aeff1bb7fb8a100e06cfdfa65d9e6
Source16:	%{name}.desktop
Patch0:		%{name}-link.patch
Patch1:		%{name}-asneeded.patch
Patch2:		%{name}-default-plib.patch
URL:		http://www.torcs.org/
BuildRequires:	OpenGL-glut-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freealut-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	plib-devel >= 1.8.3
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	zlib-devel
Requires:	%{name}-data = %{version}-%{release}
Requires:	OpenGL
Requires:	freealut
Requires:	plib >= 1.8.3
Obsoletes:	TORCS-robots-K1999
Obsoletes:	TORCS-robots-astigot
Obsoletes:	TORCS-robots-billy
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
The Open Racing Car Simulator.

%description -l pl.UTF-8
The Open Racing Car Simulator - symulator wyścigów samochodowych.

%package data
Summary:	Data files for TORCS
Summary(pl.UTF-8):	Pliki z danymi dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-data-cars-extra = %{version}-%{release}
Requires:	%{name}-data-tracks-road = %{version}-%{release}
Requires:	%{name}-robots-base = %{version}-%{release}

%description data
Data files for TORCS.

%description data -l pl.UTF-8
Pliki z danymi dla TORCS.

%package data-tracks-road
Summary:	Road-circuit tracks for TORCS
Summary(pl.UTF-8):	Trasy dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-tracks-road
Base tracks data files for TORCS.

%description data-tracks-road -l pl.UTF-8
Trasy dla TORCS.

%package data-tracks-oval
Summary:	Oval-like tracks for TORCS
Summary(pl.UTF-8):	Trasy owalne dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-tracks-oval
Oval-like tracks for TORCS.

%description data-tracks-oval -l pl.UTF-8
Trasy owalne dla TORCS.

%package data-tracks-dirt
Summary:	Dirt tracks for TORCS
Summary(pl.UTF-8):	Trasy szutrowe dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-tracks-dirt
Dirt tracks for TORCS.

%description data-tracks-dirt -l pl.UTF-8
Trasy szutrowe dla TORCS.

%package data-cars-extra
Summary:	Recommended cars for TORCS
Summary(pl.UTF-8):	Zalecane samochody dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-cars-extra
Recommended cars for TORCS.

%description data-cars-extra -l pl.UTF-8
Zalecane samochody dla TORCS.

%package data-cars-nascar
Summary:	Nascar cars for TORCS
Summary(pl.UTF-8):	Samochody Nascar dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-data-cars-extra = %{version}-%{release}

%description data-cars-nascar
Nascar cars for TORCS.

%description data-cars-nascar -l pl.UTF-8
Samochody Nascar dla TORCS.

%package data-cars-Patwo-Design
Summary:	Rally cars for TORCS
Summary(pl.UTF-8):	Samochody rajdowe dla TORCS
License:	distributable (see readme.txt)
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-cars-Patwo-Design
Rally cars for TORCS.

%description data-cars-Patwo-Design -l pl.UTF-8
Samochody rajdowe dla TORCS.

%package data-cars-kcendra-gt
Summary:	GT cars from the 60's for TORCS
Summary(pl.UTF-8):	Samochody GT z lat 60' dla TORCS
License:	distributable (see readme.txt)
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-cars-kcendra-gt
GT cars from the 60's for TORCS.

%description data-cars-kcendra-gt -l pl.UTF-8
Samochody GT z lat 60' dla TORCS.

%package data-cars-kcendra-roadsters
Summary:	Roadsters from the 60's for TORCS
Summary(pl.UTF-8):	Samochody Roadsters z lat 60' dla TORCS
License:	distributable (see readme.txt)
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-cars-kcendra-roadsters
Roadsters from the 60's for TORCS.

%description data-cars-kcendra-roadsters -l pl.UTF-8
Samochody Roadsters z lat 60' dla TORCS.

%package data-cars-kcendra-sport
Summary:	Sport cars from the 60's for TORCS
Summary(pl.UTF-8):	Samochody sportowe z lat 60' dla TORCS
License:	distributable (see readme.txt)
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-cars-kcendra-sport
Sport cars from the 60's for TORCS.

%description data-cars-kcendra-sport -l pl.UTF-8
Samochody sportowe z lat 60' dla TORCS.

%package data-cars-VM
Summary:	Race cars for TORCS
Summary(pl.UTF-8):	Samochody wyścigowe dla TORCS
License:	distributable (see readme.txt)
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-cars-VM
Race cars for TORCS.

%description data-cars-VM -l pl.UTF-8
Samochody wyścigowe dla TORCS.

%package robots-base
Summary:	Base robots files for TORCS
Summary(pl.UTF-8):	Podstawowe pliki komputerowych kierowców dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description robots-base
Base robots files for TORCS.

%description robots-base -l pl.UTF-8
Podstawowe pliki komputerowych kierowców dla TORCS.

%package robots-berniw
Summary:	Berniw robots files for TORCS
Summary(pl.UTF-8):	Pliki komputerowych kierowców dla TORCS - Berniw
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description robots-berniw
Berniw robots files for TORCS.

%description robots-berniw -l pl.UTF-8
Pliki komputerowych kierowców dla TORCS - Berniw.

%package robots-bt
Summary:	Bt robots files for TORCS
Summary(pl.UTF-8):	Pliki komputerowych kierowców dla TORCS - bt
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description robots-bt
Bt robots files for TORCS.

%description robots-bt -l pl.UTF-8
Pliki komputerowych kierowców dla TORCS - bt.

%package robots-olethros
Summary:	Olethros robots files for TORCS
Summary(pl.UTF-8):	Pliki komputerowych kierowców dla TORCS - olethros
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description robots-olethros
Olethros robots files for TORCS.

%description robots-olethros -l pl.UTF-8
Pliki komputerowych kierowców dla TORCS - olethros.

%prep
%setup -q -n torcs-%{version} -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15
mv torcs-%{version}/src/drivers/* src/drivers
rm -r torcs-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf data cars categories tracks menu $RPM_BUILD_ROOT%{_datadir}/games/torcs
install %{SOURCE16} $RPM_BUILD_ROOT%{_desktopdir}
install logo-skinner-trans.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

find $RPM_BUILD_ROOT%{_datadir}/games/torcs -name "Makefile" -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.linux
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/torcs
%attr(755,root,root) %{_libdir}/torcs/*-bin
%attr(755,root,root) %{_libdir}/torcs/*.sh
%dir %{_libdir}/torcs/lib
%attr(755,root,root) %{_libdir}/torcs/lib/*.so
%dir %{_libdir}/torcs/modules
%dir %{_libdir}/torcs/modules/graphic
%attr(755,root,root) %{_libdir}/torcs/modules/graphic/*.so
%dir %{_libdir}/torcs/modules/simu
%attr(755,root,root) %{_libdir}/torcs/modules/simu/*.so
%dir %{_libdir}/torcs/modules/telemetry
%attr(755,root,root) %{_libdir}/torcs/modules/telemetry/*.so
%dir %{_libdir}/torcs/modules/track
%attr(755,root,root) %{_libdir}/torcs/modules/track/*.so
%dir %{_datadir}/games/torcs
%{_datadir}/games/torcs/config
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/games/torcs/cars
%{_datadir}/games/torcs/cars/360-modena
%dir %{_datadir}/games/torcs/categories
%{_datadir}/games/torcs/categories/free.xml
%{_datadir}/games/torcs/categories/F1.xml
%{_datadir}/games/torcs/categories/Historic.xml
%{_datadir}/games/torcs/categories/Offroad*.xml
%{_datadir}/games/torcs/categories/Track*.xml
%{_datadir}/games/torcs/data
%dir %{_datadir}/games/torcs/drivers
%dir %{_libdir}/torcs/drivers
%{_datadir}/games/torcs/drivers/human
%dir %{_libdir}/torcs/drivers/human
%attr(755,root,root) %{_libdir}/torcs/drivers/human/*.so
%{_datadir}/games/torcs/menu
%{_datadir}/games/torcs/results
%{_datadir}/games/torcs/telemetry
%dir %{_datadir}/games/torcs/tracks

%files data-tracks-road
%defattr(644,root,root,755)
%{_datadir}/games/torcs/tracks/road

%files data-tracks-oval
%defattr(644,root,root,755)
%{_datadir}/games/torcs/tracks/oval

%files data-tracks-dirt
%defattr(644,root,root,755)
%{_datadir}/games/torcs/tracks/dirt

%files data-cars-extra
%defattr(644,root,root,755)
%{_datadir}/games/torcs/cars/155-DTM
%{_datadir}/games/torcs/cars/acura-nsx-sz
%{_datadir}/games/torcs/cars/baja-bug
%{_datadir}/games/torcs/cars/buggy
%{_datadir}/games/torcs/cars/car1-trb1
%{_datadir}/games/torcs/cars/clkdtm
%{_datadir}/games/torcs/cars/gt40
%{_datadir}/games/torcs/cars/lotus-gt1
%{_datadir}/games/torcs/cars/mclaren-f1
%{_datadir}/games/torcs/cars/p406
%{_datadir}/games/torcs/cars/porsche-gt1
%{_datadir}/games/torcs/cars/porsche-gt3rs
%{_datadir}/games/torcs/cars/sc-f1
%{_datadir}/games/torcs/cars/viper-gts-r
%{_datadir}/games/torcs/cars/xj-220

%files data-cars-nascar
%defattr(644,root,root,755)
%{_datadir}/games/torcs/cars/cg-nascar-rwd
%{_datadir}/games/torcs/categories/Nascar.xml

%files data-cars-Patwo-Design
%defattr(644,root,root,755)
%{_datadir}/games/torcs/cars/pw-*

%files data-cars-kcendra-gt
%defattr(644,root,root,755)
%{_datadir}/games/torcs/cars/kc-2000gt
%{_datadir}/games/torcs/cars/kc-5300gt
%{_datadir}/games/torcs/cars/kc-corvette-ttop
%{_datadir}/games/torcs/cars/kc-daytona
%{_datadir}/games/torcs/cars/kc-db4z
%{_datadir}/games/torcs/cars/kc-dbs
%{_datadir}/games/torcs/cars/kc-dino
%{_datadir}/games/torcs/cars/kc-ghibli
%{_datadir}/games/torcs/cars/kc-grifo

%files data-cars-kcendra-roadsters
%defattr(644,root,root,755)
%{_datadir}/games/torcs/cars/kc-bigh

%files data-cars-kcendra-sport
%defattr(644,root,root,755)
%{_datadir}/games/torcs/cars/kc-a110
%{_datadir}/games/torcs/cars/kc-alfatz2
%{_datadir}/games/torcs/cars/kc-coda
%{_datadir}/games/torcs/cars/kc-conrero
%{_datadir}/games/torcs/cars/kc-gt40
%{_datadir}/games/torcs/cars/kc-gto
%{_datadir}/games/torcs/cars/kc-p4

%files data-cars-VM
%defattr(644,root,root,755)
%{_datadir}/games/torcs/cars/vm-x2
%{_datadir}/games/torcs/cars/vm-x4

%files robots-base
%defattr(644,root,root,755)
%{_datadir}/games/torcs/drivers/cylos1
%dir %{_libdir}/torcs/drivers/cylos1
%attr(755,root,root) %{_libdir}/torcs/drivers/cylos1/*.so
%{_datadir}/games/torcs/drivers/damned
%dir %{_libdir}/torcs/drivers/damned
%attr(755,root,root) %{_libdir}/torcs/drivers/damned/*.so
%{_datadir}/games/torcs/drivers/inferno*
%dir %{_libdir}/torcs/drivers/inferno*
%attr(755,root,root) %{_libdir}/torcs/drivers/inferno*/*.so
%{_datadir}/games/torcs/drivers/lliaw
%dir %{_libdir}/torcs/drivers/lliaw
%attr(755,root,root) %{_libdir}/torcs/drivers/lliaw/*.so
%{_datadir}/games/torcs/drivers/tanhoj
%dir %{_libdir}/torcs/drivers/tanhoj
%attr(755,root,root) %{_libdir}/torcs/drivers/tanhoj/*.so
%{_datadir}/games/torcs/drivers/tita
%dir %{_libdir}/torcs/drivers/tita
%attr(755,root,root) %{_libdir}/torcs/drivers/tita/*.so

%files robots-berniw
%defattr(644,root,root,755)
%{_datadir}/games/torcs/drivers/berniw*
%dir %{_libdir}/torcs/drivers/berniw*
%attr(755,root,root) %{_libdir}/torcs/drivers/berniw*/*.so
%{_datadir}/games/torcs/drivers/sparkle
%dir %{_libdir}/torcs/drivers/sparkle
%attr(755,root,root) %{_libdir}/torcs/drivers/sparkle/*.so

%files robots-bt
%defattr(644,root,root,755)
%{_datadir}/games/torcs/drivers/bt
%dir %{_libdir}/torcs/drivers/bt
%attr(755,root,root) %{_libdir}/torcs/drivers/bt/*.so

%files robots-olethros
%defattr(644,root,root,755)
%{_datadir}/games/torcs/drivers/olethros
%dir %{_libdir}/torcs/drivers/olethros
%attr(755,root,root) %{_libdir}/torcs/drivers/olethros/*.so
