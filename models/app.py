#!/usr/bin/env python3
""" BMP Flask APP
"""
from flask import Flask, redirect, render_template, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """"""
    return render_template('index.html')


@app.route('/portfolio', methods=['GET'], strict_slashes=False)
def portfolio():
    """
    """
    return render_template('portfolio/portfolio.html')


@app.route('/portfolio/portraits', methods=['GET'], strict_slashes=False)
def portfolio_portrait():
    """
    """
    return render_template('portfolio/portrait.html')


@app.route('/portfolio/products', methods=['GET'], strict_slashes=False)
def portfolio_products():
    """
    """
    return render_template('portfolio/product.html')


@app.route('/portfolio/weddings', methods=['GET'], strict_slashes=False)
def portfolio_weddings():
    """
    """
    return render_template('portfolio/weddings.html')


@app.route('/portfolio/food', methods=['GET'], strict_slashes=False)
def portfolio_food():
    """
    """
    return render_template('portfolio/food.html')


@app.route('/about', methods=['GET'], strict_slashes=False)
def about():
    """"""
    return render_template('about.html')


@app.route('/blogs', methods=['GET'], strict_slashes=False)
def blogs():
    """"""
    return render_template('blog.html')


@app.route('/contact', methods=['GET'], strict_slashes=False)
def contact():
    """"""
    return render_template('contact.html')


@app.route('/videos', methods=['GET'], strict_slashes=False)
def videos():
    """"""
    return render_template('videos.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
