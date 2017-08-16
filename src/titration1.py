# @Author: fishnsotong
# @Date:   2017-08-10T11:35:49+08:00
# @last modified by:   fishnsotong
# @last modified time: 2017-08-16T19:55:17+08:00



import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import datetime as dt

# importing data from csv file
volume_total, pH = np.loadtxt("../data/titration1.csv", unpack=True,
delimiter=",", skiprows=1, dtype=float)

# set global parameters
conc_acid = 0.05
conc_h = 10 ** -pH
conc_oh = 10 ** -14 / conc_h # Kw = [h+][oh-]
ka = 1.10e-3
conc_base = 1
volume_base = 30

# define fitting functions
def titrationVolume(conc_acid, conc_base, conc_h, conc_oh, ka):
    """ volume of sa needed when titrating a strong acid into a weak base"""
    delta = conc_h - conc_oh
    alpha = ka / (conc_h + ka)
    volume = volume_base * ((conc_base * alpha - delta) / (conc_acid + delta))
    return volume

# fit data using SciPy's Levenburg-Marquart method
conc_base0 = (0.1, 10, 0.2, 5) # initial guess for fitting parameter
conc_base, nlcov = scipy.optimize.curve_fit(titrationVolume, conc_h, conc_oh, conc_base0, sigma=None)
# name of the function, data, data, whether you have error bars, sigma=None
# conc_base0 is the (best) fit parameter from scipy.optimize.curve_fit

# b_stddev is the standard deviation of the fit parameter
b_stddev = np.sqrt( nlcov[0][0] )

volume_theory = titrationVolume(conc_acid, conc_base, conc_h, conc_oh, ka)

# plotting
plt.plot(volume_total, pH, "bo", label="0.05 M phosphoric acid titration")

# labels
plt.ylim(7, 14)
plt.xlim(0, 100)
plt.legend(loc='best', prop={'size': 10})
plt.xlabel("Volume of phosphoric acid (mL)")
plt.ylabel("pH")
plt.title("Titration of 0.05 M phosphoric acid into DDAOH")
plt.yticks([7, 8, 9, 10, 11, 12, 13, 14])

# save plot to file
now = str(dt.datetime.today())
plt.savefig("../figs/titration1"+ now +".png")

# display plot on screen
# plt.show()
