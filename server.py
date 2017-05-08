import os
from routes import static, scatter
from bottle import run

run(port=os.environ['PORT'])
