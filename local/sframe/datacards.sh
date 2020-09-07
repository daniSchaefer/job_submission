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
	
	
	# copy needed files:
	cp -r $6/qv_models_Bkg_13TeV.rs .
        cp -r $6/vv_models_Bkg_13TeV.rs .
        cp -r $6/qv_altmodels_Bkg_13TeV.rs .
        cp -r $6/vv_altExpvv_models_Bkg_13TeV.rs .
        cp -r $6/vv_altvv_models_Bkg_13TeV.rs .
	
	# $1 = mass
	# $2 = sample
	# $3 = channel
	# $4 = alternative fit function
	# $5 = VV or qV case
	# $6 = inputdir
	# $7 = model name
	# $8 = ExoVV directory
	
	if [ $5 = "VV" ]
	then
            if [ $4 = "meep" ]
            then
               
	       root -b -q "$6/X2VVFitter.cc($1,$2,$3)"
               python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $7  --path $8 --outpath $6  --purity HP --channel WW
               python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $7  --path $8 --outpath $6  --purity LP --channel WW
               python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $7  --path $8 --outpath $6  --purity HP --channel WZ
               python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $7  --path $8 --outpath $6  --purity LP --channel WZ
               python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $7  --path $8 --outpath $6  --purity HP --channel ZZ
               python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $7  --path $8 --outpath $6  --purity LP --channel ZZ
               python ${6}implement-tau21PtUnc.py --signal $7 -m $1 --batch --path $6 
               python ${6}implement-tau21SFUnc.py --signal $7 -m $1 --batch --path $6 
               
            else
               root -b -q "$6/X2VVFitter.cc($1,$2,$3,\""$4\"")"
               python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $4$7  --path $8 --outpath $6  --purity HP --channel WW
               python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $4$7  --path $8 --outpath $6  --purity LP --channel WW
               python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $4$7  --path $8 --outpath $6  --purity HP --channel WZ
               python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $4$7  --path $8 --outpath $6  --purity LP --channel WZ
               python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $4$7  --path $8 --outpath $6  --purity HP --channel ZZ
               python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $4$7  --path $8 --outpath $6  --purity LP --channel ZZ
               python ${6}implement-tau21PtUnc.py --signal $4$7 -m $1 --batch --path $6 
               python ${6}implement-tau21SFUnc.py --signal $4$7 -m $1 --batch --path $6 
            fi
    
    
        fi
        if [ $5 = "qV" ]
        then 
        
            if [ $4 = "meep" ]
            then
                root -b -q "$6/X2qVFitter.cc($1,$2,$3)" 
           
                python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $7  --path $8 --outpath $6  --purity HP --channel qW
                python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $7  --path $8 --outpath $6  --purity LP --channel qW
                python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $7  --path $8 --outpath $6  --purity HP --channel qZ
                python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $7  --path $8 --outpath $6  --purity LP --channel qZ
                python ${6}implement-tau21PtUnc.py --signal $7 -m $1 --batch --path $6
                python ${6}implement-tau21SFUnc.py --signal $7 -m $1 --batch --path $6 
                
            
            else
                root -b -q "$6/X2qVFitter.cc($1,$2,$3,\\"$4\\")" 
           
                python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $4$7  --path $8 --outpath $6  --purity HP --channel qW
                python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $4$7  --path $8 --outpath $6  --purity LP --channel qW
                python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $4$7  --path $8 --outpath $6  --purity HP --channel qZ
                python ${6}implement-JESJMRsystematics.py --batch  --mass $1 --signal $4$7  --path $8 --outpath $6  --purity LP --channel qZ
                python ${6}implement-tau21PtUnc.py --signal $4$7 -m $1 --batch --path $6
                python ${6}implement-tau21SFUnc.py --signal $4$7 -m $1 --batch --path $6 
                
            fi
            
        fi
        # implement uncertainties:
        
        
        
	
	echo '### end of job ###'

                             
