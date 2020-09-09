#!/bin/bash
## setup CMSSW
	SPAWNPOINT=`pwd`	# save work directory 
	echo ${SPAWNPOINT}

	
	source /cvmfs/cms.cern.ch/cmsset_default.sh
	SCRAM_ARCH=slc6_amd64_gcc481
	cd  /cvmfs/cms.cern.ch/slc6_amd64_gcc530/cms/cmssw/CMSSW_8_0_20/  	# go to CMSSW installation folder
	eval `scramv1 runtime -sh`		# set variables for CMSSW

	# print given arguments
	echo "arguments:"
	for a in ${BASH_ARGV[*]} ; do
	    echo -n "$a "
	done

	# go back to work directory
	cd ${SPAWNPOINT}
	
	# $1 = model name
	# $2 = mass point
	# $3 = path to input file
	# $4 = output directory
	
	
	if [[ $1 == *"WW"* ]]; then
            python /usr/users/dschaefer/CMSSW_7_4_7/src/DijetCombineLimitCode/interpolateVV13TeV.py $3$1_13TeV_ $2 GeV
	fi
	if [[ $1 == *"WZ"* ]]; then
            python /usr/users/dschaefer/CMSSW_7_4_7/src/DijetCombineLimitCode/interpolateVV13TeV.py $3$1_13TeV_ $2 GeV
	fi
	if [[ $1 == *"ZZ"* ]]; then
            python /usr/users/dschaefer/CMSSW_7_4_7/src/DijetCombineLimitCode/interpolateVV13TeV.py $3$1_13TeV_ $2 GeV
	fi
	if [[ $1 == *"Qstar"* ]]; then
            python /usr/users/dschaefer/CMSSW_7_4_7/src/DijetCombineLimitCode/interpolateVV13TeV.py $3$1_13TeV_ $2 GeV
	fi
	echo '### end of job ###'

