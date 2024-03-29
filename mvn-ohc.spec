#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-ohc
Version  : 0.4.4
Release  : 4
URL      : https://github.com/snazy/ohc/archive/0.4.4.tar.gz
Source0  : https://github.com/snazy/ohc/archive/0.4.4.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/caffinitas/ohc/ohc-core-j8/0.4.4/ohc-core-j8-0.4.4.jar
Source2  : https://repo.maven.apache.org/maven2/org/caffinitas/ohc/ohc-core-j8/0.4.4/ohc-core-j8-0.4.4.pom
Source3  : https://repo.maven.apache.org/maven2/org/caffinitas/ohc/ohc-core/0.4.4/ohc-core-0.4.4-sources.jar
Source4  : https://repo.maven.apache.org/maven2/org/caffinitas/ohc/ohc-core/0.4.4/ohc-core-0.4.4.jar
Source5  : https://repo.maven.apache.org/maven2/org/caffinitas/ohc/ohc-core/0.4.4/ohc-core-0.4.4.pom
Source6  : https://repo.maven.apache.org/maven2/org/caffinitas/ohc/ohc-parent/0.4.4/ohc-parent-0.4.4.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-ohc-data = %{version}-%{release}
Requires: mvn-ohc-license = %{version}-%{release}

%description
OHC - A off-heap-cache
======================
Status
------
This library should be considered as **nearly** *production ready*.

%package data
Summary: data components for the mvn-ohc package.
Group: Data

%description data
data components for the mvn-ohc package.


%package license
Summary: license components for the mvn-ohc package.
Group: Default

%description license
license components for the mvn-ohc package.


%prep
%setup -q -n ohc-0.4.4

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-ohc
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-ohc/LICENSE.txt
cp ohc-benchmark/LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-ohc/ohc-benchmark_LICENSE.txt
cp ohc-core-j8/LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-ohc/ohc-core-j8_LICENSE.txt
cp ohc-core/LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-ohc/ohc-core_LICENSE.txt
cp ohc-jmh/LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-ohc/ohc-jmh_LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-core-j8/0.4.4
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-core-j8/0.4.4/ohc-core-j8-0.4.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-core-j8/0.4.4
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-core-j8/0.4.4/ohc-core-j8-0.4.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-core/0.4.4
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-core/0.4.4/ohc-core-0.4.4-sources.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-core/0.4.4
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-core/0.4.4/ohc-core-0.4.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-core/0.4.4
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-core/0.4.4/ohc-core-0.4.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-parent/0.4.4
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-parent/0.4.4/ohc-parent-0.4.4.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-core-j8/0.4.4/ohc-core-j8-0.4.4.jar
/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-core-j8/0.4.4/ohc-core-j8-0.4.4.pom
/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-core/0.4.4/ohc-core-0.4.4-sources.jar
/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-core/0.4.4/ohc-core-0.4.4.jar
/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-core/0.4.4/ohc-core-0.4.4.pom
/usr/share/java/.m2/repository/org/caffinitas/ohc/ohc-parent/0.4.4/ohc-parent-0.4.4.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-ohc/LICENSE.txt
/usr/share/package-licenses/mvn-ohc/ohc-benchmark_LICENSE.txt
/usr/share/package-licenses/mvn-ohc/ohc-core-j8_LICENSE.txt
/usr/share/package-licenses/mvn-ohc/ohc-core_LICENSE.txt
/usr/share/package-licenses/mvn-ohc/ohc-jmh_LICENSE.txt
