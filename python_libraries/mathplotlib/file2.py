import numpy as np
from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")

def plt_bar_gph():
    """plots bar
    it plots a bar graph
    """
    dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
    plt.bar(dev_x, dev_y, color = "#444444", label = "All Devs")
    plt.legend()
    plt.show()

def plt_side():
    dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    py_dev_y = [45375, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
    js_dev_y = [32442, 43213, 483921, 49328, 49927, 50321, 52382, 55134, 55521, 55913, 60000]
    
    x_index = np.arange(len(dev_x))
    width  = 0.25
    plt.bar(x_index, dev_y, color = "#444444", label = "All Devs")
    plt.bar(x_index, py_dev_y, color = "#008fd5", label = "Pyton Dev")
    plt.bar(x_index, dev_y, color = "#e5ae38", label = "javascrit Dev")
    plt.title("salary to Age")
    plt.legend()
    plt.show()
plt_side()