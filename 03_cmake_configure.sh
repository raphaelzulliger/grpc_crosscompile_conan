#!/bin/sh
source activate.sh
cmake . -DCMAKE_MODULE_PATH=$(pwd)
