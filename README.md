# Backend test
Completion for the following test: https://github.com/tembici/desafio-backend
The proposal for the test is also present in 'instructions.md' file.

## Running the API
To run the the API run the following:

``` bash
flask run
```

Make sure that you have dependencies installed.

## Dependencies
+ Python 3.7.3;
+ virtualenv (See 'Virtual Environment');
+ SQLite3 (make sure to have it installed before compiling python, so the lib is present).

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

## TODO
+ Check if email already exists (Try catch exceptions);
+ Hash password and store it;
+ Check for uuid uniqueness;