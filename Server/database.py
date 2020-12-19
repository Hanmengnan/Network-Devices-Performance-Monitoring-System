from pymongo import *
from influxdb import *
from settings import *

client = InfluxDBClient(INFLUX_HOST, INFLUX_PORT, INFLUX_USER, INFLUX_PASSWORD, INFLUX_DATABASE_NAME)
