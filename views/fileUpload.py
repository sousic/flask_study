# -*- coding: UTF-8 -*-
import os
from flask import Flask, request, render_template, redirect, Blueprint, make_response, url_for
from werkzeug.utils import secure_filename

root_path = ''
save_path = 'upload/'


class fileUpload():
    mod = Blueprint('fileUpload', __name__, url_prefix='/fileUpload')

    @mod.route('/')
    def index():
        return render_template('fileupload/index.html')

    @mod.route('/file_upload/', methods = ['GET', 'POST'])
    def file_upload():

        if request.method == 'POST':
            f = request.files['file']
            f.save(os.path.join(root_path,save_path) + secure_filename(f.filename))
            filename = secure_filename(f.filename)

            response = make_response(render_template('fileupload/index.html', filename=filename))
            #response = make_response(redirect(url_for('fileUpload.index')))
            #response.headers['filename'] = filename

        return response