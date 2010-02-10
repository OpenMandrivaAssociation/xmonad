%define _cabal_setup Setup.lhs
%define ghc_version 6.10.4

Name: xmonad
Version: 0.9
Release: %mkrel 3
License: BSD
Group: Graphical desktop/Other
URL: http://xmonad.org
Source: xmonad-%{version}.tar.gz
Summary: A tiling window manager
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: ghc
BuildRequires: haddock
BuildRequires: haskell-X11 >= 1.4.6.1
BuildRequires: haskell-macros
BuildRequires: libxinerama-devel

%description
xmonad is a tiling window manager for X. Windows are arranged
automatically to tile the screen without gaps or overlap, maximising
screen use. All features of the window manager are accessible from
the keyboard: a mouse is strictly optional. xmonad is written and
extensible in Haskell. Custom layout algorithms, and other
extensions, may be written by the user in config files. Layouts are
applied dynamically, and different layouts may be used on each
workspace. Xinerama is fully supported, allowing windows to be tiled
on several screens.


%prep
%setup -q -n %{name}-%{version}

%build
%_cabal_build

%_cabal_genscripts

%check
%_cabal_check

%install
%_cabal_install

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/xmonad
%{_libdir}/%{name}-%{version}/ghc-%{ghc_version}/*
%{_datadir}/%{name}-%{version}
%{_datadir}/doc/%{name}-%{version}/html/*
%{_datadir}/doc/%{name}-%{version}/LICENSE
%{_datadir}/haskell-deps/%{name}-%{version}-%{release}/*
