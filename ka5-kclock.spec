#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kclock
Summary:	Universal clock application
Summary(pl.UTF-8):	Uniwersalna aplikacja zegara
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	88899e9d7aa787aa72dc4b32f509b6f0
URL:		https://apps.kde.org/kclock/
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
BuildRequires:	kf5-kirigami-addons-devel >= 0.6
BuildRequires:	kf5-knotifications-devel >= 5.101.0
BuildRequires:	kf5-plasma-framework-devel >= 5.101.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A universal clock application for desktop and mobile.

%description -l pl.UTF-8
Uniwersalna aplikacja zegara dla urządzeń biurkowych i przenośnych.

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
%{_datadir}/dbus-1/interfaces/org.kde.kclockd.Alarm.xml
%{_datadir}/dbus-1/interfaces/org.kde.kclockd.AlarmModel.xml
%{_datadir}/dbus-1/interfaces/org.kde.kclockd.KClockSettings.xml
%{_datadir}/dbus-1/interfaces/org.kde.kclockd.Timer.xml
%{_datadir}/dbus-1/interfaces/org.kde.kclockd.TimerModel.xml
%{_datadir}/dbus-1/interfaces/org.kde.kclockd.Utility.xml
%{_datadir}/dbus-1/services/org.kde.kclockd.service
%{_datadir}/knotifications5/kclockd.notifyrc
%{_datadir}/metainfo/org.kde.kclock.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.kclock_1x2.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kclock_1x2
%{_desktopdir}/org.kde.kclock.desktop
%{_iconsdir}/hicolor/scalable/apps/kclock_plasmoid_1x2.svg
%{_iconsdir}/hicolor/scalable/apps/org.kde.kclock.svg
