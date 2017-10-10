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
	cd ${1}../..
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
	mkdir datacards                                                                                         
        mkdir workspaces                                                                                        
        cp ${1}/datacards/${2} datacards/  
        cp ${1}/workspaces/${3} workspaces/
        cp ${1}/workspaces/${4} workspaces/ 
        
        # 1 = directory of DijetCombineLimitCode
        # 2 = name of datacard
        # 3 = name of signal workspace
        # 4 = name of background workspace
        # 5 = mass
        # 6 = output directory
        # 7 = signal strenght for toy
        # 8 = model
                                                                                            
        cd datacards                                                                                 
                                                                                       
        echo "datacard: ${2}"
        # form of statement to be committed:
        #combine datacards/CMS_jj_altBulkWW_2000_13TeV_CMS_jj_WWHP.txt -M Asymptotic -v2 -m 2000 -n BulkWW_M2000_alt --rMax 100 --rMin 0.000001
                
        echo "make toys for signal strengt $7"
        echo "combine -M HybridNew --frequentist -m ${5} -s -1 --singlePoint $7 --saveToys --saveHybridResult  --testStat LHC -d $2 --clsAcc 0 -T 1000 --iterations 5 -n ${8}_sp${7} --fork 4 "
        combine -M HybridNew --frequentist -m ${5} -s -1 --singlePoint $7 --saveToys --saveHybridResult  --testStat LHC -d $2 --clsAcc 0 -T 500 --iterations 5 -n ${8}_sp${7} -v 2 #--fork 4
        ls
        mv  higgsCombine*.root /usr/users/dschaefer/CMSSW_7_4_7/src/DijetCombineLimitCode/Limits/toys2
	echo '### end of job ###'
	
