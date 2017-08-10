# @Author: fishnsotong
# @Date:   2017-08-10T11:35:49+08:00
# @Last modified by:   fishnsotong
# @Last modified time: 2017-08-10T13:02:09+08:00



import numpy as np
import matplotlib.pyplot as plt

# importing data from csv file
volume_total, pH = np.loadtxt("../data/titration1.csv", unpack=True,
delimiter=",", skiprows=1, dtype=float)

# plotting
plt.plot(volume_total, pH, "bo", label="0.05 M phosphoric acid titration")

# labels
plt.ylim(7, 14)
plt.xlim(0, 100)
plt.legend(loc='best', prop={'size': 10})
plt.xlabel("Volume of phosphoric acid")
plt.ylabel("pH")
plt.title("Titration of 0.05 M phosphoric acid into DDAOH")
plt.yticks([7, 8, 9, 10, 11, 12, 13, 14])

# save plot to file
#plt.savefig("titration1.png")

# display plot on screen
plt.show()
