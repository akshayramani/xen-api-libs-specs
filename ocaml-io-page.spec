%define debug_package %{nil}

Name:           ocaml-io-page
Version:        1.0.0
Release:        1
Summary:        Efficient handling of I/O memory pages on Unix and Xen.
License:        ISC
Group:          Development/Other
URL:            https://github.com/mirage/io-page
Source0:        http://github.com/mirage/io-page/archive/v%{version}/io-page-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-cstruct-devel ocaml-ounit-devel ocaml-mirage-types-devel
Requires:       ocaml ocaml-findlib

%description
This library implements support for efficient handling of I/O memory pages on Unix and Xen.

IO pages are page-aligned, and wrapped in the Cstruct library to avoid copying the data contained within the page.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-mirage-types-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n io-page-%{version}

%build
ocaml setup.ml -configure --destdir %{buildroot}%{_libdir}/ocaml
ocaml setup.ml -build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/ocaml
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
export OCAMLFIND_LDCONF=%{buildroot}%{_libdir}/ocaml/ld.conf
ocaml setup.ml -install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/ocaml/io-page/META
%{_libdir}/ocaml/io-page/io_page.cma
%{_libdir}/ocaml/io-page/io_page.cmi
%{_libdir}/ocaml/io-page/dllio_page_unix_stubs.so

%files devel
%defattr(-,root,root)
%doc CHANGES README.md
%{_libdir}/ocaml/io-page/io_page.a
%{_libdir}/ocaml/io-page/io_page.cmx
%{_libdir}/ocaml/io-page/io_page.cmxa
%{_libdir}/ocaml/io-page/io_page.cmxs
%{_libdir}/ocaml/io-page/io_page.mli
%{_libdir}/ocaml/io-page/libio_page_unix_stubs.a
%{_libdir}/ocaml/io-page/io_page_unix.a
%{_libdir}/ocaml/io-page/io_page_unix.cma
%{_libdir}/ocaml/io-page/io_page_unix.cmi
%{_libdir}/ocaml/io-page/io_page_unix.cmx
%{_libdir}/ocaml/io-page/io_page_unix.cmxa
%{_libdir}/ocaml/io-page/io_page_unix.cmxs
%{_libdir}/ocaml/io-page/io_page_unix.ml

%changelog
* Mon Jan 20 2014 David Scott <dave.scott@citrix.com> - 1.0.0-1
- Initial package
