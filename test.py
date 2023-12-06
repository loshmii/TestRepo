import matplotlib.pyplot as plt
import numpy as np

def main() : 
    x = np.arange(0,2*np.pi,0.01)
    y = np.cos(x)
    plt.plot(x,y)
    plt.show()

main()