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


LOCATIONDFC=TEMPLOCDFC

echo 'Obtaining file '${LOCATIONDFC}'/wcs/wcsim_out_FILEID.root'
echo ''
dirac-dms-get-file ${LOCATIONDFC}/wcs/wcsim_out_FILEID.root
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
dirac-dms-add-file ${LOCATIONDFC}/fqn/4_ring/fitqun_out_FILEID.root  fitqun_out_FILEID.root  UKI-LT2-QMUL2-disk -ddd


