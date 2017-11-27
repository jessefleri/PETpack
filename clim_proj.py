'''
Author: Jesse Fleri
Project: Climate projection comparison
Module: PETpack
Last revised: 2017-11-20
'''
import calendar
from math import cos,tan,sin,acos,pi,sqrt
import random
import numpy as np
import matplotlib.pyplot as plt


days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
leap_days = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
mdays = (15.5, 14, 15.5, 15, 15.5, 15, 15.5, 15.5, 15, 15.5, 15, 15.5)
mtemp = random.sample(xrange(0,30),12)
Rn = random.sample(xrange(-50,200),12)

np.cumsum(days)


def draft(n,seq):
    while True:
        for i in xrange(0,n,seq):
            yield i
        for i in xrange(n,0,-seq):
            yield i

d = draft(30,5)
mtemp = [d.next() for _ in xrange(12)]
noise = [np.random.normal(0, 3) for i in range(0,12)]
temp = [mtemp[i] + noise[i] for i in range(0,12)]



def daylight(year, lat):
    monthly_dl = []
    day = 1
    monthdays = leap_mdays if calendar.isleap(year) == True else mdays
    cum_days = np.cumsum(monthdays)
    for days in monthdays:
        daylight = 0.0
        for date in range(1, days + 1):
            dec = 0.409*sin(2*pi/365 * date - 1.39)
            solar_hrs = acos(-tan(lat) * tan(dec))
            daylight += 24/pi * solar_hrs
            day += 1
        monthly_dl.append(daylight/days)
    return monthly_dl

daylight(2014,60)

def ETt(mtemp, lat, year):
    if len(mtemp) != 12:
		raise ValueError(
            'mtemp should be length 12 but is length {0}.'
            .format(len(mtemp)))
    if lat >= 66.5:
		raise ValueError(
            'latitudes above 66.55 are subject to additional error, your latitude was {0}.'
            .format(lat))
        
    temp = [0 if (i/5.0) <= 0 else i for i in mtemp]     # Filter zeros and negatives  	
    mon_heat_index = [(i/5.0)**1.514 for i in temp]    # Monthly heat index      
    I = sum(mon_heat_index)									  # Annual heat index
    alpha = ((675e-9 * pow(I,3)) - (771e-7 * pow(I,2)) + (1792e-5 * I) + float(0.49239))    #constant coefficent
    PET_non = [16*pow(((10*i)/I),alpha) for i in temp]   # Calculate monthly uncorrected PET values
    dec = [23.45*(pi/180)*sin(2*pi*((284+day)/36.25)) for day in days]
    solar_hrs = -tan(lat) * tan(dec)
    N = 2*acos(solar_hrs)*(12/pi)
    PET_correct = [PET_non[i] * (N/12.0) * (day/30) for i,day in range(0,12),days]	
    return PET_correct				# PET corrected for sunlight


    dec = 23.45*(pi/180)*sin(2*pi*((284+day)/36.25))
    dec2 = .409*sin((2*pi/365) * day - 1.39)
    
    solar_hrs = -tan(lat) * tan(dec2)
    daylight_hrs = acos(min(max(solar_hrs,-1.0),1.0))
    daylight_hrs = ((solar_hrs*2)/15.0) * (180/pi)
    return daylight_hrs
    
    '''daily_hrs = solar_hrs * 2 * (24/2*pi)
    theta = -23.45 * cos((360/365) * day)
    ha = acos(cos(90.833) / (cos(lat)*cos(theta)) - tan(lat)*tan(theta))
    day_length = 2 * ha / (15 * 24)
    PET_correct = PET_non * (sum(day_length)/12) * (days/30)					# PET corrected for sunlight
    return PET_correct'''

plt.plot([.409*sin((2*pi/365) * i - 1.39) for i in range(0,364)])

plt.plot([pet(mtemp,40, i) for i in range(0,364)])


def ETpt(rad, mtemp, elev, lat):
    alpha = 1.74 if (20 <= lat <= 30) else 1.26
    lhv = 2.45
    B = 101.3*((293-0.0065*elev)/293)**5.26
    svp = [0.6108 ** ((17.27*i)/(i+237.3)) for i in mtemp]
    y = 0.00163*(B/lhv)
    pretay = [alpha*(svp[i]/svp[i]*y)*rad[i] for i in range(0,12)]
    return pretay

plt.plot([pretay(Rn,temp,i,45) for i in range(0,9000,500)])


def ETh(Ra, mtemp, year, lat):
    sha = acos(-tan(lat) * tan(dec))
    Ra = (24*60/pi)*Gsc*Dr*(sha*sin(dec)*sin(lat)+cos(lat)*cos(dec)*sin(sha))
    ETh = [0.408*(.0023*Ra*(mtemp[i]+17.8)*sqrt(mtemp)) for i in range(0,12)]
    return ETh
                     
def penmon(temp,vpd,wind,stom_cond)