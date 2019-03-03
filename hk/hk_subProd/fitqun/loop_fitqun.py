#!/usr/bin/env python

import os
  # To enable system command line instructions
import sys
  # For exit messages
import fileinput
  # To read and edit files


BATCHID = 'pos_1e22_HK_Tochibora'
BATCHJID = 'fitqun_' + BATCHID + '.jid'

LOCATION = '/hyperk.org/beam/miniprod/A/1e22_HK_Tochibora/pos/'

commandBLANK = 'echo " " >> ' + BATCHJID
commandDATE =  'date    >>  ' + BATCHJID

os.system( commandBLANK )
os.system( commandDATE  )
os.system( commandBLANK )


for i in range(20, 30, 1):

    for k in range(0, 650, 1):


        FILEID = BATCHID + '_' + str(i).zfill(4) + '_' +  str(k).zfill(4)
    
        print('start:  FILEID = ' + FILEID )
    
    
        # Create the JDL file for this job
        fileJDL = 'fitqun_' + FILEID + '.jdl'
        copyJDL = 'cp fitqun_temp.jdl  '+ fileJDL
        os.system( copyJDL )
    
        # Edit JDL file for this job to use specific IDs
        for line in fileinput.input(fileJDL, inplace=True):
          print line.rstrip().replace('FILEID', FILEID)
    
    
        # Create the executable file for this job
        fileSH = 'fitqun_' + FILEID + '.sh'
        copySH = 'cp fitqun_temp.sh  '+ fileSH
        os.system( copySH )
    
        # Edit executable file for this job to use specific IDs
        for line in fileinput.input(fileSH, inplace=True):
          print line.rstrip().replace('FILEID', FILEID)
        for line in fileinput.input(fileSH, inplace=True):
          print line.rstrip().replace('TEMPLOC', LOCATION)
    
      
    
        diracSub = 'dirac-wms-job-submit ' + fileJDL + ' >> ' + BATCHJID
        os.system( diracSub )
    
        print('end:  FILEID = ' + FILEID )
     


