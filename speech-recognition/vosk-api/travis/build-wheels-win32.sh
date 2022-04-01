#!/bin/bash
set -e -x

# Build libvosk
cd /opt
git clone https://github.com/alphacep/vosk-api
cd vosk-api/src
EXTRA_LDFLAGS=-Wl,--out-implib,libvosk.lib CXX=i686-w64-mingw32-g++-posix EXT=dll KALDI_ROOT=/opt/kaldi/kaldi OPENFST_ROOT=/opt/kaldi/local OPENBLAS_ROOT=/opt/kaldi/local make -j $(nproc)

# Copy dependencies
cp /usr/lib/gcc/i686-w64-mingw32/*-posix/libstdc++-6.dll /opt/vosk-api/src
cp /usr/lib/gcc/i686-w64-mingw32/*-posix/libgcc_s_sjlj-1.dll /opt/vosk-api/src
cp /usr/i686-w64-mingw32/lib/libwinpthread-1.dll /opt/vosk-api/src

# Copy dlls to output folder
mkdir -p /io/wheelhouse/win32
cp /opt/vosk-api/src/*.{dll,lib} /io/wheelhouse/win32

# Build wheel and put to the output folder
export VOSK_SOURCE=/opt/vosk-api
export VOSK_PLATFORM=Windows
export VOSK_ARCHITECTURE=32bit
python3 -m pip -v wheel /opt/vosk-api/python --no-deps -w /io/wheelhouse
