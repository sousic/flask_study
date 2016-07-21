# -*- coding: UTF-8 -*-
from flask import  Flask, Blueprint, render_template


class Main():
    mod = Blueprint('main', __name__, )

    @mod.route('/')
    def index():
        return render_template('main.html')