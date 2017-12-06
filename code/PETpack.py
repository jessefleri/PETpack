'''
Author: Jesse Fleri
Project: Climate projection comparison
Module: PETpack
Last revised: 2017-12-05
'''
import calendar
from math import cos,tan,sin,acos,pi,sqrt
import os
import numpy as np
import pandas as pd

mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cdays = [float(np.cumsum(mdays)[i+1])+float(mdays[i])/2 for i in range(-1,11)]
leap_mdays = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_cdays = [float(np.cumsum(leap_mdays)[i+1])+float(leap_mdays[i])/2 for i in range(-1,11)]

def draft(n,seq):
    while True:
        for i in xrange(0,n,seq):
            yield i
        for i in xrange(n,0,-seq):
            yield i

def daylight(lat, year):
    monthly_dl = []
    monthdays = leap_cdays if calendar.isleap(year) == True else cdays
    for days in monthdays:
        dec = 0.409*sin((2.0*pi/365.0) * days - 1.39)
        cos_solar_hrs = -tan((pi/180)*lat) * tan(dec)
        sol_ha = acos(min(max(cos_solar_hrs,-1.0),1.0))
        daylight = 24.0/pi * sol_ha
        monthly_dl.append(daylight)
    return monthly_dl

def ETbc(mtemp, lat, year):
    monthly_pet = []
    monthdays = leap_mdays if calendar.isleap(year) == True else mdays  
    ann_light = sum([daylight(40,2012)[i] * mdays[i+1] for i in range(0,12)])
    for i in range(0,12):
        ETbc = (daylight(lat, year)[i]*monthdays[i+1]/ann_light) * (0.46 * mtemp[i] + 8.13) * monthdays[i+1]
        monthly_pet.append(ETbc)
    return monthly_pet

def ETh(mtemp, lat, year):          ## estimated mm/month
    days = leap_cdays if calendar.isleap(year) == True else cdays
    Gsc = 0.082
    temp = [0.0 if t <= 0 else t for t in mtemp]
    for i in days:
        dr = 1 + 0.033*cos(2*pi/365*i)
        dec = 0.409*sin(2*pi/365 * i - 1.39)
        sha = -tan((pi/180)*lat) * tan(dec)
        Ra = (24*60/pi)*Gsc*dr*(sha*sin(dec)*sin(lat)+cos(lat)*cos(dec)*sin(sha))
        ETh = [abs(0.408*(0.0023*Ra*(temp[x]+17.8)*sqrt(temp[x]))) for x in range(0,12)]
        ETh = [ETh[i]*mdays[i+1] for i in range(0,12)]
    return ETh

def ETpt(mtemp, lat, elev, Rn):     ## Radiation-based method 
    alpha = 1.74 if (20 <= lat <= 30) else 1.26
    lhv = 2.45
    B = 101.3*((293-0.0065*elev)/293)**5.26
    svp = [0.6108 ** ((17.27*i)/(i+237.3)) for i in mtemp]
    y = 0.00163*(B/lhv)
    pretay = [alpha*(svp[i]/(svp[i]*y))*Rn[i] for i in range(0,12)]
    return pretay

def ETt(mtemp, lat, year):           ## estimated mm/month
    if len(mtemp) != 12:
		raise ValueError(
            'mtemp should be length 12 but is length {0}.'
            .format(len(mtemp)))
    if lat >= 66.5:
		raise ValueError(
            'latitudes above 66.55 are subject to additional error, your latitude was {0}.'
            .format(lat))
    day = leap_mdays if calendar.isleap(year) == True else mdays    
    temp = [0 if (i/5.0) <= 0 else i for i in mtemp]
    mon_heat_index = [(i/5.0)**1.514 for i in temp]     # Monthly heat index      
    I = sum(mon_heat_index)									 # Annual heat index
    alpha = ((675e-9 * pow(I,3)) - (771e-7 * pow(I,2)) + (1792e-5 * I) + float(0.49239))    #constant coefficent
    PET_non = [16*((10*i)/I)**alpha for i in temp]      # Calculate monthly uncorrected PET values
    N = daylight(lat, year)
    PET_correct = [(PET_non[i] * (N[i]/12.0) * (day[i+1]/30.0))/2 for i in range(0,12)]	
    return PET_correct

def ET(mtemp, lat, year, rn, elev):
    model_op = []
    for i in range(0,12):
        thorn = ETt(mtemp,lat,year)[i]
        bc = ETbc(mtemp,lat,year)[i]
        harg = ETh(mtemp,lat,year)[i]
        pt = ETpt(mtemp,lat,elev,rn)[i]
        model_op.append([thorn,bc,harg,pt])
    ETcomp = pd.DataFrame(model_op, columns=['thorn','bc','har','pt'], index=[range(1,13)])
    return ETcomp

def ET1(mtemp, lat, year):
    model_op = []
    for i in range(0,12):
        thorn = ETt(mtemp,lat,year)[i]
        bc = ETbc(mtemp,lat,year)[i]
        harg = ETh(mtemp,lat,year)[i]
        model_op.append([thorn,bc,harg])
    ETcomp = pd.DataFrame(model_op, columns=['thornthwait','blaney-criddle','hargreaves'], index=[range(1,13)])
    return ETcomp

def rasterarray(infile, outfile):
    filein = os.path.join(os.getcwd(), infile)
    fileout = os.path.join(os.getcwd(), outfile)
    blocksize = 512
    myRaster = arcpy.Raster(filein)
    arcpy.env.overwriteOutput = True
    arcpy.env.outputCoordinateSystem = filein
    arcpy.env.cellSize = filein
    
    filelist = []
    blockno = 0
    for x in range(0, myRaster.width, blocksize):
        for y in range(0, myRaster.height, blocksize):
    
            mx = myRaster.extent.XMin + x * myRaster.meanCellWidth
            my = myRaster.extent.YMin + y * myRaster.meanCellHeight
            lx = min([x + blocksize, myRaster.width])
            ly = min([y + blocksize, myRaster.height])
    
            myData = arcpy.RasterToNumPyArray(myRaster, arcpy.Point(mx, my),
                                              lx-x, ly-y)
    
            myData -= np.mean(myData, axis=0, keepdims=True)
    
            myRasterBlock = arcpy.NumPyArrayToRaster(myData, arcpy.Point(mx, my),
                                                     myRaster.meanCellWidth,
                                                     myRaster.meanCellHeight)
    
            filetemp = ('_%i.' % blockno).join(fileout.rsplit('.',1))
            myRasterBlock.save(filetemp)
    
            filelist.append(filetemp)
            blockno += 1
    
    arcpy.Mosaic_management(';'.join(filelist[1:]), filelist[0])
    if arcpy.Exists(fileout):
        arcpy.Delete_management(fileout)
    arcpy.Rename_management(filelist[0], fileout)
    
    for fileitem in filelist:
        if arcpy.Exists(fileitem):
            arcpy.Delete_management(fileitem)
    
    del myRasterBlock
    del myRaster