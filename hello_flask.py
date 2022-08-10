from flask import Flask, render_template
from mymodules.vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return "Hello world from Flask!"

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
    the_title='Welcome to search4letters on the web!')
    
@app.route('/search4')
def do_search() -> str:
    '''Return vowels found in a given string'''
    s = "hello world!"
    vowels = "aeiou"
   
    return f"In '{s}' word(s) we found {search4letters(s, vowels)} as vowel"


app.run()