#! /usr/bin/python
# -*- coding: utf-8 -*-
path2xml="xml/"
path2tmp="/usr/users/dschaefer/job_submission/local/sframe/AnalysisTemp/"
path2ExoDir="/usr/users/dschaefer/SFrame_setup/ExoDiBosonAnalysis"
storage="/storage/b/psi_data/"
outDir="/storage/jbod/dschaefer/AnalysisOutput/80X/test/ptordered/"
# ============== for systematics ===================================
#outDir="/shome/dschafer/AnalysisOutput/80X/SignalMC/Summer16/Sys/"
# ==================================================================
jobName="exovvJob"
cycleName="ExoDiBosonAnalysis"
nEventsMax=-1
nProcesses=2
nFiles=1
hCPU="00:30:00"
hVMEM="3000M"
postFix = ".qV_for2Dfit" 

dataSets=[

     # these sets are on storage/b/psi_data

     ["QCD_HT2000toInf",  ["madgraphQCD_MHT2000toInf.xml"]],
     ["QCD_HT1500to2000", ["madgraphQCD_MHT1500to2000.xml"]],
     ["QCD_HT1000to1500", ["madgraphQCD_MHT1000to1500.xml"]],
    
    # rest is on jbod directory!
    
    #["QCD_HT100to200", ["QCD_HT100to200.xml"]],
    #["QCD_HT200to300", ["QCD_HT200to300.xml"]],
    #["QCD_HT200to300_part2", ["QCD_HT200to300_part2.xml"]],
    #["QCD_HT300to500", ["QCD_HT300to500.xml"]],
    #["QCD_HT300to500_part2", ["QCD_HT300to500_part2.xml"]],
    #["QCD_HT500to700", ["QCD_HT500to700.xml"]],
    #["QCD_HT500to700_part2", ["QCD_HT500to700_part2.xml"]],
    #["QCD_HT500to700_part3", ["QCD_HT500to700_part3.xml"]],
    #["QCD_HT700to1000", ["QCD_HT700to1000.xml"]],
    #["QCD_HT700to1000_part2", ["QCD_HT700to1000_part2.xml"]],
    #["QCD_HT1000to1500", ["QCD_HT1000to1500.xml"]],
    #["QCD_HT1500to2000", ["QCD_HT1500to2000.xml"]],
    #["QCD_HT2000toInf", ["QCD_HT2000toInf.xml"]],
        
  ]

userItems = [ 
  ["Channel","qVdijet_for2Dfit"], #jetmassSidebandqVdijet
  ["MassWindow","qV"],
  ["isSignal","false"],
  ["runOnMC","true"],
  ["Trigger","false"],
  ["applyFilters","false"],
  ["scaleUncPar" ,""],
  ["MjjCut","1050.0"] # Mjj cut 1050.0 for double tag region and 1050.0 for single tag region, 1080 for no tag region
]  

jobOptionsFile2=open("AnalysisOptions_80X.py", 'r')
command2=""
for i in [o for o in jobOptionsFile2.readlines()]:
  if ("#E" + "nd") in i : break
  command2+=i
jobOptionsFile2.close()
exec command2
userItems += AddUserItems

inputTrees=["ntuplizer/tree"]
outputTrees=["tree"]

