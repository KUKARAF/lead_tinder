#!/usr/bin/env python
# -*- coding: utf-8 -*-



from flask import Flask, render_template, request, redirect, jsonify, send_from_directory, redirect, make_response
from requests import get
import csv 
import os
import pickle
import codecs

class work: 
    def __init__(self): 
        self.TODOLIST = []
        self.CURRENT_ITEM = []
        self.out_path = 'out.csv'

    def populate(self, csvdata):
        self.TODOLIST = csvdata
        self.CURRENT_ITEM = self.TODOLIST.pop().split("\t")

    def next(self):
        while self.CURRENT_ITEM[-1] in ['kein', 'niedrig', 'mittel', 'hoch']:
            with open('out.csv', 'a', newline='') as csvfile:
                csvfile = csv.writer(csvfile, delimiter='\t',
                                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csvfile.writerow(self.CURRENT_ITEM)
                self.CURRENT_ITEM = self.TODOLIST.pop().split("\t")

    def rate(self, rating):
        if self.CURRENT_ITEM[-1] in [' ', '\r', '']:
            self.CURRENT_ITEM = rating
            self.next()
        else:
            self.CURRENT_ITEM.append(rating)
            
    def url(self):
        return self.CURRENT_ITEM[-2]

    def scrub(self):
        os.remove(self.out_path)
        w.TODOLIST = []
        w.CURRENT_ITEM = []

app = Flask(__name__)

w = work()

@app.route("/tinder_lead", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
#        while w.CURRENT_ITEM[-1] in ['kein', 'niedrig', 'mittel', 'hoch']:
#            w.CURRENT_ITEM = w.TODOLIST.pop().split("\t")
        return render_template('index.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file_index():
    if request.method == 'GET':
        file_path="out.csv"
        if os.path.exists(file_path):
            w.scrub()
        return render_template('upload.html')
    elif request.method == 'POST':
        w.populate(request.form.get("confirmationText").split("\n"))
        return redirect("/tinder_lead")
	
#@app.route('/uploader', methods = ['GET', 'POST'])
#def upload_file():
#    if request.method == 'POST':
#        f = request.files['file']
#        f.save(f.filename)
#        with codecs.open('input_file.csv', mode='r', encoding='utf-8') as read_file:
#            for n, row in enumerate(csv.reader(read_file)):
#                w.TODOLIST.append(row)
#        return 'file uploaded successfully'


@app.route('/next_url', methods = ['GET', 'POST'])
def next_url():
    if request.method == 'POST':
        data = request.data.decode()
        w.rate(data)
        resp = jsonify(success=True)
        return resp
    elif request.method == 'GET':
        a = f'http://{w.url()}'
        return redirect(a)

@app.route('/tinder_lead_proxy', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    print(w.url())
    if not w.TODOLIST == [] or not w.CURRENT_ITEM[-1] in ['kein', 'niedrig', 'mittel', 'hoch']:
        try: 
            return get(f'https://{w.url()}{path}').content
        except: 
            return get(f'http://{w.url()}{path}').content
    else: 
        return send_from_directory("./", "out.csv")

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=123)
