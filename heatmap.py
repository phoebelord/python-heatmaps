import matplotlib.pyplot as plt
import numpy as np

size = 50

fig = plt.figure()
ax = fig.add_subplot(111)
plt.axis('off')
arr = np.random.random((size, size))
im = ax.imshow(arr)

for i in range(60):
    plt.pause(1)
    arr = np.concatenate((arr, np.random.random((1, size))))
    arr = np.delete(arr, 0, 0)
    im.set_array(arr)

plt.show()
