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
URL:		http://torcs.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix /usr/X11R6

%description

%description -l pl

%prep
%setup -q -n torcs-1.2.0 -a 2 4 5 6

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
