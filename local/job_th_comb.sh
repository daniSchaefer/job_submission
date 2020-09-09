#!/bin/bash

## check cms.cern.ch and storage a
if [ ! -e /cvmfs/cms.cern.ch/cmsset_default.sh ]
then
	exit 1
fi

if [ ! -d /storage/jbod/dschaefer/ ]
then
	exit 1
fi



## setup CMSSW
	SPAWNPOINT=`pwd`
	echo ${SPAWNPOINT}
	source $VO_CMS_SW_DIR/cmsset_default.sh
	
	SCRAM_ARCH=slc6_amd64_gcc481
	cd /portal/ekpcms6/home/dschaefer/
	#scramv1 project CMSSW_7_1_19
	cd CMSSW_7_1_5/src/
	eval `scramv1 runtime -sh`



## setup combine
	#git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
	#echo 'after git clone'
	#cd HiggsAnalysis/CombinedLimit
	#git fetch origin
	#git checkout v5.0.2
	#scramv1 b clean; scramv1 b


	echo "arguments:"
    for a in ${BASH_ARGV[*]} ; do
	    echo -n "$a "
    done
    	

	cd ${SPAWNPOINT}
	pwd
	ls
	#which combine
	cp /home/dschaefer/CMSSW_7_1_5/src/DijetCombineLimitCode/datacards/CMS_jj_BulkWW_${1}_w0p0_13TeV_CMS_jj_VVHP.txt .datacard.txt
	cp /home/dschaefer/CMSSW_7_1_5/src/DijetCombineLimitCode/workspaces/CMS_jj_BulkWW_${1}_w0p0_13TeV.root .
	cp /home/dschaefer/CMSSW_7_1_5/src/DijetCombineLimitCode/workspaces/
	#pwd 
	#ls -la
	
    for arg in ${@:2} ; do
        /portal/ekpcms6/home/dschaefer/CMSSW_7_1_5/bin/slc6_amd64_gcc481/combine -M HybridNew --frequentist -m ${1} -s -1 --singlePoint ${arg} --saveToys --saveHybridResult  --testStat LHC -d datacard.txt --clsAcc 0 -T 500 --iterations 5 -n BulkWW_sp$i > result_M${m}_sp${i}.txt
        #mv higgsCombineBulkWW_sp$i.HybridNew.mH$m.*.root higgsCombineBulkWW_sp$i.HybridNew.T500.mH$m.root
    	#/storage/a/mschnepf/tHq/13tev/CMSSW_7_1_19/bin/slc6_amd64_gcc481/combine tH_comb_${1}.txt -M HybridNew --frequentist -s -1 --saveToys --saveHybridResult --clsAcc 0 --setPhysicsModelParameterRanges r=0,1500 --rMax 1500 -T 2000 --iterations 5 -n tH_comb --singlePoint ${arg} > result_${arg}.txt
        mv higgsCombineBulkWW.HybridNew.*.root /storage/jbod/dschaefer/fullCLs/BulkWW.HybridNew.M${1}_${arg}.root	
    done


## end of script

	echo '### end of job ###'



