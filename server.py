import os
import matplotlib
matplotlib.use('Agg')
from routes import static, scatter
from bottle import run

run(port=os.environ['PORT'])
