#!/bin/bash
rm -r doxy_docs/doxygen
mkdir doxy_docs/doxygen
doxygen
cd docs
make html
cd _build/html
python -m http.server 8082 &
cd ../../../julia_docs
julia make.jl
cd build
python -m http.server 8081

