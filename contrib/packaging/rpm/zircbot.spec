%global srcname zircbot

Name:           %{srcname}
Version:        0.0.1
Release:        1%{?dist}

Summary:        IRC bot that forwards 0mq messages
License:        ASL 2.0
URL:            https://github.com/fredericlepied/%{srcname}
Source0:        https://github.com/fredericlepied/%{srcname}/archive/%{version}.tar.gz
Source1:        %{srcname}.service


BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  systemd
BuildRequires:  systemd-units

Requires:       PyYAML
Requires:       python-txzmq
Requires:       python-twisted-words

Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%description
zircbot is an IRC bot that relays notification from 0mq messages.
It now supports trello notifications (see https://github.com/fredericlepied/ztrellohook), gerrit events (see https://github.com/fredericlepied/zgerrit) and
sensu notifications.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py2_build


%install
%py2_install
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{srcname}.service


%check
%{__python2} setup.py test


%post
%systemd_post %{srcname}.service


%preun
%systemd_preun %{srcname}.service


%postun
%systemd_postun_with_restart %{srcname}.service


%files
%doc README.rst
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/*.egg-info
%{_bindir}/%{srcname}
%{_unitdir}/%{srcname}.service


%changelog
* Tue Oct 18 2016 Yanis Guenane <yguenane@redhat.com> 0.0.1-1
- Initial commit
