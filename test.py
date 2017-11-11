from flask import Flask

app = Flask(__name__)


@app.route("/sequence/<int:number>")
def hello(number):
    result = ', '.join(sequence(number))
    return result


def sequence(num):
    seqs = list()
    try:
        i = int(num)
    except ValueError:
        print("Enter an integer!")
    else:
        while (i > 1):
            if (i % 2) != 0:
                i = (3 * i) + 1
                seqs.append(str(i))
            else:
                i = i / 2;
                seqs.append(str(i))
    return seqs
