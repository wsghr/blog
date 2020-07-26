from app import app
from flask import render_template,request,jsonify
import os
import json
import re
from app import utils

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/editor', methods=['GET', 'POST'])
def editor():
    return render_template('editor.html')


@app.route('/xingzuo', methods=['GET', 'POST'])
def xingzuo():
    if request.method == "POST":
        data = request.get_json()
        # print(type(data))
        # print(data)
        xz = utils.request1(data, 'GET')
        print(xz)
        # print(type(xz))
        return jsonify(json.dumps(xz,ensure_ascii=False))

    return render_template('xingzuo.html')


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    result = {}
    action = request.args.get('action')

    if action in ('uploadimage', 'uploadvideo', 'uploadfile'):
        upfile = request.files['upfile']  # 这个表单名称以配置文件为准
        # upfile 为 FileStorage 对象
        # 这里保存文件并返回相应的URL
        upfile.save(upload)
        result = {
            "state": "SUCCESS",
            "url": "upload/demo.jpg",
            "title": "demo.jpg",
            "original": "demo.jpg"
        }

    return json.dumps(result)
