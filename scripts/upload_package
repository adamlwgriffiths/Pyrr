#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
pushd $DIR
cd ..
python setup.py sdist bdist_wheel
twine upload dist/*
popd
