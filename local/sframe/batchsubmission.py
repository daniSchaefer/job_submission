#! /usr/bin/python
import sys
import os
import optparse
sys.path.append('/usr/users/dschaefer/how-to_jdl_creator/jdl_creator/')
sys.path.append('/usr/users/dschaefer/how-to_jdl_creator/jdl_creator/classes/')
from classes.JDLCreator import JDLCreator # import the class to create and submit JDL files
import numpy
import tempfile
import platform
from copy import deepcopy
import subprocess

# check for python version
if platform.python_version() < "2.5.1":
  print "FATAL: you need a newer python version"
  sys.exit()

from multiprocessing import Process
import thread
import subprocess
import time
import shutil
import socket


# if ntuplizer trees are to be put into trees: python batchsubmission.py --sframe -j SignalMC_Summer16.py 
# or better yet: nohup python batchsubmission.py --sframe -j SignalMC_Summer16.py & 


class ConfigReader:
    model = []
    opt = []
    outDir=[]
    inDir =[]
    mass =[]
    masses =[]
    massmax=[]
    massmin=[]
    step=[]
    channel=[]
    purity=[]
    purities=[]
    channels=[]
    channel2=[]
    def __init__(self,filename):
        config = open(filename,'r')
        for i in config.readlines():
            if '#' in i: continue
            if 'model' in i: 
                self.model.append(  (i.split("=")[1]).split("\n")[0])
            if 'options' in i:
                self.opt .append( (i.split('"')[1]).split('"')[0])
            if 'inDir' in i:
                self.inDir .append( (i.split("=")[1]).split("\n")[0])
            if 'outDir' in i:
                self.outDir .append( (i.split("=")[1]).split("\n")[0])
            if 'masses' in i:
                self.mass .append( (i.split("=")[1]).split("\n")[0])
            if 'channels' in i:
                self.channel2 .append( (i.split("=")[1]).split("\n")[0])    
            if 'purities' in i:
                self.purity .append( (i.split("=")[1]).split("\n")[0])
            
            if 'massmax' in i:
                self.massmax .append( (i.split("=")[1]).split("\n")[0])
            if 'massmin' in i:
                self.massmin .append( (i.split("=")[1]).split("\n")[0])
            if 'step' in i:
                self.step .append( (i.split("=")[1]).split("\n")[0])
            if 'channel' in i:
                self.channel .append( (i.split("=")[1]).split("\n")[0])
        for l in self.mass:
            self.masses .append(l.split(','))
        for l in self.channel2:
            self.channels .append(l.split(','))
        for l in self.purity:
            self.purities .append(l.split(','))
        #print self.model
        #print self.opt
        #print self.inDir
        #print self.outDir
        #print self.mass
        #print self.masses


class XMLcreator:
    inputDir = ''  
    inputFile =''
    tmpJobDir =''
    typeName =''
    version =''
    def __init__(self,filename):
        jobOptionsFile=open(filename, 'r')
        command2=""
        for i in [o for o in jobOptionsFile.readlines()]:
            if ("#E" + "nd") in i : break
            command2+=i
        jobOptionsFile.close()
        exec command2
        self.userItems = userItems
        self.dataSets = dataSets
        self.path2xml= path2xml
        self.path2tmp = path2tmp
        self.outDir = outDir
        self.jobName =jobName
        self.cycleName = cycleName
        self.nEventsMax = nEventsMax
        self.nProcesses = nProcesses
        self.nFiles = nFiles
        self.hCPU = hCPU
        self.hVMEM = hVMEM
        self.postFix=postFix
        self.loadPacks = loadPacks
        self.loadLibs = loadLibs
        self.storage = storage
        self.path2ExoDir = path2ExoDir
        
        
    def makeXML(self,name,inputFile):
        a = inputFile.split('"')
        l = a[1].split('/')
        infilename =''
        for s in a:
            #print s
            if s.find('storage')==1: 
                infilename+=l[-1]+'"'
                continue
            infilename +=s+'"' 
        tmp = infilename.split('\n')
        self.inputFile = l[-1]
        s1,s2 = l[-1].split('.')
        for i in range(0,len(l)-1):
            self.tmpJobDir +=l[i]+"/"
        name1,name2,name3 = name.split('.')    
        self.xml = open(self.path2tmp+name,'w')
        self.xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        self.xml.write('<!DOCTYPE JobConfiguration PUBLIC "" "JobConfig.dtd">\n')
        self.xml.write('<JobConfiguration JobName="'+self.jobName+'" OutputLevel="INFO">\n')
        for lib in self.loadLibs:
            self.xml.write('<Library Name="'+lib +'" />\n') 
        for pack in self.loadPacks:
            self.xml.write('<Package Name="'+pack+'" />\n')
        self.xml.write('<Cycle Name="'+self.cycleName+'" OutputDirectory="" PostFix="'+self.postFix+'" ProofServer="lite" ProofWorkDir="" RunMode="LOCAL" TargetLumi="1.0">\n')
        self.xml.write('<InputData Lumi="0.0" NEventsMax="'+str(self.nEventsMax)+'" NEventsSkip="0" SkipValid="False" Version="'+s1+'" Type="'+name1 +'">\n')
        self.xml.write(tmp[0]+"\n")  
        self.xml.write('<InputTree Name="ntuplizer/tree" /> \n  <OutputTree Name="tree" /> \n </InputData> \n')
        self.xml.write('<UserConfig>\n')      
        for i in self.userItems:
             self.xml.write(' <Item Name="'+i[0]+'" Value="'+i[1]+'" />\n') 
        self.xml.write('</UserConfig> \n </Cycle> \n </JobConfiguration>')
        self.inputDir = self.storage+self.tmpJobDir
        self.typeName = name1
        self.version = s1

 
 
def writeJDL(arguments,mem,time,name):
    #jobs = JDLCreator('condocker')  #run jobs on condocker cloude site
    jobs = JDLCreator('condocker')
    jobs.wall_time = time
    jobs.memory = mem 
    jobs.requirements = "(TARGET.ProvidesCPU) && (TARGET.ProvidesEkpResources)"
    ##################################
    ## submit job to set up CMSSW 
    ##################################
    #jobs.SetExecutable("job_setup.sh")  # set job script
    #jobs.SetArguments(' ')              # set arguments
    #jobs.SetFolder('../setup/')         # set subfolder !!! you have to copy your job file into the folder


    ##################################
    # submit job to run combine
    ##################################
    jobs.SetExecutable(name)  # set job script
    #jobs.SetFolder('/usr/users/dschaefer/job_submission/local/sframe')  # set subfolder !!! you have to copy your job file into the folder
    jobs.SetArguments(arguments)              # write an JDL file and create folder f            # set arguments
    jobs.WriteJDL()                           # write an JDL file and create folder for log files

        
def calcSframeTrees(joboptions):
    parser = XMLcreator(jobOptions)
    counter=0
    arguments=[]
    Njobs=0
    haddList=[]
    finalName=[]
    
    # arg1 = name of .xml file for this job 
    # arg2 = ordner to copy input file from
    # arg3 = temoporary dir to copy input file into
    # arg4 = name of input file to be copied
    # arg5 = name of output OutputDirectory
    #
    tmplist=[]
    tmpTypeName="tmp"
    for dset in parser.dataSets:
        filedset = open(parser.path2xml+dset[1][0],'r')
        for line in filedset:
            counter+=1
            parser.makeXML(dset[0]+parser.postFix+"_"+str(counter)+".xml",line)
            #print parser.inputDir
            arguments.append(dset[0]+parser.postFix+"_"+str(counter)+".xml"+" "+parser.storage+" "+parser.tmpJobDir+" "+parser.inputFile+" "+parser.outDir+ " "+parser.path2ExoDir+" "+parser.path2tmp)
            print parser.tmpJobDir
            
            parser.tmpJobDir =''
            print tmpTypeName
            if parser.typeName.find(tmpTypeName)==-1:
                if len(tmplist)!=0:
                    haddList.append(tmplist)
                tmplist=[]
                finalName.append(parser.outDir+parser.cycleName+"."+parser.typeName+parser.postFix+".root")
            tmplist.append(parser.outDir+parser.cycleName+"."+parser.typeName+"."+parser.version+parser.postFix+".root")
            tmpTypeName = parser.typeName
    haddList.append(tmplist)
    #finalName.append(parser.outDir+parser.cycleName+"."+parser.typeName+parser.postFix+".root")
    Njobs = counter
    writeJDL(arguments,3000,30*60,"job_calc.sh")
    command = "condor_submit JDL_job_calc"
    process = subprocess.Popen(command,shell=True)
    
    waitForBatchJobs("job_calc")
    
    
    i=0
    ts=""
    for s in finalName:
        haddString =""
        ts = ""
        for h in haddList[i]:
            ts += h+" "
        i+=1
        haddString = "hadd -f "+s + " "+ts
        print haddList
        print haddString 
        os.system(haddString)
    if not options.saveTmp:
        tmp = ""
        for l in haddList:
            for h in l:
                print "rm "+h
                tmp+=h+ " "
        #os.system("rm -f "+tmp)
            #print haddList
    

def waitForBatchJobs(nameJobFile):
    timeCheck = 10 #delay for process check
    while (True):
        time.sleep(timeCheck)
        proc = subprocess.Popen(["(condor_q dschaefer | grep "+nameJobFile+" )"], stdout=subprocess.PIPE, shell=True)
        (query, err) = proc.communicate()
        print "program output:", query
        if query.find("dschaefer")==-1:
            break
        listOfJobs = query.split('\n')
        #print listOfJobs
        jobID=[]
        numberRunningJobs=[]
        numberJobs=[]
        numberIdleJobs=[]
        numberHeldJobs=[]

        for i in range(0,len(listOfJobs)-1):
            tmp = listOfJobs[i].split(' ')
            #print tmp
            add =0
            if tmp[-2]=="...":
                add = -3
            numberRunningJobs.append(tmp[-14+add])
            numberJobs.append(tmp[-2+add])
            numberIdleJobs.append(tmp[-8+add])
            jobID.append(tmp[-1])
            numberHeldJobs.append(tmp[-4+add])
        
            print "number of submitted jobs : "+numberJobs [i]   
            print "number of idle jobs :      "+numberIdleJobs[i]
            print "number of running jobs :   "+numberRunningJobs[i]
            print "number of held jobs :      "+numberHeldJobs[i]
        #print jobID[i]
    

def doInterpolation(config):
    print "starting interpolation jobs"
    reader = ConfigReader(config)
    arguments =[]
    for i in range(0,len(reader.model)):
        print "use model " +reader.model[i]
        outfilename = reader.model[i]+"_VV"
        if "Qstar" in reader.model[i]:
            outfilename = reader.model[i]+"_qV"
        if "Data" in reader.model[i]:
            outfilename = "ReRecoData_VVdijet"
        if "Data" in reader.model[i] and "q" in reader.model[i]:
            outfilename = "ReRecoData_qVdijet"
        if "QCD" in reader.model[i] and "madgraph" in reader.model[i]:
            outfilename = "QCD_madgraph_pythia8"
        if "QCD" in reader.model[i] and "pythia" in reader.model[i]:
            outfilename = "QCD_pythia8"
        if "QCD" in reader.model[i] and "herwig" in reader.model[i]:
            outfilename = "QCD_herwig"
        if "QCD" in reader.model[i] and "Summer16" in reader.inDir[i]:
            outfilename += "_summer16"
            
        
        if "SB" in reader.model[i]:
            outfilename+="_SB"
        outfilename+=".root"
        for j in range(0,len(reader.masses[i])):
            print "use masses" + reader.masses[i][j]
            arguments.append(reader.model[i]+" "+reader.masses[i][j]+" "+reader.opt[i]+" "+reader.inDir[i]+" "+reader.outDir[i]+" "+outfilename)
    writeJDL(arguments,30,10*60,"interpolate.sh")
    command = "condor_submit JDL_interpolate"
    process = subprocess.Popen(command,shell=True)
    waitForBatchJobs("interpolate.sh")
    
    arguments=[]
    for i in range(0,len(reader.model)):
        for m in range(0,int((int(reader.massmax[i])-int(reader.massmin[i]))/100.)):
            #print m*100+int(reader.massmin[i])
            arguments.append(reader.model[i]+" "+str(m*100+int(reader.massmin[i]))+" "+reader.outDir[i])
    writeJDL(arguments,30,10*60,"interpolate2.sh")
    command = "condor_submit JDL_interpolate2"
    process = subprocess.Popen(command,shell=True)
    waitForBatchJobs("interpolate2.sh")
    samplemin=1
    samplemax=10
    for i in range(0,len(reader.model)):
        suffix = "VV"
        if "Zprime" in reader.model[i]:
            samplemin=7
            samplemax=8
        if "Wprime" in reader.model[i]:
            samplemin=8
            samplemax=9
        if "BulkWW" in reader.model[i]:
            samplemin=5
            samplemax=6
        if "BulkZZ" in reader.model[i]:
            samplemin=6
            samplemax=7
        if "QstarQW" in reader.model[i]:
            samplemin=3
            samplemax=4
            suffix="qV"
        if "QstarQZ" in reader.model[i]:
            samplemin=4
            samplemax=5
            suffix="qV"
        # mini tree produce takes all masses! might not work if not all masses are interpolated!    
        command2 = 'root -b -q "/usr/users/dschaefer/CMSSW_7_4_7/src/DijetCombineLimitCode/MiniTreeSignalProducer'+suffix+'13TeV.C('+str(samplemin)+','+str(samplemax)+')"'
        print command2
        os.system(command2)
    
    return 0


def makeDatacards(config):
    reader = ConfigReader(config)
    arguments=[]
    chan =1
    sample=2
    for i in range(0,len(reader.model)):
        if "prime" in reader.model[i]:
            sample =2
        if "Bulk" in reader.model[i]:
            sample = 4
        if "q" in reader.model[i] or "Q" in reader.model[i]:
            sample = 6
        if "RS" in reader.model[i]:
            sample =0
        if "qV" in reader.channel[i]:
            chan= 2
        for m in range(0,int((int(reader.massmax[i])-int(reader.massmin[i]))/100.)):
            #print m*100+int(reader.massmin[i])
            arguments.append(str(m*100+int(reader.massmin[i]))+" "+str(sample)+" "+str(chan)+" "+reader.opt[i]+" "+reader.channel[i]+ " "+reader.inDir[i]+" "+reader.model[i]+" /usr/users/dschaefer/SFrame_setup/ExoDiBosonAnalysis/forSystematics/")
    writeJDL(arguments,30,10*60,"datacards.sh")
    print arguments
    command = "condor_submit JDL_datacards"
    process = subprocess.Popen(command,shell=True)
    waitForBatchJobs("datacards.sh")
    
    
def calcLimits(config):
        # $1 input directory i.e. path to DijetCombineLimitCode
	# $2 name of datacard
	# $3 name of workspace
	# $4 name of background workspace
	# $5 mass of the resonance
	# $6 output directory
	# $7 name of output file
    reader = ConfigReader(config)
    arguments=[]
    for i in range(0,len(reader.model)):
        for c in reader.channels[i]:
            for p in reader.purities[i]:
                for m in range(0,int((int(reader.massmax[i])-int(reader.massmin[i]))/100.)):
                    if "new" in c:
                        print " datacards must be combined: start CombineDatacards.py"
                        os.system("python CombineDatacards.py --batch --signal "+reader.model[i]+" --mass "+mass+" --path "+reader.inDir[i] )
                    mass = str(m*100+int(reader.massmin[i]))
                    datacard = "CMS_jj_"+reader.opt[i]+reader.model[i]+"_"+mass+"_13TeV_CMS_jj_"+c+p+".txt"
                    workspace = "CMS_jj_"+reader.opt[i]+reader.model[i]+"_"+mass+"_13TeV.root"
                    bkgworkspace = "CMS_jj_bkg_"+reader.channel[i]+reader.opt[i]+"_13TeV.root"
                    outputname = "CMS_jj_"+mass+"_"+reader.opt[i]+reader.model[i]+"_13TeV_CMS_jj_"+c+p+"_asymptoticCLs_new.root"
                    arguments.append(reader.inDir[i]+" "+datacard+" "+workspace+" "+bkgworkspace+" "+mass+" "+reader.outDir[i]+" "+outputname)
    writeJDL(arguments,30,10*60,"limits.sh")
    command = "condor_submit JDL_limits"
    process = subprocess.Popen(command,shell=True)
    waitForBatchJobs("limits.sh")

        
if __name__=="__main__":
    optparser=optparse.OptionParser(usage="%prog -j jobOption.py")
    optparser.add_option("-j", "--jobOptions", dest="jobOptions",
                    action="store", default="Datasets.py",
                    help="joboptions to process [default = %default]")
    optparser.add_option("-s", "--saveTmp", dest="saveTmp",
                    action="store_true", default=False,
                    help="save temporary output files [default = %default]")
    
    optparser.add_option("-n", "--sframe", dest="sframe",
                    action="store_true", default=False,
                    help="do first analysis step i.e. calculate trees from ntuplizer trees [default = %default]")
    optparser.add_option("-a", "--all", dest="ALL",
                    action="store_true", default=False,
                    help="do everything from beginning to end !needs right joboptions file! [default = %default]")
    optparser.add_option("-c", "--combine", dest="combine",
                    action="store_true", default=False,
                    help="calculate the limits only [default = %default]")
    optparser.add_option("-w", "--workspaces", dest="workspaces",
                    action="store_true", default=False,
                    help="calculate workspaces and datacards for limit setting [default = %default]")
    optparser.add_option("-i", "--interpolate", dest="interpolate",
                    action="store_true", default=False,
                    help="interpolate trees for limit setting [default = %default]")
    
    
    (options, args)=optparser.parse_args()
    jobOptions=options.jobOptions
    
    
    if options.sframe:
        calcSframeTrees(jobOptions)
    
    if options.interpolate:
        doInterpolation("interpolation.cfg")
        
    if options.workspaces:
        makeDatacards("datacards.cfg")
    
    if options.combine:
        calcLimits("datacards.cfg")
        
    if options.ALL:
        calcSframeTrees(jobOptions)
        doInterpolation("interpolation.cfg")
        makeDatacards("datacards.cfg")
        calcLimits("datacards.cfg")
        
    
    
    
    
    
    
    
    
