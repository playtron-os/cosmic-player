Name:           cosmic-player
Epoch:          1
Version: 1.0.9
Release:        1%{?dist}
Summary:        Media Player (Playtron fork)

License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-player
Source0:        %{name}-%{_arch}.tar.gz

%global debug_package %{nil}

# No BuildRequires - binary is pre-built

Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good

%description
Media player for music and videos.
A libcosmic-based multimedia player with GPU acceleration.

%prep
%autosetup -n %{name} -p1

%build

%install
install -Dm0755 "usr/bin/cosmic-player" "%{buildroot}%{_bindir}/cosmic-player"
install -Dm0644 "usr/share/applications/com.system76.CosmicPlayer.desktop" "%{buildroot}%{_datadir}/applications/com.system76.CosmicPlayer.desktop"
install -Dm0644 "usr/share/metainfo/com.system76.CosmicPlayer.metainfo.xml" "%{buildroot}%{_datadir}/metainfo/com.system76.CosmicPlayer.metainfo.xml"
install -Dm0644 "usr/share/thumbnailers/com.system76.CosmicPlayer.thumbnailer" "%{buildroot}%{_datadir}/thumbnailers/com.system76.CosmicPlayer.thumbnailer"
install -Dm0644 "usr/share/licenses/cosmic-player/LICENSE" "%{buildroot}%{_datadir}/licenses/cosmic-player/LICENSE"

# Install icons
install -Dm0644 "usr/share/icons/hicolor/16x16/apps/com.system76.CosmicPlayer.svg" "%{buildroot}%{_datadir}/icons/hicolor/16x16/apps/com.system76.CosmicPlayer.svg"
install -Dm0644 "usr/share/icons/hicolor/24x24/apps/com.system76.CosmicPlayer.svg" "%{buildroot}%{_datadir}/icons/hicolor/24x24/apps/com.system76.CosmicPlayer.svg"
install -Dm0644 "usr/share/icons/hicolor/32x32/apps/com.system76.CosmicPlayer.svg" "%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/com.system76.CosmicPlayer.svg"
install -Dm0644 "usr/share/icons/hicolor/48x48/apps/com.system76.CosmicPlayer.svg" "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/com.system76.CosmicPlayer.svg"
install -Dm0644 "usr/share/icons/hicolor/64x64/apps/com.system76.CosmicPlayer.svg" "%{buildroot}%{_datadir}/icons/hicolor/64x64/apps/com.system76.CosmicPlayer.svg"
install -Dm0644 "usr/share/icons/hicolor/128x128/apps/com.system76.CosmicPlayer.svg" "%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/com.system76.CosmicPlayer.svg"
install -Dm0644 "usr/share/icons/hicolor/256x256/apps/com.system76.CosmicPlayer.svg" "%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/com.system76.CosmicPlayer.svg"

%files
%license %{_datadir}/licenses/cosmic-player/LICENSE
%{_bindir}/cosmic-player
%{_datadir}/applications/com.system76.CosmicPlayer.desktop
%{_datadir}/metainfo/com.system76.CosmicPlayer.metainfo.xml
%{_datadir}/thumbnailers/com.system76.CosmicPlayer.thumbnailer
%{_datadir}/icons/hicolor/*/apps/com.system76.CosmicPlayer.svg

%changelog
* Fri Mar 27 2026 Playtron <dev@playtron.one> - 1.0.8-1
- Initial RPM package for Playtron fork
