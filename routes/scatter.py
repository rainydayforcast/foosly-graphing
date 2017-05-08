from bottle import get
import numpy as np
import matplotlib.pyplot as plt
import uuid

plt.use('Agg')

@get('/test')
def test():
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    path = 'static/' + str(uuid.uuid4()) + '.png'
    plt.savefig(path, bbox_inches='tight')
    return { 'path': path }
