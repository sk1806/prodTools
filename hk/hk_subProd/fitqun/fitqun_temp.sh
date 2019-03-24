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

# Retrieve file:  wcsim_out_FILEID.root
WCSIMFILE=${LOCATION}/wcsim/wcsim_out_ FILEID.root 

echo''
echo 'WCSIMFILE'
echo $WCSIMFILE
dirac-dms-get-file ${WCSIMFILE}
echo ''
dirac-dms-get-file ${LOCATION}/wcsim/wcsim_out_FILEID.root

echo ${LOCATION}/wcsim/wcsim_out_ FILEID.root

echo ''

source /cvmfs/hyperk.egi.eu/prod2018/env-WCSim_CVMFS.sh
export FITQUN_ROOT=/cvmfs/hyperk.egi.eu/prod2018/fiTQun

cd  /cvmfs/hyperk.egi.eu/prod2018/fiTQun
source /cvmfs/hyperk.egi.eu/prod2018/fiTQun/sourceme_forHK
cd -

PARAM=/cvmfs/hyperk.egi.eu/prod2018/fiTQun/ParameterOverrideFiles/HyperK_4ring.parameters.dat

# for copying to sandbox and bookkeeping
cp ${PARAM} ./param.dat

$FITQUN_ROOT/runfiTQunWC -p ${PARAM} -r  fitqun_out_FILEID.root    ./wcsim_out_FILEID.root


echo ' '
ls -l
echo ' '
date
echo ' '

# save file to grid
dirac-dms-add-file $LOCATION/fitqun/4_ring/fitqun_out_FILEID.root  fitqun_out_FILEID.root  UKI-LT2-QMUL2-disk -ddd


