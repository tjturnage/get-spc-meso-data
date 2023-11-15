"""
gets data
"""
from datetime import datetime,timedelta
import urllib.request
import os
import shutil
import sys
surface = [
['pmsl', 'Pressure and Wind'], ['bigsfc', 'Surface Plot'], ['ttd', 'Temp/Wind/Dwpt'],
['thet', 'MSL Press/Theta-e/Wind'], ['mcon', 'Moisture Convergence'], ['thea', 'Theta-E Advection'],
['mxth', 'Mixing Ratio / Theta'], ['icon', 'Inst Contraction Rate'], ['trap', 'Fluid Trapping'],
['vtm', 'Velocity Tensor Mag'], ['dvvr', 'Sfc Div and Vort'],
['def', 'Deformation / Axis of Dilitation'],['pchg', '2hr Press Change'],
['temp_chg', '3hr Temp Change'], ['dwpt_chg', '3hr Dewpoint Change'], 
['mixr_chg', '3hr 100mb MixR Change'], ['thte_chg', '3hr Thetae Change']]

upper_air =[['925mb', '925mb Analysis'], ['850mb2', '850mb Analysis'],
['850mb', '850mb Analysis v2'], ['700mb', '700mb Analysis'], ['500mb', '500mb Analysis'],
['300mb', '300mb Analysis'], ['dlcp', 'Deep Moist Conv'], ['tadv_925', '925mb Temp Adv'],
['tadv', '850mb Temp Adv'], ['7tad', '700mb Temp Adv'], ['sfnt', 'Surface FGEN'],
['9fnt', '925mb FGEN'], ['8fnt', '850mb FGEN'], ['7fnt', '700mb FGEN'], ['epvl', '850 fgen & EPV'],
['epvm', '700 fgen & EPV'], ['98ft', '925-850mb FGEN'], ['857f', '850-700mb FGEN'],
['75ft', '700-500mb FGEN'], ['vadv', '700-400mb Diff PVA'], ['padv', '400-250mb Pot Vort Adv'],
['ddiv', '850-250mb Diff Div'], ['ageo', '300mb Jet Circ'], ['500mb_chg', '12hr H5 chg'],
['trap_500', 'Fluid Trapping (H500)'], ['trap_250', 'Fluid Trapping (H250)']]

thermodynamics = [['sbcp', 'SBCAPE'], ['mlcp', 'MLCAPE'], ['mucp', 'MUCAPE'],
['eltm', 'EL Temp/MUCAPE/MUCIN'], ['ncap', 'CAPE - Normalized'], ['dcape', 'CAPE - Downdraft'],
['muli', 'Sfc Based LI'], ['laps', 'Mid-Level Lapse Rates'], ['lllr', 'Low-Level Lapse Rates'], 
['maxlr', 'Max 2-6 km AGL Lapse Rate'], ['lclh', 'LCL hght'], ['lfch', 'LFC hght'],
['lfrh', 'LCL-LFC RH'], ['sbcp_chg', '3-hour SBCAPE Change'], ['sbcn_chg', '3-hour SBCIN Change'],
['mlcp_chg', '3-hour MLCAPE Change'], ['mucp_chg', '3-hour MUCAPE Change'],
['lllr_chg', '3-hour Low LR Change'], ['laps_chg', '6-hour Mid LR Change'],
['skewt', 'Skew-T Maps']]

wind_shear = [['eshr', 'Bulk Shear - Effective'], ['shr6', 'Bulk Shear - Sfc-6km'],
['shr8', 'Bulk Shear - Sfc-8km'], ['shr3', 'Bulk Shear - Sfc-3km'],
['shr1', 'Bulk Shear - Sfc-1km'],['brns', 'BRN Shear'], ['effh', 'SR Helicity - Effective'],
['srh3', 'SR Helicity - Sfc-3km'], ['srh1', 'SR Helicity - Sfc-1km'],
['srh5', 'SR Helicity - Sfc-500m'], ['llsr', 'SR Wind - Sfc-2km'], ['mlsr', 'SR Wind - 4-6km'], 
['ulsr', 'SR Wind - 9-11km'], ['alsr', 'SR Wind - Anvil Level'], ['mnwd', '850-300mb Mean Wind'],
['xover', '850 and 500mb Winds'], ['srh3_chg', '3hr Sfc-3km SR Helicity Change'],
['shr1_chg', '3hr Sfc-1km Bulk Shear Change'], ['shr6_chg', '3hr Sfc-6km Bulk Shear Change'], 
['hodo', 'Hodograph Map']]

composite_indices = [['scp', 'Supercell Composite'], ['stor', 'Sig Tor (fixed)'],
['stpc', 'Sig Tor (eff)'], ['stpc5', 'Sig Tor (0-500m SRH)'], ['sigt1', 'Cond Prob SigTor 1'],
['sigt2', 'Cond Prob SigTor 2'], ['nstp', 'Non-Supercell Tor'], ['vtp3', 'Violent Tor Parm'],
['sigh', 'Significant Hail'], ['sars1', 'SARS Hail Size'], ['sars2', 'SARS Hail %age'],
['lghl', 'Large Hail Parm'], ['dcp', 'Derecho Comp'], ['cbsig', 'Craven/Brooks SigSvr'],
['brn', 'Bulk Ri Number'], ['mcsm', 'MCS Maint'], ['mbcp', 'Microburst Composite'],
['desp', 'Enh Stretch Pot'], ['ehi1', 'EHI - Sfc-1km'], ['ehi3', 'EHI - Sfc-3km'],
['vgp3', 'VGP - Sfc-3km'], ['crit', 'Critical Angle']]

multi_parameter_fields = [['mlcp_eshr', 'MLCAPE / Eff Shear'],['cpsh', 'MUCAPE / Eff Shear'],
['comp', 'MU LI / H8 & H5 Wind'], ['lcls', 'LCL Hgt / 0-1 SRH'],
['lr3c', '0-3km Lapse Rate/MLCAPE'], ['3cape_shr3', '0-3km Bulk Shear/MLCAPE'],
['3cvr', 'Sfc Vort / 0-3km MLCAPE'], ['tdlr', 'Sfc Dwpt / H7-H5 LapseR'],
['qlcs1', '0-3km ThetaE diff/Shear Vec & MUCAPE'],
['qlcs2', '', '0-3km ThetaE diff/Shear Vec & MLCAPE']]

heavy_rain = [['pwtr', 'PWAT'], ['tran_925', '925 Moist Trans'], ['tran', '850 Moist Trans'],
['tran_925-850', '925-850 Mtrans'],['prop', 'Propagation Vec'], ['peff', 'Pcpn Potential'],
['mixr', '100mb Mean Mixing Ratio']]

winter_weather = [['ptyp', 'Precipitation Type'], ['epvl', '800-750mb EPVg'],
['epvm', '650-500mb EPVg'],['les1', 'Lake Effect Snow 1'],['les2', 'Lake Effect Snow 2'],
['snsq', 'Snow Squall Parameter'],
['dend', 'Dendritic Growth Layer Depth'], ['dendrh', 'Dendritic Growth Layer RH']]

fire_weather = [ ['sfir', 'Sfc RH / T / Wind'], ['fosb', 'Fosberg Index'],
['lhan', 'Low Haines Index'],['mhan', 'Mid Haines Index'],['hhan', 'High Haines Index'],
['lasi', 'Lower Atmos Severity Index']]

classic = [['ttot', 'Total Totals'], ['show', 'Showalter Index'], ['kidx', 'K Index']]

beta = [['sherbe', 'SHERBE'], ['moshe', 'Modified SHERBE'], ['cwasp', 'CWASP'], 
['tehi', 'Tornadic 0-1 km EHI'], ['tts', 'Tornadic Tilting and Stretching parameter (TTS)'],
['ptstpe', 'Conditional probability of EF0+ tornadoes'],
['pstpe', 'Conditional probability of EF2+ tornadoes'], ['pvstpe', 'Conditional probability of EF4+ tornadoes']]



#######################################################################################################################
# Set directory in which image directories and images will be created
#--------------------------------------------------------------------
BASEDIR = "C:/data/events"
#--------------------------------------------------------------------

class GetMesoImages:
    """
    start_date_hour
            string: Date and Hour to start grabbing images -- yyyymmdd_hh
    total_hours
            int: number of hours from startingDateHour to grab images
    sector
            2 digit string (not integer) representing SPC meso sector to download
                11:NW       12:SW           13:N Plns
                14:C Plns   15:S Plns       16:NE
                17:EC       18:SE           19:National
                20:MW       21:Great Lakes
    parm_groups
            list of lists of strings. options are:
                [surface, upper_air, thermodynamics, wind_shear, composite_indices,
                multi_parameter_fields, heavy_rain, winter_weather, fire_weather, classic, beta]
    location_bool
            True: if obtaining images from a case requested of SPC
                    -https://www.spc.noaa.gov/exper/mesoanalysis/archive/
            False: if searching to see if images for a date already exist in their main directory
                    -https://www.spc.noaa.gov/exper/mesoanalysis/
    """
    def __init__(self,start_date_hour,total_hours,sector,parm_groups,location_bool):
        """
        initialize instance
        """
        self.start_date_hour = start_date_hour
        self.total_hours = total_hours
        self.sector = 's' + sector
        self.parm_groups = parm_groups
        self.location_bool = location_bool
        #self.date_hour_list = self.date_hour_list()
        self.download_and_store_images()

    def sector_name(self) -> str:
        """
        adds an "s" to sectorname
        """
        return f's{self.sector}'

    def date_hour_list(self) -> list:
        """
        Returns a list of strings representing date and hour, generated using datetime.
        The list starts from the start_date_hour specified during object initialization,
        and continues for the number of hours specified by total_hours.
        """
        date_hour_list = []
        starting_datehour = datetime.strptime(self.start_date_hour,"%Y%m%d_%H")
        ending_datehour = starting_datehour + timedelta(hours=self.total_hours)
        while starting_datehour <= ending_datehour:
            dt_str = datetime.strftime(starting_datehour,'%y%m%d%H')
            date_hour_list.append(dt_str)
            starting_datehour = starting_datehour + timedelta(hours=1)
        print(date_hour_list)
        return date_hour_list

    def url_pre(self) -> str:
        """
        set the url based on selection
        """
        if self.location_bool:
            return 'https://www.spc.noaa.gov/exper/mesoanalysis/archive/'
        return 'https://www.spc.noaa.gov/exper/mesoanalysis/'

    def full_elements_list(self) -> list:
        """
        aggregates lists of products based on category into single list
        """
        graphics_list = []
        for group in self.parm_groups:
            for element in group:
                graphics_list.append(element[0])
        return graphics_list

    def download_and_store_images(self):
        """
        download and store images
        Returns nothing
        """
        if not isinstance(self.date_hour_list(), list):
            print("date_hour_list is not a list")
            return
        for date_hour in self.date_hour_list():
            # create an image directory for each hour being downloaded
            image_dir = os.path.join(BASEDIR,date_hour)
            # copy meso graphics html browser into this new directory
            src = os.path.join(os.getcwd(),'spc_meso_graphics_viewer.html')
            try:
                if not os.path.exists(image_dir):
                    os.mkdir(image_dir)
            except ValueError:
                print(f'Can not make {image_dir}')
            for group in self.parm_groups:
                for element in group:
                    graphic = element[0]
                    source_filename = f'{graphic}_{date_hour}.gif'
                    dest_filename = f'{graphic}.gif'
                    full_url = f'{self.url_pre()}{self.sector}/{graphic}/{source_filename}'
                    print(full_url)
                    # all downloaded files will be renamed to remove date and hour to standardize names
                    destination_filepath = os.path.join(image_dir,dest_filename)
                    #print(destination_filepath)
                    try:
                        opener = urllib.request.build_opener()
                        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                        urllib.request.install_opener(opener)
                        urllib.request.urlretrieve(full_url,destination_filepath)
                    except :
                        print(f'could not download {source_filename}')
                        pass
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(full_url,destination_filepath)


# --------------------------------------------------------------------------------------
# Instantiate class
# --------------------------------------------------------------------------------------

#groups = [surface, upper_air, thermodynamics, wind_shear, composite_indices, multi_parameter_fields, heavy_rain, winter_weather, fire_weather, classic, beta]
groups = [surface, upper_air, thermodynamics, wind_shear, composite_indices, multi_parameter_fields,
heavy_rain, winter_weather]

test = GetMesoImages('20230824_21',6,'21',groups,False)
