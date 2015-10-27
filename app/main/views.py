#!/usr/bin/pyhton
# -*- coding: utf-8 -*-
from ..models import *
from flask.ext.restful import Resource, reqparse
import time
from ..util.pase import paser


def to_json(model):
    """ Returns a JSON representation of an SQLAlchemy-backed object. """
    json = {}
    for col in model._sa_class_manager.mapper.mapped_table.columns:
        json[col.name] = getattr(model, col.name)
    return json


def to_json_list(model_list):
    json_list = []
    for model in model_list:
        json_list.append(to_json(model))
    return json_list


class monitorResource(Resource):

    def get(self, id):
        record = Monitor.query.filter_by(id=id).first()
        return to_json(record)

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('data', type=str)
        args = parser.parse_args(strict=True)
        record = Monitor.query.filter_by(id=id).first()
        if record:
            record.username = args['data']
            db.session.commit()
            return {"status": "updated"}, 201
        return {"message": "not exit"}, 400

    def delete(self, id):
        record = Monitor.query.filter_by(id=id).first()
        if record:
            db.session.delete(record)
            db.session.commit()
            return {"status": "deleted"}, 204
        return {"message": "not exit"}, 400


class monitorList(Resource):

    def get(self):
        records = Monitor.query.limit(10)
        return to_json_list(records)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('mac', type=str)
        parser.add_argument('data', type=str)
        args = parser.parse_args(strict=True)
        if args is None:
            return {"erro": "no data"}
        buf = args['data'].split(' ')
        if len(buf) == 28:
            result = paser(buf)
        else:
            return {"error": "data error"}
        args['time'] = time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        new_record = Monitor(args['mac'], result['pm2_5'],
                             result['CO2'], result['temperature'],
                             result['humidity'], args['time'])
        db.session.add(new_record)
        db.session.commit()
        return {"status": "0k"}, 200
