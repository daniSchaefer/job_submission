#!bin/bash

m=4000
#sp=(0.45  0.40  0.35  0.30  0.25  0.20  0.15  0.10  0.05)
#sp=(0.0 0.03 0.05 0.08 0.1 0.13 0.15 0.18 0.2 0.23 0.25 0.28 0.3 0.33 0.35 0.38)
sp=(0.01 0.02 0.04 0.06 0.07 0.09 0.12 0.14 0.16 0.17 0.19 0.21 0.22 0.24 0.26 0.27 0.29 0.31 0.32 0.34 0.36 0.37)

# cp /home/dschaefer/CMSSW_7_1_5/src/DijetCombineLimitCode/datacards/CMS_jj_BulkWW_${mas}_w0p0_13TeV_CMS_jj_VVHP.txt .datacard.txt
# cp /home/dschaefer/CMSSW_7_1_5/src/DijetCombineLimitCode/workspaces/CMS_jj_BulkWW_${mass}_w0p0_13TeV.root .
# cp /home/dschaefer/CMSSW_7_1_5/src/DijetCombineLimitCode/workspaces/CMS_jj_VVHP CMS_jj_bkg_13TeV.root .


for i in "${sp[@]}"
do
    echo "make toys for signal strengt $i"
    /portal/ekpcms6/home/dschaefer/CMSSW_7_1_5/bin/slc6_amd64_gcc481/combine -M HybridNew --frequentist -m $m -s -1 --singlePoint $i --saveToys --saveHybridResult  --testStat LHC -d datacard.txt --clsAcc 0 -T 500 --iterations 5 -n BulkWW_sp$i --fork 4 > result_M${m}_sp${i}.txt
    mv higgsCombineBulkWW_sp$i.HybridNew.mH$m.*.root higgsCombineBulkWW_sp$i.HybridNew.T500.mH$m.root
done


#calculate the fullCLs observed limit using the precalculated grid from above:

#combine datacard.txt -M HybridNew --freq --grid=all_merged.root --mass 3000 --setPhysicsModelParameterRanges r=0,1 > result_M${mass}_w0p0.txt

#calculate the fullCLs expected limit using the precalculated grid: for 0.5 get median, 0.16/0.84 to get the endpoints of 68% interval, 0.025/0.975 to get the 95% one

combine datacard.txt -M HybridNew --freq --grid=all_merged.root --expectedFromGrid 0.5 --mass 3000 >result_expected_M${mass}_w0p0.txt

#plot the test statistics distribution under the signal+background and background only hypothesis:
#python /home/dschaefer/CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/plotTestStatCLs.py --input all_merged.root --poi r --val all --mass 3000
