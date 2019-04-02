#!/usr/bin/env python

import os
  # To enable system command line instructions
import sys
  # For exit messages
import fileinput
  # To read and edit files


BATCHID = 'pos_1e22_HK_Tochibora'
BATCHJID = 'wcsim_' + BATCHID + '.jid'

LOCATION = '/hyperk.org/beam/miniprod/A/1e22_HK_Tochibora/pos/wcsim'


commandBLANK = 'echo " " >> ' + BATCHJID
commandDATE =  'date    >>  ' + BATCHJID

os.system( commandBLANK )
os.system( commandDATE  )
os.system( commandBLANK )


f_in = open('wcsim_dfc_mis.list', "r")

for line in f_in:

    line = line.rstrip('\n')
    i = line[:4]
    k = line[-4:]

    FILEID = BATCHID + '_' + str(i).zfill(4) + '_' +  str(k).zfill(4)

    print('start:  FILEID = ' + FILEID )


    # Create the JDL file for this job
    fileJDL = 'wcsim_' + FILEID + '.jdl'
    copyJDL = 'cp wcsim_temp.jdl  '+ fileJDL
    os.system( copyJDL )

    # Edit JDL file for this job to use specific IDs
    for line in fileinput.input(fileJDL, inplace=True):
      print line.rstrip().replace('FILEID', FILEID)


    # Create the executable file for this job
    fileSH = 'wcsim_' + FILEID + '.sh'
    copySH = 'cp wcsim_temp.sh  '+ fileSH
    os.system( copySH )

    # Edit executable file for this job to use specific IDs
    for line in fileinput.input(fileSH, inplace=True):
      print line.rstrip().replace('FILEID', FILEID)
    for line in fileinput.input(fileSH, inplace=True):
      print line.rstrip().replace('TEMPLOC', LOCATION)


    # Create the MAC file for this job
    fileMAC = 'wcsim_' + FILEID + '.mac'
    copyMAC = 'cp wcsim_temp.mac  '+ fileMAC
    os.system( copyMAC )

    # Edit JDL file for this job to use specific IDs
    for line in fileinput.input(fileMAC, inplace=True):
      print line.rstrip().replace('FILEID', FILEID)


    diracSub = 'dirac-wms-job-submit ' + fileJDL + ' >> ' + BATCHJID
    os.system( diracSub )

    print('end:  FILEID = ' + FILEID )
   


