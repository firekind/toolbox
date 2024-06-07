#!/bin/bash

set -eo pipefail

NAME=toolbox-tweaked
VERSION=0.0.99.5
PROJDIR=$PWD
TARGETDIR=$PWD/target
BUILDOUTPUT=$TARGETDIR/$NAME-$VERSION

if [[ -d $TARGETDIR ]]; then
    rm -rf $TARGETDIR
fi
mkdir $TARGETDIR


# building
meson setup builddir --prefix $BUILDOUTPUT/usr
cd builddir
meson configure -Dprofile_dir=$BUILDOUTPUT/etc/profile.d
meson configure --sysconfdir $BUILDOUTPUT/etc
meson configure -Dbash_completions_dir=$BUILDOUTPUT/usr/share/bash-completion/completions
meson configure -Dfish_completions_dir=$BUILDOUTPUT/usr/share/fish/vendor_completions.d
meson configure -Dtmpfiles_dir=$BUILDOUTPUT/usr/lib/tmpfiles.d  
ninja install

# for some reason when in docker, the interpreter of the binary is set to
# /run/host/usr/lib64/ld-linux-x86-64.so.2 so fixing that
if [ -f /.dockerenv ]; then
    patchelf --set-rpath "" $BUILDOUTPUT/usr/bin/toolbox
    patchelf --set-interpreter /lib64/ld-linux-x86-64.so.2 $BUILDOUTPUT/usr/bin/toolbox
fi

# rpm setup
if [[ -d ~/rpmbuild ]]; then
    rm -rf ~/rpmbuild
fi
rpmdev-setuptree

cd $TARGETDIR
SOURCETAR=$NAME-$VERSION.tar.gz
tar -cvf $SOURCETAR $NAME-$VERSION

mv $SOURCETAR ~/rpmbuild/SOURCES
cp $PROJDIR/toolbox.spec ~/rpmbuild/SPECS
QA_RPATHS=$(( 0x0010 )) rpmbuild --define "debug_package %{nil}" -bb ~/rpmbuild/SPECS/toolbox.spec
cp ~/rpmbuild/RPMS/$(arch)/$NAME-$VERSION-1.fc40.$(arch).rpm $TARGETDIR
