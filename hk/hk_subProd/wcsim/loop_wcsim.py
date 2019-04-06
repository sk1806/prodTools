#!/usr/bin/env python

import os
  # To enable system command line instructions
import sys
  # For exit messages
import fileinput
  # To read and edit files


BATCHID = 'pos_1e22_HK_Tochibora'
BATCHJID = 'wcsim_' + BATCHID + '.jid'

LOCATIONDFC = '/hyperk.org/beam/miniprod/B/1e22_HK_Tochibora/pos/wcsim'
LOCATIONLOCAL = '/data/hyperk/prod/LBL2019Mar/pos_split_dat/0000_0000-0019_9999/'

commandBLANK = 'echo " " >> ' + BATCHJID
commandDATE =  'date    >>  ' + BATCHJID

os.system( commandBLANK )
os.system( commandDATE  )
os.system( commandBLANK )

for i in range(5, 30, 1):
    for k in range(0, 650, 1):


        FILEID = BATCHID + '_' + str(i).zfill(4) + '_' +  str(k).zfill(4)
    
        print('start:  FILEID = ' + FILEID )
    
    
        # Create the JDL file for this job
        fileJDL = 'wcsim_' + FILEID + '.jdl'
        copyJDL = 'cp wcsim_temp.jdl  '+ fileJDL
        os.system( copyJDL )
    
        # Edit JDL file for this job to use specific IDs
        for line in fileinput.input(fileJDL, inplace=True):
          print line.rstrip().replace('FILEID', FILEID)
        for line in fileinput.input(fileJDL, inplace=True):
          print line.rstrip().replace('TEMPLOCLOCAL', LOCATIONLOCAL)
    
    
        # Create the executable file for this job
        fileSH = 'wcsim_' + FILEID + '.sh'
        copySH = 'cp wcsim_temp.sh  '+ fileSH
        os.system( copySH )
    
        # Edit executable file for this job to use specific indevidual IDs
        # And also edit the dfc path and local path
        for line in fileinput.input(fileSH, inplace=True):
          print line.rstrip().replace('FILEID', FILEID)
        for line in fileinput.input(fileSH, inplace=True):
          print line.rstrip().replace('TEMPLOCDFC', LOCATIONDFC)
   
    
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
     


