#!/usr/bin/env python

import os
  # To enable system command line instructions
import sys
  # For exit messages
import fileinput
  # To read and edit files


# subdirectory
SUBDIR='0000_0000-0019_9999'
# Local directory for JDL, SH files
OUT = '/data/king/grid/prodTools/hk/hk_subProd/fitqun/out/'+SUBDIR

BATCHID = 'pos_1e22_HK_Tochibora_LBL2019Mar'
BATCHJID = OUT+'/fitqun_' + BATCHID + '.jid'

# DFC location for output (full path excluding /fqn)
LOCATIONDFC = '/hyperk.org/beam/miniprod/A/1e22_HK_Tochibora_LBL2019Mar/pos/'+SUBDIR

commandBLANK = 'echo " " >> ' + BATCHJID
commandDATE =  'date    >>  ' + BATCHJID

os.system( commandBLANK )
os.system( commandDATE  )
os.system( commandBLANK )

# expecting input to be list of file ID including underscrore:
# ABCD_EFGH
f_in = open('wcsim.list_ab', "r")

for line in f_in:

    line = line.rstrip('\n')
    i = line[:4]
    k = line[-4:]


    FILEID = BATCHID + '_' + str(i).zfill(4) + '_' +  str(k).zfill(4)

    print('start:  FILEID = ' + FILEID )


    # Create the JDL file for this job
    fileJDL = OUT+'/fitqun_' + FILEID + '.jdl'
    copyJDL = 'cp fitqun_temp.jdl  '+ fileJDL
    os.system( copyJDL )

    # Edit JDL file for this job to use specific IDs
    for line in fileinput.input(fileJDL, inplace=True):
      print line.rstrip().replace('FILEID', FILEID)
    for line in fileinput.input(fileJDL, inplace=True):
      print line.rstrip().replace('TEMPOUT', OUT)


    # Create the executable file for this job
    fileSH = OUT+'/fitqun_' + FILEID + '.sh'
    copySH = 'cp fitqun_temp.sh  '+ fileSH
    os.system( copySH )

    # Edit executable file for this job to use specific IDs
    for line in fileinput.input(fileSH, inplace=True):
      print line.rstrip().replace('FILEID', FILEID)
    for line in fileinput.input(fileSH, inplace=True):
      print line.rstrip().replace('TEMPLOCDFC', LOCATIONDFC)
  

    diracSub = 'dirac-wms-job-submit ' + fileJDL + ' >> ' + BATCHJID
    os.system( diracSub )

    print('end:  FILEID = ' + FILEID )
 

