Summary:	The Open Racing Car Simulator
Summary(pl):	The Open Racing Car Simulator - symulator wy¶cigów samochodowych
Name:		TORCS
Version:	1.2.2
Release:	3
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src.tgz
# Source0-md5:	cf03f0623eab7f9f7d6b13ac20660515
Source1:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src-robots-base.tgz
# Source1-md5:	425b9737f951f95e4255f81b60449f94
Source2:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src-robots-berniw.tgz
# Source2-md5:	7e49902b503edb9245c95ffb682bc5c1
Source3:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src-robots-K1999.tgz
# Source3-md5:	b092acfca04bd4708f9722fe0732ba75
Source4:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src-robots-astigot.tgz
# Source4-md5:	653c522a007d01c9e8d8fc069651517b
Source5:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src-robots-billy.tgz
# Source5-md5:	43af2098b788aa96556c8939048ac1b3
Source6:	http://dl.sourceforge.net/torcs/%{name}-%{version}-src-robots-bt.tgz
# Source6-md5:	e81c9f15a8089b138113621e9e7013d1
Source7:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data.tgz
# Source7-md5:	241552524488396fc5cca4ff8c943709
Source8:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-tracks-road.tgz
# Source8-md5:	78dabde8e38aa618fcfa570a5835732e
Source9:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-tracks-oval.tgz
# Source9-md5:	846a977e0a147de2560b23e740ebdecb
Source10:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-tracks-dirt.tgz
# Source10-md5:	630e7e53ffcd84a46175a7627438ba2b
Source11:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-extra.tgz
# Source11-md5:	96ff8279e7d77a40564122fa1a7a78b6
Source12:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-nascar.tgz
# Source12-md5:	4b20ced6ffc65357ffddb31fbc561682
Source13:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-Patwo-Design.tgz
# Source13-md5:	df5706fd877d98cebf0d9977005304d4
Source14:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-kcendra-gt.tgz
# Source14-md5:	858c0e05e589c88264472a27c94f2a29
Source15:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-kcendra-roadsters.tgz
# Source15-md5:	7d490c510914a0cdab5939cca66f37cb
Source16:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-kcendra-sport.tgz
# Source16-md5:	3e574373fe582269f927b94b3d01ccfa
Source17:	http://dl.sourceforge.net/torcs/%{name}-%{version}-data-cars-VM.tgz
# Source17-md5:	4394bdbe9722cc8b962fea29dec9531d
Source18:	%{name}.desktop
Source19:	%{name}.png
Patch0:		%{name}-inc.patch
URL:		http://torcs.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glut-devel >= 3.7
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	plib-devel >= 1.8.0
BuildRequires:	zlib-devel
Requires:	%{name}-data = %{version}-%{release}
Requires:	OpenGL
Requires:	plib >= 1.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
The Open Racing Car Simulator.

%description -l pl
The Open Racing Car Simulator - symulator wy¶cigów samochodowych.

%package data
Summary:	Data files for TORCS
Summary(pl):	Pliki z danymi dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data
Data files for TORCS.

%description data -l pl
Pliki z danymi dla TORCS.

%package data-tracks-road
Summary:	Road-circuit tracks for TORCS
Summary(pl):	Trasy dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-tracks-road
Base tracks data files for TORCS.

%description data-tracks-road -l pl
Trasy dla TORCS.

%package data-tracks-oval
Summary:	Oval-like tracks for TORCS
Summary(pl):	Trasy owalne dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-tracks-oval
Oval-like tracks for TORCS.

%description data-tracks-oval -l pl
Trasy owalne dla TORCS.

%package data-tracks-dirt
Summary:	Dirt tracks for TORCS
Summary(pl):	Trasy szutrowe dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-tracks-dirt
Dirt tracks for TORCS.

%description data-tracks-dirt -l pl
Trasy szutrowe dla TORCS.

%package data-cars-extra
Summary:	Recommended cars for TORCS
Summary(pl):	Zalecane samochody dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-cars-extra
Recommended cars for TORCS.

%description data-cars-extra -l pl
Zalecane samochody dla TORCS.

%package data-cars-nascar
Summary:	Nascar cars for TORCS
Summary(pl):	Samochody Nascar dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-cars-nascar
Nascar cars for TORCS.

%description data-cars-nascar -l pl
Samochody Nascar dla TORCS.

%package data-cars-Patwo-Design
Summary:	Rally cars for TORCS
Summary(pl):	Samochody rajdowe dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-cars-Patwo-Design
Rally cars for TORCS.

%description data-cars-Patwo-Design -l pl
Samochody rajdowe dla TORCS.

%package data-cars-kcendra-gt
Summary:	GT cars from the 60's for TORCS
Summary(pl):	Samochody GT z lat 60' dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-cars-kcendra-gt
GT cars from the 60's for TORCS.

%description data-cars-kcendra-gt -l pl
Samochody GT z lat 60' dla TORCS.

%package data-cars-kcendra-roadsters
Summary:	Roadsters from the 60's for TORCS
Summary(pl):	Samochody Roadsters z lat 60' dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-cars-kcendra-roadsters
Roadsters from the 60's for TORCS.

%description data-cars-kcendra-roadsters -l pl
Samochody Roadsters z lat 60' dla TORCS.

%package data-cars-kcendra-sport
Summary:	Sport cars from the 60's for TORCS
Summary(pl):	Samochody sportowe z lat 60' dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-cars-kcendra-sport
Sport cars from the 60's for TORCS.

%description data-cars-kcendra-sport -l pl
Samochody sportowe z lat 60' dla TORCS.

%package data-cars-VM
Summary:	Race cars for TORCS
Summary(pl):	Samochody wy¶cigowe dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description data-cars-VM
Race cars for TORCS.

%description data-cars-VM -l pl
Samochody wy¶cigowe dla TORCS.

%package robots-base
Summary:	Base robots files for TORCS
Summary(pl):	Podstawowe pliki komputerowych kierowców dla TORCS
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description robots-base
Base robots files for TORCS.

%description robots-base -l pl
Podstawowe pliki komputerowych kierowców dla TORCS.

%package robots-berniw
Summary:	Berniw robots files for TORCS
Summary(pl):	Pliki komputerowych kierowców dla TORCS - Berniw
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description robots-berniw
Berniw robots files for TORCS.

%description robots-berniw -l pl
Pliki komputerowych kierowców dla TORCS - Berniw.

%package robots-K1999
Summary:	K1999 robots files for TORCS
Summary(pl):	Pliki komputerowych kierowców dla TORCS - K1999
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description robots-K1999
K1999 robots files for TORCS.

%description robots-K1999 -l pl
Pliki komputerowych kierowców dla TORCS - K1999.

%package robots-astigot
Summary:	astigot robots files for TORCS
Summary(pl):	Pliki komputerowych kierowców dla TORCS - astigot
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description robots-astigot
astigot robots files for TORCS.

%description robots-astigot -l pl
Pliki komputerowych kierowców dla TORCS - astigot.

%package robots-billy
Summary:	Billy robots files for TORCS
Summary(pl):	Pliki komputerowych kierowców dla TORCS - billy
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description robots-billy
Billy robots files for TORCS.

%description robots-billy -l pl
Pliki komputerowych kierowców dla TORCS - billy.

%package robots-bt
Summary:	Bt robots files for TORCS
Summary(pl):	Pliki komputerowych kierowców dla TORCS - bt
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description robots-bt
Bt robots files for TORCS.

%description robots-bt -l pl
Pliki komputerowych kierowców dla TORCS - bt.

%prep
%setup -q -n torcs-%{version} -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17
mv torcs-%{version}/src/drivers/* src/drivers
rm -r torcs-%{version}
%patch0 -p1

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
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf data cars categories tracks menu $RPM_BUILD_ROOT%{_datadir}/games/torcs
install %{SOURCE18} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE19} $RPM_BUILD_ROOT%{_pixmapsdir}

find $RPM_BUILD_ROOT%{_datadir}/games/torcs -name "Makefile" -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.html README.linux TODO.html
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
%{_desktopdir}/*
%{_pixmapsdir}/*

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/games/torcs/cars
%{_datadir}/games/torcs/cars/360-modena
%dir %{_datadir}/games/torcs/categories
%{_datadir}/games/torcs/categories/free.xml
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
%{_datadir}/games/torcs/cars/clkdtm
%{_datadir}/games/torcs/cars/gt40
%{_datadir}/games/torcs/cars/lotus-gt1
%{_datadir}/games/torcs/cars/mclaren-f1
%{_datadir}/games/torcs/cars/p406
%{_datadir}/games/torcs/cars/porsche-gt1
%{_datadir}/games/torcs/cars/porsche-gt3rs
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
%{_datadir}/games/torcs/cars/kc-gullwing

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

%files robots-K1999
%defattr(644,root,root,755)
%{_datadir}/games/torcs/drivers/K1999
%dir %{_libdir}/torcs/drivers/K1999
%attr(755,root,root) %{_libdir}/torcs/drivers/K1999/*.so

%files robots-astigot
%defattr(644,root,root,755)
%{_datadir}/games/torcs/drivers/astigot
%dir %{_libdir}/torcs/drivers/astigot
%attr(755,root,root) %{_libdir}/torcs/drivers/astigot/*.so

%files robots-billy
%defattr(644,root,root,755)
%{_datadir}/games/torcs/drivers/billy
%dir %{_libdir}/torcs/drivers/billy
%attr(755,root,root) %{_libdir}/torcs/drivers/billy/*.so

%files robots-bt
%defattr(644,root,root,755)
%{_datadir}/games/torcs/drivers/bt
%dir %{_libdir}/torcs/drivers/bt
%attr(755,root,root) %{_libdir}/torcs/drivers/bt/*.so
