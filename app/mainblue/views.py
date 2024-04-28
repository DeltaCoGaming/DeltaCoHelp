from flask import Blueprint, jsonify, render_template, request
import os

mainblue = Blueprint('mainblue', __name__)

@mainblue.route('/')
def home():
    return render_template('index.html')

