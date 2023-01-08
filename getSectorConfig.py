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

from datetime import datetime,timedelta
from time import strftime

startDateTime = "20220512_16"
endDateTime = "20220513_04"
sector = "13"
parmKeys = "ALL"

startDateTime = datetime.strptime(startDateTime,"%Y%m%d_%H")
endDateTime = datetime.strptime(endDateTime,"%Y%m%d_%H")
dateList = []
while startDateTime <= endDateTime:
    dt_str = datetime.strftime(startDateTime,'%y%m%d%H')
    #dateList.append(startDateTime)
    dateList.append(dt_str)
    startDateTime = startDateTime + timedelta(hours=1)

#print(dateList)

urlpre = f'https://www.spc.noaa.gov/exper/mesoanalysis/s{sector}'

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

ma_list = []
#https://www.spc.noaa.gov/exper/mesoanalysis/s16/pmsl/pmsl_22102521.gif
for g in download_groups:
    for e in g:
        ma_list.append(e)
        #for d in dateList:
            #print(f'{urlpre}/{name}/{name}_{d}.gif')

print(ma_list)

descriptions = {'trap': '<div class="spc-prod">Fluid Trapping Parameter</div><div class="spc-info">In regions of strong vorticity \
    (i.e., cyclones), air parcels tend to become trapped within the vortex.  This can produce a boundary within which air \
    parcels are trapped and so follow the vortex over extended periods. In regions with strong deformation, some air parcels are \
    brought closer together but others become increasingly separated.  The trapping parameter (TRAP) is defined according to the simple \
    formula:  TRAP = 1/4 [(DEFres)^2 - (VOR)^2]. Negative values are identified regions where the vorticity is larger than the deformation, \
    and it is within such regions that air parcels are likely to be trapped. This parameter is useful for identifying the development \
    of strong vortices and for tracking them. <div class="spc-ref">Reference: Cohen, R. A., and D. M. Schultz, 2005: Contraction rate and \
    its relationship to frontogenesis, the Lyapunov exponent, fluid trapping, and airstream boundaries, <i>Mon. Wea. Rev.</i>, \
    <b>133</b>, 1353-1369.</div>',

    'td': '<div class="spc-prod">Surface</div><div class="spc-info">Temperature (solid purple &lt; 32 F, \
    solid brown &lt; 60 F, solid red > 60 F), Dewpoint (dashed blue, values > 56F shaded), and Pressure (solid black).</div>',

    'mcon': '<div class="spc-prod">Surface Moisture Convergence (solid blue) and Mixing Ratio (solid green).</div>',

    'mxth': '<div class="spc-prod">Surface Mixing Ratio (dashed blue > 6 g/kg, values > 9 shaded), Theta (solid red in K), and Wind.</div>',

    'thea': '<div class="spc-prod">Surface Theta-e, Theta-e Advection (+ values solid purple), and Wind.</div>',

    'icon': '<div class="spc-prod">Instantaneous Contraction Rate</div><div class="spc-info">\
    SPC Documentation <b><a href="https://www.spc.noaa.gov/exper/mesoanalysis/help/help_icon.html" \
    target="_blank">HERE</a></b></div>',

    'sfnt': '<div class="spc-prod">Surface Frontogenesis (solid red), Temperature (dashed blue in deg F), Pressure (solid black), and Wind.</div>',

    'temp_chg': '<div class="spc-prod">3-Hr Temperature Change</div><div class="spc-info">Temperature Change (solid black) and Wind. Values > \
    4 C shaded red (warmer); &lt; -4 shaded blue (cooler).</div>',

    'dwpt_chg': '<div class="spc-prod">3-Hr Dewpoint Change</div><div class="spc-info">Dewpoint Change (solid black) and Wind. Values > \
    4 C shaded green (moister); &lt; -4 shaded orange/brown (drier).</div>',

    'thte_chg': '<div class="spc-prod">3-Hr Theta-e Change</div><div class="spc-info">Theta-e Change (solid black) and Wind. Values \
    > 4 shaded green (warmer and/or moister); &lt; -4 shaded blue (cooler and/or drier).</div>',


    '850mb': '<div class="spc-prod">850 mb</div><div class="spc-info"> Height (solid black), Temperature (dashed red > 0 C, dashed \
    blue &lt; 0 C), Dewpoint (solid green > 6 C), and Wind.</div>',

    '700mb': '<div class="spc-prod">700 mb</div><div class="spc-info"> Height (solid black), Temperature (dashed red > 0 C, dashed \
    blue &lt; 0 C), Wind, and 700-500 mb RH > 70 Pct (shaded).</div>',

    '500mb': '<div class="spc-prod">500 mb</div><div class="spc-info">Height (solid black), Temperature (dashed red), \
    Wind, and Isotachs (shaded > 40 kts).</div>',

    '300mb': '<div class="spc-prod">300 mb</div><div class="spc-info">Heights(solid black), Wind, Isotachs (shaded > \
    60 kts), and Divergence (solid magenta).</div>',

    'dlcp': '<div class="spc-prod">Deep Layer Moisture Flux Convergence and 100 mb Mean Mixing Ratio</div><div class="spc-info">\
    (solid red = CON; dashed blue = DIV) and 100 mb Mean Mixing Ratio (solid green > 6). High values = good moisture supply/replenishment \
    to MCS. New cell development may occur in/near max values associated with boundaries.</div>',

    'tadv_925': '<div class="spc-prod">925 mb Temperature Advection</div><div class="spc-info">Temperature Advection (red shade = \
    WAA; blue shade = CAA), Height (solid black), and Wind. 925 mb WAA = 925 mb (+) theta-e advection, if moisture is constant or \
    increasing, i.e., favorable location for convection, especially elevated convection.</div>',

    'tadv': '<div class="spc-prod">850 mb Temperature Advection</div><div class="spc-info">Temperature Advection (red shade = \
    WAA; blue shade = CAA), Height (solid black), and Wind. 850 mb WAA = 850 mb (+) theta-e advection, if moisture is constant or \
    increasing, i.e., favorable location for convection, especially elevated convection.</div>',

    '7tad': '<div class="spc-prod">700 mb Temperature Advection</div><div class="spc-info">Temperature Advection (red shade = \
    WAA; blue shade = CAA), Height (solid black), and Wind. Elevated convection may be within/near max in 700 mb WAA/700 mb (+) \
    theta-e advection.</div>',

    '7fnt': '<div class="spc-prod">700 mb Petterssen`s Frontogenesis</div><div class="spc-info">700 mb Petterssen`s Frontogenesis \
    (solid purple), Height (solid black), Temperature (dashed red), and Wind. Compare 850-700 frontogenesis axis to 700-500 axis \
    to determine depth and slope of frontogenetical surface. If they are nearly superimposed, then steep mesoscale lifting is \
    likely to promote banded precip and convection.</div>',

    'tadv_925': '<div class="spc-prod"> </div><div class="spc-info"></div>',

    '98ft': '<div class="spc-prod">925-850 mb Petterssen`s Frontogenesis</div><div class="spc-info">925-850 mb Petterssen`s \
    Frontogenesis(solid purple), Height (solid black), Temperature (dashed red), and Wind. Note that label below graphic \
    (925-700 mb) is wrong.',

    '857f': '<div class="spc-prod">850-700 mb Petterssen`s Frontogenesis (solid purple), Height (solid black), \Temperature \
    (dashed red), and Wind</div><div class="spc-info">. 850-700 mb Petterssen`s Frontogenesis (solid purple), Height (solid black), \
    Temperature (dashed red), and Wind Compare 850-700 frontogenesis axis to 700-500 axis to determine depth and slope of \
    frontogenetical surface. If they are nearly superimposed, then steep mesoscale lifting is likely to promote banded precip\
    and convection.</div>',

    '75ft': "700-500 mb Petterssen's Frontogenesis (solid purple), Height (solid black), Temperature (dashed blue), and Wind. \
    Compare 700-500 frontogenesis axis to 850-700 axis to determine depth and slope of frontogenetical surface. If they are \
    nearly superimposed, then steep mesoscale lifting is likely to promote banded precip and convection.",

    'epvl': "850 mb Frontogenesis (solid red), 850-700 mb EPV (blue shading = stable; red/green/purple shading = unstable), \
    and Conditional Instability (solid black). Look for max 850 mb frontogenesis coincident with or just downstream from (-) \
    EPV. Also consider 700 mb frontogenesis and frontal slope between the 2 levels. It is likely that (-) EPV may only appear \
    above 850 mb (even above 700 mb), especially in cool season and with a low-level frontal inversion.",

    'epvm': "700 mb Frontogensis (solid red), 650-500 mb EPV (blue shading = stable; red/green shading = unstable), and \
    Conditional Instability (solid black). Look for max 700 mb frontogenesis coincident with or just downstream from (-) EPV. \
    Also consider 850 mb frontogenesis and frontal slope between the 2 levels. Frontogenesis and (-) EPV may extend or be \
    located above 700 mb at times, especially in cool season.",

    'vadv': '<div class="spc-prod">700-400 mb Differential Vorticity Advection</div><div class="spc-info"> 700-400 mb Differential \
    Vorticity Advection (DVA) and 500 mb Height (solid black) and Vorticity (shaded). (+) DVA = solid blue. (-) DVA = dashed red. \
    (+) DVA promotes synoptic-scale (isentropic) lift, moisture and temperature advection and convergence, and destabilization.</div>',

    'padv': '<div class="spc-prod">400-250 mb Potential Vorticity Advection</div><div class="spc-info">Identifies depressions in the \
    tropopause by assessing PV in a fixed layer. Movement of these depressions induces vertical motion depending on the static stabilty \
    of the atmosphere. Positive Potential Vorticity Advection is fairly well correlated with forcing for upward vertical motion.</div>',

    'ddiv': '<div class="spc-prod">850-250mb Differential Divergence</div><div class="spc-info">Differential Divergence (fill) \
    850 mb convergence (red contours) and 250 mb divergence (purple contours). Shows larger scale mass adjustments resulting in \
    forced upward vertical motion. Large values result in rapid convective destabilization if low-level moisture is large.</div>',

    'ageo': '<div class="spc-prod">300 mb Height, Isotachs, Ageostrophic Wind, 700-500 mb Omega</div><div class="spc-info">300 \
    mb Height (solid black), Isotachs (shaded), Ageostrophic Wind, and 700-500 mb Omega. Ascent = solid magenta. Descent = dashed \
    red. Best locations for organized convection is anticyclonically-curved right entrance regions (QLCS/MCS) and exit regions of \
    mid-to-upper jet streaks (supercells).</div>',

    '500mb_chg': '<div class="spc-prod">12hr 500 mb Height Change</div><div class="spc-info">12hr 500 mb Height change \
    Shows areas where longer-term forcing for upward vertical motion has taken place, allowing for atmospheric destabilization.\
    </div>',


    'sbcp': '<div class="spc-prod">Surface-Based CAPE/CIN (J kg<sup>-1</sup>)</div><div class="spc-info">SBCAPE \
    (<u><b>S</b></u>urface-<u><b>B</b></u>ased <u><b>C</b></u>onvective<u><b>A</b></u>vailable <u><b>P</b></u>otential <u><b>E</b></u>nergy) \
    is a measure of instability in the troposphere.  This value represents the total amount of potential energy available to a parcel \
    of air originating at the surface and being lifted to its level of free convection (LFC). No parcel entrainment is considered. The CAPE and \
    CIN calculations use the virtual temperature correction. CIN (<u><b>C</b></u>onvective <u><b>IN</b></u>hibition) represents the "negative" \
    area on a sounding that must be overcome before storm initiation can occur.</div>',

    'mlcp': '<div class="spc-prod">100-mb Mixed Layer CAPE/CIN (J kg<sup>-1</sup>)</div><div class="spc-info">MLCAPE (<u><b>M</b></u>ixed \
    <u><b>L</b></u>ayer <u><b>C</b></u>onvective<u><b>A</b></u>vailable <u><b>P</b></u>otential <u><b>E</b></u>nergy) is a measure of \
    instability in the troposphere.  This value represents the mean potential energy conditions available to parcels of air located in the \
    lowest \ 100-mb when lifted to the level of free convection (LFC). No parcel entrainment is considered. The CAPE and CIN calculations \
    use the virtual temperature correction. CIN (<u><b>C</b></u>onvective <u><b>IN</b></u>hibition) represents the "negative" area on a \
    sounding that must be overcome before storm initiation can occur.</div>',

    'mucp': '<div class="spc-prod">Most Unstable CAPE (J kg<sup>-1</sup>) &amp LPL Height (m AGL)</div><div class="spc-info">MUCAPE \
    (<u><b>M</b></u>ost <u><b>U</b></u>nstable <u><b>C</b></u>onvective <u><b>A</b></u>vailable <u><b>P</b></u>otential \
    <u><b>E</b></u>nergy) is a measure of instability in the troposphere.  This value represents the total amount of potential energy \
    available to the maximum equivalent potential temperature (within the lowest 300-mb of the atmosphere) while being lifted to its \
    level of free convection (LFC). No parcel entrainment is considered. The CAPE and CIN calculations use the virtual temperature \
    correction. The LPL (<u><b>L</b></u>ifted <u><b>P</b></u>arcel <u><b>L</b></u>evel) allows for the determination of the height of \
    the most unstable parcel. This makes it easy to identify areas where the largest CAPE is "elevated."</div>',

    'eltm': '<div class="spc-prod">EL temperature, MUCAPE, and MUCIN</div><div class="spc-info">Equilibrium level (EL) temperature \
    and most-unstable (MU) parcel CAPE are utilized to identify areas of potential lightning production, while large MUCIN suggests \
    that deep convection is unlikely.  Charge separation and lightning production occur with sufficiently strong updrafts (represented \
    by MUCAPE) that extend into the mixed phase (both ice and water) region (represented by EL temperature). Thunderstorms become more \
    probable as MUCAPE increases to above 100 J kg<sup>-1</sup> with EL temperatures of -20 C or colder.</div>',

    'ncap': '<div class="spc-prod">Normalized CAPE (J kg<sup>-1</sup>)</div><div class="spc-info">The NCAPE (<u><b>N</b></u>ormalized \
    CAPE) is CAPE that is divided by the depth of the buoyancy layer (units of m s**-2).  Values near or less than .1 suggest a "tall, \
    skinny" CAPE profile with relatively weak parcel accelerations, while values closer to .3 to .4 suggest a "fat" CAPE profile with \
    large parcel accelerations possible. Normalized CAPE and lifed indicies are similar measures of instability.</div>',

    'dcape': '<div class="spc-prod">Downdraft CAPE (J kg<sup>-1</sup>)</div><div class="spc-info">The DCAPE (<u><b>D</b></u>owndraft CAPE) \
    can be used to estimate the potential strength of rain-cooled downdrafts within deep convection, and is similar to CAPE. Larger DCAPE \
    values are associated with stronger downdrafts.  Likewise, DCIN (downdraft inhibition) is analogous to convective inhibition (hatching \
    at 25 and 100 J kg<sup>-1</sup>)</div>',

    'muli': '<div class="spc-prod">Surface-Based Lifted Index (C) & Convective Inhibition (J kg-1)</div><div class="spc-info">SBLI (Surface \
    Based Lifted Index & Convective Inhibition) is the Lifted Index at 500-mb, based on the surface parcel, and the convective inhibition \
    for the same parcel. These fields are meant to identify areas of surface-based CAPE and minimal convective inhibition, which suggests \
    some threat for surface-based thunderstorms.</div>',

    'laps': '<div class="spc-prod">Mid-Level Lapse Rates (C km<sup>-1</sup>)</div><div class="spc-info">A lapse rate is the rate of temperature \
    change with height.  The faster the temperature decreases with height, the "steeper" the lapse rate and the more "unstable" the atmosphere \
    becomes. Lapse rates are shown in terms of degrees Celcius change per kilometer in height.  Values less than 5.5-6.0 C km<sup>-1</sup> \
    ("moist" adiabatic) represent "stable" conditions, while values greater than 9.8 C km<sup>-1</sup> ("dry" adiabatic) are considered \
    "absolutely unstable."  In between these two values, lapse rates are considered "conditionally unstable." Conditional instability means \
    that if enough moisture is present, lifted air parcels could have a negative LI (lifted index) or positive CAPE. The 700-500 mb lapse \
    rates, also referred to as mid-level lapse rates, are meant to identify regions where deep convection is more probable (all else being \
    equal).  Likewise, steeper lapse rates correspond to the possibility of larger CAPE and stronger storm updrafts.</div>',

    'lllr': '<div class="spc-prod">Low-Level Lapse Rates (C km<sup>-1</sup>)</div><div class="spc-info">A lapse rate is the rate of temperature \
    change with height.  The faster the temperature decreases with height, the "steeper" the lapse rate and the more "unstable" the atmosphere \
    becomes. Lapse rates are shown in terms of degrees Celcius change per kilometer in height.  Values less than 5.5-6.0 C km<sup>-1</sup>("moist" \
    adiabatic) represent "stable" conditions, while values greater than 9.8 C km<sup>-1</sup> ("dry" adiabatic) are considered "absolutely \
    unstable."  In between these two values, lapse rates are considered "conditionally unstable." Conditional instability means that if \
    enough moisture is present, lifted air parcels could have a negative LI (lifted index) or positive CAPE. The 0-3 km lapse rates, \
    also referred to as low-level lapse rates, are meant to identify regions of deeper mixing (e.g., steeper lapse rates) that often result \
    in weakening convective inhibition that precedes surface-based thunderstorm development, as well as the potential for strong downdrafts \
    in the low levels.</div>',

    'maxlr': '<div class="spc-prod">Max Lapse Rate</div><div class="spc-info">The maximum lapse rate (C km<sup>-1</sup>) in a 2 km deep \
    layer (incremented every 250 m in the vertical) from 2-6 km above ground level.</div>',

    'lclh': '<div class="spc-prod">Lifting Condensation Level (m AGL)</div><div class="spc-info">The LCL (<u><b>L</b></u>ifting \
    <u><b>C</b></u>ondensation <u><b>L</b></u>evel) is the level at which a parcel becomes saturated.  It is a reasonable estimate \
    of cloud base height when parcels experience forced ascent. The height difference between this parameter and the LFC is important \
    when determining convection initiation.  The smaller the difference between the LCL and the LFC, the more likely deep convection \
    becomes. The LFC-LCL difference is similar to CIN (convective inhibition).</div>',

    'lfch': '<div class="spc-prod">Level of Free Convection (m AGL)</div><div class="spc-info">The LFC (<u><b>L</b></u>evel of \
    <u><b>F</b></u>ree <u><b>C</b></u>onvection) is the level at which a lifted parcel begins a free acceleration upward to the \
    equilibrium level.  Recent preliminary research suggests that tornadoes become more likely in supercells when LFC heights are \
    less than 2000-m above ground level. The EL (equilibrium level) is the level at which a lifted parcel becomes cooler than the \
    environmental temperature and is no longer unstable.  The EL is used primarily to estimate the height of a thunderstorm \
    anvil. The height difference between this parameter and the LCL is important when determining convection initiation.  The smaller \
    the difference between the LFC and the LCL, the more likely deep convection becomes. The LFC-LCL difference is similar to CIN (convective \
    inhibition).</div>',

    'lfrh': '<div class="spc-prod">LCL-LFC Relative Humidity (%)</div><div class="spc-info">This is the mean relative humidity in the \
    layer between the LCL(<u><b>L</b></u>ifting <u><b>C</b></u>ondensation <u><b>L</b></u>evel)and the LFC (<u><b>L</b></u>evel of \
    <u><b>F</b></u>ree<u><b>C</b></u>onvection). Near saturation (RH=100%), from the LCL to the LFC, suggests that the LFC is near the \
    LCL.  When this occurs, a parcel experiencing forced ascent above the LCL may not be diluted with dry environmental air prior to \
    reaching the LFC. The height difference between the LCL and the LFC is important when determining convection initiation. The smaller \
    the difference between the LCL and the LFC, the more likely deep convection becomes. The LCL-LFC difference is similar to CIN \
    (convective inhibition).</div>',

    'skewt': '<div class="spc-prod">0-9 km AGL skew-T diagram </div><div class="spc-info">Display depicts the vertical profiles of \
    temperature (red) and dew point temperature (green), in the form of a standard skew-T/logP diagram for the lowest 9 km above ground \
    level. The 0 C and -20 C isotherms (dashed black and brown diagonal lines, respectively) are plotted for reference. The dashed \
    black curve denotes the "most unstable" lifted parcel trace (only when MUCAPE >= 100 J kg<sup>-1</sup>), and the shaded area \
    (light red) shows lifted parcel buoyancy.</div>',

    'ttot': '<div class="spc-prod">Total Totals</div><div class="spc-info">The equation is:\
    <br><br>TT = (T850 - T500) + (Td850 - T500) ... or equivalently ... TT=T850 + Td850 - (2 x T500)</div>',

    'kidx': '<div class="spc-prod">K Index</div><div class="spc-info">The K index is a measure of thunderstorm potential based \
    on the vertical temperature lapse rate, and the amount and vertical extent of low-level moisture in the atmosphere.\
    <br><br>K = T(850 mb) + Td(850 mb) - T(500 mb) - DD(700 mb)<br><br>\
    in degrees C, where T represents temperature, Td represents dewpoint temperature, and DD represents dewpoint depression at the indicated level.\
    K < 30 --  Thunderstorms with heavy rain or severe weather possible (see note below).<br>\
    K > 30 --  Better potential for thunderstorms with heavy rain.<br>\
    K = 40 --  Best potential for thunderstorms with very heavy rain.<br><br>\
    In general, the higher the ambient or inflow K index value, the greater the potential for heavy rain. However, beware of low (less than 30) \
    values of K. Since the K index includes the dewpoint depression (i.e., difference between the temperature and dewpoint temperature) at 700 \
    mb, dry air at this level will cause a low K value. However, given moisture below 700 mb, unstable air, and a lifting mechanism, strong or \
    severe organized thunderstorms, and even heavy rain, can still occur. Scattered diurnal convection occurring in an environment containing \
    high K (and PW) values can cause a quick burst of very heavy rain.</div>',

    'show': '<div class="spc-prod">Showalter Index</div><div class="spc-info">The Showalter Index is a long-standing, simple stability \
    index uisng the 850 mb to 500 mb lifted index. </div><div class="spc-ref"><br>Additional Information \
    <a href="https://glossary.ametsoc.org/wiki/Stability_index" target="_blank">Here</a></div>',

    'eshr': '<div class="spc-prod">Effective Bulk Wind Difference (kts)</div><div class="spc-info">The magnitude of the vector wind difference \
    from the effective inflow base upward to 50% of the equilibrium level height for the most unstable parcel in the lowest 300 mb. This parameter \
    is similar to the 0-6 km bulk wind difference, though it accounts for storm depth (effective inflow base to EL) and is designed to identify \
    both surface-based and "elevated" supercell environments. Supercells become more probable as the effective bulk wind difference increases \
    in magnitude through the range of 25-40 kt and greater.</div><div class="spc-ref"><br>Additional information \
    <a href="https://www.spc.noaa.gov/publications/thompson/effshear.pdf" target="blank">HERE</a></div>',

    'shr6': '<div class="spc-prod">SFC-6 km Vertical Shear Vector (kts)</div><div class="spc-info">The surface through 6-km above ground level shear vector \
    denotes the change in wind throughout this height.  Thunderstorms tend to become more organized and persistent as vertical shear increases. Supercells are \
    commonly associated with vertical shear values of 35-40 knots and greater through this depth.</div><div class="spc-ref">Additional information \
    <a href="https://www.spc.noaa.gov/publications/thompson/ruc-waf.pdf" target="_blank">here</a>.</div>',

    'shr8': '<div class="spc-prod">SFC-8 km Vertical Shear Vector (kts)</div><div class="spc-info">The surface through 8 km above ground level shear vector \
    denotes the change in wind throughout this height.  Thunderstorms tend to become more organized and persistent as vertical shear increases. Bunkers et al. \
    2006 found that long-lived supercells occur in environments with much stronger 0-8-km bulk wind shear ( > 50 kt) than that observed with short-lived supercells.\
    <div class="spc-ref">Reference: Bunkers, M.J., J.S. Johnson, L.J. Czepyha, J.M. Grzywacz, B.A. Klimowski and M.R. Hjelmfelt, 2006: An observational \
    examination of long-lived supercells. Part II: environmental conditions and forecasting. <i>Wea. Forecasting</i>, <b>21</b>, 689-714. </div>',

    'shr1': '<div class="spc-prod">SFC-1 km Vertical Shear Vector (kts)</div><div class="spc-info">Surface-1-km Vertical Shear is the difference \
    between the surface wind and the wind at 1-km above ground level. These data are plotted as vectors with shear magnitudes contoured.  0-1-km shear \
    magnitudes greater than 15-20 knots tend to favor supercell tornadoes.</div> \
    <div class="spc-ref">Additional information <a href="https://www.spc.noaa.gov/publications/thompson/ruc-waf.pdf" target="_blank">HERE</a>.</div>',

    'brns': '<div class="spc-prod">Bulk Richardson Number Shear (m<sup>2</sup> s<sup>-2</sup>)</div><div class="spc-info">The BRN \
    (<u><b>B</b></u>ulk <u><b>R</b></u>ichardson <u><b>N</b></u>umber)shear is similar to the BL-6-km shear, except that the BRN Shear uses a \
    difference between the low-level wind and a density-weighted mean wind through the mid-levels.  Values of 35-40 m<sup>2</sup> s<sup>-2</sup> or \
    greater have been associated with supercells.</div>',

    'effh': '<div class="spc-prod">Effective Storm Relative Helicity (m <sup>2</sup> s<sup>-2</sup>)</div><div class="spc-info">Effective SRH \
    (<u><b>S</b></u>torm <u><b>R</b></u>elative <u><b>H</b></u>elicity) is based on threshold values of lifted parcel CAPE (100 J kg<sup>-1</sup>) and \
    CIN (-250 J kg<sup>-1</sup>). These parcel constraints are meant to confine the SRH layer calculation to the part of a sounding where lifted parcels \
    are buoyant, but not too strongly capped. For example, a supercell forms or moves over an area where the most unstable parcels are located a couple of \
    thousand feet above the ground, and stable air is located at ground level. The question then becomes "how much of the cool air can the supercell ingest \
    and still survive?" Our estimate is to start with the surface parcel level ... and work upward until a lifted parcels CAPE value increases to 100 \
    Jkg<sup>-1</sup> or more ... with an associated CIN greater than -250 Jkg<sup>-1</sup>. From the first level meeting the constraints (the "effective surface")\
    ... we continue to look upward in the sounding until a lifted parcel has a CAPE less than 100 Jkg<sup>-1</sup> OR a CIN less than -250 J kg<sup>-1</sup>. \
    Of the three SRH calculations displayed on the SPC mesoanalysis page, effective SRH is the most applicable across the widest range of storm environments, and \
    effective SRH discriminates as well as 0-1 km SRH between significant tornadic and nontornadic supercells.</div>\
    <div class="spc-ref">More information is available <b><a href="https://www.spc.noaa.gov/publications/thompson/eff-srh.pdf" target="_blank">here</div>',

    'srh5': '<div class="spc-prod">0-500 m Storm Relative Helicity (m<sup>2</sup> s<sup>-2</sup>)</div><div class="spc-info">SRH (<u><b>S</b></u>torm \
    <u><b>R</b></u>elative<u><b>H</b></u>elicity) in the lowest 500 m AGL has been found by Coffer et al. (2019), October issue of <em>Weather and \
    Forecasting</em>, to be a better discriminator than effective SRH between significant tornadoes and nontornadic supercells.  This calculation \
    of 0-500 m SRH is limited to within the effective inflow layer ... as long as the inflow base is at the ground.</div>',

    'srh1': '<div class="spc-prod">Storm Relative Helicity (m<sup>2</sup> s<sup>-2</sup>)</div><div class="spc-info">SRH (<u><b>S</b></u>torm <u><b>R</b></u>elative<u><b>H</b></u>elicity) \
    is a measure of the potential for cyclonic updraft rotation in right-moving supercells, and is calculated for the lowest 1-km and 3-km layers above ground level. \
    There is no clear threshold value for SRH when forecasting supercells, since the formation of supercells appears to be related more strongly to the deeper \
    layer vertical shear.  Larger values of 0-3-km SRH (greater than 250 m<sup>2</sup> s<sup>-2</sup>) and 0-1-km SRH (greater than 100 m<sup>2</sup> s<sup>-2</sup>), \
    however, do suggest an increased threat of tornadoes with supercells. For SRH, larger values are generally better, but there are no clear thresholds between \
    non-tornadic and significant tornadic supercells.</div><div class="spc-ref">Additional information <a href="https://www.spc.noaa.gov/publications/thompson/ruc_waf.pdf" taget="_blank">HERE</a>.</div>',

    'llsr': '<div class="spc-prod">Surface-2-km Storm Relative Winds (kts)</div><div class="spc-info">Low-Level SR (<u><b>S</b></u>torm <u><b>R</b></u>elative) \
    winds (0-2-km) are meant to represent low-level storm inflow. The majority of sustained supercells have 0-2-km storm inflow values of 15-20 knots or greater.</div>',

    'mlsr': '<div class="spc-prod">4-6-km Storm Relative Winds (kts)</div><div class="spc-info">Mid-Level SR (<u><b>S</b></u>torm <u><b>R</b></u>elative) winds \
    (4-6-km) are of some use in discriminating between tornadic and non-tornadic supercells.  Tornadic supercells tend to have 4-6-km SR wind speeds in excess \
    of 15 knots, while non-tornadic supercells tend to have weaker mid-level storm-relative winds.</div><div class="spc-ref">\
    Reference: Thompson, R. L., 1998:  Eta model storm-relative winds associated with tornadic and nontornadic supercells.  <i>Wea. Forecasting,</i>, <b>13</b>, 125-137.</div>',

    'ulsr': '<div class="spc-prod">Anvil Level/9-11-km SR Winds (kts)</div><div class="spc-info">The Anvil Level SR (<u><b>S</b></u>torm <u><b>R</b></u>elative) winds and \
    SR winds from 9-11-km are meant to discriminate supercell type.  In general, upper-level SR winds less than 40 knots correspond to "high precipitation" supercells, \
    40-60 knots SR winds denote "classic" supercells, while SR winds greater than 60 knots correspond to "low precipitation" supercells.</div><div class="spc-ref">\
    Reference: Rasmussen, E. N., and J. M. Straka, 1998: Variations in supercell morphology.  Part I:  Observations of the role of upper-level storm-relative flow. \
    <em>Mon. Wea. Rev.</em>, <b>126</b>, 2406-2421.</div>',

    'mnwd': '<div class="spc-prod">850-300 mb Mean Wind</div><div class="spc-info"> (kts; solid blue > 30 kts). Steering flow. Storms moving to right of \
    mean wind may ingest better streamwise horizontal vorticity/SRH.</div>',

    'xover': '<div class="spc-prod">850mb and 500mb Wind Crossover</div><div class="spc-info">Determines the presences of deep layer directional shear, which is often \
    favorable for supercells</div>',

    'srh3_chg': '<div class="spc-prod">3hr 0-3km SRH (m<sup>2</sup> s<sup>-2</sup>) and current storm motion estimate (kt)</div><div class="spc-info">3 hour change in SRH</div>',

    'srh1_chg': '<div class="spc-prod">3hr 0-1km SRH (m<sup>2</sup> s<sup>-2</sup>) and current storm motion estimate (kt)</div><div class="spc-info">3 hour change in SRH</div>',

    'shr6_chg': '<div class="spc-prod">3hr 0-6km Bulk Shear (barbs - kt) and change (kt)</div><div class="spc-info">3 hour change in 0-6km Bulk Shear</div>',

    'hodo': '<div class="spc-prod">0-9 km AGL hodograph</div><div class="spc-info">Display depicts ground-relative hodographs from the 1-h RAP model forecast and latest \
    merged surface analysis [the hodograph connects the ends of the individual wind vectors, plotted from the origin (the small crosshair)]. \
    Color coding is as follows:  0-500 m (magenta), 500-3000 m (red), 3000-6000 m (green), and 6000-9000 m (yellow).  The dashed gray range rings \
    denote wind speeds of 20 and 40 kt. Hodographs are only plotted where MUCAPE >= 100 J kg<sup>-1</sup>. The red and blue circles represent Bunkers \
    right and left storm motion, respectively. The area within the effective inflow layer is shaded blue. The brown squares denote Bunkers mean wind \
    (pressure weighted) in the lowest 65% of storm depth (effective inflow base to 65% of MU parcel equilibrium level height). In cases where the LFC \
    is above the effective inflow layer, an orange dashed line is plotted.</div>',



    'scp': '<div class="spc-prod">Supercell Composite Parameter</div><div class="spc-info">A multiple ingredient, composite index that includes \
    effective storm-relative helicity (ESRH, based on Bunkers right supercell motion), most unstable parcel CAPE (muCAPE) and convective inhibition \
    (muCIN), and effective bulk wind difference (EBWD). Each ingredient is normalized to supercell "threshold" values, and larger values of SCP denote greater \
    "overlap" in the three supercell ingredients. Only positive values of SCP are displayed, which correspond to environments favoring right-moving (cyclonic) \
    supercells. This index is formulated as follows:<br>SCP = (muCAPE / 1000 J kg<sup>-1</sup>) * (ESRH / 50 m<sup>2</sup> s<sup>-2</sup>) * \
    (EBWD / 20 m s<sup>-1</sup>) * (-40 J kg<sup>-1</sup> / muCIN)<br><br>EBWD is divided by 20 m s<sup>-1</sup> in the range of 10-20 m s<sup>-1</sup>. EBWD \
    less than 10 m s<sup>-1</sup>is set to zero, and EBWD greater than 20 m s<sup>-1</sup> is set to one. The muCIN term is based on work by Gropp and Davenport \
    (2018), August issue of <em>Weather and Forecasting</em>, and it is set to 1.0 when muCIN is greater than -40 kg<sup>-1</sup>.</div><div class="spc-ref">Additional \
    information can be found <a href="https://www.spc.noaa.gov/publications/thompson/stp_scp.pdf" target_"blank">here</a>.</div>',

    'stor': '<div class="spc-prod">Significant Tornado Parameter (fixed layer)</div><div class="spc-info">A multiple ingredient, composite index that \
    includes 0-6 km bulk wind difference (6BWD), 0-1 km storm-relative helicity (SRH1), surface parcel CAPE (sbCAPE), and surface parcel LCL \
    height (sbLCL). This version of STP mimics the formulation presented by Thompson et al. (2012) by using fixed-layer calculations of vertical \
    shear, and substitutes the surface lifted parcels as an alternative to the ML parcels in the "effective layer" version of STP. \
    The index is formulated as follows:<br><br> STP = (sbCAPE/1500 J kg<sup>-1</sup>) * ((2000-sbLCL)/1000 m) * (SRH1/150 m<sup>2</sup> s<sup>-2</sup>) * \
    (6BWD/20 m s<sup>-1</sup>)* ((200+sbCIN)/150 J kg<sup>-1</sup>) <br><br>The sbLCL term is set to 1.0 when sbLCL < 1000 m, and set to 0.0 when sbLCL > 2000 m; \
    the sbCIN term is set to 1.0 when sbCIN > -50 J kg<sup>-1</sup>, and set to 0.0 when sbCIN < -200; the 6BWD term is capped at a value of 1.5 for 6BWD > \
    30 m s<sup>-1</sup>, and set to 0.0 when 6BWD < 12.5 m s<sup>-1</sup>.<br><br> A majority of significant tornadoes (F2 or greater damage) have been \
    associated with STP values greater than 1, while most non-tornadic supercells have been associated with values less than 1 in a large sample of RAP \
    analysis proximity soundings.</div><div class="spc-ref">Additional information can be found <a href="https://www.spc.noaa.gov/publications/thompson/waf-env.pdf" target="_blank">here</a></div>',

    'stpc': '<div class="spc-prod">Significant Tornado Parameter (effective layer)</div><div class="spc-info">A multiple ingredient, composite index that \
    includes effective bulk wind difference (EBWD), effective storm-relative helicity (ESRH), 100-mb mean parcel CAPE (mlCAPE), 100-mb mean parcel \
    CIN (mlCIN), and 100-mb mean parcel LCL height (mlLCL). The index is formulated as follows:<br><br> \
    STP = (mlCAPE/1500 J kg<sup>-1</sup>) * ((2000-mlLCL)/1000 m) * (ESRH/150 m<sup>2</sup> s<sup>-2</sup>) * (EBWD/20 m s<sup>-1</sup>) * \
    ((200+mlCIN)/150 J kg<sup>-1</sup>)<br><br>The mlLCL term is set to 1.0 when mlLCL < 1000 m, and set to 0.0 when mlLCL > 2000 m; the mlCIN term \
    is set to 1.0 when mlCIN > -50 J kg<sup>-1</sup>, and set to 0.0 when mlCIN < -200; the EBWD term is capped at a value of 1.5 for EBWD > 30 m s<sup>-1</sup>, \
    and set to 0.0 when EBWD < 12.5 m s<sup>-1</sup>.  Lastly, the entire index is set to 0.0 when the effective inflow base is above the ground. A majority of \
    significant tornadoes (F2 or greater damage) have been associated with STP values greater than 1 within an hour of tornado occurrence, while most non-tornadic \
    supercells have been associated with values less than 1 in a large sample of RAP analysis proximity soundings.<div class="spc-ref">Additional information \
    can be found <a href="https://www.spc.noaa.gov/publications/thompson/waf-env.pdf" target="_blank">here</a>.</div>',

    'stpc5': '<div class="spc-prod">Significant Tornado Parameter (uses 0-500 m SRH within effective inflow layer)</div><div class="spc-info">A multiple ingredient, \
    composite index that includes effective bulk wind difference (EBWD), effective storm-relative helicity (ESRH), 100-mb mean parcel CAPE (mlCAPE), 100-mb mean \
    parcel CIN (mlCIN), and 100-mb mean parcel LCL height (mlLCL). The index is formulated as follows:<br><br> STP = (mlCAPE/1500 J kg<sup>-1</sup>) * \
    ((2000-mlLCL)/1000 m) * (0-500 m SRH/75 m<sup>2</sup> s<sup>-2</sup>) * (EBWD/20 m s<sup>-1</sup>) * ((200+mlCIN)/150 J kg<sup>-1</sup>)<br><br> The 0-500 m SRH \
    is limited to within the effective inflow layer, if it exists.  The mlLCL term is set to 1.0 when mlLCL < 1000 m, and set to 0.0 when mlLCL > 2000 m; \
    the mlCIN term is set to 1.0 when mlCIN > -50 J kg<sup>-1</sup>, and set to 0.0 when mlCIN < -200; the EBWD term is capped at a value of 1.5 for EBWD > \
    30 m s<sup>-1</sup>, and set to 0.0 when EBWD < 12.5 m s<sup>-1</sup>.  Lastly, the entire index is set to 0.0 when the effective inflow base is above \
    the ground. A majority of significant tornadoes (F2 or greater damage) have been associated with STP values greater than 1 within an hour of tornado \
    occurrence, while most non-tornadic supercells have been associated with values less than 1 in a large sample of RAP analysis proximity soundings.  \
    Replacing effective SRH with 0-500 m SRH improves discrimination between significant tornadoes and non-tornadic supercells, per work by Coffer et al. (2019), \
    October issue of <em>Weather and Forecasting</em>.</div><div class="spc-ref">Additional information can be \
    found <a href="https://journals.ametsoc.org/view/journals/wefo/34/5/waf-d-19-0115_1.xml" target="_blank">here</a>.</div>',

    'sigt1': '<div class="spc-prod">Conditional Probability of a Significant Tornado (Eqn 1)</div><div class="spc-info">Contour analysis of conditional significant \
    (EF2+) tornado probabilities that are estimated via two forms of a linear regression equation.  The probability is conditional on the occurrence of a supercell \
    thunderstorm. The components of the significant tornado parameter (STP) make up the basis of the two regression equations, both of which use a product of the \
    0-6 km bulk wind difference and the square root of MLCAPE,and MLCIN. The primary variation between the two conditional probability equations involves the use \
    of 0-1 km SRH (equation 1) and the 0-1 km bulk wind difference (equation 2).  The conditional probabilities tend to overestimate the rate of occurrence of \
    signficant tornadoes,especially where the initial convective mode is nondiscrete, or where the mode evolves from discrete to linear. The regression equations \
    complement the STP in a probabilistic sense, and overall performance is similar to the STP.</div><div class="spc-ref">Additional information <br>\
    Togstad, W. E., J. M. Davies, S. J. Corfidi, D.R. Bright, and A. R. Dean, 2011:  Conditional probability estimation for significant tornadoes based on \
    Rapid Update Cycle (RUC) profiles.  Wea. Forecasting, 26, 729-743.</div>',

    'sigt2': '<div class="spc-prod">Conditional Probability of a Significant Tornado (Eqn 2)</div><div class="spc-info">Contour analysis of conditional significant \
    (EF2+) tornado probabilities that are estimated via two forms of a linear regression equation.  The probability is conditional on the occurrence of a supercell \
    thunderstorm. The components of the significant tornado parameter (STP) make up the basis of the two regression equations, both of which use a product of the \
    0-6 km bulk wind difference and the square root of MLCAPE,and MLCIN. The primary variation between the two conditional probability equations involves the use \
    of 0-1 km SRH (equation 1) and the 0-1 km bulk wind difference (equation 2).  The conditional probabilities tend to overestimate the rate of occurrence of \
    signficant tornadoes,especially where the initial convective mode is nondiscrete, or where the mode evolves from discrete to linear. The regression equations \
    complement the STP in a probabilistic sense, and overall performance is similar to the STP.</div><div class="spc-ref">Additional information <br>\
    Togstad, W. E., J. M. Davies, S. J. Corfidi, D.R. Bright, and A. R. Dean, 2011:  Conditional probability estimation for significant tornadoes based on \
    Rapid Update Cycle (RUC) profiles.  Wea. Forecasting, 26, 729-743.</div>',

    'nstp': '<div class="spc-prod">Non-Supercell Tornado parameter (NST)</div><div class="spc-info">The non-supercell tornado parameter (NST) is the normalized \
    product of the following terms:<br><br>(0-1 km lapse rate/9 C/km) * (0-3 km MLCAPE/100 J/kg) * ((225 - MLCIN/200) * ((18 - 0-6 km bulk wind \
    difference)/5 m/s) * (surface relative vorticity/8**10-5/s)<br><br>This normalized parameter is meant to highlight areas where steep \
    low-level lapse rates correspond with low-level instability, little convective inhibition, weak deep-layer vertical shear, and large \
    cyclonic surface vorticity.  Values > 1 suggest an enhanced potential for non-mesocyclone tornadoes.</div><div class="spc-ref">Additional Information \
    <a href="http://ams.confex.com/ams/23SLS/techprogram/paper_115294.htm" target="_blank">HERE</a></div>',

    'vtp3': '<div class="spc-prod">Violent Tornado Parameter</div><div class="spc-info">A multiple ingredient, composite index that includes \
    effective bulk wind difference (EBWD), effective storm-relative helicity (ESRH), 100-mb mean parcel CAPE (mlCAPE), 100-mb mean parcel CIN (mlCIN), \
    and 100-mb mean parcel LCL height (mlLCL), 0-3 km mean parcel CAPE and 0-3 km lapse rates. The index is formulated as follows:<br><br> \
    VTP = (mlCAPE/1500 J kg<sup>-1</sup>) * ((2000-mlLCL)/1000 m) * (ESRH/150 m<sup>2</sup> s<sup>-2</sup>) * (EBWD/20 m s<sup>-1</sup>) * \
    ((200+mlCIN)/150 J kg<sup>-1</sup>) * (0-3 km MLCAPE/50 J kg<sup>-1</sup>) * (0-3 km Lapse Rate/6.5 &#8451 km<sup>-1</sup>)<br><br>The \
    0-3 km lapse rate term is set to 2.0 when 0-3 km MLCAPE > 100 J kg<sup>-1</sup>.  Like STP, the mlLCL term is set to 1.0 when \
    mlLCL < 1000 m, and set to 0.0 when mlLCL > 2000 m; the mlCIN term is set to 1.0 when mlCIN > -50 J kg<sup>-1</sup>, and set to 0.0 when \
    mlCIN < -200; the EBWD term is capped at a value of 1.5 for EBWD > 30 m s<sup>-1</sup>, and set to 0.0 when EBWD < 12.5 m s<sup>-1</sup>. \
    Lastly, the entire index is set to 0.0 when the effective inflow base is above the ground. Research using observed soundings found that 0-3 km \
    CAPE and 0-3 km lapse rate were notable discriminators of violent tornado environments (verses weak and/or significant tornado environments). \
    These parameters were combined into the effective layer version of the Significant Tornado Parameter (STP) to create the Violent Tornado Parameter \
    (VTP).</div><div class="spc-ref">Additional information <a href="https://www.spc.noaa.gov/publications/mosier/2018-JOM1.pdf" target="_blank">HERE</a>.</div>',

    'sigh': '<div class="spc-prod">Significant Hail Parameter</div><div class="spc-info">Visit <a href="https://www.spc.noaa.gov/exper/mesoanalysis/help/help_sigh.html"\
    target="_blank">https://www.spc.noaa.gov/exper/mesoanalysis/help/help_sigh.html</a> for details.</div>',

    'sars1': '<div class="spc-prod">SARS Hail Size</div><div class="spc-info">The SARS method returns a maximum expected hail report by matching existing environmental \
    conditions to historic severe hail cases. These forecast maximum sizes are conditional on severe hail of any size occurring.<br><br>This graphic shows the \
    "best guess" maximum hail report.</div> ',

    'sars2': '<div class="spc-prod">SARS Significant Hail Percentage and Conditional Matches</div><div class="spc-info">The SARS method returns a maximum \
    expected hail report by matching existing environmental conditions to historic severe hail cases. These forecast maximum sizes are conditional on \
    severe hail of any size occurring. This graphic shows two items: First, the color fill denotes the percent of matching analog soundings that \
    had significant (2" diameter or larger) hail. Color fill starts at 50 percent. Second, the contours denote the actual number of matching cases \
    for each grid point. Percentiles for the number of matches are based on a set of about 1200 severe hail cases. For example, a grid point that has over \
    100 matches suggests a "common" severe hail environment, while a grid point with 5 matches would suggest severe hail is unlikely. A high number of matches, \
    combined with a high significant hail percentage would suggest significant hail is likely.</div>',

    'lghl': '<div class="spc-prod">Large Hail Parameter</div><div class="spc-info">A multiple ingredient, composite index that includes three thermodynamic \
    components [MUCAPE, 700-500 mb lapse rates, the depth of the hail growth zone (-10 to -30 C)], as well as three vertical shear components \
    [surface to EL bulk shear, the direction difference between the ground-relative winds at the EL and in the 3-6 km layer, and the direction difference \
    between the storm-relative winds in the 3-6 km and 0-1 km layers]. The index is formulated as follows:<br><br>If if 0-6 km BWD < 14 m s <sup>-1</sup> \
    or MUCAPE < 400 J kg<sup>-1</sup>, LHP = 0.  If both the shear and MUCAPE are >= to the above conditions (a loose supercell check): <br> LHP = (TERM A * TERM B) + \
    5 <br> TERM A = (((MUCAPE-2000)/1000) + ((3200-THK<sub>HGZ</sub>)/500) + ((LR<sub>75</sub>-6.5)/2)) where THK<sub>HGZ</sub> is the depth of the hail growth zone \
    (the -10 to -30 C layer), and LR<sub>75</sub> is the 700-500 mb temperature lapse rate. <br> TERM B = (((Shear<sub>EL</sub>-25)/5) + ((GRW<sub>dirEL</sub>+5)/20) + \
    ((SRW<sub>dirMID</sub>-80)/10)) where Shear<sub>EL</sub> is the magnitude of the vector wind difference between the surface wind and the mean wind in the 1.5 km \
    layer immediately below the EL height for the MU parcel, GRW<sub>dirEL</sub> is the directional difference between the ground-relative mean wind in the 1.5 km \
    layer below the EL and the mean wind in the 3-6 km layer AGL, and SRW<sub>dirMID</sub> is the directional difference betweem the mean storm-relative winds in the 3-6 km \
    and 0-1 km layers. <br> The LHP is meant to discriminate between significant hail (>= 2 inch diameter and smaller hail). </div><div class="spc-ref"> \
    Additional information <a href="http://www.ejssm.org/ojs/index.php/ejssm/article/view/137/101" target="_blank">HERE</a>.</div>',

    'dcp': '<div class="spc-prod">Derecho Composite Parameter (DCP)</div><div class="spc-info">This parameter is based on a data set of 113 derecho events compiled by \
    Evans and Doswell (2001).  The DCP was developed to identify environments considered favorable for cold pool "driven" wind events through four primary mechanisms: <br>\
    1) Cold pool production [DCAPE]<br>2) Ability to sustain strong storms along the leading edge of a gust front [MUCAPE]<br>3) Organization potential for any ensuing \
    convection [0-6 km shear]<br>4) Sufficient flow within the ambient environment to favor development along downstream portion of the gust front [0-6 km mean wind]. \
    This index is fomulated as follows: <br> DCP = (DCAPE/980)*(MUCAPE/2000)*(0-6 km shear/20 kt)*(0-6 km mean wind/16 kt)</div><div class="spc-ref">Reference: <br>\
    Evans, J.S., and C.A. Doswell, 2001: Examination of derecho environments using proximity soundings.  <i>Wea. Forecasting</i>, <b>16</b>, 329-342.</div>',

    'cbsig': '<div class="spc-prod">Craven SigSvr Parameter</div><div class="spc-info">The simple product of 100mb MLCAPE and 0-6km magnitude of the vector difference \
    (m/s; often referred to as "deep layer shear") accounts for the compensation between instability and shear magnitude.  Using a database of about 60,000 soundings, \
    the majority of significant severe events (2+ inch hail, 65+ knot winds, F2+ tornadoes) occur when the product exceeds 20,000 m3/s3. The index is formulated as \
    follows:<br>C = (MLCAPE J kg<sup>-1</sup>) * (SHR6 m s<sup>-1</sup>)<br>For example, a 0-6-km shear of 20 m s<sup>-1</sup> (40 knots) and CAPE of \
    3000 J kg<sup>-1</sup> results in a Craven SigSvr index of 60,000.  Units are scaled to the nearest 1000 on the web plot.</div><div class="spc-ref">Reference: <br>\
    Craven, J. P., and H. E. Brooks, 2004:  Baseline climatology of sounding derived parameters associated with deeep moist convection.  <em> Natl. Wea. Digest</em>, <b>28</b>, 13-24.</div>',

    'brn': '<div class="spc-prod">Bulk Richardson Number</div><div class="spc-info">The bulk Richardson number (BRN) is a ratio of buoyancy to vertical shear: \
    BRN = (MLCAPE) / 0.5 * (U)**2 where U = the wind speed difference between the density weighted 0-6 km mean wind and the lowest 500 m mean wind. The BRN is meant to \
    estimate the balance between vertical shear and buoyancy, with low BRN values suggestive of vertical shear that is too strong relative to the buoyancy, and large BRN \
    values are suggestive of multicell clusters. Intermediate BRN values favor sustained supercells. BRN values in the range of 10-45 (dimesionless) have been associated \
    with supercells via numerical simulations.  Close proximity soundings reveal supercell environments with larger CAPE and larger resultant BRN values (in the range of \
    50-100) than suggested by the original modeling work of Weisman and Klemp (1982).</div><div class="spc-ref">References:<br> Weisman, M. L., and J. B. Klemp, 1982: \
    The dependence of numerically simulated convective storms on vertical wind shear and buoyancy.  Mon. Wea. Rev., 110, 504-520. <br>Thompson, R. L., R. Edwards, \
    J. A. Hart, K. L. Elmore, and P. Markowski, 2003:  Close proximity soundings within supercell environments obtained from the Rapid Updage Cycle.  Wea. Forecasting, \
    18, 1243-1261.<br>Additional information <a href="https://www.spc.noaa.gov/publications/thompson/ruc_waf.pdf" target="_blank">HERE</a>.</div>',

    'mcsm': '<div class="spc-prod">Probability of MCS maintenance</div><div class="spc-info">348 warm-season MCS proximity soundings from a variety of MCS types were \
    used to develop this parameter.  Though hypothesis testing and discriminant analysis on hundreds of sounding parameters, the following four parameters were selected \
    to develop the probabilities: <br>1) maximum bulk shear (m/s) in the 0-1 and 6-10 km layer<br>2) 3-8 km lapse rate (degrees C/km)<br>3) most unstable CAPE<br>4) \
    3-12 km mean wind speed (m/s)</div><div class="spc-ref">Reference: <br> Coniglio, M.C., and S.F. Corfidi, 2006: Forecasting the speed and longevity of <br>\
    severe mesoscale convective systems. Preprints, Severe Local Storms Symposium, Amer. Meteor. Soc., Atlanta, GA, CD-ROM.</div>',

    'mbcp': '<div class="spc-prod">Microburst Composite</div><div class="spc-info">The Microburst Composite is a weighted sum of the following individual parameters: \
    SBCAPE, SBLI, lapse rates, vertical totals (850-500 mb temperature difference), DCAPE, and precipitable water. The specific terms and weights are listed below: <br>\
    SBCAPE term -> < 3100 set to 0; 3100-3999 set to 1; >= 4000 set to 2; \
    SBLI term -> > -8 set to 0; <= -8 set to 1; <= -9 set to 2; <= -10 set to 3; \
    0-3 km lapse rate term -> <= 8.4 set to 0; > 8.4 set to 1; vertical totals term -> < 27 set to \
    0; >= 27 set to 1; >= 28 set to 2; >= 29 set to 3; DCAPE term -> < 900 set to 0; >= 900 set to 1; >= 1100 set to 2; >= 1300 set to 3; \
    precipitable water term -> <= 1.5 set to -5; > 1.5 set to 0.<br>\
    All six of the terms are summed to arrive at the final microburst composite value.<br>\
    3-4 = "slight chance" of a microburst<br>\
    5-8 infers a "chance" of a microburst<br>\
    >= 9 infers that microbursts are "likely".<br>These values are conditional upon the existence of a storm. </div>',

    'desp': '<div class="spc-prod">Enhanced Stretching Potential</div><div class="spc-info">This non-dimensional composite parameter based on work by Jon Davies that identifies \
    areas where low-level buoyancy and steep low-level lapse rates are co-located, which may favor low-level vortex stretching and tornado potential.  ESP is formulated as \
    follows: <br><br> ESP = (0-3 km MLCAPE / 50 J kg<sup>-1</sup>) * ((0-3 km lapse rate - 7.0) / 1.0 C km<sup>-1</sup>) <br><br> where ESP is set to zero when the 0-3 km lapse rate \
    is < 7 C km<sup>-1</sup>, or when total MLCAPE < 250 J kg<sup>-1</sup>.</div><div class="spc-ref">Additional information <a href="http://nwafiles.nwas.org/ej/pdf/2005-EJ4.pdf" \
    target="_blank">HERE</a>.</div>',

    'ehi1': '<div class="spc-prod">Energy-Helicity Index (Sfc-1 km)</div><div class="spc-info">The basic premise behind the EHI (<u><b>E</b></u>nergy-<u><b>H</b></u>elicity \
    <u><b>I</b></u>ndex) is that storm rotation should be maximized when CAPE is large and SRH is large.  0-1-km EHI values greater than 1-2 have been associated with \
    significant tornadoes in supercells.</div><div class="spc-ref">References:<br> Rasmussen, E. N., 2003: Refined supercell and tornado forecast parameters. \
    <i>Wea. Forecasting,</i>, <b>18</b>, 530-535. <br><br> Thompson, R. L., R. Edwards, J. A. Hart, K. L. Elmore, and P. Markowski, 2003:  Close proximity soundings \
    within supercell environments obtained from the Rapid Updage Cycle.  <i>Wea. Forecasting,</i> <b>18</b>, 1243-1261.<br>Additional information \
    <a href="https://www.spc.noaa.gov/publications/thompson/ruc_waf.pdf" target="_blank">HERE</a></div>',

    'ehi3': '<div class="spc-prod">EHI3</div>Energy-Helicity Index (Sfc - 3km)</div><div class="spc-info">The basic premise behind the EHI \
    (<u><b>E</b></u>nergy-<u><b>H</b></u>elicity <u><b>I</b></u>ndex) is that storm rotation should be maximized when CAPE is large and SRH is large. \
    0-3-km EHI values greater than 1-2 have been associated with significant tornadoes in supercells.</div>',

    'vgp3': '<div class="spc-prod">Vorticity Generation Parameter (m s<sup>-2</sup>)</div><div class="spc-info">The VGP (<u><b>V</b></u>orticity <u><b>G</b></u>eneration \
    <u><b>P</b></u>arameter) is meant to estimate the rate of tilting and stretching of horizontal vorticity by a thunderstorm updraft.  Values greater than \
    0.2 m s<sup>-2</sup> suggest an increasing possibility of tornadic storms.</div><div class="spc-ref"> \
    Reference:<br> Rasmussen, E. N., and D. O. Blanchard, 1998: A baseline climatology of sounding-derived supercell and tornado forecast parameters. \
    <em>Wea. Forecasting.</em>, <b>13</b>, 1148-1164.</div>',

    'crit': '<div class="spc-prod">Critical Angle</div><div class="spc-info">The "critical angle" is the angle between the storm-relative wind at the surface and the 0-500 m \
    AGL shear vector [(kt) displayed only for areas where the effective inflow base is the ground (SBCAPE 100 J kg<sup>-1</sup> or greater, and less than 250 J kg<sup>-1</sup> \
    CIN]. A critical angle near 90 degrees infers streamwise vorticity near the ground, which favors stronger cyclonic rotation and dynamically forced ascent closer to the ground in a \
    right-moving supercell (through the effects of tilting and stretching of horizontal vorticity).  Critical angles in the range of 45 to 135 degrees suggest near-surface \
    vorticity is more streamwise than crosswise, and values in this range are highlighted by the color fill.  Large SRH colocated with a critical angle close to 90 degrees is \
    most favorable for tornadic supercells.</div><div class="spc-ref">Additional information \
    <a href="http://www.ejssm.org/ojs/index.php/ejssm/article/view/33/38" target="_blank">HERE</a>.</div>',


    'sherbe': '<div class="spc-prod">SHERBE></div><div class="spc-info">The SHERBE is a normalized composite parameter intended to identify the potential for significant \
    damaging winds and tornadoes in low CAPE, high shear environments typical of the southeast U.S. cool season.\
    <br><br>SHERBE = (LR<sub>0-3</sub>/5.2) * (LR<sub>75</sub>/5.6) * (EBWD/27)<br><br> \
    where the lapse rate (LR) terms apply to the 0-3 km and 700-500 mb layers (C km<sup>-1</sup>), respectively, and the EBWD is the effective bulk wind \
    difference (m s<sup>-1</sup>). This formulation of SHERBE inherently accounts for at least weak buoyancy by utilizing the EBWD (which requires an effective \
    inflow layer), which tends to reduce false alarms compared to the original version of SHERB using the fixed-layer 0-3 km shear.  Still, the parameter can \
    suggest an over-estimate of the severe weather threat in areas of relatively steep 0-3 km lapse rates which overlap with the 700-500 mb layer in the vertical. \
    </div><div class="spc-ref"><br>Additional information <a href="http://journals.ametsoc.org/doi/pdf/10.1175/WAF-D-13-00041.1" target="_blank">here</a>.</div>',

    'moshe': '<div class="spc-prod">Modified SHERBE</div><div class="spc-info">The Modified SHERBE is a composite parameter designed to highlight "low CAPE/high shear" \
    environments capable of producing significant severe storms.  MOSHE is formulated as follows:\
    <br><br>MOSHE = ((0-3 km lapse rate - 4 K km<sup>-1</sup>)<sup>2</sup> / 4 K<sup>2</sup> km<sup>-2</sup>) * ((0-1.5 km bulk shear - 8.0 m s<sup>-1</sup>) / \
    10 m s<sup>-1</sup>) * ((effective bulk shear - 8 m s<sup>-1</sup>) / 10 m s<sup>-1</sup>) * (MAXTEVV + 10 K Pa km <sup>-1</sup> s<sup>-1</sup>) / 9 K Pa km<sup>-1</sup> \
    s<sup>-1</sup>)<br><br>\
    where MAXTEVV is the maximum product of theta-e decrease with height and upward motion at the top of each 2 km deep layer from the surface to 6 km, incremented every \
    0.5 km. This composite parameter indirectly includes some influence of buoyancy through the effective bulk shear term, which requires at least 100 J kg<sup>-1</sup> of \
    CAPE and no more than 250 J kg<sup>-1</sup> of CIN.  Overall, MOSHE represents and improvement to the original SHERB parameters developed by Sherburn et al. (2014), \
    primarily through reduction in false alarm area.  Please note that this parameter formulation is very sensitive to the magnitude of vertical velocity, and may not \
    translate well between differing modeling systems (e.g., the RAP model versus a convection-allowing model).</div><div class="spc-ref"><br>\
    Additional information can be found <a href="http://journals.ametsoc.org/doi/pdf/10.1175/WAF-D-16-0086.1" target="_blank">here</a>.</div>',

    'cwasp': '<div class="spc-prod">Craven-Wiedenfeld Aggregate Severe Parameter</div><div class="spc-info">This aggregate parameter is the sum of 33 individual weighted \
    parameters, ranging from mandatory pressure level winds, temperature and moisture, to CAPE and vertical shear. Typical ranges of values were established for \
    each parameter in association with significant tornado (EF2+) events, and a numerical weight of 0-3 was assigned to each parameter. If all parameters are \
    consistent with historical EF2+ tornado events, the CWASP total will reach a maximum value of 99.  The majority of EF2+ tornadoes have occurred with CWASP values \
    above about 70.</div><div class="spc-ref"><br>Additional information \
    <a href="//www.nws.noaa.gov/cgi-bin/nwsexit.pl?url=//ftp.nwas.org/meetings/nwa2012/extendedabstracts/NWA2012_D8.2_Craven_Wiedenfeld.pdf" target="_blank">here</a>.</div>',

    'tts': '<div class="spc-prod">Tornadic Tilting and Stretching parameter (TTS)</div><div class="spc-info">TTS is a parameter developed by Jon Davies that \
    focuses on storm-relative helicity in the lowest 1 km (SRH1) and 100 mb mixed-layer CAPE in the lowest 3 km above ground level (mlCAPE3). The presence of \
    both ingredients suggests potential for increased low-level tilting and stretching of horizontal, streamwise vorticity within updrafts, which may increase the \
    potential for tornadic supercells. Enhancements are added based on total CAPE and deep-layer shear that strengthen updrafts; LCL height and CIN are used as \
    limiting factors when they are too high or large, respectively. In preliminary testing, values approaching 2 and greater suggest potential for tornadic \
    supercells. This experimental parameter is intended to help diagnose environments supporting tornadoes where total CAPE is relatively small, such as during \
    the cool season. This non-dimensional parameter is formulated as follows:<br><br>\
    TTS = ((SRH1 * mlCAPE3)/6500) * ((mlCAPE/2000 J kg -1)) * (6BWD/20 m s-1)<br><br>\
    In the first term, mlCAPE3 is capped at 150 J kg-1; the mlCAPE term is set to 1.0 if total mlCAPE < 2000 J kg-1 and is capped at 1.5 for mlCAPE > 3000 J \
    kg -1; the 6BWD term is capped at 1.5 for 6BWD > 30 m s-1 and set to zero when 6BWD < 12.5 m s-1 (similar to STP); if mlLCL > 1700 m AGL, or mlCIN < -100 J kg-1, \
    or sbCIN < -200 J kg-1, or TTS < 0, TTS is set to zero.</div>',

    'tehi': '<div class="spc-prod">Tornadic 0-1 km EHI</div><div class="spc-info">This updated version of the 0-1 km EHI adds 0-3 km mlCAPE and 0-6 km bulk wind difference as \
    enhancing factors, and LCL/CIN as limiting factors. Because EHI values are often deceptively large over wide areas when other factors suggest reduced \
    potential for tornadic supercells (such as weak 0-6 km bulk wind difference, high LCL heights, or large nighttime CIN), this modified version of EHI \
    should consolidate areas supporting tornadic supercells (values of 1-2 or greater). The inclusion of 0-3 km mlCAPE also helps identify areas with greater \
    potential for low-level stretching, even if total mlCAPE is relatively small. This non-dimensional parameter (updated by Jon Davies) is formulated as follows:\
    <br><br>TEHI = ((SRH1 * mlCAPE)/160,000) * ((mlCAPE3/200 J kg -1)) * (6BWD/20 m s-1)<br><br>\
    The mlCAPE3 term is set to 1.0 if total mlCAPE > 1500 J kg-1, and is capped at 1.5 for mlCAPE3 > 300 J kg -1; the 6BWD term is capped at 1.5 for 6BWD > \
    30 m s-1 and set to zero when 6BWD < 12.5 m s-1 (similar to STP); if mlLCL > 1700 m AGL, or mlCIN < -100 J kg-1, or sbCIN < -200 J kg-1, or TEHI < 0, TEHI is set to zero.</div>',

    'ptstpe': '<div class="spc-prod">Conditional probability of EF0+ tornadoes</div><div class="spc-info">The conditional probability of EF0+ tornadoes \
    given a right-moving supercell, based on the grid-point value of effective-layer STP. The probabilities are derived from a mutually exclusive \
    2014-2015 sample of right-moving supercells that produced tornadoes, large hail, and damaging winds. The probabilities are plotted as grid point \
    values (rounded integer %), with color coding related to the climatology of the sample. For example, brown denotes values lower than the sample \
    climatology, and yellow is near climatological EF4+ frequency. Red, magenta, and dark purple values are all increasingly larger than the \
    climatological EF4+ frequency. The source data for the EF4+ tornado probabilities is shown by the red curve shown in \
    <a href="https://www.spc.noaa.gov/publications/smith/fig18_stp_probs_14-15only_ef0+_ef2+_ef4+_adjusted.png" target="_blank">this plot</a>. <br>\
    </div><div class="spc-ref">see <a href="https://www.spc.noaa.gov/publications/smith/vrot-env.pdf" target="_blank">this paper</a> for additional details.</div>',

    'pstpe': '<div class="spc-prod">Conditional probability of EF2+ tornadoes</div><div class="spc-info">The conditional probability of EF2+ tornadoes \
    given a right-moving supercell, based on the grid-point value of effective-layer STP. The probabilities are derived from a mutually exclusive \
    2014-2015 sample of right-moving supercells that produced tornadoes, large hail, and damaging winds. The probabilities are plotted as grid point \
    values (rounded integer %), with color coding related to the climatology of the sample. For example, brown denotes values lower than the sample \
    climatology, and yellow is near climatological EF4+ frequency. Red, magenta, and dark purple values are all increasingly larger than the \
    climatological EF4+ frequency. The source data for the EF4+ tornado probabilities is shown by the red curve shown in \
    <a href="https://www.spc.noaa.gov/publications/smith/fig18_stp_probs_14-15only_ef0+_ef2+_ef4+_adjusted.png" target="_blank">this plot</a>. \
    </div><div class="spc-ref">Please see <a href="https://www.spc.noaa.gov/publications/smith/vrot-env.pdf" target="_blank">this paper</a> \
    for additional details.</div>',

    'pvstpe': '<div class="spc-prod">Conditional probability of EF4+ tornadoes</div><div class="spc-info">The conditional probability of EF4+ tornadoes \
    given a right-moving supercell, based on the grid-point value of effective-layer STP. The probabilities are derived from a mutually exclusive \
    2014-2015 sample of right-moving supercells that produced tornadoes, large hail, and damaging winds. The probabilities are plotted as grid point \
    values (rounded integer %), with color coding related to the climatology of the sample. For example, brown denotes values lower than the sample \
    climatology, and yellow is near climatological EF4+ frequency. Red, magenta, and dark purple values are all increasingly larger than the \
    climatological EF4+ frequency. The source data for the EF4+ tornado probabilities is shown by the red curve shown in \
    <a href="https://www.spc.noaa.gov/publications/smith/fig18_stp_probs_14-15only_ef0+_ef2+_ef4+_adjusted.png" target="_blank">this plot</a>. Please \
    see <a href="https://www.spc.noaa.gov/publications/smith/vrot-env.pdf" target="_blank">this paper</a> for additional details.</div>',

    'lclsrh': '100 mb Mean LCL Height (dashed green &lt; 1250 m, solid orange > 1500 m, shaded > 1750 m) and 0-1 km SRH (solid blue > 50 m2/s2). Dashed green LCLs more favorable for tornadoes.',

    'lr3c': '<div class="spc-prod">0-3 km Lapse Rate (> 7 deg C/km shaded) and 0-3 km MLCAPE (solid red).</div><div class="spc-info">Very useful for determining where \
    mesovortexgenesis could be particularly robust if low-level MLCAPE is available to enhance stretching</div>',

    '3cvr': '<div class="spc-prod">3-km CAPE (J/kg) & Surface Vorticity</div><div class="spc-info">CAPE in the lowest 3-km above ground level, and surface relative vorticity. \
    Areas of large 0-3-km CAPE tend to favor strong low-level stretching, and can support tornado formation when co-located with significant vertical vorticity \
    near the ground.</div>',

    'tdlr': 'Surface Dewpoint (solid light green > 48 F, dark green > 60 F) and 700-500 mb Lapse Rate (solid red > 7 C/km).',

    'hail': '<div class="spc-prod">Hail Forecasting Parameters</div><div class="spc-info">This image depicts three forecasting parameters used to predict hail. They are CAPE in the \
    layer from -10 C to -30 C, 0-6-km shear vector, and the freezing level height.  Large CAPE in the layer from -10 C to -30 C favors rapid hail growth.  0-6-km shear in excess \
    of 30-40 knots supports supercells with persistent updrafts that contribute to large hail production.  Finally, lower freezing level heights suggest a greater probability of \
    hail reaching the surface prior to melting, though melting impacts small hail much more than very large hailstones.</div>',

    'qlcs1': '<div class="spc-prod">0-3 km Bulk Shear (kt) and Theta-e Differential (C), with MUCAPE (J/kg)</div><div class="spc-info">This combination parameter plot attempts \
    to highlight areas potentially favorable for QLCS mesovortex generation.  The three plotted ingredients are 1) 0-3-km bulk shear vector (kt), 2) 0-3-km maximum \
    theta-e difference (C), and 3) MUCAPE (J/kg).  Areas with substantial buoyancy and line-normal bulk shear (30 kt or greater) favor deep upright convection over the gust \
    front of a QLCS, while the theta-e difference infers the potential strength of the cold pool. <br><br>Strong surges in the cold pool (often denoted by bowing segments of a \
    QLCS), when coincident with substantial buoyancy and strong line-normal shear, can favor stretching of vorticity generated along the gust front, and subsequent \
    mesovortex formation.</div><div class="spc-ref"><br>Additional information <a href="https://ams.confex.com/ams/26SLS/webprogram/Manuscript/Paper212008/SchaumannSLS2012_P142.pdf">HERE</a>.</div>',

    'qlcs2': '<div class="spc-prod">0-3 km Bulk Shear (kt) and Theta-e Differential (C), with 100 mb MLCAPE (J/kg)</div><div class="spc-info">This combination parameter plot \
    attempts to highlight areas potentially favorable for QLCS mesovortex generation.  The three plotted ingredients are 1) 0-3-km bulk shear vector (kt), 2) 0-3-km \
    maximum theta-e difference (C), and 3) MUCAPE (J/kg).  Areas with substantial buoyancy and line-normal bulk shear (30 kt or greater) favor deep upright convection over \
    the gust front of a QLCS, while the theta-e difference infers the potential strength of the cold pool. Strong surges in the cold pool (often denoted by bowing segments \
    of a QLCS), when coincident with substantial buoyancy and strong line-normal shear, can favor stretching of vorticity generated along the gust front, and subsequent \
    mesovortex formation.</div><div class="spc-info"><br>Additional information <a href="https://ams.confex.com/ams/26SLS/webprogram/Manuscript/Paper212008/SchaumannSLS2012_P142.pdf">HERE</a>.</div>',

    'pwtr': '<div class="spc-prod">Precipitable Water (inches)</div><div class="spc-info">Precipitable Water (inches). Values > 1 inch shaded green. Consider \
    values and anomalies for the time of year.</div>',

    'tran': '<div class="spc-prod">850 mb Moisture Transport</div><div class="spc-info">The 850 mb moisture transport is the product of the wind speed \
    (m s<sup>-1</sup>) and the mixing ratio (g g<sup>-1</sup>) at 850 mb.  Values are scaled by factor of 100, such that a 40 kt (~20 m s<sup>-1</sup>) \
    wind speed and a 12 g kg<sup>-1</sup> mixing ratio (0.012 g g<sup>-1</sup>) results in a moisture transport of 24 m s<sup>-1</sup> (the first pink \
    shade in the color fill). High values of moisture transport have been related to heavy rainfall potential with convective systems. </div><div class="spc-info"> \
    Reference:<br> Junker, N. M., R. S. Schneider, and S. L. Fauver, 1999: A study of heavy rainfall events during the great Midwest flood of 1993.  Wea. Forecasting, 14, 701-712.</div>',

    'tran_925': '<div class="spc-prod">925 mb Moisture Transport</div><div class="spc-info">The 925 mb moisture transport is the product of the wind speed \
    (m s<sup>-1</sup>) and the mixing ratio (g g<sup>-1</sup>) at 925 mb.  Values are scaled by factor of 100, such that a 40 kt (~20 m s<sup>-1</sup>) \
    wind speed and a 12 g kg<sup>-1</sup> mixing ratio (0.012 g g<sup>-1</sup>) results in a moisture transport of 24 m s<sup>-1</sup> (the first pink \
    shade in the color fill). High values of moisture transport have been related to heavy rainfall potential with convective systems. </div><div class="spc-info"> \
    Reference:<br> Junker, N. M., R. S. Schneider, and S. L. Fauver, 1999: A study of heavy rainfall events during the great Midwest flood of 1993.  Wea. Forecasting, 14, 701-712. </div> ',

    'prop': '<div class="spc-prod">Upwind Propagation</div><div class="spc-info">The upwind "vector approach" is a method developed by Corfidi et al. (1996) to forecast \
    MCS (or more specifically mesoscale beta element - MBE) movement. It is the vector sum of the mean flow through the cloud-bearing layer and the propagation component. \
    The magnitude and direction of the propagation component is assumed to be equal and opposite to that of the low-level jet (850 mb). </div><div class="spc-info"> \
    Reference:<br> Corfidi, S. F., J. H. Merritt and J. M. Fritsch, 1996: Predicting the movement of mesoscale convective complexes. Wea. Forecasting,11, 41-46. </div> ',

    'peff': '<div class="spc-prod">Precipitation Potential Placement<div class="spc-info">Precipitation Potential Placement is a derived parameter combining \
    precipitable water and low-level mean RH to help better place where rainfall will occur. Research has been published in the National Weather Association Digest in \
    2003 and stems from research and operational use of this product originally developed at NESDIS and Rod Scofield for satellite rainfall estimates dating back to 1981. \
    Rainfall is usually maximized where the best low level convergence and instability overlay with the highest values for this parameter. The risk for heavy rainfall \
    increases as values go up.  Additionally, thresholds for precipitation also change based on temperatures.  Onset of rainfall ranges from around 0.3 inches with \
    temperatures below 30 to 1.0 inches above 80.  Values above 1.0-1.4 inches with temperatures below 60 usually increase the risk for heavy rainfall while values \
    above 1.6-2.0 inches increase the risk for heavy rainfall events with temperatures above 60. </div><div class="spc-info"> \
    For more information, see: http://www.srh.noaa.gov/ffc/research/finalPP2.htm </div>',

    'snsq': '<div class="spc-prod">Snow Squall Parameter</div><div class="spc-info">A non-dimensional composite parameter \
    that combines 0-2 km AGL relative humidity,  0-2 km AGL potential instability (theta-e decreases with height), \
    and 0-2 km AGL mean wind speed (m/s). The intent of the parameter is to identify areas with low-level potential \
    instability, sufficient moisture, and strong winds to support snow squall development.  Surface potential temperatures \
    (theta) and MSL pressure are also plotted to identify strong baroclinic zones which often provide the focused low-level \
    ascent in cases of narrow snow bands. The index is formulated as follows: <br><br>\
    Snow Squall = ((0-2km mean RH - 60%) / 15%) * (( 4 - 2km_delta_theta-e) / 4) * (0-2km mean wind / 9 m s<sup>-1</sup>)<br><br>\
    The 2km_delta_theta-e term is the change in theta-e (K) from the surface to 2km AGL, where negative values represent \
    potential instability.  Areas with 0-2 km RH < 60% are filtered out in the color fill plots.<br><br>\
    <div class="spc-ref">Additional information can be found <a href="http://www.squallwx.com/snowsqualls">here</a> \
    (PowerPoint presentation).</div>',

    'dend': '<div class="spc-prod">Dendritic Layer Depth</div><div class="spc-info">The depth of the dendritic layer \
    (defined here as the layer with temperatures from -12 to -17 C) in meters. Deeper dendritic layer depths may correspond \
    to greater snowfall rates, assuming no melting layers below. Please keep in mind that these real-time fields \
    reflect the 1-h RAP model forecast of temperature, and are subject to any biases in the model forecast itself.</div>',

    'dendrh': '<div class="spc-prod">Dendritic Layer RH and Omega</div><div class="spc-info">The relative humidity (RH) and \
    upward vertical motion (Omega) are displayed for the dendritic growth layer (defined here as the layer with temperatures \
    from -12 to -17 C). Strong ascent and saturated conditions in this layer supports rapid growth of dendritic cyrstals, \
    which favors heavy snow production. Potential melting below the dendritic layer must be considered when evaluating snowfall \
    potential. Also, please keep in mind that these real-time fields reflect the 1-h RAP model forecast of temperature, moisture, and \
    omega aloft, and are subject to any biases in the model forecast itself.</div>',

    'sfir': 'No description',

    'fosb': '<div class="spc-prod">Fosberg Index</div><div class="spc-info">The FWI (Fire Weather Index) is defined by a quantitative \
    model that provides a nonlinear filter of meteorological data which results in a linear relationship between the combined \
    meteorological variables of relative humidity and wind speed, and the behavior of wildfires. Thus the index deals with \
    only the weather conditions, not the fuels. Several sets of conditions have been defined by Fosberg (Fosberg, 1978) \
    to apply this to fire weather management. The upper limits have been set to give an index value of 100 if the moisture \
    content is zero and the wind is 30 mph. Thus, the numbers range from 0 to 100 and if any number is larger than 100, \
    it is set back to 100. The index can be used to measure changes in fire weather conditions. Over several years of use, \
    Fosberg index values of 50 or greater generally appear significant on a national scale. The SPC fire weather \
    verification scheme uses the Fosberg Index, but with a check for both temperature (60F) and adjective fire danger rating \
    (3-High, 4-Very High, 5-Extreme). Fosberg index values are displayed in increments of 10 starting at 50 through \
    100 with the color pink indicating values of 50 or 60, dark orange indicating values of 70 or 80, while values of \
    90 and 100 are shown in bright orange. <br>The Fosberg Index, orginially called the Fire Weather Index (Fosberg, 1978), \
    was created to meet management needs for timeliness of weather information and for a meaningful interpretation of the \
    short time and close space weather impacts on fire management. It is a non-linear filter of meteorological data \
    developed by first transforming temperature and relative humidity to equilibrium moisture content, then \
    transforming the equilibrium moisture content to combustion efficiency. The index is approximated by \
    F = D((Rate of Spread) (Energy Release)) ^0.46 </div>',

    'lhan': '<div class="spc-prod">Haines Index</div><div class="spc-info">This is a fire weather index based on the stability \
    and moisture content of the lower atmosphere that measures the potential for existing fires to become large fires \
    (although this is not a predictor of fire starts). Orange will indicate Haines index values of 4 (low), dark orange \
    will show Haines index values of 5 (moderate), and red will depict Haines index values of 6 (high). Values of 4 and \
    above are plotted on each map even though the overall Haines index is from 2 to 6, with six being the highest potential \
    for large fires (see table below). It is calculated by determining the sum the atmospheric stability index (term A) \
    and the lower atmospheric dryness index (term B). The stability index is determined from measurements of the temperature \
    difference between two atmospheric levels and the dryness index is determined from measurements of the dew-point depression.<br>\
    Due to large variations in elevation across the United States, the index is calculated for three different pressure ranges: \
    low elevation is 950-850mb; mid elevation is 850-700mb; and high elevation is 700-500mb. It is named after its developer, \
    Donald Haines, a Forest Service research meteorologist, who did the initial work and published the scale in 1988.</div> ',

    'lasi': 'No description',

}

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