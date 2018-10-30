from flask import Flask, render_template
import csv
__author__='Koray Toksoz'

app = Flask(__name__)


@app.route('/')
def hello_world():

    with open('reader.csv', 'r') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        cardInfo = list(csvReader)

    return render_template('index.html', cards=cardInfo)


if __name__ == '__main__':
    app.run()
