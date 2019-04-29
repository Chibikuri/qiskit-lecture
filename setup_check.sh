#!/bin/bash

result= python ./test/test.py
# if [ "$result" = "OK" ]; then
#     echo "success"
# else
#     echo "fail"
# fi
version= pip list|fgrep "qiskit-terra"

