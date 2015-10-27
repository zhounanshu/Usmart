#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import db


class Monitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(255), unique=False)
    mac = db.Column(db.String(255), unique=True)
    pm2_5 = db.Column(db.String(255))
    CO2 = db.Column(db.String(255))
    temperature = db.Column(db.String(255))
    humidity = db.Column(db.String(255))

    def __init__(self, mac, pm2_5, CO2, temperature, humidity, time):
        self.mac = mac
        self.pm2_5 = pm2_5
        self.CO2 = CO2
        self.temperature = temperature
        self.humidity = humidity
        self.time = time
