# @author: Wayne Yeo <fishnsotong>
# @date:   2017-08-10T23:45:53+08:00
# @email:  wayne.yeo.wei.zhong.2017@vjc.sg
# @last modified by:   fishnsotong
# @last modified time: 2017-08-11T00:03:01+08:00

# calculates

import numpy as np

Ka1 = 7.6e-3
Ka2 = 6.2e-8
Ka3 = 2.1e-13

pH = float(raw_input("Enter pH of solution at equivalence: "))
conc_hydronium = 10 ** -pH

def H_value(conc_hydronium, Ka1, Ka2, Ka3):
    H = conc_hydronium ** 3 + conc_hydronium ** 2 * Ka1 + conc_hydronium * Ka1 * Ka2 + Ka1 * Ka2 * Ka3
    return H

H = H_value(conc_hydronium, Ka1, Ka2, Ka3)

def fraction_calculator(H, Ka1, Ka2, Ka3):
    f_h3po4 = conc_hydronium ** 3 / H
    f_h2po4 = Ka1 * conc_hydronium ** 2 / H
    f_hpo4 = Ka1 * Ka2 * conc_hydronium / H
    f_po4 = Ka1 * Ka2 * Ka3 / H
    x = [f_h3po4, f_h2po4, f_hpo4, f_po4]
    return x

calculator_output = fraction_calculator(H, Ka1, Ka2, Ka3)
output = np.round(calculator_output, 4)

names = ['h3po4','h2po4','hpo4','po4']
output = np.vstack([names, output])

print "Fractional composition of phosphoric acid species: "
print output
