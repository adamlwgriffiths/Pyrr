#!/bin/bash

# get the directory this file is stored in
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# push current directory onto stack
# and move to this file's directory
pushd $DIR

# move up to the parent
cd ..

# run our test
python setup.py sdist


# return our path to its original state
popd

