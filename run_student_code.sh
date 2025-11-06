#!/bin/bash

EXECUTABLE=./assembler

pushd /autograder/source/ >/dev/null

# run student-submitted code (untrusted)
runuser -u student -- ${EXECUTABLE} $(pwd)/${1}

# copy outputs to own directory
mv *.hack /autograder/outputs

popd >/dev/null
