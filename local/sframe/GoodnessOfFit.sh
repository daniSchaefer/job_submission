#!/bin/bash
## setup CMSSW
	SPAWNPOINT=`pwd`	# save work directory 
	echo ${SPAWNPOINT}

	# $1 input directory i.e. path to DijetCombineLimitCode
	# $2 name of datacard
	# $3 name of workspace
	# $4 name of background workspace
	# $5 mass of the resonance
	# $6 output directory
	# $7 name of output file
	
	source $VO_CMS_SW_DIR/cmsset_default.sh
        SCRAM_ARCH=slc6_amd64_gcc491
        #cd ${1}../../..
        cd /portal/ekpbms2/home/dschaefer/CMSSW_8_1_0/src/
	
	eval `scramv1 runtime -sh`		# set variables for CMSSW
	# print given arguments
	echo "arguments:"
	for a in ${BASH_ARGV[*]} ; do
	    echo -n "$a "
	done

	# go back to work directory
	cd ${SPAWNPOINT}
	

	# copy needed files
	cp ${1}/${2} .
	ls
	
	#combine -M GoodnessOfFit /portal/ekpbms2/home/dschaefer/DiBoson3D/workspace_JJ_BulkGWW_13TeV.root --algo=saturated -t 5000 -s -1 --toysFreq -m 2500
	# set signal strength to 0 for tests in LPLP controll-region
	if [ "${5}" = "1" ]; then
	
            combine -M GoodnessOfFit ${2}  -m ${3} --algorithm saturated -t 50 -s -1  --toysFreq --fixedSignalStrength=0       
        else 
            combine -M GoodnessOfFit ${2}  -m ${3} --algo=saturated -s -1 --fixedSignalStrength=0
        fi    
        mv higgs*.root /portal/ekpbms2/home/dschaefer/DiBoson3D/GoodnessOfFitTests/${4}
	echo '### end of job ###'
