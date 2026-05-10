#!/bin/bash

EXECUTABLE=./Assembler

pushd /autograder/source/ >/dev/null

# run student-submitted code (untrusted)
runuser -u student -- ${EXECUTABLE} $(pwd)/${1}

popd >/dev/null
