# ToDo:
# - make it compile - this one is horrible, it creates exports/include dir
#   in top source directory and puts symlinks to various *.h files there.
#   However, it does not put symlinks to plib/*.h or GL/*.h. Anyone knows
#   how to fix it? Or maybe this one should be removed from repo?
Summary:	The Open Racing Car Simulator
Summary(pl):	The Open Racing Car Simulator - symulator wy¶cigów samochodowych
Name:		TORCS
Version:	1.2.1
Release:	0.2
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
Patch0:		%{name}-inc.patch
Patch1:		%{name}-compile_fix.patch
URL:		http://torcs.sourceforge.net/
BuildRequires:	plib > 1.7.0-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Open Racing Car Simulator.

%description -l pl
The Open Racing Car Simulator - symulator wy¶cigów samochodowych.

%prep
%setup -q -n torcs-%{version} -a1 -a2 -a3 -a4 -a5 -a6
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
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf data cars categories tracks menu $RPM_BUILD_ROOT%{_datadir}/games/torcs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.html README.linux
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_datadir}/games/torcs
%{_datadir}/games/torcs/cars
%{_datadir}/games/torcs/categories
%{_datadir}/games/torcs/config
%{_datadir}/games/torcs/data
%{_datadir}/games/torcs/drivers
%{_datadir}/games/torcs/menu
%{_datadir}/games/torcs/modules
%{_datadir}/games/torcs/results
%{_datadir}/games/torcs/telemetry
%{_datadir}/games/torcs/tracks
%{_datadir}/games/torcs/setup_linux.sh
%attr(755,root,root) %{_datadir}/games/torcs/torcs
