import os
import matplotlib
matplotlib.use('Agg')
from routes import static, scatter
from bottle import run

run(host='0.0.0.0', port=int(os.environ.get("PORT")))
