[![AWS 3.7](https://github.com/MasciadriAndrea/github-actions-demo/actions/workflows/aws.yml/badge.svg)](https://github.com/MasciadriAndrea/github-actions-demo/actions/workflows/aws.yml)

# Multi-Cloud Continuous Integration sample project

This is a repo for building out Github Actions and Tricks. This is what i did:
* I practiced setting up this project over two Cloud environment: AWS Cloud9 and Google Cloud Shell.
* performed the following operations: install, lint and test via GitHub Actions
* changed the project over more Cloud Environments

[Demo Video of this repo](https://www.youtube.com/watch?v=4gbUYOgALik)



## Steps to run this project

* Create a Github Repo (if not created)
* Open a Cloud Shell
* Create ssh-keys in Azure Cloud Shell
* Upload ssh-keys to Github
* Create scaffolding for project (if not created)
  - Makefile

Should look similar to the file below

```bash
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_hello.py


lint:
	pylint --disable=R,C hello.py

all: install lint test
```

  - requirements.txt
  
The requirements.txt should include:

```bash
pylint
pytest
```

* Create a python virtual environment and source it if not created

```bash
python3 -m venv ~/.myrepo
source ~/.myrepo/bin/activate
```

* Create initial `hello.py` and `test_hello.py`

hello.py
```python
def toyou(x):
    return "hi %s" % x


def add(x):
    return x + 1


def subtract(x):
    return x - 1
```

test_hello.py
```python
from hello import toyou, add, subtract


def setup_function(function):
    print("Running Setup: %s" % {function.__name__})
    function.x = 10


def teardown_function(function):
    print("Running Teardown: %s" % {function.__name__})
    del function.x


### Run to see failed test
#def test_hello_add():
#    assert add(test_hello_add.x) == 12

def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9

```


* Run `make all` which will install, lint and test code.

* Setup Github Actions in `pythonapp.yml`

```yaml
name: Python application test with Github Actions

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.5
      uses: actions/setup-python@v1
      with:
        python-version: 3.5
    - name: Install dependencies
      run: |
        make install
    - name: Lint with pylint
      run: |
        make lint
    - name: Test with pytest
      run: |
        make test
```
