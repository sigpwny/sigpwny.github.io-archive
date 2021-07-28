#!/bin/bash
cat page-top-half.html <(python3 profile.py) page-bottom-half.html > index.html
