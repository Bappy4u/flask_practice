from flask import Flask, render_template, request
from mymodules.vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def entry_page() -> 'html':
    return render_template('entry.html',
    the_title='Welcome to search4letters on the web!')
    
@app.route('/search4', methods=['POST'])
def do_search() -> str:
    '''Return vowels found in a given string'''
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    title = "Here is your results:"

    log_request(request, results)
    return render_template('results.html',the_title=title, the_results=results, the_letters=letters, the_phrase=phrase)


def log_request(req:'flask_request', res:str):
    with open("todos.txt",'a') as log:
        print(req, res, file=log)


if __name__=='__main__':
    app.run(debug=True)
