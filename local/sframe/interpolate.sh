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
	

	if [[ $1 == *"Data"* ]]; then
            python /usr/users/dschaefer/SFrame_setup/ExoDiBosonAnalysis/do-mjj-histos_SR.py $1 --data $1 --$2 --path $3
            root -b -q "/usr/users/dschaefer/CMSSW_7_4_7/src/DijetCombineLimitCode/MiniTreeProducerVV13TeV.C(\""$4\"")"
        fi
        if [[ $1 == *"QCD"* ]]; then
            python /usr/users/dschaefer/SFrame_setup/ExoDiBosonAnalysis/do-mjj-histos_SR.py $1 --bkg $1 --$2 --path $3
            root -b -q "/usr/users/dschaefer/CMSSW_7_4_7/src/DijetCombineLimitCode/MiniTreeProducerVV13TeV.C(\""$4\"")"
        fi
        if [[ $1 == *"jets"* ]]; then
            python /usr/users/dschaefer/SFrame_setup/ExoDiBosonAnalysis/do-mjj-histos_SR.py $1 --bkg $1 --$2 --path $3
        fi
        if [[ $1 == *"WW"* ]]; then
            python /usr/users/dschaefer/SFrame_setup/ExoDiBosonAnalysis/do-mjj-histos_SR.py --signal $1 --mass $2 --$3 --path $4
        fi
        if [[ $1 == *"ZZ"* ]]; then
            python /usr/users/dschaefer/SFrame_setup/ExoDiBosonAnalysis/do-mjj-histos_SR.py --signal $1 --mass $2 --$3 --path $4
        fi
        if [[ $1 == *"WZ"* ]]; then
            python /usr/users/dschaefer/SFrame_setup/ExoDiBosonAnalysis/do-mjj-histos_SR.py --signal $1 --mass $2 --$3 --path $4
        fi
        if [[ $1 == *"Qstar"* ]]; then
            python /usr/users/dschaefer/SFrame_setup/ExoDiBosonAnalysis/do-mjj-histos_SR.py --signal $1 --mass $2 --$3 --path $4
        fi
	
	mv *.root $5
	echo '### end of job ###'

