#!/bin/bash
rm ./test.db
python3 -m unittest discover . "*_test.py"
rm ./test.db
