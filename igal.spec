Summary:	Easy and flexible online Image GALlery generator
Summary(pl.UTF-8):	Łatwy i elastyczny generator obrazków dla WWW
Name:		igal
Version:	1.4
Release:	3
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.stanford.edu/~epop/igal/%{name}-%{version}.tar.gz
# Source0-md5:	49f1b27229e80a7719a9378afa0981a3
URL:		http://www.stanford.edu/~epop/igal/
Requires:	ImageMagick
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Igal is a quick, easy and flexible program meant to help you place
your digital images online. It generates a pretty good-looking set of
HTML slides even with its default settings -- which can otherwise be
easily changed with a good number of command-line options or by
altering igal's two HTML template files.

%description -l pl.UTF-8
Igal jest sprawnym, łatwym w użyciu i elastycznym programem mającym na
celu pomóc Ci w umieszczeniu Twoich obrazków w sieci. Generuje całkiem
ładnie wyglądający zestaw HTML-owych slajdów, z możliwością zmiany
wielu parametrów z wiersza poleceń lub przez podanie igalowi innych
wzorców plików.

%prep
%setup  -q

%build
cat igal |sed -e "s#%{_prefix}/local/lib/igal#%{_datadir}/igal#g" >igal.new
mv igal{.new,}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install indextemplate.html slidetemplate.html tile.png igal.css \
	$RPM_BUILD_ROOT%{_datadir}/%{name}
install -D igal $RPM_BUILD_ROOT%{_bindir}/igal
install -D igal.1 $RPM_BUILD_ROOT%{_mandir}/man1/igal.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README THANKS
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man?/*
%{_datadir}/%{name}
