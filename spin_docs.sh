#!/bin/bash
set -e  # stop on errors

# Cleanup and rebuild
rm -rf doxy_docs/doxygen
mkdir -p doxy_docs/doxygen
doxygen

# Build Sphinx docs
cd docs
make html

# Start Sphinx server in background
cd _build/html
python -m http.server 8082 &
SPHINX_PID=$!

# Return to julia_docs
cd ../../../julia_docs

# Build JuliaDocs
julia make.jl

# Start JuliaDocs server in background
cd build
python -m http.server 8081 &
JULIA_PID=$!

# Trap Ctrl+C and kill both servers
trap "echo 'Stopping servers...'; kill $SPHINX_PID $JULIA_PID; exit 0" SIGINT

# Wait for background jobs
wait
