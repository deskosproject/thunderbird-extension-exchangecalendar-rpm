Name:           thunderbird-extension-exchangecalendar
Version:        3.8.0
Release:        1%{?dist}
Summary:        Exchange 2007/2010/2013 Calendar, Tasks, Contacts and GAL Provider for Thunderbird

Group:          Applications/Internet
License:        GPLv3
URL:            https://github.com/Ericsson/exchangecalendar
Source0:        https://github.com/Ericsson/exchangecalendar/archive/v3.8.0.tar.gz

BuildArch:      noarch
Requires:       thunderbird

%description
Add-on for the Lightning Calendering Add-on that allows to communicate with an
Exchange 2007, 2010 and 2013 server using the Exchange Web Service (EWS) interface.

%prep
%setup -q -n exchangecalendar-%{version}

%build
./build.sh -d

%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/thunderbird/extensions/
cp -p exchangecalendar-v3.8.0.xpi $RPM_BUILD_ROOT/%{_libdir}/thunderbird/extensions/exchangecalendar@extensions.1st-setup.nl.xpi

%files
%defattr(-,root,root,-)
%{_libdir}/thunderbird/extensions/*.xpi

%changelog
* Mon Dec 19 2016 Ricardo Arguello <rarguello@deskosproject.org> - 3.8.0-1
- Initial release for DeskOS
