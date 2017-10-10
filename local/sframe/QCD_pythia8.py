#! /usr/bin/python
# -*- coding: utf-8 -*-
path2xml="xml/Bkg/"
path2tmp="/usr/users/dschaefer/job_submission/local/sframe/AnalysisTemp/"
path2ExoDir="/usr/users/dschaefer/SFrame_setup/ExoDiBosonAnalysis"
storage="/storage/b/psi_data/"
outDir="/storage/jbod/dschaefer/AnalysisOutput/80X/Bkg/Summer16/"
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
postFix = ".VV_for2DFit" 

dataSets=[
   
     #["QCD_Pt_300to470_ext",["QCD_Pt_300to470_ext_part0.xml"]],
     #["QCD_Pt_300to470",["QCD_Pt_300to470_part0.xml"]],
    
    #["QCD_Pt_470to600_ext", ["QCD_Pt_470to600_ext_part0.xml"]],
    #["QCD_Pt_470to600_ext1",["QCD_Pt_470to600_ext_part1.xml"]],
    #["QCD_Pt_470to600",     ["QCD_Pt_470to600_part0.xml"]],
    
    #["QCD_Pt_800to1000_ext", ["QCD_Pt_800to1000_ext_part0.xml"]],
    #["QCD_Pt_800to1000",     ["QCD_Pt_800to1000_part0.xml"]],
    
    #["QCD_Pt_1400to1800_ext", ["QCD_Pt_1400to1800_ext_part0.xml"]],
    #["QCD_Pt_1400to1800",     ["QCD_Pt_1400to1800_part0.xml"]],
    
    #["QCD_Pt_2400to3200_ext", ["QCD_Pt_2400to3200_ext_part0.xml"]],
    #["QCD_Pt_2400to3200",     ["QCD_Pt_2400to3200_part0.xml"]],
    
    #["QCD_Pt_3200toInf_ext", ["QCD_Pt_3200toInf_ext_part0.xml"]],
    #["QCD_Pt_3200toInf",     ["QCD_Pt_3200toInf_part0.xml"]],
    
    #["QCD_Pt_600to800_ext", ["QCD_Pt_600to800_ext_part0.xml"]],
    #["QCD_Pt_600to800",     ["QCD_Pt_600to800_part0.xml"]],
 
    #["QCD_Pt_1800to2400_ext", ["QCD_Pt_1800to2400_ext_part0.xml"]],
    #["QCD_Pt_1800to2400",   ["QCD_Pt_1800to2400_part0.xml"]],

    
  ]

userItems = [ 
  ["Channel","VVdijet_for2Dfit"], #jetmassSidebandqVdijet
  ["MassWindow","VV"],
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

