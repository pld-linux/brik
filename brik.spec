Summary:	Checks archive integrity
Summary(pl):	Program do sprawdzania integralno¶ci archiwum
Name:		brik
Version:	1.0
Release:	1
License:	distributable
Group:		Applications/System
# no clue if it works:
Vendor:		Rahul Dhesi <dhesi@bsu-cs.bsu.edu>
Source0:	ftp://ftp.kernel.pl/pub/People/malekith/%{name}-%{version}.tar.gz
# Source0-md5:	d987c9a3ab21154108635c0dfbfaea33
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Checks archive integrity. Quite old program, but sometimes used.

%description -l pl
Program do sprawdzania integralno¶ci archiwum. Ca³kiem stary program,
jednak wci±¿ czasem u¿ywany.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install brik $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Usenet README
%attr(755,root,root) %{_bindir}/*
