from flask import Flask
from mymodules import vsearch

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return "Hello world from Flask!"


@app.route('/search4')
def do_search() -> str:
    '''Return vowels found in a given string'''
    s = "hello world!"
    vowels = "aeiou"
   
    return f"In '{s}' word(s) we found {vsearch.search4letters(s, vowels)} as vowel"

print(help(do_search))
app.run()