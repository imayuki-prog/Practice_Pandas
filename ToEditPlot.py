import matplotlib.pyplot as plt
import numpy as np

x_arr = np.arange(10) #holizontal line
y_arr = np.random.randint(0, 10, 10) #vertical line
plt.plot(x_arr, y_arr)

print(x_arr)
print(y_arr)

# zip joins x and y coordinates in pairs
for x,y in zip(x_arr,y_arr):
    print(x,y)
    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
    
plt.show()