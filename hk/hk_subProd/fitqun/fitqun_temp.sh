#!/bin/bash


echo ' '
date        2>&1 | tee -a logfq_out_FILEID.txt
echo ' '    2>&1 | tee -a logfq_out_FILEID.txt
echo ' '
echo ' --------------------------------------------------- '
echo ' '
printenv    2>&1 | tee -a logwc_out_FILEID.txt
echo ' '
echo ' --------------------------------------------------- '


LOCATIONDFC=TEMPLOCDFC

echo 'Obtaining file '${LOCATIONDFC}'/wcs/wcsim_out_FILEID.root'
echo ''
dirac-dms-get-file ${LOCATIONDFC}/wcs/wcsim_out_FILEID.root
ES1=$? # Exist status
if [ ${ES1} -neq 0 ];
  then 
    echo 'Failed to obtain wcsim file ' >&2
    exit 1
fi


echo ''

source /cvmfs/hyperk.egi.eu/prod2018/env-WCSim_CVMFS.sh
export FITQUN_ROOT=/cvmfs/hyperk.egi.eu/prod2018/fiTQun

cd  /cvmfs/hyperk.egi.eu/prod2018/fiTQun
source /cvmfs/hyperk.egi.eu/prod2018/fiTQun/sourceme_forHK
cd -

PARAM=/cvmfs/hyperk.egi.eu/prod2018/fiTQun/ParameterOverrideFiles/HyperK_4ring.parameters.dat

# for copying to sandbox and bookkeeping
cp ${PARAM} ./param.dat

$FITQUN_ROOT/runfiTQunWC -p ${PARAM} -r  fitqun_out_FILEID.root    ./wcsim_out_FILEID.root     2>&1 | tee -a logfq_out_FILEID.txt


echo ' '    2>&1 | tee -a logfq_out_FILEID.txt
ls -l       2>&1 | tee -a logfq_out_FILEID.txt
echo ' '    2>&1 | tee -a logfq_out_FILEID.txt
date
echo ' '    2>&1 | tee -a logfq_out_FILEID.txt

# save file to grid
dirac-dms-add-file ${LOCATIONDFC}/fqn/fitqun_out_FILEID.root  fitqun_out_FILEID.root  UKI-LT2-QMUL2-disk -ddd     2>&1 | tee -a logfq_out_FILEID.txt

ES2=$? # Exit status
if [ ${ES1} -neq 0 ];
  then
    echo 'Failed to add fitqun file to DFC ' >&2
    exit 1
fi

dirac-dms-add-file ${LOCATIONDFC}/lfq/logfq_out_FILEID.txt     logfq_out_FILEID.txt   UKI-LT2-QMUL2-disk -ddd

