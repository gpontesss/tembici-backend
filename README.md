# Backend test
Completion for the following test: https://github.com/tembici/desafio-backend
The proposal for the test is present in 'instructions.md' file.

## Virtual Environment
I'm using a python virtual enviroment, python version 3.7.3. To create a python virtual envivorment run the following, assuming not having the virtualenv installed on your pc and a *NIX system.

``` bash
# Install virtualenv and create virtual enviroment
pip install virtualenv
virtualenv --python=/path/to/python /path/to/env

# Activate virtual enviroment and install requirements
. /path/to/env/bin/active
pip install -r requirements.txt
```

## Running the API
To run the the API run the following:

``` bash
python server.py
```

## Notes
I just did the first commit :). Don't expect more than a 'hello world'.