#! /usr/bin/python
# -*- coding: utf-8 -*-
path2xml="xml/"
path2tmp="/usr/users/dschaefer/job_submission/local/sframe/AnalysisTemp/"
path2ExoDir="/usr/users/dschaefer/SFrame_setup/ExoDiBosonAnalysis"
storage="/storage/b/psi_data/"
outDir="/storage/jbod/dschaefer/AnalysisOutput/80X/Data/"
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
postFix = ".VVdijet"
                                                                         
dataSets=[
  #["JetHT_Run2016C",["JetHT_Run2016C_PromptReco-v2.xml"]],
  #["JetHT_Run2016D",["JetHT_Run2016D_PromptReco-v2.xml"]],
  #["JetHT_Run2016E",["JetHT_Run2016E_PromptReco-v2.xml"]],
  #["JetHT_Run2016F",["JetHT_Run2016F_PromptReco-v2.xml"]],
  #["JetHT_Run2016G_part1",["JetHT_Run2016G_PromptReco-v2_part1.xml"]],
  #["JetHT_Run2016G_part2",["JetHT_Run2016G_PromptReco-v2_part2.xml"]],
  #["JetHT_Run2016H_part1",["JetHT_Run2016H_PromptReco-v2_part1.xml"]],
  #["JetHT_Run2016H_part2",["JetHT_Run2016H_PromptReco-v2_part2.xml"]],
  
  





   
   #=============== xmls for Rereco dataset for Moriond 2017 ===========================
   #["JetHT_Run2016B_part1",["JetHT_Run2016B_0000_part0.xml"]],                                              
   #["JetHT_Run2016B_part2",["JetHT_Run2016B_0000_part1.xml"]],
   #["JetHT_Run2016B_part3",["JetHT_Run2016B_0000_part2.xml"]],
   #["JetHT_Run2016B_part4",["JetHT_Run2016B_0000_part3.xml"]],
   #["JetHT_Run2016B_part5",["JetHT_Run2016B_0001_part0.xml"]],
   #["JetHT_Run2016B_part6",["JetHT_Run2016B_0001_part1.xml"]],
   #["JetHT_Run2016B_part7",["JetHT_Run2016B_0001_part2.xml"]],
   #["JetHT_Run2016B_part8",["JetHT_Run2016B_0001_part3.xml"]],
   #["JetHT_Run2016B_part9",["JetHT_Run2016B_0002_part0.xml"]],
   #["JetHT_Run2016B_part10",["JetHT_Run2016B_0002_part1.xml"]],
   #["JetHT_Run2016B_part11",["JetHT_Run2016B_0002_part2.xml"]],
    ["JetHT_test",["Data.xml"]],
   
   
   
   #["JetHT_Run2016C_part1",["JetHT_Run2016C_0000_part0.xml"]],
   #["JetHT_Run2016C_part2",["JetHT_Run2016C_0000_part1.xml"]],
   #["JetHT_Run2016C_part3",["JetHT_Run2016C_0000_part2.xml"]],
   
    #["JetHT_Run2016D_part1",["JetHT_Run2016D_0000_part0.xml"]],
    #["JetHT_Run2016D_part2",["JetHT_Run2016D_0000_part1.xml"]],
    #["JetHT_Run2016D_part3",["JetHT_Run2016D_0000_part2.xml"]],
    #["JetHT_Run2016D_part4",["JetHT_Run2016D_0000_part3.xml"]],
    #["JetHT_Run2016D_part5",["JetHT_Run2016D_0001_part0.xml"]],
    #["JetHT_Run2016D_part6",["JetHT_Run2016D_0001_part1.xml"]],

    #["JetHT_Run2016E_part1",["JetHT_Run2016E_0000_part0.xml"]],
    #["JetHT_Run2016E_part2",["JetHT_Run2016E_0000_part1.xml"]],
    #["JetHT_Run2016E_part3",["JetHT_Run2016E_0000_part2.xml"]],
    #["JetHT_Run2016E_part4",["JetHT_Run2016E_0000_part3.xml"]],
    #["JetHT_Run2016E_part5",["JetHT_Run2016E_0001_part0.xml"]],


    #["JetHT_Run2016F_part1",["JetHT_Run2016F_0000_part0.xml"]],
    #["JetHT_Run2016F_part2",["JetHT_Run2016F_0000_part1.xml"]],
    #["JetHT_Run2016F_part3",["JetHT_Run2016F_0000_part2.xml"]],

    #["JetHT_Run2016G_part1",["JetHT_Run2016G_0000_part0.xml"]],
    #["JetHT_Run2016G_part2",["JetHT_Run2016G_0000_part1.xml"]],
    #["JetHT_Run2016G_part3",["JetHT_Run2016G_0000_part2.xml"]],
    #["JetHT_Run2016G_part4",["JetHT_Run2016G_0000_part3.xml"]],
    #["JetHT_Run2016G_part5",["JetHT_Run2016G_0001_part0.xml"]],
    #["JetHT_Run2016G_part6",["JetHT_Run2016G_0001_part1.xml"]],
    #["JetHT_Run2016G_part7",["JetHT_Run2016G_0001_part2.xml"]],
    #["JetHT_Run2016G_part8",["JetHT_Run2016G_0001_part3.xml"]],
    #["JetHT_Run2016G_part9",["JetHT_Run2016G_0002_part0.xml"]],

    #["JetHT_Run2016H_part1",["JetHT_Run2016H_0001_part0.xml"]],
    #["JetHT_Run2016H_part2",["JetHT_Run2016H_0001_part1.xml"]],
    #["JetHT_Run2016H_part3",["JetHT_Run2016H_0001_part2.xml"]],
    #["JetHT_Run2016H_part4",["JetHT_Run2016H_0001_part3.xml"]],
    #["JetHT_Run2016H_part5",["JetHT_Run2016H_0000_part0.xml"]],
    #["JetHT_Run2016H_part6",["JetHT_Run2016H_0000_part1.xml"]],
    #["JetHT_Run2016H_part7",["JetHT_Run2016H_0000_part2.xml"]],
    #["JetHT_Run2016H_part8",["JetHT_Run2016H_0000_part3.xml"]],
    #["JetHT_Run2016H_part9",["JetHT_Run2016H_0002_part0.xml"]],
    #["JetHT_Run2016H_part10",["JetHT_Run2016H_0002_part1.xml"]],

    #["JetHT_Run2016H_part11",["JetHT_Run2016Hpart2_0000_part0.xml"]],
    #["JetHT_Run2016H_part12",["JetHT_Run2016Hpart2_0000_part1.xml"]],
    #["JetHT_Run2016H_part13",["JetHT_Run2016Hpart2_0000_part2.xml"]],
    #["JetHT_Run2016H_part14",["JetHT_Run2016Hpart2_0000_part3.xml"]],


#=============== xmls for ReRereco Test ===========================
   #["JetHT_Run2016B_rerereco_part1",["JetHT_Run2016B_0000_part0.xml"]],                                              
   #["JetHT_Run2016B_rerereco_part2",["JetHT_Run2016B_0000_part1.xml"]],
   #["JetHT_Run2016B_rerereco_part3",["JetHT_Run2016B_0000_part2.xml"]],
   #["JetHT_Run2016B_rerereco_part4",["JetHT_Run2016B_0000_part3.xml"]],
   #["JetHT_Run2016B_rerereco_part5",["JetHT_Run2016B_0001_part0.xml"]],
   #["JetHT_Run2016B_rerereco_part6",["JetHT_Run2016B_0001_part1.xml"]],
   #["JetHT_Run2016B_rerereco_part7",["JetHT_Run2016B_0001_part2.xml"]],
   #["JetHT_Run2016B_rerereco_part8",["JetHT_Run2016B_0001_part3.xml"]],
   #["JetHT_Run2016B_rerereco_part9",["JetHT_Run2016B_0002_part0.xml"]],
   #["JetHT_Run2016B_rerereco_part10",["JetHT_Run2016B_0002_part1.xml"]],
   #["JetHT_Run2016B_rerereco_part11",["JetHT_Run2016B_0002_part2.xml"]],
   
]

userItems = [ 
  ["Channel","VVdijet"],
  ["MassWindow","VV"],
  ["isSignal","false"],
  ["runOnMC","false"],
  ["Trigger","true"], # put false to do trigger efficiency plots!
  ["applyFilters","true"],
  ["scaleUncPar" ,""],
  ["MjjCut","1050.0"] # Mjj cut 995.0 for double tag region and 1035.0 for single tag region, 1055 for no tag region
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
