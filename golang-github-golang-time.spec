# http://github.com/golang/time
%global forgeurl        https://github.com/golang/time
%global goipath         golang.org/x/time
%global commit          c06e80d9300e4443158a03817b8a8cb37d230320

%gometa -i

Name:           golang-github-golang-time
Version:        0
Release:        0.9%{?dist}
Summary:        Go supplementary time packages
# Detected licences
# - BSD (3 clause) at 'LICENSE'
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTORS CONTRIBUTING.md README AUTHORS PATENTS

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 10 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.8.gitc06e80d
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.7.20170420gitc06e80d
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitc06e80d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.5.gitc06e80d
- Bump to upstream c06e80d9300e4443158a03817b8a8cb37d230320
  resolves: #1494518

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gita4bde12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gita4bde12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gita4bde12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 11 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.gita4bde12
- First package for Fedora
  resolves: #1354398
