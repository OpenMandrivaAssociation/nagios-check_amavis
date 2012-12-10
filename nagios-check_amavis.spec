%define plugin	check_amavis

Summary:	Check Amavis
Name:		nagios-%{plugin}
Version:	1.1
Release:	%mkrel 1
Group:		Networking/Other
License:	GPL
URL:		 http://exchange.nagios.org/directory/Plugins/Anti-2DVirus/Amavis/check_amavis/details
Source0:	%{plugin}.pl
BuildArch:	noarch
BuildRequires:	perl
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
check_amavis checks if amavisd-new daemon is working and if its
antivirus engine is working. This check talks with amavisd-new daemon.
It tests if the daemon is up and if it's able to scan an email with a
virus (EICAR test virus is sent).
	
Please note that if amavisd-new is run on a different machine, you
should enable the connection from nagios ip address (take a look at
amavisd.conf).

%prep
%setup -qcT

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_amavis.cfg <<'EOF'

define command {
        command_name    check_amavis
        command_line    %{_datadir}/nagios/plugins/%{plugin}.pl --server $HOSTADDRESS$ --port 10025 $ARG1$
}
EOF
install -d -m 755 %{buildroot}%{_datadir}/nagios/plugins
install -m 755 %{SOURCE0} %{buildroot}%{_datadir}/nagios/plugins

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_amavis.cfg
%{_datadir}/nagios/plugins/%{plugin}.pl




%changelog
* Sun Jan 15 2012 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1.1-1mdv2011.0
+ Revision: 761637
- import nagios-check_amavis

