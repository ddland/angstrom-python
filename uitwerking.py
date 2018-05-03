#!analyse van de data

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as so
import TISTNplot as TN # https://github.com/HHS-TN/TIS-TN-python-code

data = {'ugly':{'fn':'ugly_data.txt', 'sep':'.', 'decimal':','},
        'easy':{'fn':'easy_data.txt', 'sep':',', 'decimal':'.'},
       }

fn = 'ugly'

data = pd.read_csv(data[fn]['fn'], sep=data[fn]['sep'],
                   decimal=data[fn]['decimal'], header=None)

#print(data.info())

data = data.rename(columns={0:'tijd',1:'intensiteit'})

#print(data.info())


###
# Wat is max, argmax, sigma
# hoe ziet een gauss er uit ?
# hoe ziet de data eruit

#plt.show()

Imax = data['intensiteit'].max()
Iargmax = data['intensiteit'].argmax()


# in idle!
#print('max: \t', Imax)
#print('argmax: \t', Iargmax)
#print('Tmax: \t', data['tijd'][Iargmax])

## Theorie
def gauss(x,a,b,c):
    return a*np.exp(-(x-b)**2/(2*c**2))

def lijn(x,a,b):
    return a+b*x

def fit(x,a,b,c,d,e):
    return gauss(x,a,b,c) + lijn(x,d,e)

# fit coefficienten met de hand
lijna = 2.5
lijnb = (data['intensiteit'][-10:].mean() - data['intensiteit'][0:10].mean())\
        / (data['tijd'][-10:].mean() - data['tijd'][0:10].mean())

gauss_sigma = 2.0

d1 = gauss(data['tijd'], Imax, data['tijd'][Iargmax], gauss_sigma)
d2 = gauss(data['tijd'], Imax, data['tijd'][Iargmax], gauss_sigma)\
     + lijn(data['tijd'], lijna, lijnb)

d3 = gauss(data['tijd'], Imax - lijn(data['tijd'][Iargmax],lijna, lijnb),
           data['tijd'][Iargmax], gauss_sigma)\
     + lijn(data['tijd'], lijna, lijnb)

# datafit met scipy
popt, pcov = so.curve_fit(fit, data['tijd'], data['intensiteit'])

def plotdata(x,y1,y2):
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.plot(x, y1, label='data')
    ax1.plot(x, y2, label='theorie')
    ax1.grid()
    ax2.plot(x,y1-y2)
    ax2.grid()
    TN.label_x('t', 's', ax2)
    TN.label_y('I', 'mV', ax1)
    TN.label_y('I', 'mV', ax2, text='residu ')
    TN.fix_axis(ax1)
    TN.fix_axis(ax2)
    
plotdata(data['tijd'], data['intensiteit'], d1)
plotdata(data['tijd'], data['intensiteit'], d2)
plotdata(data['tijd'], data['intensiteit'], d3)
plotdata(data['tijd'], data['intensiteit'], fit(data['tijd'], *popt))

print('Fit')
print('{:10s}{:>10s}{:>10s}'.format('parameter', 'hand', 'curvefit'))
print('{:10s}{:10.2f}{:10.2f}'.format('a', Imax, popt[0]))
print('{:10s}{:10.2f}{:10.2f}'.format('b', data['tijd'][Iargmax], popt[1]))
print('{:10s}{:10.2f}{:10.2f}'.format('c', gauss_sigma, popt[2]))
print('{:10s}{:10.2f}{:10.2f}'.format('d', lijna, popt[3]))
print('{:10s}{:10.4f}{:10.4f}'.format('e', lijnb, popt[4]))
plt.show()
