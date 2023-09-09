import numpy as np
import matplotlib.pyplot as plt
array=np.array(
    [
        [0,0, 0, 0, 0, 0,0,0,0,0],
        [0,1, 1, 1, 0, 0,1,1,1,0],
        [0,0, 1, 0, 0, 0,0,1,0,0],
        [0,0, 1, 0, 0, 0,0,1,0,0],
        [0,0, 1, 0, 0, 0,0,1,0,0],
        [0,1, 1, 1, 0, 0,0,1,0,0],
        [0,0, 0, 0, 0, 0,0,0,0,0],

    ]
)
plt.imshow(array,cmap="gray")
plt.axis("off")
plt.show()