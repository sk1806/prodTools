#! /usr/bin/env python

from t2k_check import*

#import os
#import sys
##sys.path.append('../../libFns')





#dfc_path = '/t2k.org/nd280/production006/L/mcp/neut/2015-08-water/magnet/run9/'
#clean = '/p6L_run9water_neut/'

dfc_path = '/t2k.org/nd280/production006/T/mcp/anti-neut_D/2010-11-water/magnet/run5/'
clean = 'p6T_run5water_anti-neut_D'
start = 80510000
end   = 80510079
checkND280 = False

local_path = '/data/king/t2k/GRID/dirac/ND280Computing/processing_scripts/cleanup/runs/' + clean


types=[]
types.append('numc')
types.append('cata')
if(checkND280):
    types.append('anal')
    types.append('reco')
    types.append('cali')
    types.append('elmc')
    types.append('g4mc')
#types.append('cnfg')

for e in types:

    print('Checking:  '),
    print(e)

    dfc_list(local_path, dfc_path, '/'+e+'/', e)

    l_dfc  = local_path +'/'+ e +'_dfc.list'
    l_num = local_path +'/'+ e +'_dfc_num.list'
    extract_num_list(l_dfc, l_num)

    l_mis = local_path +'/'+ e +'_dfc_mis.list'
    l_rep = local_path +'/'+ e +'_dfc_rep.list'
    extract_miss_rep( l_num, l_mis, l_rep, start, end )



