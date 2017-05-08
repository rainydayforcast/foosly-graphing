from bottle import post, request
import numpy as np
import matplotlib.pyplot as plt
import uuid

@post('/scatter')
def test():
    for entity in request.json:
        x = entity['x']
        y = entity['y']
        name = entity['name']
        size = entity['size'] if 'size' in entity else 80
        plt.scatter(x, y, label=name, s=size)

    plt.legend()
    path = 'static/' + str(uuid.uuid4()) + '.png'
    plt.savefig(path, bbox_inches='tight')
    plt.gcf().clear()
    return { 'path': path }
