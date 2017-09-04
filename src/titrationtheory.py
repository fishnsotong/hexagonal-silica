# @author: Wayne Yeo <fishnsotong>
# @date:   2017-08-17T01:21:07+08:00
# @email:  wayne.yeo.wei.zhong.2017@vjc.sg
# @last modified by:   fishnsotong
# @last modified time: 2017-08-17T01:42:07+08:00



import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import datetime as dt

# importing data from csv file
volume_total, pH = np.loadtxt("../data/titration1.csv", unpack=True,
delimiter=",", skiprows=1, dtype=float)
pH = np.flipud(pH)

# set global parameters
conc_acid = 0.05
conc_h = 10 ** -pH
conc_oh = 10 ** -14 / conc_h # Kw = [h+][oh-]
ka =  6.2e-8
kw = 10e-14
Va = 20

# define fitting function
def volumeBase(Ca, Va, Cb, Ka, Kw, H):
    Vb = -Va*((H^3+Ka*H^2-(Kw+Ka*Ca)*H-Kw*Ka)/(H^3+(Ka+Cb)*H^2+(Ka*Cb-Kw)*H-Ka*Kw))
    return Vb

# fit data using SciPy's Levenburg-Marquart method
conc_base0 = 0.1 # initial guess for fitting parameter
conc_base, nlcov = scipy.optimize.curve_fit(volumeBase, pH, volume_total, conc_base0, sigma=None)
# name of the function, data, data, whether you have error bars, sigma=None
# conc_base0 is the (best) fit parameter from scipy.optimize.curve_fit

# b_stddev is the standard deviation of the fit parameter
b_stddev = np.sqrt( nlcov[0][0] )

# create array using fitting function
volume_theory = volumeBase(conc_acid, Va, conc_base, ka, kw, conc_h)

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
