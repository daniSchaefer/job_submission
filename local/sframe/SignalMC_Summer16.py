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
    #["BulkWW_13TeV_600GeV",    ["BulkWW_M600.xml"]],
    #["BulkWW_13TeV_1000GeV",    ["BulkWW_M1000.xml"]],
    #["BulkWW_13TeV_1200GeV",    ["BulkWW_M1200.xml"]],
    #["BulkWW_13TeV_1400GeV",    ["BulkWW_M1400.xml"]],
    #["BulkWW_13TeV_1600GeV",    ["BulkWW_M1600.xml"]],
    #["BulkWW_13TeV_1800GeV",    ["BulkWW_M1800.xml"]],
    ["BulkWW_13TeV_2000GeV",    ["BulkWW_M2000.xml"]],
    #["BulkWW_13TeV_2500GeV",    ["BulkWW_M2500.xml"]],
    ##["BulkWW_13TeV_3000GeV",    ["BulkWW_M3000.xml"]],
    #["BulkWW_13TeV_3500GeV",    ["BulkWW_M3500.xml"]],
    #["BulkWW_13TeV_4000GeV",    ["BulkWW_M4000.xml"]],
    #["BulkWW_13TeV_4500GeV",    ["BulkWW_M4500.xml"]],
    
    ##["BulkZZ_13TeV_1000GeV",    ["BulkZZ_M1000.xml"]],
    #["BulkZZ_13TeV_1200GeV",    ["BulkZZ_M1200.xml"]],
    #["BulkZZ_13TeV_1400GeV",    ["BulkZZ_M1400.xml"]],
    #["BulkZZ_13TeV_1600GeV",    ["BulkZZ_M1600.xml"]],
    #["BulkZZ_13TeV_1800GeV",    ["BulkZZ_M1800.xml"]],
    #["BulkZZ_13TeV_2000GeV",    ["BulkZZ_M2000.xml"]],
    #["BulkZZ_13TeV_2500GeV",    ["BulkZZ_M2500.xml"]],
    #["BulkZZ_13TeV_3000GeV",    ["BulkZZ_M3000.xml"]],
    #["BulkZZ_13TeV_3500GeV",    ["BulkZZ_M3500.xml"]],
    #["BulkZZ_13TeV_4000GeV",    ["BulkZZ_M4000.xml"]],
    #["BulkZZ_13TeV_4500GeV",    ["BulkZZ_M4500.xml"]],
    
    #["ZprimeWW_13TeV_1000GeV",    ["ZprimeWW_M1000.xml"]],
    #["ZprimeWW_13TeV_1200GeV",    ["ZprimeWW_M1200.xml"]],
    #["ZprimeWW_13TeV_1400GeV",    ["ZprimeWW_M1400.xml"]],
    ##["ZprimeWW_13TeV_1600GeV",    ["ZprimeWW_M1600.xml"]],
    #["ZprimeWW_13TeV_1800GeV",    ["ZprimeWW_M1800.xml"]],
    #["ZprimeWW_13TeV_2000GeV",    ["ZprimeWW_M2000.xml"]],
    #["ZprimeWW_13TeV_2500GeV",    ["ZprimeWW_M2500.xml"]],
    #["ZprimeWW_13TeV_3000GeV",    ["ZprimeWW_M3000.xml"]],
    #["ZprimeWW_13TeV_3500GeV",    ["ZprimeWW_M3500.xml"]],
    #["ZprimeWW_13TeV_4000GeV",    ["ZprimeWW_M4000.xml"]],
    #["ZprimeWW_13TeV_4500GeV",    ["ZprimeWW_M4500.xml"]],
    
    #["WprimeWZ_13TeV_1000GeV",    ["WprimeWZ_M1000.xml"]],
    #["WprimeWZ_13TeV_1200GeV",    ["WprimeWZ_M1200.xml"]],
    #["WprimeWZ_13TeV_1400GeV",    ["WprimeWZ_M1400.xml"]],
    #["WprimeWZ_13TeV_1600GeV",    ["WprimeWZ_M1600.xml"]],
    #["WprimeWZ_13TeV_1800GeV",    ["WprimeWZ_M1800.xml"]],
    #["WprimeWZ_13TeV_2000GeV",    ["WprimeWZ_M2000.xml"]],
    #["WprimeWZ_13TeV_2500GeV",    ["WprimeWZ_M2500.xml"]],
    #["WprimeWZ_13TeV_3000GeV",    ["WprimeWZ_M3000.xml"]],
    #["WprimeWZ_13TeV_3500GeV",    ["WprimeWZ_M3500.xml"]],
    #["WprimeWZ_13TeV_4000GeV",    ["WprimeWZ_M4000.xml"]],
    #["WprimeWZ_13TeV_4500GeV",    ["WprimeWZ_M4500.xml"]],
    
    #["QstarQW_13TeV_1000GeV",    ["QstarQW_M1000.xml"]],
    #["QstarQW_13TeV_1200GeV",    ["QstarQW_M1200.xml"]],
    #["QstarQW_13TeV_1400GeV",    ["QstarQW_M1400.xml"]],
    #["QstarQW_13TeV_1600GeV",    ["QstarQW_M1600.xml"]],
    #["QstarQW_13TeV_1800GeV",    ["QstarQW_M1800.xml"]],
    #["QstarQW_13TeV_2000GeV",    ["QstarQW_M2000.xml"]],
    #["QstarQW_13TeV_2500GeV",    ["QstarQW_M2500.xml"]],
    #["QstarQW_13TeV_3000GeV",    ["QstarQW_M3000.xml"]],
    #["QstarQW_13TeV_3500GeV",    ["QstarQW_M3500.xml"]],
    #["QstarQW_13TeV_4000GeV",    ["QstarQW_M4000.xml"]],
    #["QstarQW_13TeV_4500GeV",    ["QstarQW_M4500.xml"]],
    #["QstarQW_13TeV_5000GeV",    ["QstarQW_M5000.xml"]],
    #["QstarQW_13TeV_6000GeV",    ["QstarQW_M6000.xml"]],
    #["QstarQW_13TeV_7000GeV",    ["QstarQW_M7000.xml"]],
    
     
    #["QstarQZ_13TeV_1000GeV",    ["QstarQZ_M1000.xml"]],
    #["QstarQZ_13TeV_1200GeV",    ["QstarQZ_M1200.xml"]],
    #["QstarQZ_13TeV_1400GeV",    ["QstarQZ_M1400.xml"]],
    #["QstarQZ_13TeV_1600GeV",    ["QstarQZ_M1600.xml"]],
    #["QstarQZ_13TeV_1800GeV",    ["QstarQZ_M1800.xml"]],
    #["QstarQZ_13TeV_2000GeV",    ["QstarQZ_M2000.xml"]],
    #["QstarQZ_13TeV_2500GeV",    ["QstarQZ_M2500.xml"]],
    #["QstarQZ_13TeV_3000GeV",    ["QstarQZ_M3000.xml"]],
    ##["QstarQZ_13TeV_3500GeV",   ["QstarQZ_M3500.xml"]],
    ##["QstarQZ_13TeV_4000GeV",   ["QstarQZ_M4000.xml"]],
    #["QstarQZ_13TeV_4500GeV",    ["QstarQZ_M4500.xml"]],
    ##["QstarQZ_13TeV_5000GeV",   ["QstarQZ_M5000.xml"]],
    #["QstarQZ_13TeV_6000GeV",    ["QstarQZ_M6000.xml"]],
    ##["QstarQZ_13TeV_7000GeV",   ["QstarQZ_M7000.xml"]],
    
    
    
  ]

userItems = [ 
  ["Channel","qVdijet_for2Dfit"],
  ["MassWindow","qV"],
  ["isSignal","true"],
  ["runOnMC","true"],
  ["Trigger","false"],
  ["applyFilters","false"],
  ["scaleUncPar" ,""],
  ["MjjCut","1050.0"], # Mjj cut 995.0 for double tag region and 1035.0 for single tag region, 1055 for no tag region
  #["PDFSET" ,""]
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
