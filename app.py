from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route('/')
def print_date():
    # Returns the current local date
    today = date.today()
    return 'Today date is: ' + str(today)
