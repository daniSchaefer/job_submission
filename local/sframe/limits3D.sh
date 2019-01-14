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
	#cd /portal/ekpbms2/home/dschaefer/CMSSW_8_1_0/src/
	cd /portal/ekpbms2/home/dschaefer/CMSSW_7_4_7/src/
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
	
	
	 
        combine -m ${3} -M Asymptotic ${2} -H ProfileLikelihood #--run blind  new version  AsymptoticLimits --verbose 3 #--rAbsAcc 0.00001 --rRelAcc 0.00001
	#mv  higgs*.root $1/Limits/$4
	mv higgs*.root /portal/ekpbms2/home/dschaefer/DiBoson3D/forBiasTests/kernels2017/limits/${4}

	echo '### end of job ###'




