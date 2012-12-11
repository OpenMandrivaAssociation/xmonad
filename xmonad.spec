#% global debug_package %{nil}
%define _cabal_setup Setup.lhs
%define _no_haddock 1
%define module  xmonad
Name:           %{module}
Version:        0.10
Release:        1
Summary:        A tiling window manager
Group:          Development/Other
License:        BSD
URL:            http://hackage.haskell.org/package/%{module}
Source0:        http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz

#BuildRequires:  ghc, ghc-devel, haskell-macros
#buildrequires:  haskell(utf8-string)

#BuildRequires:  ghc < 7.6
#buildrequires:  ghc-devel < 7.6
BuildRequires:  ghc
buildrequires:  ghc-devel
buildrequires:  haskell-macros
buildrequires:  cabal-install
buildrequires:  X11-devel

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
%setup -q -n %{module}-%{version}

%build
#% _cabal_build
cabal update
cabal install
cabal configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-executable-stripping
cabal build
%_cabal_genscripts

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

%files
%defattr(-,root,root,-)
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%_cabal_rpm_deps_dir
%_cabal_haddoc_files
%{_bindir}/%{module}
%{_datadir}/%{module}-%{version}


