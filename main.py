
from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

sales_plays_data = [
    {
        "name": "Sales Play 1",
        "metrics": {
            "revenue": 10000,
            "bookings": 50,
            "conversion_rate": 10
        },
        "details": "This sales play is designed to target large enterprise customers with complex needs."
    },
    {
        "name": "Sales Play 2",
        "metrics": {
            "revenue": 5000,
            "bookings": 25,
            "conversion_rate": 5
        },
        "details": "This sales play is designed to target small businesses with limited budgets."
    }
]

book_of_business_data = [
    {
        "customer_name": "Customer 1",
        "revenue": 100000,
        "bookings": 500,
        "growth_rate": 10
    },
    {
        "customer_name": "Customer 2",
        "revenue": 50000,
        "bookings": 250,
        "growth_rate": 5
    }
]

performance_data = [
    {
        "fsr_name": "FSR 1",
        "metrics": {
            "revenue": 1000000,
            "bookings": 5000,
            "conversion_rate": 10
        },
        "details": "FSR 1 is a top performer with a strong track record of success."
    },
    {
        "fsr_name": "FSR 2",
        "metrics": {
            "revenue": 500000,
            "bookings": 2500,
            "conversion_rate": 5
        },
        "details": "FSR 2 is a new hire with potential but needs to improve their performance."
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sales_plays')
def sales_plays():
    return render_template('sales_plays.html', sales_plays=sales_plays_data)

@app.route('/book_of_business')
def book_of_business():
    return render_template('book_of_business.html', book_of_business=book_of_business_data)

@app.route('/performance_dashboards')
def performance_dashboards():
    return render_template('performance_dashboards.html', performance_data=performance_data)

@app.route('/api/sales_plays')
def api_sales_plays():
    return jsonify(sales_plays_data)

@app.route('/api/book_of_business')
def api_book_of_business():
    return jsonify(book_of_business_data)

@app.route('/api/performance_data')
def api_performance_data():
    return jsonify(performance_data)

if __name__ == '__main__':
    app.run(debug=True)
