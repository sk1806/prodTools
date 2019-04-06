#!/bin/bash

# Should make a .sh that runs this .sh and pies into log file
# rather than writing   2>&1 | tee -a logwc_out_FILEID.txt  everywhere

echo ' '
date      2>&1 | tee -a logwc_out_FILEID.txt
echo ' '  2>&1 | tee -a logwc_out_FILEID.txt
echo ' '
echo ' --------------------------------------------------- '
echo ' '
printenv  2>&1 | tee -a logwc_out_FILEID.txt
echo ' '  2>&1 | tee -a logwc_out_FILEID.txt
echo ' --------------------------------------------------- '


LOCATIONDFC=TEMPLOCDFC

source /cvmfs/hyperk.egi.eu/prod2018/env-WCSim_CVMFS.sh

#PATH=${PATH}:/cvmfs/hyperk.egi.eu/prod2018/WCSim-v1.7.0/exe/bin/Linux-g++/


WCSIM_MAC=wcsim_FILEID.mac

# for copying to sandbox and bookkeeping
cp ${WCSIM_MAC} wcsim.mac

WCSIMEXE=/cvmfs/hyperk.egi.eu/prod2018/WCSimSandBox/grid/


${WCSIMEXE}/WCSim ${WCSIM_MAC}   2>&1 | tee logwc_out_FILEID.txt




echo ' '  2>&1 | tee -a logwc_out_FILEID.txt
ls -l     2>&1 | tee -a logwc_out_FILEID.txt
echo ' '  2>&1 | tee -a logwc_out_FILEID.txt
date      2>&1 | tee -a logwc_out_FILEID.txt
echo ' '  2>&1 | tee -a logwc_out_FILEID.txt


echo ' '
echo ' '
echo ' '
dirac-dms-add-file ${LOCATIONDFC}/wcs/wcsim_out_FILEID.root  wcsim_out_FILEID.root  UKI-LT2-QMUL2-disk -ddd    2>&1 | tee -a logwc_out_FILEID.txt
dirac-dms-add-file ${LOCATIONDFC}/lwc/logwc_out_FILEID.txt   logwc_out_FILEID.txt   UKI-LT2-QMUL2-disk -ddd    




