############################################################################
# startDateTime: Date and time you want to start grabbing images for (yyyymmdd_hh)
# endDateTime: Date and time you want to stop grabbing images for (inclusive [yyyymmdd_hh])
# sector: SPC meso sector you wish to grab (number[string] only - see below)
#
# 11:NW
# 12:SW
# 13:N Plns
# 14:C Plns
# 15:S Plns
# 16: NE
# 17: EC
# 18: SE
# 19: National
# 20: MW
# 21: Great Lakes
# 
# parmKeys: What parameters you'd like to download imagery for. Note that using
#           the string "ALL" downloads all configured imagery. Including a comma delimited
#           list of keys corresponding to the spcDict accessed by running the following will
#           only download those select parms.
#           ./getSectorData -key        
############################################################################

surface = [
['pmsl', 'Pressure and Wind'], ['bigsfc', 'Surface Plot'], ['ttd', 'Temp/Wind/Dwpt'],
['thet', 'MSL Press/Theta-e/Wind'], ['mcon', 'Moisture Convergence'], ['thea', 'Theta-E Advection'],
['mxth', 'Mixing Ratio / Theta'], ['icon', 'Inst Contraction Rate'], ['trap', 'Fluid Trapping'],
['vtm', 'Velocity Tensor Mag'], ['dvvr', 'Sfc Div and Vort'], ['def', 'Deformation / Axis of Dilitation'],
['pchg', '2hr Press Change'], ['temp_chg', '3hr Temp Change'], ['dwpt_chg', '3hr Dewpoint Change'], 
['mixr_chg', '3hr 100mb MixR Change'], ['thte_chg', '3hr Thetae Change']]

upper_air =[['925mb', '925mb Analysis'], 
['850mb2', '850mb Analysis'], ['850mb', '850mb Analysis v2'], ['700mb', '700mb Analysis'], ['500mb', '500mb Analysis'], 
['300mb', '300mb Analysis'], ['dlcp', 'Deep Moist Conv'], ['tadv_925', '925mb Temp Adv'], ['tadv', '850mb Temp Adv'], 
['7tad', '700mb Temp Adv'], ['sfnt', 'Surface FGEN'], ['9fnt', '925mb FGEN'], ['8fnt', '850mb FGEN'], ['7fnt', '700mb FGEN'], 
['epvl', '850 fgen & EPV'], ['epvm', '700 fgen & EPV'], ['98ft', '925-850mb FGEN'], ['857f', '850-700mb FGEN'], 
['75ft', '700-500mb FGEN'], ['vadv', '700-400mb Diff PVA'], ['padv', '400-250mb Pot Vort Adv'], ['ddiv', '850-250mb Diff Div'], 
['ageo', '300mb Jet Circ'], ['500mb_chg', '12hr H5 chg'], ['trap_500', 'Fluid Trapping (H500)'], ['trap_250', 'Fluid Trapping (H250)']]

thermodynamics = [['sbcp', 'SBCAPE'], ['mlcp', 'MLCAPE'], ['mucp', 'MUCAPE'], ['eltm', 'EL Temp/MUCAPE/MUCIN'], ['ncap', 'CAPE - Normalized'], 
['dcape', 'CAPE - Downdraft'], ['muli', 'Sfc Based LI'], ['laps', 'Mid-Level Lapse Rates'], ['lllr', 'Low-Level Lapse Rates'], 
['maxlr', 'Max 2-6 km AGL Lapse Rate'], ['lclh', 'LCL hght'], ['lfch', 'LFC hght'], ['lfrh', 'LCL-LFC RH'], 
['sbcp_chg', '3-hour SBCAPE Change'], ['sbcn_chg', '3-hour SBCIN Change'], ['mlcp_chg', '3-hour MLCAPE Change'], 
['mucp_chg', '3-hour MUCAPE Change'], ['lllr_chg', '3-hour Low LR Change'], ['laps_chg', '6-hour Mid LR Change'], 
['skewt', 'Skew-T Maps']]

wind_shear = [['eshr', 'Bulk Shear - Effective'], ['shr6', 'Bulk Shear - Sfc-6km'], ['shr8', 'Bulk Shear - Sfc-8km'], ['shr3', 'Bulk Shear - Sfc-3km'], 
['shr1', 'Bulk Shear - Sfc-1km'], ['brns', 'BRN Shear'], ['effh', 'SR Helicity - Effective'], ['srh3', 'SR Helicity - Sfc-3km'], 
['srh1', 'SR Helicity - Sfc-1km'], ['srh5', 'SR Helicity - Sfc-500m'], ['llsr', 'SR Wind - Sfc-2km'], ['mlsr', 'SR Wind - 4-6km'], 
['ulsr', 'SR Wind - 9-11km'], ['alsr', 'SR Wind - Anvil Level'], ['mnwd', '850-300mb Mean Wind'], ['xover', '850 and 500mb Winds'], 
['srh3_chg', '3hr Sfc-3km SR Helicity Change'], ['shr1_chg', '3hr Sfc-1km Bulk Shear Change'], ['shr6_chg', '3hr Sfc-6km Bulk Shear Change'], 
['hodo', 'Hodograph Map']]

composite_indices = [['scp', 'Supercell Composite'], ['stor', 'Sig Tor (fixed)'], ['stpc', 'Sig Tor (eff)'], ['stpc5', 'Sig Tor (0-500m SRH)'],
['sigt1', 'Cond Prob SigTor 1'], ['sigt2', 'Cond Prob SigTor 2'], ['nstp', 'Non-Supercell Tor'], ['vtp3', 'Violent Tor Parm'],
['sigh', 'Significant Hail'], ['sars1', 'SARS Hail Size'], ['sars2', 'SARS Hail %age'], ['lghl', 'Large Hail Parm'], ['dcp', 'Derecho Comp'],
['cbsig', 'Craven/Brooks SigSvr'], ['brn', 'Bulk Ri Number'], ['mcsm', 'MCS Maint'], ['mbcp', 'Microburst Composite'], ['desp', 'Enh Stretch Pot'],
['ehi1', 'EHI - Sfc-1km'], ['ehi3', 'EHI - Sfc-3km'], ['vgp3', 'VGP - Sfc-3km'], ['crit', 'Critical Angle']]

multi_parameter_fields = [['mlcp_eshr', 'MLCAPE / Eff Shear'],['cpsh', 'MUCAPE / Eff Shear'], ['comp', 'MU LI / H8 & H5 Wind'], ['lcls', 'LCL Hgt / 0-1 SRH'],
['lr3c', '0-3km Lapse Rate/MLCAPE'], ['3cape_shr3', '0-3km Bulk Shear/MLCAPE'], ['3cvr', 'Sfc Vort / 0-3km MLCAPE'], ['tdlr', 'Sfc Dwpt / H7-H5 LapseR'],
['qlcs1', '0-3km ThetaE diff/Shear Vec & MUCAPE'], ['qlcs2', '', '0-3km ThetaE diff/Shear Vec & MLCAPE']]

heavy_rain = [['pwtr', 'PWAT'], ['tran_925', '925 Moist Trans'], ['tran', '850 Moist Trans'], ['tran_925-850', '925-850 Mtrans'],
['prop', 'Propagation Vec'], ['peff', 'Pcpn Potential'], ['mixr', '100mb Mean Mixing Ratio']]

winter_weather = [['ptyp', 'Precipitation Type'], ['epvl', '800-750mb EPVg'], ['epvm', '650-500mb EPVg'], ['les1', 'Lake Effect Snow 1'],
['les2', 'Lake Effect Snow 2'], ['snsq', 'Snow Squall Parameter'], ['dend', 'Dendritic Growth Layer Depth'], ['dendrh', 'Dendritic Growth Layer RH']]

fire_weather = [ ['sfir', 'Sfc RH / T / Wind'], ['fosb', 'Fosberg Index'], ['lhan', 'Low Haines Index'], ['mhan', 'Mid Haines Index'], ['hhan', 'High Haines Index'],
['lasi', 'Lower Atmos Severity Index']]

classic = [['ttot', 'Total Totals'], ['show', 'Showalter Index'], ['kidx', 'K Index']]

beta = [['sherbe', 'SHERBE'], ['moshe', 'Modified SHERBE'], ['cwasp', 'CWASP'], 
['tehi', 'Tornadic 0-1 km EHI'], ['tts', 'Tornadic Tilting and Stretching parameter (TTS)'], ['ptstpe', 'Conditional probability of EF0+ tornadoes'], 
['pstpe', 'Conditional probability of EF2+ tornadoes'], ['pvstpe', 'Conditional probability of EF4+ tornadoes']]

#download_groups = [surface, upper_air, thermodynamics, wind_shear, composite_indices, multi_parameter_fields, heavy_rain, winter_weather, fire_weather, classic, beta]
download_groups = [surface, upper_air, thermodynamics, wind_shear, composite_indices, multi_parameter_fields] #, heavy_rain, winter_weather, fire_weather, classic, beta]

#Example: https://www.spc.noaa.gov/exper/mesoanalysis/s16/pmsl/pmsl_22102521.gif

from datetime import datetime,timedelta
from time import strftime
import urllib.request
import os
from pathlib import PurePath

baseDir = "C:/data/events/"
spcDir = "https://www.spc.noaa.gov/exper/mesoanalysis/"

startDateTime = "20220512_16"
endDateTime = "20220513_04"
sector = "13"
parmKeys = "ALL"
class GetMesoImages:
    def __init__(self,startDateTime='20220512_16',endDateTime='20220512_16',sector='s13',parm_groups=[surface, upper_air, thermodynamics, wind_shear, composite_indices, multi_parameter_fields]):
        self.startDateTime = startDateTime
        self.endDateTime = endDateTime
        self.date_hour_list = self.make_date_hour_list()
        self.sector = sector
        self.urlpre = f'https://www.spc.noaa.gov/exper/mesoanalysis/s{self.sector}'
        self.parm_groups = parm_groups
        self.graphics_list = self.make_graphics_list()
        self.download_and_store_images()

    def make_date_hour_list(self):
        dateList = []
        starting_datetime = datetime.strptime(self.startDateTime,"%Y%m%d_%H")
        ending_datetime = datetime.strptime(self.endDateTime,"%Y%m%d_%H")
        while starting_datetime <= ending_datetime:
            dt_str = datetime.strftime(starting_datetime,'%y%m%d%H')
            dateList.append(dt_str)
            starting_datetime = starting_datetime + timedelta(hours=1)
        return dateList

    def make_graphics_list(self):
        graphics_list = []
        for g in self.parm_groups:
            for e in g:
                graphics_list.append(e)
        return graphics_list

    def download_and_store_images(self):
        for dt in self.date_hour_list:
            imagePath = PurePath(baseDir).joinpath(dt,self.sector)
            PurePath.mkdir(imagePath,exist_ok=False)
            # mkdir baseDir + dt + self.sector
            for gr in self.graphics_list:
                #Example: https://www.spc.noaa.gov/exper/mesoanalysis/s16/pmsl/pmsl_22102521.gif
                source_filename = f'{gr}_{dt}.gif'
                fullURL = f'{spcDir}{self.sector}/{gr}/{source_filename}'
                destination_filepath = PurePath(imagePath).joinpath(f'{gr}.gif')
                try:
                    opener = urllib.request.build_opener()
                    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                    urllib.request.install_opener(opener)
                    urllib.request.urlretrieve(fullURL,destination_filepath)
                except Exception as e:
                    print(f'{source_filename} plot not available')
        return


# instantiate class

test = GetMesoImages()

