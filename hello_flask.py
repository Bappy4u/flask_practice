from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return "Hello world from Flask!"


@app.route('/search4')
def do_search() -> str:
    '''Return vowels found in a given string'''
    s = "hello world!"
    res = []
    vowels = set("aeiou")
    '''
    dic = {}
    for c in set(s):
        dic[c.lower()]=1

    for c in vowels:
        if dic.get(c):
            res.append(c)
    '''
    return f"In '{s}' word(s) we found {vowels.intersection(set(s))} as vowel"

print(help(do_search))
app.run()