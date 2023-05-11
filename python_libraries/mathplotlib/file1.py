from matplotlib import pyplot as plt

#creating a list for x and y axis
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(dev_x, dev_y, label = 'all dev')

py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45375, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(py_dev_x, py_dev_y, label = 'python dev')

plt.xlabel('Ages')
plt.ylabel('salary USD')
plt.title('median salary (USD) by age ')#add graph title

#add legend in order which they were plot
#plt.legend(['All developers', 'python developers'])
#or we can add lable as we plot, and call the legend method
plt.legend()
plt.show()