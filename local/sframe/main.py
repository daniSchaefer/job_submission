#!/usr/bin/python2.7
import sys
sys.path.append('/usr/users/dschaefer/how-to_jdl_creator/jdl_creator/')
sys.path.append('/usr/users/dschaefer/how-to_jdl_creator/jdl_creator/classes/')
from classes.JDLCreator import JDLCreator # import the class to create and submit JDL files
import numpy

def main():
    #jobs = JDLCreator('condocker')  #run jobs on condocker cloude site
    jobs = JDLCreator('condocker')
    jobs.wall_time = 10*60
    jobs.memory = 10 
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
    jobs.SetExecutable("job_calc.sh")  # set job script
    #build list of arguments
    arguments=[]
    
   
    arguments.append("testconfig.xml Summer16/ZprimeToWW_narrow_M-3000_13TeV-madgraph/ZprimeToWW_narrow_M-3000_13TeV-madgraph20170203_signal/170203_123700/0000/ flatTuple_1.root")
    #jobs.SetFolder('/usr/users/dschaefer/job_submission/local/sframe')  # set subfolder !!! you have to copy your job file into the folder
    jobs.SetArguments(arguments)              # write an JDL file and create folder f            # set arguments
    jobs.WriteJDL()                           # write an JDL file and create folder for log files



if __name__ == "__main__":
        main()



