path2xml="xml/"
path2tmp="/usr/users/dschaefer/job_submission/local/sframe/AnalysisTemp/"
path2ExoDir="/usr/users/dschaefer/SFrame_setup/ExoDiBosonAnalysis"
storage="/storage/b/psi_data/"
outDir="/storage/jbod/dschaefer/AnalysisOutput/80X/test/"
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
postFix = ".qVdijet_for2Dfit"      

dataSets=[

    #["Data1",          ["Data1_part1.xml"]],
    #["Data1_part2",    ["Data1_part2.xml"]],     
    #["Data1_part3",    ["Data1_part3.xml"]],                          
    #["Data1_part4",    ["Data1_part4.xml"]],                          
    #["Data1_part5",    ["Data1_part5.xml"]],                          
    #["Data1_part6",    ["Data1_part6.xml"]],                          
    #["Data1_part7",    ["Data1_part7.xml"]],                          
    #["Data1_part8",    ["Data1_part8.xml"]],                          
                                                                      
    ["Data2",          ["Data2_part1.xml"]],                          
    ["Data2_part2",    ["Data2_part2.xml"]],                          
    ["Data2_part3",    ["Data2_part3.xml"]],                          
                                                                      
    ["Data3",          ["Data3_part1.xml"]],                          
    ["Data3_part2",    ["Data3_part2.xml"]],                          
    ["Data3_part3",    ["Data3_part3.xml"]],                          
    ["Data3_part4",    ["Data3_part4.xml"]],                          
    ["Data3_part5",    ["Data3_part5.xml"]],                          
                                                                      
    ["Data4",          ["Data4_part1.xml"]],                          
    ["Data4_part2",    ["Data4_part2.xml"]],                         
    ["Data4_part3",    ["Data4_part3.xml"]],                         
    ["Data4_part4",    ["Data4_part4.xml"]],                          
                                                                      
    ["Data5",          ["Data5_part1.xml"]],                          
    ["Data5_part2",    ["Data5_part2.xml"]],                          
                                                                      
    ["Data6",          ["Data6_part1.xml"]],                          
                                                                     
    ["Data7",          ["Data7_part1.xml"]],                          
                                                                      
    #["Data8",          ["Data8_part1.xml"]],                          
    #["Data8_part2",    ["Data8_part2.xml"]],                          
    #["Data8_part3",    ["Data8_part3.xml"]],                          
    #["Data8_part4",    ["Data8_part4.xml"]],                          
    #["Data8_part5",    ["Data8_part5.xml"]],                          
    #["Data8_part6",    ["Data8_part6.xml"]],                          
    #["Data8_part7",    ["Data8_part7.xml"]],                          
                                                                      
    #["Data9",          ["Data9_part1.xml"]],                          
    #["Data9_part2",    ["Data9_part2.xml"]],                          
    #["Data9_part3",    ["Data9_part3.xml"]],                          
    #["Data9_part4",    ["Data9_part4.xml"]],                          
    #["Data9_part5",    ["Data9_part5.xml"]],                          
    #["Data9_part6",    ["Data9_part6.xml"]],
    #["Data9_part7",    ["Data9_part7.xml"]],
    
    #["Data10",    ["Data10_part1.xml"]],
    
    #["MC1000",    ["MC1000.xml"]],
  ]

userItems = [ 
  ["Channel","qVdijet_for2Dfit"],
  ["MassWindow","qV_for2Dfit"],
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
