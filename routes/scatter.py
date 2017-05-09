from bottle import post, request
import numpy as np
import matplotlib.pyplot as plt
import uuid

@post('/scatter')
def scatter():
    for entity in request.json:
        x = entity['x']
        y = entity['y']
        name = entity['name']
        plt.scatter(x, y, label=name, size=(np.pi * (6)**2))

    plt.legend()
    path = 'static/' + str(uuid.uuid4()) + '.png'
    plt.savefig(path, bbox_inches='tight')
    plt.gcf().clear()
    return { 'path': path }
