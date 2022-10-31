#!/usr/bin/env python3

import getSectorConfig as sConf
from datetime import datetime, timedelta
import urllib.request
import os


# get a date range
# get a list of parameters to dl
# print a list of available
# https://www.spc.noaa.gov/exper/mesoanalysis/s18/

urlpre = "https://www.spc.noaa.gov/exper/mesoanalysis/s"+sConf.sector+"/"

spcDict = {
    # SATRAD
    # 1:{"varDir":"1kmv","filePre":"vis_","title":"Visible Satellite","ymdFmt":"%Y%m%d_%H00"},
    # 2:{"varDir":"rgnlrad","filePre":"rad_","title":"Radar","ymdFmt":"%Y%m%d_%H00"},
    # SURFACE
    3:{"varDir":"pmsl","filePre":"pmsl_","title":"MSLP and Wind","ymdFmt":"%y%m%d%H"},
    4:{"varDir":"ttd","filePre":["ttd_sf_","ttd_"],"title":"MSLP, Wind, T and Td","ymdFmt":"%y%m%d%H"},
    5:{"varDir":"thet","filePre":"thet_","title":"MSLP, Wind, Theta-E","ymdFmt":"%y%m%d%H"},
    6:{"varDir":"pchg","filePre":"pchg_","title":"2hr Sfc Pres Chg","ymdFmt":"%y%m%d%H"},
    7:{"varDir":"thte_chg","filePre":"thte_chg_","title":"3hr Theta-E Chg","ymdFmt":"%y%m%d%H"},
    # UPPER AIR
    8:{"varDir":"925mb","filePre":"925mb_","title":"925mb Analysis","ymdFmt":"%y%m%d%H"},
    9:{"varDir":"850mb","filePre":"850mb_","title":"850mb Analysis","ymdFmt":"%y%m%d%H"},
    10:{"varDir":"850mb2","filePre":"850mb2_","title":"850mb Analysis Version 2","ymdFmt":"%y%m%d%H"},
    11:{"varDir":"700mb","filePre":"700mb_","title":"700mb Analysis","ymdFmt":"%y%m%d%H"},
    12:{"varDir":"500mb","filePre":"500mb_","title":"500mb Analysis","ymdFmt":"%y%m%d%H"},
    13:{"varDir":"300mb","filePre":"300mb_","title":"300mb Analysis","ymdFmt":"%y%m%d%H"},
    14:{"varDir":"500mb_chg","filePre":"500mb_chg_","title":"12hr 500mb Height Change, Cur Height, Wind","ymdFmt":"%y%m%d%H"},
    # THERMO
    15:{"varDir":"sbcp","filePre":"sbcp_","title":"SBCAPE and SBCIN","ymdFmt":"%y%m%d%H"},
    16:{"varDir":"mlcp","filePre":"mlcp_","title":"MLCAPE and MLCIN","ymdFmt":"%y%m%d%H"},
    17:{"varDir":"mucp","filePre":"mucp_","title":"MUCAPE and Lifted Parcel Level","ymdFmt":"%y%m%d%H"},
    18:{"varDir":"dcape","filePre":"dcape_","title":"DCAPE and DCIN","ymdFmt":"%y%m%d%H"},
    19:{"varDir":"laps","filePre":"laps_","title":"700-500mb Lapse Rate","ymdFmt":"%y%m%d%H"},
    20:{"varDir":"lllr","filePre":"lllr_","title":"0-3km Lapse Rate","ymdFmt":"%y%m%d%H"},
    21:{"varDir":"lclh","filePre":"lclh_","title":"100 mb mean parcel LCL height","ymdFmt":"%y%m%d%H"},
    # WIND SHEAR
    22:{"varDir":"eshr","filePre":"eshr_","title":"Effective Bulk Shear","ymdFmt":"%y%m%d%H"},
    23:{"varDir":"shr6","filePre":"shr6_","title":"Surface to 6km Shear","ymdFmt":"%y%m%d%H"},
    24:{"varDir":"shr3","filePre":"shr3_","title":"Surface to 3km Shear","ymdFmt":"%y%m%d%H"},
    25:{"varDir":"shr1","filePre":"shr1_","title":"Surface to 1km Shear","ymdFmt":"%y%m%d%H"},
    26:{"varDir":"effh","filePre":"effh_","title":"Effective Layer SRH and Storm Motion","ymdFmt":"%y%m%d%H"},
    27:{"varDir":"srh1","filePre":"srh1_","title":"0-1km SRH and Storm Motion","ymdFmt":"%y%m%d%H"},
    28:{"varDir":"srh3","filePre":"srh3_","title":"0-3km SRH and Storm Motion","ymdFmt":"%y%m%d%H"},
    29:{"varDir":"srh5","filePre":"srh5_","title":"0-500m SRH and Storm Motion","ymdFmt":"%y%m%d%H"},
    30:{"varDir":"mnwd","filePre":"mnwd_","title":"850-300mb Mean Wind","ymdFmt":"%y%m%d%H"},
    31:{"varDir":"alsr","filePre":"alsr_","title":"Anvil Level SR Wind","ymdFmt":"%y%m%d%H"},
    32:{"varDir":"hodo","filePre":"hodo_","title":"RAP Hodographs","ymdFmt":"%y%m%d%H"},
    # Multi-Parm Fields
    33:{"varDir":"stor","filePre":"stor_","title":"Sig Tor Parm. (Fixed Layer)","ymdFmt":"%y%m%d%H"},
    34:{"varDir":"stpc","filePre":"stpc_","title":"Sig Tor Parm. (Effective Layer)","ymdFmt":"%y%m%d%H"},
    35:{"varDir":"stpc5","filePre":"stpc5_","title":"Sig Tor Parm. (0-500m Within Effective Layer)","ymdFmt":"%y%m%d%H"},
    36:{"varDir":"hail","filePre":"hail_","title":"-10 to -30 C CAPE, FZL, Shear","ymdFmt":"%y%m%d%H"},
    37:{"varDir":"qlcs1","filePre":"qlcs1_","title":"Theta-E Diff, MUCAPE, Shear","ymdFmt":"%y%m%d%H"},
    38:{"varDir":"qlcs2","filePre":"qlcs2_","title":"Theta-E Diff, MLCAPE, Shear","ymdFmt":"%y%m%d%H"},
    # Heavy Rain
    39:{"varDir":"pwtr","filePre":"pwtr_","title":"Precipitable Water","ymdFmt":"%y%m%d%H"},
    40:{"varDir":"pwtr2","filePre":"pwtr2_","title":"Precipitable Water and 850mb Transport","ymdFmt":"%y%m%d%H"},
    41:{"varDir":"tran","filePre":"tran_","title":"850mb Transport and Theta-E","ymdFmt":"%y%m%d%H"},
    42:{"varDir":"tran_925","filePre":"tran_925_","title":"925mb Transport and Theta-E","ymdFmt":"%y%m%d%H"},
    43:{"varDir":"tran_925-850","filePre":"tran_925-850_","title":"925-850mb Transport and Avg Theta-E","ymdFmt":"%y%m%d%H"},
    44:{"varDir":"prop","filePre":"prop_","title":"850mb Transport and Theta-E","ymdFmt":"%y%m%d%H"}
}

def makeDLDict():
    if type(sConf.parmKeys) is list:
        dlDict = {}
        for idx, parm in sConf.parmKeys:
            dlDict[idx] = spcDict[idx]
    else:
        dlDict = spcDict.copy()
    return dlDict

def makeDateList():
    startDateTime = datetime.strptime(sConf.startDateTime,"%Y%m%d_%H")
    endDateTime = datetime.strptime(sConf.endDateTime,"%Y%m%d_%H")
    dateList = []
    while startDateTime <= endDateTime:
        dateList.append(startDateTime)
        startDateTime = startDateTime + timedelta(hours=1)
    return dateList

def dlAndStoreImage(eachDate,val,dateDir):
    fmtdDate = eachDate.strftime(val["ymdFmt"])
    if type(val["filePre"]) is list:
        for eachPrefix in val["filePre"]:
            fileName = eachPrefix + fmtdDate + ".gif"
            fullURL = urlpre + val["varDir"] + "/" + fileName
            try:
                opener = urllib.request.build_opener()
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve(fullURL,os.path.join(dateDir,fileName))
            except Exception as e:
                print(val["title"] + " plot not available")
    else:
        fileName = val["filePre"] + fmtdDate + ".gif"
        fullURL = urlpre + val["varDir"] + "/" + val["filePre"] + fmtdDate + ".gif"
        try:
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(fullURL,os.path.join(dateDir,fileName))
        except Exception as e:
            print(val["title"] + " plot not available")
    return

dlDict = makeDLDict()
dateList = makeDateList()
for eachDate in dateList:
    dateDir = "C:/data/scripts/" + eachDate.strftime("%y%m%d%H")
    if not os.path.exists(dateDir):
        os.makedirs(dateDir)
    for key, val in dlDict.items():
        dlAndStoreImage(eachDate,val,dateDir)

