# @Author: fishnsotong
# @Date:   2017-08-10T11:35:49+08:00
# @Last modified by:   fishnsotong
# @Last modified time: 2017-11-22T00:46:52+08:00



import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# importing data from csv file
volume_total, pH = np.loadtxt("../data/titration2.csv", unpack=True,
delimiter=",", skiprows=1, dtype=float)

# plotting
fig = plt.figure()
plt.plot(volume_total, pH, "bo", label="0.05 M phosphoric acid titration")
ax = fig.add_subplot(111)

# labels
plt.ylim(0, 14)
plt.xlim(0, 25)
plt.legend(loc='best', prop={'size': 10})
plt.xlabel("Volume of phosphoric acid (mL)")
plt.ylabel("pH", fontsize = 20)
plt.title("Titration of 0.05 M phosphoric acid into DDAOH")
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# plt.axhspan(11.6, 13, alpha=0.2, color='yellow')
# plt.axhspan(10.9, 11.6, alpha=0.2, color='blue')

ax.annotate('titration endpoint', xy=(8.4, 7),  xycoords='data',
            xytext=(0.8, 0.7), textcoords='axes fraction',
            arrowprops=dict(facecolor='green', shrink=0.05),
            horizontalalignment='right', verticalalignment='top',
            )

# save plot to file
now = str(dt.datetime.today())
plt.savefig("../figs/titration2"+ now +".png")

# display plot on screen
#plt.show()
