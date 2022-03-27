Summary:	Manage ip ranges
Name:		iprange
Version:	1.0.4
Release:	2%{?dist}
License:	GPLv2+
URL:		http://firehol.org
Source:		%{name}-1.0.4.tar.bz2


%description
Manage ip ranges.

%prep
%setup -q -n %{name}-1.0.4

%build
%configure \
	--docdir="%{_docdir}/%{name}-%{version}" \
	%{?conf}
make %{?_smp_mflags}

%install
rm -rf "%{buildroot}"
make %{?_smp_mflags} install DESTDIR="%{buildroot}"

%files
%{_mandir}/man1/iprange.1.gz
%{_bindir}/iprange

%changelog
* Sat Sep 16 2017 Phil Whineray <phil@firehol.org> - 1.0.4-1
- Bugfix release

* Sat Oct 16 2016 Costa Tsaousis <costa@tsaousis.gr> - 1.0.3-1
- speedup release

* Sat Nov 28 2015 Phil Whineray <phil@firehol.org> - 1.0.2-1
- Bugfix release

* Sat Nov 28 2015 Phil Whineray <phil@firehol.org> - 1.0.1-1
- Release new version

* Sun Nov 15 2015 Alon Bar-Lev <alonbl@redhat.com> - 1.0.0-1
- Initial add.
