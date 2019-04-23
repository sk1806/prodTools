#!/usr/bin/env python

import os
  # To enable system command line instructions
import sys
  # For exit messages
import fileinput
  # To read and edit files

SIGN = 'neg'

# subdirectory
SUBDIR='0000_0000-0019_9999'
#SUBDIR='0020_2000-0039_9999' XXX WRONG XXX
#SUBDIR='0040_0000-0059_9999'
#SUBDIR='0060_0000-0079_9999'

# Directory for wcsimSandBox
SAND = '/data/king/grid/prodTools/hk/hk_subProd/wcsim/wcsimSandBox/'
# Local directory for JDL, SH, MAC files
OUT = '/data/king/grid/prodTools/hk/hk_subProd/wcsim/out/'+ SIGN + '/' +SUBDIR
# File name where JID will be stored
BATCHID = SIGN +'_1e22_HK_Tochibora_LBL2019Mar'
BATCHJID = OUT+'/wcsim_' + BATCHID + '.jid'

# DFC location for output (full path excluding /wcsim)
LOCATIONDFC = '/hyperk.org/beam/miniprod/A/1e22_HK_Tochibora_LBL2019Mar/'+SIGN+'/'+SUBDIR
# Local directory of the .dat vector files
LOCATIONLOCAL = '/data/hyperk/prod/LBL2019Mar/'+SIGN+'_split_dat/'+SUBDIR



commandBLANK = 'echo " " >> ' + BATCHJID
commandDATE =  'date    >>  ' + BATCHJID

os.system( commandBLANK )
os.system( commandDATE  )
os.system( commandBLANK )

# expecting input to be list of file ID including underscrore:
# ABCD_EFGH
f_in = open('wcsim_dfc_mis.list', "r")

for line in f_in:

    line = line.rstrip('\n')
    i = line[:4]
    k = line[-4:]

    FILEID = BATCHID + '_' + str(i).zfill(4) + '_' +  str(k).zfill(4)

    print('start:  FILEID = ' + FILEID )


    # Create the JDL file for this job
    fileJDL = OUT+'/wcsim_' + FILEID + '.jdl'
    copyJDL = 'cp wcsim_temp.jdl  '+ fileJDL
    os.system( copyJDL )

    # Edit JDL file for this job to use specific IDs
    for line in fileinput.input(fileJDL, inplace=True):
      print line.rstrip().replace('FILEID', FILEID)
    for line in fileinput.input(fileJDL, inplace=True):
      print line.rstrip().replace('TEMPLOCLOCAL', LOCATIONLOCAL)
    for line in fileinput.input(fileJDL, inplace=True):
      print line.rstrip().replace('TEMPOUT', OUT)
    for line in fileinput.input(fileJDL, inplace=True):
      print line.rstrip().replace('TEMPSAND', SAND)


    # Create the executable file for this job
    fileSH = OUT+'/wcsim_' + FILEID + '.sh'
    copySH = 'cp wcsim_temp.sh  '+ fileSH
    os.system( copySH )

    # Edit executable file for this job to use specific IDs
    for line in fileinput.input(fileSH, inplace=True):
      print line.rstrip().replace('FILEID', FILEID)
    for line in fileinput.input(fileSH, inplace=True):
      print line.rstrip().replace('TEMPLOCDFC', LOCATIONDFC)


    # Create the MAC file for this job
    fileMAC = OUT+'/wcsim_' + FILEID + '.mac'
    copyMAC = 'cp wcsim_temp.mac  '+ fileMAC
    os.system( copyMAC )

    # Edit MAC file for this job to use specific IDs
    for line in fileinput.input(fileMAC, inplace=True):
      print line.rstrip().replace('FILEID', FILEID)


    # Local vector
    fileVEC=LOCATIONLOCAL+'/vector_'+FILEID+'.dat'
   # Read the number of events to feed into the mac
    nEvts = 0
    search = open(fileVEC)
    for line in search:
        
        if 'begin' in line:
            nEvts = nEvts + 1
    print 'nEvts',
    print nEvts

    # Edit MAC file for this job to use specific IDs
    for line in fileinput.input(fileMAC, inplace=True):
      print line.rstrip().replace('TEMPEVENTS', str(nEvts) )

    diracSub = 'dirac-wms-job-submit ' + fileJDL + ' >> ' + BATCHJID
    os.system( diracSub )

    print('end:  FILEID = ' + FILEID )
   

