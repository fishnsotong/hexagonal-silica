# @author: Wayne Yeo <fishnsotong>
# @date:   2017-08-10T12:53:16+08:00
# @email:  wayne.yeo.wei.zhong.2017@vjc.sg
# @last modified by:   fishnsotong
# @last modified time: 2017-08-11T00:29:55+08:00



import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# importing data
volume_total, pHdata = np.loadtxt("../data/titration1.csv", unpack=True,
delimiter=",", skiprows=1, dtype=float)

# declaring constants
Ka1 = 7.6e-3
Ka2 = 6.2e-8
Ka3 = 2.1e-13
pHeqv = 7.02

# defining functions
pH = np.linspace(0, 14, 1000)
conc_hydronium = 10 ** -pH
conc_hydronium_data = 10 ** -pHdata

def H_value(conc_hydronium, Ka1, Ka2, Ka3):
    H = conc_hydronium ** 3 + conc_hydronium ** 2 * Ka1 + conc_hydronium * Ka1 * Ka2 + Ka1 * Ka2 * Ka3
    return H

H = H_value(conc_hydronium, Ka1, Ka2, Ka3)

H_data = H_value(conc_hydronium_data, Ka1, Ka2, Ka3)


f_h3po4 = conc_hydronium ** 3 / H
f_h2po4 = Ka1 * conc_hydronium ** 2 / H
f_hpo4 = Ka1 * Ka2 * conc_hydronium / H
f_po4 = Ka1 * Ka2 * Ka3 / H

f_h3po4_data = conc_hydronium_data ** 3 / H_data
f_h2po4_data = Ka1 * conc_hydronium_data ** 2 / H_data
f_hpo4_data = Ka1 * Ka2 * conc_hydronium_data / H_data
f_po4_data = Ka1 * Ka2 * Ka3 / H_data

# plotting
plt.figure(figsize=(15, 8))
plt.subplot(211)
plt.plot(pH, f_h3po4, "r-", label=r"$\mathregular{H_3PO_4}$")
plt.plot(pH, f_h2po4, "b-", label=r"$\mathregular{H_2PO_4^{-}}$")
plt.plot(pH, f_hpo4, "g-", label=r"$\mathregular{HPO_4^{2-}}$")
plt.plot(pH, f_po4, "y-", label=r"$\mathregular{PO_4^{3-}}$")

plt.subplot(212)
plt.plot(pHdata, f_h3po4_data, "ro", label=r"$\mathregular{H_3PO_4}$")
plt.plot(pHdata, f_h2po4_data, "bo", label=r"$\mathregular{H_2PO_4^{-}}$")
plt.plot(pHdata, f_hpo4_data, "go", label=r"$\mathregular{HPO_4^{2-}}$")
plt.plot(pHdata, f_po4_data, "yo", label=r"$\mathregular{PO_4^{3-}}$")

# labels
plt.subplot(211)
plt.ylim(0, 1)
plt.xlim(0, 14)
plt.legend(loc='best', prop={'size': 10})
plt.xlabel("pH")
plt.ylabel("Fraction of species")
plt.title("Fractional composition of phosphoric acid ions")
plt.xticks([0, 7, 14])
plt.yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])

plt.subplot(212)
plt.ylim(0, 1)
plt.xlim(0, 14)
plt.legend(loc='best', prop={'size': 10})
plt.xlabel("pH")
plt.ylabel("Fraction of species")
plt.title("Fractional composition of phosphoric acid ions")
plt.xticks([0, 7, 14])
plt.yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.text(5, .65, r'$\mathregular{H_2PO_4^{-}=0.6063}$')
plt.text(5, .35, r'$\mathregular{HPO_4^{2-}=0.3936}$')
# save plot to file
now = str(dt.datetime.today())
plt.savefig("../figs/phosfraction"+ now +".png")

# display plot on screen
plt.show()
