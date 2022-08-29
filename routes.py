from flask import render_template
from server import app

@app.route('/', methods=['GET', 'POST'])
def root_route():
  return render_template('main.html')