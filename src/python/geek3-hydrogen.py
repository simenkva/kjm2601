#!/usr/bin/python3
# -*- coding: utf8 -*-

'''
hydrogen, version 1.1
draws hydrogen eigenstates as solid 3D bodies
requires: unix, gcc, python, scipy
written by Geek3 @ commons.wikimedia.org
http://commons.wikimedia.org/wiki/User:Geek3/hydrogen

Copyright (C) 2010-2018 Geek3

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation;
either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, see http://www.gnu.org/licenses/
'''


from math import *
import cmath as cm
import colorsys
import ctypes
from PIL import Image
import os
import random as rn
import scipy as sc
import numpy as np
import scipy.integrate as ig
import scipy.optimize as op
import sys



##############################################################################
# create numeric c library for speedup
c_code = """
#include <math.h>
#include <stdlib.h>

const double pi = 3.141592653589793;

static double laguerrel(const double n, const double k, const double x)
{
    int i;
    double L0, L1 = 0.0;
    double LaguerreL = 1.0;
    for (i = 0; i < n; i++)
    {
        L0 = L1;
        L1 = LaguerreL;
        LaguerreL = ((2 * i + 1 + k - x) * L1 - (i + k) * L0) / (i + 1);
    }
    return LaguerreL;
}


static double Rnl(const int n, const int l, const double r)
{
    // radial wave function
    int i;
    double rho, a;
    rho = 2.0 * r / n;
    a = 4.0;
    for (i = n - l; i <= n + l; i++)
    {
        a /= i;
    }
    a = sqrt(a);
    a /= n * n;
    
    return a * exp(-0.5 * rho) * pow(rho, l) * laguerrel(n-l-1, 2*l+1, rho);
}


static double legendrepn(const int l, int m, const double x)
{
    // renormalized associated legendre polynomials
    // = polar angle part of spherical harmonics
    int i, j;
    double fac, fac1, pn, a, b, c;
    m = abs(m);
    a = 1.0;
    if (m > 0)
    {
        fac = 1.0;
        c = (1.0 + x) * (1.0 - x);
        for (i = 1; i <= m; i++)
        {
            a *= c * fac / (fac + 1.0);
            fac += 2.0;
        }
    }
    a = sqrt((2 * m + 1) * a / (4.0 * pi));
    if (m & 1)
        a = -a;
    if (l == m)
        return a;
    else
    {
        b = a * x * sqrt(2.0 * m + 3.0);
        if (l == m + 1)
            return b;
        else
        {
            fac1 = sqrt(2.0 * m + 3.0);
            for (j = m + 2; j <= l; j++)
            {
                fac = sqrt((4.0 * j * j - 1.0) / (j * j - m * m));
                pn = fac * (b * x - a / fac1);
                fac1 = fac;
                a = b;
                b = pn;
            }
            return pn;
        }
    }
}


void Psi(const int n, const int l, const int m,
    const double x, const double y, const double z,
    double *pabs, double *pphase)
{
    double r, rxy, p0;
    // absolute value of Psi without phi dependency
    r = sqrt(x * x + y * y + z * z);
    if (r == 0.0)
        *pabs = Rnl(n, l, r) * legendrepn(l, m, 0.0);
    else
        *pabs = Rnl(n, l, r) * legendrepn(l, m, z / r);
    
    // phase of Psi
    p0 = (n + l + m + 1) * pi;
    if (*pabs < 0.0)
    {
        *pabs = -*pabs;
        p0 += pi;
    }
    if (m != 0)
    {
        rxy = sqrt(x * x + y * y);
        if (rxy != 0.0)
            p0 += m * atan2(y, x);
    }
    *pphase = fmod(p0, 2.0 * pi);
}


double Psi_sqr(const int n, const int l, const int m,
    const double x, const double y, const double z)
{
    // Probability density function
    double pabs;
    double r = sqrt(x * x + y * y + z * z);
    if (r == 0.0)
        pabs = Rnl(n, l, r) * legendrepn(l, m, 0.0);
    else
        pabs = Rnl(n, l, r) * legendrepn(l, m, z / r);
    return pabs * pabs;
}
"""

try:
    open('./libhydrogen.so', 'r')
except IOError:
    cfile = open('./hydrogen.c', 'w')
    cfile.write(c_code)
    cfile.flush()
    commands = ['gcc -O1 -fpic -c hydrogen.c',
#                'ld -G hydrogen.o -o libhydrogen.so']
                'clang hydrogen.o -o libhydrogen.dylib -dynamiclib']
#                'rm ./hydrogen.c ./hydrogen.o']
    for c in commands:
        print(c)
        os.system(c)
        
    os.system('ls -l ./libhydrogen.so')




# load the dynamic library and adjust settings
clib = ctypes.cdll.LoadLibrary('./libhydrogen.dylib')

clib.Psi.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.c_double, ctypes.c_double, ctypes.c_double]
clib.Psi_sqr.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int,
    ctypes.c_double, ctypes.c_double, ctypes.c_double]
clib.Psi_sqr.restype = ctypes.c_double
##############################################################################



# helper functions
def vnorm(x):
    d = sqrt(sum([i**2 for i in x]))
    if d != 0.: return np.array(x) / d
    return np.array(x)
def rtp_to_xyz(rtp):
    st, ct = sin(rtp[1]), cos(rtp[1])
    sp, cp = sin(rtp[2]), cos(rtp[2])
    return rtp[0] * np.array([cp * st, sp * st, ct])
def xyz_to_rtp(xyz):
    r = sqrt(xyz[0]**2 + xyz[1]**2 + xyz[2]**2)
    t = atan2(sqrt(xyz[0]**2 + xyz[1]**2), xyz[2])
    p = atan2(xyz[1], xyz[0])
    return np.array([r, t, p])
def ray_func(p, n):
    p = np.array(p)
    n = vnorm(n)
    return lambda t: p + n * t



def find_first_root(f, x0, x1):
    # surface searching algorithm
    def distribution(x):
        # how to distribute initial search values on a line
        return copysign(1. - sqrt(1. - fabs(x)), x)
    xl = [0.5*(x1+x0)+0.5*(x1-x0)*distribution(i) for i in np.linspace(-1, 1, 40)]
    
    # line search at given steps
    xyl = []
    x_positive = None
    for x in xl:
        y = f(x)
        i = len(xyl)
        xyl.append([x, y])
        if y > 0.0:
            x_positive = x
        elif i > 1:
            # surrond extrema. This section needs a cleanup
            d0 = xyl[i-1][1] - xyl[i-2][1]
            d1 = xyl[i][1] - xyl[i-1][1]
            if (d0 < 0.0 and 0.0 < d1) or (d1 < 0.0 and 0.0 < d0):
                x0 = (2.0 * xyl[i-1][0] + xyl[i-2][0]) / 3.0
                x1 = (2.0 * xyl[i-1][0] + xyl[i][0]) / 3.0
                y0 = f(x0)
                xyl.insert(i-1, [x0, y0])
                if y0 >= 0.0:
                    x_positive = x1
                else:
                    y1 = f(x1)
                    xyl.insert(i+1, [x1, y1])
                    if y1 >= 0.0:
                        x_positive = x1
                    else:
                        xnewl = []
                        for j in range(i-1, i+2):
                            d0 = xyl[j][1] - xyl[j-1][1]
                            d1 = xyl[j+1][1] - xyl[j][1]
                            if (d0 < 0.0 and 0.0 < d1) or (d1 < 0.0 and 0.0 < d0):
                                xnewl.append((2.0 * xyl[j][0] + xyl[j-1][0]) / 3.0)
                                xnewl.append((2.0 * xyl[j][0] + xyl[j+1][0]) / 3.0)
                        for xn in xnewl:
                            y = f(xn)
                            j = len(xyl)
                            while xn < xyl[j-1][0]:
                                j -= 1
                            xyl.insert(j, [xn, y])
                            if y >= 0.0:
                                x_positive = xn
                                break
        
        if x_positive is not None:
            while xyl[-1][0] > x_positive:
                del xyl[-1]
            # check last intervals
            m = 3
            for j in range(m):
                if len(xyl) > m - j:
                    x = [((j+1-k) * xyl[j-m-1][0] + (k+1) * xyl[j-m][0])
                        / (j+2.0) for k in range(j+1)]
                    x_positive = False
                    for k in range(j+1):
                        xy = [x[k], f(x[k])]
                        xyl.insert(j - m, xy)
                        if xy[1] >= 0.0:
                            x_positive = True
                            break
                    if x_positive == True: break
            break
    
    # find maxima
    i = 1
    while i < len(xyl) - 1:
        if xyl[i-1][1] < xyl[i][1] and xyl[i][1] > xyl[i+1][1]:
            # there must be a maximum, find it
            xymax = op.brent(lambda t: -f(t),
                brack=(xyl[i-1][0], xyl[i][0], xyl[i+1][0]),
                tol=1e-5*(x1-x0) / max(abs(xyl[i][0]), 1e-3*(x1-x0)), full_output=True)
            if xymax[0] < xyl[i][0]:
                xyl.insert(i, [xymax[0], -xymax[1]])
                j = i
            else:
                xyl.insert(i+1, [xymax[0], -xymax[1]])
                j = i + 1
            if xyl[j][1] >= 0.0:
                n = i - 1
                break
            i += 1
        i += 1
    
    # calculate precise root
    i = 1
    while i < len(xyl) - 1 and xyl[i][1] < 0.0:
        i += 1
    if i > 0 and xyl[i-1][1] <= 0.0 and 0.0 <= xyl[i][1]:
        return op.brentq(f, xyl[i-1][0], xyl[i][0])
    else:
        return None



def heuristic_density(n, l, m):
    # heuristic density estimation that orbitals are best visible
    if n <= 0:
        return 1.0
    if l == 0:
        # round ball
        d = 0.03 + 0.1 / n**3
    elif l == 1 and m == 0:
        # standard p-orbital
        d = (0.065 + 0.22 / n**2)
    else:
        a = l / (n - 1.0)
        b = (m / l)**2
        d = (0.04 + b * 0.1 * a**2 + (1.0-b) * (0.07 * a**5 - 0.01 * a))
        if l == n - 1 and fabs(m) == l: d *= 0.9
        if l == n - 2 and fabs(m) == l: d *= 0.8
    return d / n**6



def probability(psi_sqr, dens, R, tol=0.005e-2):
    # probability integration for volume with p-density >= dens
    # inside a sphere with radius R
    # tol: absolute error goal
    
    def rho(z0, r):
        rxy = sqrt(1.0 - z0**2)
        x = r * rxy
        z = r * z0
        d = psi_sqr((x, 0.0, z))
        if d < dens:
            return 0.0
        else:
            return d * 2.0 * pi * r**2
    # get rid of annoying integration warnings due to discontinuities
    class Dummy_write():
        def write(self, s): pass
    sys.stdout = Dummy_write()
    p = ig.dblquad(rho, 0.0, R,
        lambda t: -1.0, lambda t: 1.0, epsabs=tol)[0]
    sys.stdout = sys.__stdout__   
    return p



def phong(phase, vlight, vsurf, vview, adds=(0.33, 0.2, 0.4, 0.2), spec=15.):
    # phong shading
    # ads[0]: ambient shading 0.3
    # ads[1]: diffuse darkening on shadow side 0.15
    # ads[2]: diffuse reflection lighting on bright side 0.35
    # ads[3]: specularity 0.35
    vlight = vnorm(vlight)
    vsurf = vnorm(vsurf)
    vview = vnorm(vview)
    vreflect = vnorm(2. * np.dot(vlight, vsurf) * vsurf - vlight)
    ambient = adds[0]
    diffuse_frac = np.dot(vsurf, vlight)
    if diffuse_frac < 0.:
        diffuse = adds[1] * diffuse_frac
    else:
        diffuse = adds[2] * diffuse_frac
    specular = (adds[3]) * max(0., np.dot(vreflect, vview))**spec
    hue = phase - 1.0 / 3.0 # phase=0: blue
    lightness = max(0, min(ambient + diffuse + specular, 1))
    rgb = colorsys.hls_to_rgb(hue, lightness, 1.)
    rgb = [min(255, int(256. * i)) for i in rgb]
    return rgb



def draw_orbital(nlm, w=200, fname=None, density=None,
    camera_phi=radians(-90), camera_theta=0.9, light_phi=radians(30), light_theta=0.7,
    angle_of_view=atan(4 / 3), view_center=[0,0,0], zoom=None, time=0.0, cut=None):
    '''
    creates a pixel graphic of an orbital.
    nlm: either quantum numbers [n, l, m] or a list [[n1, l1, m1, ampl1], ...]
    cut: a function f(x, y, z), which cuts away the part of an image where f<0
    '''
    
    # shortcut for wavefunction
    if type(nlm[0]) == int:
        n, l, m = nlm
        Psi_sqr = lambda xyz: clib.Psi_sqr(n, l, m, *xyz)
        def Psi_phase(xyz):
            pabs, phase = ctypes.c_double(), ctypes.c_double()
            clib.Psi(n, l, m, xyz[0], xyz[1], xyz[2],
                ctypes.byref(pabs), ctypes.byref(phase))
            return phase.value + 2 * time * pi / n**2
    elif len(nlm[0]) == 4:
        # mix of different eigenfunctions
        # nlm = [[n1, l1, m1, amplitude1], [n2, l2, m2, amplitude2], ...]
        n, l, m = nlm[0][0:3]
        def Psi_sqr(xyz):
            psi = complex(0.0, 0.0)
            for n, l, m, a in nlm:
                pabs, phase = ctypes.c_double(), ctypes.c_double()
                clib.Psi(n, l, m, xyz[0], xyz[1], xyz[2],
                    ctypes.byref(pabs), ctypes.byref(phase))
                psi += a * pabs.value * cm.exp(1j * phase.value + 2j*time*pi/n**2)
            return psi.real**2 + psi.imag**2
        def Psi_phase(xyz):
            psi = complex(0.0, 0.0)
            for n, l, m, a in nlm:
                pabs, phase = ctypes.c_double(), ctypes.c_double()
                clib.Psi(n, l, m, xyz[0], xyz[1], xyz[2],
                    ctypes.byref(pabs), ctypes.byref(phase))
                psi += a * pabs.value * cm.exp(1j * phase.value + 2j*time*pi/n**2)
            return atan2(psi.imag, psi.real)
    
    if zoom is None:
        zoom = 1 / (1 - 3 / (n + 1)**2)
    bohr_radii_per_halfwidth = 2 * n**2 / zoom
    h = w # image size
    unit = (w / 2) / bohr_radii_per_halfwidth
    print(f"scale: {unit:.3g}px/a0")
    
    if density is not None:
        dens = density
    else:
        dens = 0.03 / n**6
    
    view_center = np.array(view_center)
    
    # camera location
    camera = view_center + rtp_to_xyz([bohr_radii_per_halfwidth *
        sqrt(1.0 + (h / w)**2) / tan(radians(angle_of_view) / 2),
        camera_theta, camera_phi])
    
    # light source
    dlight = rtp_to_xyz([1.0, light_theta, light_phi])
    vm = view_center - camera
    z0 = np.array([0, 0, 1.0])
    
    # image plane axes
    image_z = vnorm(vm)
    image_y = vnorm(z0 - np.dot(z0, image_z) * image_z)
    image_x = vnorm(np.cross(image_z, z0))
    
    # draw
    im = Image.new('RGBA', (w, h))
    for ny in range(h):
        for nx in range(w):            
            x, y = (nx - 0.5*(w-1)) / unit, (0.5*(h-1) - ny) / unit
            p2 = view_center + x * image_x + y * image_y
            rf = ray_func(p2, p2 - camera)
            
            if cut is None:
                def isosurf(t):
                    return Psi_sqr(rf(t)) - dens
            else:
                def isosurf(t):
                    p = rf(t)
                    return min(Psi_sqr(p) - dens, cut(p))
            first_root = find_first_root(isosurf,
                -bohr_radii_per_halfwidth,
                bohr_radii_per_halfwidth)
            cut_point = None
            if cut is not None:
                if (cut(rf(-bohr_radii_per_halfwidth)) < 0 and
                    cut(rf(bohr_radii_per_halfwidth)) > 0):
                    t0 = op.brentq(lambda t: cut(rf(t)),
                        -bohr_radii_per_halfwidth, bohr_radii_per_halfwidth)
                    if Psi_sqr(rf(t0)) - dens > 0:
                        # The orbital is actually cut at cut_point
                        cut_point = t0
            
            if first_root is not None or cut_point is not None:
                d = 1e-5
                if cut_point is not None and cut_point <= first_root + 1e-10:
                    ps = rf(cut_point)
                    vsurf = vnorm([(cut(ps-d*np.eye(1,3,i)[0])
                        - cut(ps+d*np.eye(1,3,i)[0])) for i in range(3)])
                else:
                    ps = rf(first_root)
                    # surface vector (gradient vector for smooth functions)
                    vsurf = vnorm([(Psi_sqr(ps-d*np.eye(1,3,i)[0])
                        - Psi_sqr(ps+d*np.eye(1,3,i)[0])) for i in range(3)])
            
                # phong shading
                rgba = phong(Psi_phase(ps) / (2*pi), dlight, vsurf, camera - ps) + [255]
            else:
                rgba = [0, 0, 0, 0] # transparent background
            im.putpixel((nx,ny), tuple(rgba))
        
        # print message
        outstr = ' row ' + str(ny+1) + ' of ' + str(h) + ' complete'
        print('\b{0}{1}'.format(outstr, '\b' * len(outstr)), end='', flush=True)
    
    if fname is None:
        fname = 'hydrogen_n' + str(n) + '_l' + str(l) + '_m' + str(m) + '.png'
    else:
        if len(fname) < 4 or fname[-4] != '.':
            fname += '.png'
    im.save(fname, optimize=1)
    print('image written to', fname)



for n in range(4,5):
  for l in range(n):
    for m in range(-l, l + 1):
      draw_orbital([n, l, m], w=256, density=heuristic_density(n,l,m),
          fname = 'hydrogen_n'+str(n)+'_l'+str(l)+'_m'+str(m)+'.png')
      #p = probability(lambda xyz: clib.Psi_sqr(n, l, m, *xyz),
      #    heuristic_density(n,l,m), n**2 * 4.0)
      #print('n{0} n{1} l{2}:'.format(n,l,m), heuristic_density(n,l,m), "; p =", p*100., "%")

### append your specific settings which orbitals to plot here ###
print("individual image description code must be inserted at the end of this program's source code!")
# example code:
#for n in range(4,5):
#  for l in range(n):
#    for m in range(-l, l + 1):
#      draw_orbital([n, l, m], w=100, density=heuristic_density(n,l,m))
#      p = probability(lambda xyz: clib.Psi_sqr(n, l, m, *xyz),
#          heuristic_density(n,l,m), n**2 * 4.0)
#      print('n{0} n{1} l{2}:'.format(n,l,m), heuristic_density(n,l,m), "; p =", p*100., "%")