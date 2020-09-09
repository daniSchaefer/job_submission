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
                                                                                            
        cd datacards                                                                                 
                                                                                       
        echo "datacard: ${2}"
        # form of statement to be committed:
        #combine datacards/CMS_jj_altBulkWW_2000_13TeV_CMS_jj_WWHP.txt -M Asymptotic -v2 -m 2000 -n BulkWW_M2000_alt --rMax 100 --rMin 0.000001
        
        echo "combine ${2}.txt -M Asymptotic -m ${5} -n test --rMax 100 --rMin 0.000001"
        
        combine ${2} -M Asymptotic -m ${5} -n test --rMax 100 --rMin 0.000001 
        mv  higgs*.root $6$7 

	echo '### end of job ###'
	
