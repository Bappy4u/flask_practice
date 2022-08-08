from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return "Hello world from Flask!"


@app.route('/search4')
def do_search() -> str:
    s = "Learning flask"
    res = []
    vowels = "aeiou"
    dic = {}
    for c in set(s):
        dic[c.lower()]=1

    for c in vowels:
        if dic.get(c):
            res.append(c)

    return f"In '{s}' word(s) we found {len(res)} vowel(s) which is/are {','.join(res)}."


app.run()