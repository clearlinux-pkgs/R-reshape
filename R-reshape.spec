#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-reshape
Version  : 0.8.8
Release  : 23
URL      : https://cran.r-project.org/src/contrib/reshape_0.8.8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/reshape_0.8.8.tar.gz
Summary  : Flexibly Reshape Data
Group    : Development/Tools
License  : MIT
Requires: R-plyr
BuildRequires : R-plyr
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n reshape

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569371168

%install
export SOURCE_DATE_EPOCH=1569371168
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reshape
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reshape
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reshape
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc reshape || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/reshape/CITATION
/usr/lib64/R/library/reshape/DESCRIPTION
/usr/lib64/R/library/reshape/INDEX
/usr/lib64/R/library/reshape/LICENSE
/usr/lib64/R/library/reshape/Meta/Rd.rds
/usr/lib64/R/library/reshape/Meta/data.rds
/usr/lib64/R/library/reshape/Meta/features.rds
/usr/lib64/R/library/reshape/Meta/hsearch.rds
/usr/lib64/R/library/reshape/Meta/links.rds
/usr/lib64/R/library/reshape/Meta/nsInfo.rds
/usr/lib64/R/library/reshape/Meta/package.rds
/usr/lib64/R/library/reshape/NAMESPACE
/usr/lib64/R/library/reshape/NEWS
/usr/lib64/R/library/reshape/R/reshape
/usr/lib64/R/library/reshape/R/reshape.rdb
/usr/lib64/R/library/reshape/R/reshape.rdx
/usr/lib64/R/library/reshape/data/Rdata.rdb
/usr/lib64/R/library/reshape/data/Rdata.rds
/usr/lib64/R/library/reshape/data/Rdata.rdx
/usr/lib64/R/library/reshape/help/AnIndex
/usr/lib64/R/library/reshape/help/aliases.rds
/usr/lib64/R/library/reshape/help/paths.rds
/usr/lib64/R/library/reshape/help/reshape.rdb
/usr/lib64/R/library/reshape/help/reshape.rdx
/usr/lib64/R/library/reshape/html/00Index.html
/usr/lib64/R/library/reshape/html/R.css
