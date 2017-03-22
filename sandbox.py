#!/usr/bin/env python3

# Charles McEachern

# Spring 2016

# Example driver for the Charlesplotlib plotting library.

# ######################################################################

import numpy as np
import os
import random
import sys

import charlesplotlib as cpl

# ######################################################################

def main():

    return scratch()

    return contour()



# ----------------------------------------------------------------------

import matplotlib.pyplot as plt

import cubehelix


def scratch():

    fig = cpl.Figure()

    '''
    n = 21
    x, y = np.arange(n), np.arange(n)
    z = np.zeros( (n, n) )
    for i in range(n):
        for j in range(n):
            z[i, j] = random.uniform(0, 10)
    cmap = cubehelix.cmap(startHue=240,endHue=-300,minSat=1,maxSat=2.5,minLight=.3,maxLight=.8,gamma=.9)
    plt.pcolor(x, y, z, cmap=cmap)
    plt.show()
    return
    '''

    data = load_season(2)

    for name, scores in data.items():
        print(name, '\t', scores)

    cmap = cpl.helpers.seq_cmap()
    cmap = cubehelix.cmap(startHue=240,endHue=-300,minSat=1,maxSat=2.5,minLight=.3,maxLight=.8,gamma=.9)

    items = list( data.items() )

    for i, (name, scores) in enumerate(items):
        xvals = range(1, len(scores)+1)
        color = cmap( i*1./len(items) )
        fig.line(xvals, scores, color=color, label=name)

    fig.xlabel('Episode')
    fig.ylabel('Technical Rank')

    return fig.draw()




# ######################################################################

def load_season(n):
    scores = {}
    for line in cpl.helpers.read('gbbo/s' + str(n) + '.txt'):
        # Skip spacer lines. We don't need to explicitly track episodes,
        # since each baker appears exactly once in each.
        if not line:
            continue
        name, score = line.split()
        if name not in scores:
            scores[name] = []
        scores[name].append( int(score) )
    return scores









# ######################################################################

def flip(n=2):
    """Returns True one time out of n (default 2)."""
    return np.random.randint(n)==0

def lims(scalemax):
    maybe_min = np.random.randint(scalemax)
#    if flip(4):
#        maybe_min *= -1
    maybe_max = np.random.randint(scalemax)
    return sorted( [maybe_min, maybe_max] )


def zvals(n, scalemax=1000):
    scale = np.random.randint(scalemax)
    # One time in four, make it negative.
    if flip(4):
        return 2*scale*np.random.rand(n, n) - scale
    else:
        return scale*np.random.rand(n, n)



def contour():

    # Let's do four plots.

    # For each, figure out the domain. Magnitude no greater than 10.
    # Each minimum has a 1 in 4 chance of being negative (so they will
    # all four be positive decently often).

    xlims = [ lims(1000) for _ in range(4) ]
    ylims = [ lims(1000) for _ in range(4) ]

    n = 5

    pw = cpl.plotwindow(2, 2, slope=1.)

    xvals = [ np.linspace(x[0], x[1], n) for x in xlims ]
    yvals = [ np.linspace(y[0], y[1], n) for y in ylims ]

    pw[0].mesh( xvals[0], yvals[0], zvals(n) )
    pw[1].contour( xvals[1], yvals[1], zvals(n) )
    pw[2].contour( xvals[2], yvals[2], zvals(n) )
    pw[3].mesh( xvals[3], yvals[3], zvals(n) )

    clabs = ('row 0 $w^2 = \\sqrt{b}$ test', 'row 1')

    rlabs = ('$m = 1$', '$m = 4$')

    pw.style(clabs=clabs, rlabs=rlabs, title='ABCD sample title')

    if flip():
        pw.style(xlog=True)
    else:
        pw.style(ylog=True)

    if flip():
        pw.style(zlog=True)

    pw.draw()

    return








    pw = cpl.plotwindow(1, 2, slope=1.)

    n = 5

    x = np.linspace(3, 8, n)
    y = np.linspace(0, 10, n)
    scale = np.random.randint(100)
    if flip():
        z = scale*np.random.rand(n, n)
    else:
        z = 2*scale*np.random.rand(n, n) - scale
    pw[0].contour(x, y, z)

    x = np.linspace(0, 10, n+1)
    y = np.linspace(2, 7, n+1)
    scale = np.random.randint(100)
    if flip():
        z = scale*np.random.rand(n, n)
    else:
        z = 2*scale*np.random.rand(n, n) - scale
    pw[1].mesh(x, y, z)

    clabs = ('row 0 $w^2 = \\sqrt{b}$ test', 'row 1')
    pw.style(clabs=clabs, title='ABCD sample title')

    pw.draw()

    return






# ######################################################################
# #################################################### For Importability
# ######################################################################

if __name__=='__main__':
  main()
