#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kclock
Summary:	kclock
Name:		ka5-%{kaname}
Version:	23.08.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	dc26f70215c5992c0b416f52b9cf7863
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= 5.15.2
BuildRequires:	Qt5Gui-devel >= 5.15.2
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5Network-devel >= 5.15.10
BuildRequires:	Qt5Qml-devel >= 5.15.10
BuildRequires:	Qt5Quick-controls2-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel >= 5.15.2
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.101.0
BuildRequires:	kf5-kconfig-devel >= 5.109.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.109.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.101.0
BuildRequires:	kf5-ki18n-devel >= 5.101.0
BuildRequires:	kf5-kirigami2-devel >= 5.101.0
BuildRequires:	kf5-knotifications-devel >= 5.101.0
BuildRequires:	kf5-plasma-framework-devel >= 5.101.0
BuildRequires:	kirigami-addons-devel >= 0.6
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExcludeArch:	x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A convergent clock application for Plasma.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/autostart/org.kde.kclockd-autostart.desktop
%attr(755,root,root) %{_bindir}/kclock
%attr(755,root,root) %{_bindir}/kclockd
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/applets/plasma_applet_kclock_1x2.so
%{_desktopdir}/org.kde.kclock.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kclockd.Alarm.xml
%{_datadir}/dbus-1/interfaces/org.kde.kclockd.AlarmModel.xml
%{_datadir}/dbus-1/interfaces/org.kde.kclockd.KClockSettings.xml
%{_datadir}/dbus-1/interfaces/org.kde.kclockd.Timer.xml
%{_datadir}/dbus-1/interfaces/org.kde.kclockd.TimerModel.xml
%{_datadir}/dbus-1/interfaces/org.kde.kclockd.Utility.xml
%{_datadir}/dbus-1/services/org.kde.kclockd.service
%{_iconsdir}/hicolor/scalable/apps/kclock_plasmoid_1x2.svg
%{_iconsdir}/hicolor/scalable/apps/org.kde.kclock.svg
%{_datadir}/knotifications5/kclockd.notifyrc
%{_datadir}/metainfo/org.kde.kclock.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.kclock_1x2.appdata.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kclock_1x2
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kclock_1x2/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kclock_1x2/contents/config
%{_datadir}/plasma/plasmoids/org.kde.plasma.kclock_1x2/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kclock_1x2/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.kclock_1x2/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.kclock_1x2/contents/ui/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kclock_1x2/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kclock_1x2/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.kclock_1x2/metadata.json.license
