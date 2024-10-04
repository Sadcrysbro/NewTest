from flask import Flask, jsonify, request
import psycopg2
import getopt
import sys
import argparse
import os
from tkinter import messagebox 

app = Flask("DB_API")
conn = psycopg2.connect(database="dawgcrysdatabase", host="dpg-crvl6ia3esus7392qkr0-a.oregon-postgres.render.com", user="dawgcrysdatabase_user", password="DPkPqCumvSvQq80duAMSqCvBWklsfAme", port="5432")
cursor = conn.cursor()

@app.route('/create', methods=['POST'])
def create_table():
    data = request.get_data().decode('utf-8')
    messagebox.showinfo("showinfo", "Information")

    return jsonify({"test": 1})

app.run()