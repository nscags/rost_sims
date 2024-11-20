# RoST Sims Tutorial

```
# this is the version of python these commands were run with
# just in case there are errors
python3 --version
> Python 3.12.3

# create python virtual env
python3 -m venv venv

# activate venv
source venv/bin/activate

# install bgpy
pip install bgpy_pkg

# clone repo 
git clone git@github.com:nscags/rost_sims.git

# navigate to engine_tests dir
cd rost_sims/rost/tests/engine_tests

# run pytest
pytest
```