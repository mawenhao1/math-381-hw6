import numpy as np
import matplotlib.pyplot as plt
import re
import io
contents=""
with open("hist.txt") as f:
    contents = f.read()
contents = contents[1:-1]

hist = np.fromstring(contents, sep = ",")
value= np.array(hist)
n, bins, patches = plt.hist(hist, 23, 
                            density = 1, 
                            color ='green',
                            alpha = 0.7)
print(np.std(value))
print(np.mean(value))
print((str(np.mean(value) - np.std(value))) + "," + (str(np.mean(value) + np.std(value))))
plt.show()