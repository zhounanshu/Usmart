#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint,send_from_directory
import os
from flask import render_template
from flask.ext.restful import Api


main = Blueprint('main', __name__)
api = Api(main)

from .views import *
api.add_resource(monitorResource, '/v1/enviroment/<id>')
api.add_resource(monitorList, '/v1/mobile')


@main.route('/favicon.ico')
def favicon():
    temp = main.root_path.split('/')[1: -1]
    path = ''
    for cell in temp:
        path += '/'
        path += cell
    return send_from_directory(os.path.join(path, 'static'),'ico/favicon.ico')


@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.route("/")
def index():
    return render_template('index.html')
