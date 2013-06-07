#!/usr/bin/python

import re
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def answer():
    q = request.args.get("q", "")
    print "Question:", q

    m = re.search("what is ([0-9]+) plus ([0-9]+)", q)

    answer = "Unknown"

    if m:
        answer = str(int(m.group(1)) + int(m.group(2)))

    print "Answer:", answer
    return answer

if __name__ == "__main__":
    app.run(host='0.0.0.0')
