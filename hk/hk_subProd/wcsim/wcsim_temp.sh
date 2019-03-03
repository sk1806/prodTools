#!/bin/bash


echo ' '
date
echo ' '
echo ' '
echo ' --------------------------------------------------- '
echo ' '
printenv
echo ' '
echo ' --------------------------------------------------- '


LOCATION=TEMPLOC

source /cvmfs/hyperk.egi.eu/prod2018/env-WCSim_CVMFS.sh

#PATH=${PATH}:/cvmfs/hyperk.egi.eu/prod2018/WCSim-v1.7.0/exe/bin/Linux-g++/


WCSIM_MAC=wcsim_FILEID.mac

# for copying to sandbox and bookkeeping
cp ${WCSIM_MAC} wcsim.mac

WCSIMEXE=/cvmfs/hyperk.egi.eu/prod2018/WCSimSandBox/grid/
${WCSIMEXE}/WCSim ${WCSIM_MAC}




echo ' '
ls -l
echo ' ' 
date

echo ' '
echo ' '
echo ' '
echo ' '
dirac-dms-add-file $LOCATION/wcsim_out_FILEID.root  wcsim_out_FILEID.root  UKI-LT2-QMUL2-disk -ddd


