from flask import Flask, render_template, request, redirect
from functions import add_transaction, view_summary, generate_pie_chart, generate_bar_chart
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    date = request.form['date']
    t_type = request.form['type']
    category = request.form['category']
    amount = request.form['amount']
    add_transaction(date, t_type, category, amount)
    return redirect('/summary')

@app.route('/summary')
def summary():
    total_income, total_expense, net = view_summary()
    generate_pie_chart()
    generate_bar_chart()
    return render_template('summary.html', income=total_income, expense=total_expense, net=net)

if __name__ == '__main__':
    app.run(debug=True)
