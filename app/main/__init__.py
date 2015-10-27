#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint
from flask.ext.restful import Api


main = Blueprint('main', __name__)
api = Api(main)

from .views import *
api.add_resource(monitorResource, '/v1/enviroment/<id>')
api.add_resource(monitorList, '/v1/mobile')
