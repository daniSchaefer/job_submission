#! /usr/bin/python
# -*- coding: utf-8 -*-
path2xml="xml/"
path2tmp="/usr/users/dschaefer/job_submission/local/sframe/AnalysisTemp/"
path2ExoDir="/usr/users/dschaefer/SFrame_setup/HadronicVV/TreeAnalyzer/"
storage="/storage/b/psi_data/"
#outDir="/storage/jbod/dschaefer/AnalysisOutput/80X/2Dfit/"
outDir="/storage/b/psi_data/"
# ============== for systematics ===================================
#outDir="/shome/dschafer/AnalysisOutput/80X/SignalMC/Summer16/Sys/"
# ==================================================================
jobName="VVanalysisJob"
cycleName="VVanalysis"
nEventsMax=-1
nProcesses=2
nFiles=1
hCPU="00:30:00"
hVMEM="3000M"
postFix = ".tau21Order"               

dataSets=[
 ["QCD_pythia_1000to1400",["QCD_PtQCD_MPt_1000to1400.xml"]],
 ["QCD_pythia_1400to1800",["QCD_PtQCD_MPt_1400to1800.xml"]],
 ["QCD_pythia_1800to2400",["QCD_PtQCD_MPt_1800to2400.xml"]],
 ["QCD_pythia_2400to3200",["QCD_PtQCD_MPt_2400to3200.xml"]],
# ["QCD_pythia_300to470",["QCD_PtQCD_MPt_300to470.xml"  ]],
# ["QCD_pythia_3200toInf",["QCD_PtQCD_MPt_3200toInf.xml" ]],
# ["QCD_pythia_470to600",["QCD_PtQCD_MPt_470to600.xml"  ]],
# ["QCD_pythia_600to800",["QCD_PtQCD_MPt_600to800.xml"  ]],
# ["QCD_pythia_800to1000",["QCD_PtQCD_MPt_800to1000.xml" ]],

    
    #summer16 herwig pp
# ["QCD_herwigpp",["herwigQCD_MPt-15to7000.xml"]], 
        


#summer16 W plus jets samples
    #["WJetsToQQ",["WJetsToQQ.xml"]],
  #  ["ZJetsToQQ",["ZJetsToQQ.xml"]],
]

userItems = [ 
  ["Channel","qVdijet_for2Dfit"],
  ["IsSignal","false"],
  ["IsData","false"],
]  

jobOptionsFile2=open("AnalysisOptions_3DFit.py", 'r')
command2=""
for i in [o for o in jobOptionsFile2.readlines()]:
  if ("#E" + "nd") in i : break
  command2+=i
jobOptionsFile2.close()
exec command2
userItems += AddUserItems

inputTrees=["ntuplizer/tree"]
outputTrees=["tree"]
