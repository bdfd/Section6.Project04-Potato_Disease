'''
Date         : 2022-12-05 14:13:08
Author       : BDFD,bdfd2005@gmail.com
Github       : https://github.com/bdfd
LastEditTime : 2023-10-26 13:20:14
LastEditors  : BDFD
Description  : 
FilePath     : \app.py
Copyright (c) 2022 by BDFD, All Rights Reserved. 
'''
from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from predict.predict import predict

app = Flask(__name__)

app.register_blueprint(predict, url_prefix="/predict")


@app.route('/')
def index():
    # Redirecting to the '/predict' route
    return redirect(url_for('predict.predict_index'))
    # return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
