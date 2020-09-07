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
	SCRAM_ARCH=slc6_amd64_gcc530
	cd /portal/ekpbms2/home/dschaefer/CMSSW_8_1_0/src/
 	# go to CMSSW installation folder
	#cd CMSSW_7_1_5/src
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
        
        # 1 = directory of DijetCombineLimitCode
        # 2 = name of workspace
        # 3 = output directory
        # 4 = mass
        # 5 = signal strenght for toy
        # 6 = output name
        # 7 = number of toys
                                                                                            
        cd datacards                                                                                 
                                                                                       
        echo "datacard: ${2}"
        # form of statement to be committed:
        #combine datacards/CMS_jj_altBulkWW_2000_13TeV_CMS_jj_WWHP.txt -M Asymptotic -v2 -m 2000 -n BulkWW_M2000_alt --rMax 100 --rMin 0.000001
                
        echo "make toys for signal strengt $7"
        echo "combine -M HybridNew -m ${4} -s -1 --singlePoint $5 --saveToys --saveHybridResult  --LHCmode LHC-limits --clsAcc 0 -T $7 --iterations $7 -n $6 $2 "
        combine -M HybridNew -t $7 -m ${4} -s -1 --singlePoint $5 --saveToys --saveHybridResult  --LHCmode LHC-limits --clsAcc 0 --frequentist --newToyMCSampler 1 --cminPoiOnlyFit -n $6 $2 #--fork 4
        ls
        #time combine workspace_JJ_HPHP_13TeV_2017.root -M HybridNew --testStat LHC --singlePoint 1.025 --saveToys --saveHybridResult -t 1 --clsAcc 0 --frequentist --newToyMCSampler 1 -m 3600 -n test3600_6 -v3 -s -1 --cminPoiOnlyFit
        mv  higgsCombine*.root $3
	echo '### end of job ###'
	
	
	
