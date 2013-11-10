%include	/usr/lib/rpm/macros.perl
Summary:	Master High Availability Manager and Tools for MySQL, Node Package
Name:		mha4mysql-node
Version:	0.54
Release:	1
License:	GPL v2
Group:		Applications/Databases
Source0:	https://mysql-master-ha.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	8dd07fabcddcd17a2973cf4b85c61e19
URL:		http://code.google.com/p/mysql-master-ha/
BuildRequires:	mysql-devel
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:	perl-DBI
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-NoWarnings
BuildRequires:	perl-Test-Tester
BuildRequires:	perl-Encode
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-DBD-mysql
Requires:	perl-DBI
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Master High Availability Manager and tools for MySQL (MHA) for
automating master failover and fast master switch.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/mha4mysql/node/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/apply_diff_relay_logs
%attr(755,root,root) %{_bindir}/filter_mysqlbinlog
%attr(755,root,root) %{_bindir}/purge_relay_logs
%attr(755,root,root) %{_bindir}/save_binary_logs
%{_mandir}/man1/apply_diff_relay_logs.1p*
%{_mandir}/man1/filter_mysqlbinlog.1p*
%{_mandir}/man1/purge_relay_logs.1p*
%{_mandir}/man1/save_binary_logs.1p*
%{perl_vendorlib}/MHA
