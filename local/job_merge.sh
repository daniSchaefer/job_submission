#!/bin/bash

## setup CMSSW
	source $VO_CMS_SW_DIR/cmsset_default.sh
	SCRAM_ARCH=slc6_amd64_gcc481
	scramv1 project CMSSW_7_1_5
	cd CMSSW_7_1_5/src
	eval `scramv1 runtime -sh`

## test something
	#whoami
	id -u
    #cd /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/
    cd /storage/jbod/dschaefer/fullCLs/
    for file in *.tar ; do tar -xf $file ; done 
	ls
	hadd -f /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tHq_part_0_merge.root /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tH_comb.HybridNew.*.0*.root 
	hadd -f /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tHq_part_1_merge.root /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tH_comb.HybridNew.*.1*.root 
	hadd -f /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tHq_part_2_merge.root /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tH_comb.HybridNew.*.2*.root 
	hadd -f /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tHq_part_3_merge.root /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tH_comb.HybridNew.*.3*.root 
	hadd -f /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tHq_part_4_merge.root /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tH_comb.HybridNew.*.4*.root 
	hadd -f /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tHq_part_5_merge.root /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tH_comb.HybridNew.*.5*.root 
	hadd -f /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tHq_part_6_merge.root /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tH_comb.HybridNew.*.6*.root 
	hadd -f /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tHq_part_7_merge.root /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tH_comb.HybridNew.*.7*.root 
	hadd -f /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tHq_part_8_merge.root /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tH_comb.HybridNew.*.8*.root 
	hadd -f /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tHq_part_9_merge.root /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tH_comb.HybridNew.*.9*.root 



	hadd -f /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tHq_merge.root  /storage/a/mschnepf/tHq/13tev/full_workdir/${1}/tHq_part_?_merge.root
	

## end of script

	echo '### end of job ###'

