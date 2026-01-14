#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	POE
%define	pnam	Component-Schedule
Summary:	POE::Component::Schedule - Schedule POE events using DateTime::Set iterators
Summary(pl.UTF-8):	POE::Component::Schedule - Planuje zdarzenia POE przy użyciu iteratorów DateTime::Set
Name:		perl-POE-Component-Schedule
Version:	0.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/D/DO/DOLMEN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7f3b1b2b368d588243c1c74685de3cd4
URL:		http://search.cpan.org/dist/POE-Component-Schedule/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DateTime
BuildRequires:	perl-DateTime-Set >= 0.25
BuildRequires:	perl-DateTime-TimeZone
BuildRequires:	perl-POE >= 1.000
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This component encapsulates a session that sends events to client sessions
on a schedule as defined by a DateTime::Set iterator.

%description -l pl.UTF-8
Moduł ten planuje zdarzenia POE przy użyciu iteratorów DateTime::Set.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/*.pm
%{_mandir}/man3/*
