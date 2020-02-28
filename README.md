# Mastercard Code Challenge

The Mastercard Code Challenge is a small application that carries out a request on the Wiki API to return a 
JSON formatted object.

## Installation

```
1. Open bash or command terminal and navigate to directroy where the repository it to be cloned to.  
2. Input command " git clone ADD URL
3. Navigate into installed directory
4. Input command " pip install -r requirements.txt "
5. Run application from the console by inputing command " python mastercard_code_challenge.py "
```

## Technology

```
The Mastercard Code Challenge application is written in Python language and utilises the Requests module to execute the 
request on the API and return the JSON object for parsing.
```

## unit test

```
Two unit tests were constructed for this application.  The first ensures that any other datatype than integer is passed 
to the check_information function that a ValueError is raised.  The second test ensures that a successful connection 
has been established before continuing to execute the code.
```