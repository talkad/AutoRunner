#!/bin/bash

script_path=$1
compiler=$2

module purge
module load cmake/3.25.1
module load gnu8/8.3.0
module load openmpi3/3.1.4


cd $script_path
chmod +x clean.sh
./clean.sh $compiler
