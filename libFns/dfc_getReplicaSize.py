#!/usr/bin/env python

# Script to register a list local files in the hyperk.org DFC
# soph.e.king123@gmail.com


#  Relevant documentation
#https://dirac.readthedocs.io/en/stable/CodeDocumentation/DataManagementSystem/Client/DataManager.html
#https://dirac.readthedocs.io/en/stable/DeveloperGuide/AddingNewComponents/DevelopingCommands/index.html#coding-commands


#  Relevant functions
#
# DataManager module
#  def getReplicaIsFile( self, lfn, storageElementName, singleFile = False ):
#    """ Determine whether the supplied lfns are files at the supplied StorageElement
#
#        'lfn' is the file(s) to check
#        'storageElementName' is the target Storage Element  """

#import os
#import sys
#sys.path.append('../../libFns')

from diracTools import dirac__ls

from DIRAC.Core.Base import Script
Script.parseCommandLine() 

from DIRAC.DataManagementSystem.Client.DataManager import DataManager
dm = DataManager()

#
##lfn = "/t2k.org/nd280/production006/L/mcp/neut/2015-08-water/magnet/run9/numc/oa_nt_beam_90910104-0038_e6emxphl6w3g_numc_000_magnet201508waterrun9.root"
#lfn='/t2k.org/nd280/production006/L/mcp/neut/2015-08-water/magnet/run9/numc/oa_nt_beam_90910059-0016_dm4kw3yo2aeb_numc_000_magnet201508waterrun9.root'
site = "UKI-LT2-QMUL2-disk"
#
#res = dm.getReplicaSize(lfn, site)
#print('res = ' )
#print(res)
#
#size = res['Value']['Successful'][lfn]
#print('size = ')
#print(size)
#


f_size = open("size.list", "w+")
f_size_small = open("size_small.list", "w+")
f_size_small_del = open("size_small_del.list", "w+")
f_size_error = open("size_error.list", "w+")

#dfc_path = "/t2k.org/nd280/production006/L/mcp/neut/2015-08-water/magnet/run9/"
#lower_lim = 30000000 
#type_dir = "numc"
#lower_lim = 170000000
#type_dir = "anal"

dfc_path = "/t2k.org/nd280/production006/T/mcp/anti-neut_D/2010-11-water/magnet/run5/"
lower_lim = 19200000 
type_dir = "numc"
#lower_lim = 170000000
#type_dir = "anal"




dfc_list = dirac__ls(dfc_path + type_dir)

count=0

for lfn in dfc_list:
    res = dm.getReplicaSize(lfn, site)
    print(lfn)
    try:
        size = res['Value']['Successful'][lfn]
        str_lfn = lfn + '\n'
        str_size_lfn = str(size) + " : " + str_lfn
        print(str_size_lfn)
        f_size.write(str_size_lfn)
        if(size < lower_lim):
            f_size_small.write(str_size_lfn)
            f_size_small_del.write(str_lfn)
    except:
        print('Error for:  '),
        print(lfn)
        str_lhn = lfn + '\n'
        f_size_error.write(lfn)


f_size.close()
f_size_small.close()      
f_size_small_del.close()

exit()

######## Parts to Edit ########

# local list of files (read-only)
file_list = open('t5-t6.list', 'r')

# local directory of files
local_folder = '/data/king/t2k/GRID/dirac/dirac_api_tests'


# LFNs that correspond to list of files (read-only)
# Usuaully we use the file list to also deifne the LFNs
# But you could provide a different list of corresponding LFNs if you wish
lfn_list = open('t5-t6.list', 'r')

# DFC directory of files
# If the DFC folder does not exist, it will be created automatically
dfc_folder = '/t2k.org/user/king/b'

# Site where you wish to copy the files to
site = 'UKI-LT2-QMUL2-disk'

#############################

print('debug 1')
#print dm.putAndRegister( '/hyperk.org/user/king/t1.txt', '/data/king/t2k/GRID/dirac/dirac_api_tests/t1.txt' , site )
print('debug 2')

for i,j in  zip(file_list, lfn_list):

    # use  rstrip() to remove the '\n' from reading the text file
    local = local_folder + '/' + i.rstrip()  
    dfc =   dfc_folder   + '/' + j.rstrip()
    
    print('')
    print(local)
    print(dfc)
    print('')

    print dm.putAndRegister( dfc, local, site )
  

file_list.close()
lfn_list.close()








