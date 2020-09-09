#!/bin/bash
## setup CMSSW
# 	SPAWNPOINT=`pwd`	# save work directory 
# 	echo ${SPAWNPOINT}
# 
# 	
# 	source /cvmfs/cms.cern.ch/cmsset_default.sh
# 	SCRAM_ARCH=slc6_amd64_gcc481
# 	cd  /cvmfs/cms.cern.ch/slc6_amd64_gcc530/cms/cmssw/CMSSW_8_0_20/  	# go to CMSSW installation folder
# 	eval `scramv1 runtime -sh`		# set variables for CMSSW

	# print given arguments
	echo "arguments:"
	for a in ${BASH_ARGV[*]} ; do
	    echo -n "$a "
	done

	# go back to work directory
# 	cd ${SPAWNPOINT}
	source /usr/users/dschaefer/SFrame_setup/SFrame-04-00-01/setup.sh
	
        echo $SFRAME_DIR
        echo $LD_LIBRARY_PATH
	# copy needed files
	echo "copy neede files"
	cp $6/config/JobConfig.dtd .
	cp $7$1 .
	mkdir -p $3
	echo "mkdir -p $3"
	cp $2$3$4 $3
	echo "cp $2$3$4 $3"
	mkdir data
	cp $6/data/*.root data/

	
	#start your run
	/usr/users/dschaefer/SFrame_setup/SFrame-04-00-01/bin/sframe_main ${1}
	echo "/usr/users/dschaefer/SFrame_setup/SFrame-04-00-01/bin/sframe_main ${1} "
	#/portal/ekpcms6/home/dschaefer/CMSSW_7_1_5/bin/slc6_amd64_gcc481/combine -M Asymptotic -v3 -m ${1} -n _lim_${1}_had_${3}_${5}_ -d CMS_jj_${4}_${1}_w0p${2}_13TeV_CMS_jj_VV${3}.txt --rMax 1000 
	
	# rename and move your outout files
	echo "write output in file : "
	#ls
	mv ExoDiBosonAnalysis* $5
	#ls 
## end of script
        
	echo '### end of job ###'
