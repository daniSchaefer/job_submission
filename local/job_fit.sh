#!/bin/bash

	echo "arguments:"
    echo -n "$* "
	SPAWNPOINT=`pwd`
	echo ${SPAWNPOINT}


## setup CMSSW
	source $VO_CMS_SW_DIR/cmsset_default.sh
	SCRAM_ARCH=slc6_amd64_gcc481
	cd /storage/a/mschnepf/tHq/13tev/
	scramv1 project CMSSW_7_1_5
	cd CMSSW_7_1_5/src
	eval `scramv1 runtime -sh`

## test something
	#whoami
	id -u
## setup combine
	#git config --global user.email "maschnepf@schnepf-net.de" 
	#git config --global user.name "Matthias Schnepf"
	#git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
	#echo 'after git clone'
	#pwd
	#ls HiggsAnalysis/
	#find /root/ -name 'CombinedLimit'
	#cd HiggsAnalysis/CombinedLimit
	#git fetch origin
	#git checkout v5.0.2
	#scramv1 b clean; scramv1 b

	#cd ../../../..
	cd ${SPAWNPOINT}
	pwd

	
# 	cp /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tH_comb_${1}.txt . 
# 	cp /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tHq_merge.root . 
# 	cp /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tH_?m_${1}.root .
# 	cp /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tH_?m_${1}.txt .
	
	cp /portal/ekpcms6/home/dschaefer/CMSSW_7_1_5/src/DijetCombineLimitCode/datacards/CMS_jj_BulkWW_${1}_w0p0_13TeV_CMS_jj_VVHP.txt .
	cp /portal/ekpcms6/home/dschaefer/CMSSW_7_1_5/src/DijetCombineLimitCode/workspaces/CMS_jj_BulkWW_${1}_w0p0_13TeV.root .
	cp /storage/jbod/dschaefer/fullCLs/merge_${1}.root .

	/portal/ekpcms6/home/dschaefer/CMSSW_7_1_5/bin/slc6_amd64_gcc481/combine CMS_jj_BulkWW_${1}_*.txt -M HybridNew --setPhysicsModelParameterRanges r=0,1500 --rMax 1500 --freq ${@:2} > limit_result.txt
	ls
        cp higgsCombineTest.HybridNew.mH120* /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/	
	if [ "$#" -ne 4 ]; then
		cp limit_result.txt /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/limit_result_observed.txt	
	else	
		cp limit_result.txt /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/limit_result_${4}.txt
	fi
	

## end of script

	echo '### end of job ###'


