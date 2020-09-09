#!/usr/bin/env python
import sys
sys.path.append('/usr/users/dschaefer/how-to_jdl_creator/jdl_creator/')
sys.path.append('/usr/users/dschaefer/how-to_jdl_creator/jdl_creator/classes/')
from classes.JDLCreator import JDLCreator
import numpy


# decide which signal strengt to use in the calculation from the asymptotic CLs limit calculation
def ListOfSteps(Number):
    #create list of signal strength from asymptotic
    min=0
    max=0
    #step=0.05
    step=0.005
    NumberPerJobs=1

    # filename of asymptotic limits
    AsymptoticFilename = "/home/dschaefer/CMSSW_7_1_5/src/DijetCombineLimitCode/Limits/higgsCombine_lim_" + str(Number) + "_had_HP_0.0_.Asymptotic.mH" + str(Number) +".txt"
    AsymptoticFile = open(AsymptoticFilename).readlines()
    for line in AsymptoticFile:
        # look for lower boundry
        if line.find("Expected 2.5%:") > -1:
            arguments = line.split(" ")
            #print arguments
            for i in range(0,len(arguments)):
                arguments[i].replace("\n", "")
            #print arguments
            #if float(arguments[-1]) < 1.0:
            min= float(arguments[2])
            #print min
            #else:
            #    min = 1.0
        # look for upper boundry
        if line.find("Expected 97.5%:") > -1:
            arguments = line.split(" ")
            #arguments[-1].replace("\n", "")
            max= float(arguments[2])
            #print max

    #print(str(min)+" "+str(max))
    # create file with list of arguments in directory
    ArgumentFilename = "arguments.txt"
    ArgumentFile = open(ArgumentFilename, 'w')
    for i, item in enumerate(numpy.arange(round(min*0.40,1),round(max*1.40,1),step)):

            if i % int(NumberPerJobs) == 0:
                ArgumentFile.write(str(int(Number)))

            ArgumentFile.write(" "+str(round(item,3)))
            if (i+int(NumberPerJobs)+1) % int(NumberPerJobs)  == 0:
                ArgumentFile.write('\n')
    #ArgumentFile.write("2")

def plot_asym():
    jobs = JDLCreator("condocker")
    jobs.SetExecutable("../../job_plot_asym.sh")
    liste=['']     ## fake arguments
    jobs.SetArguments(liste)
    jobs.SetFolder("../full_workdir/plots/")
    jobs.SetWalltime(8*60)
    jobs.requirements = "TARGET.ProvidesEKPResources && TARGET.ProvidesCPU"
    jobs.SetMemory(1500)
       #jobs.PrintJDL()
    jobs.WriteJDL()     # write JDL file
    jobs.Submit()

def plot_fullcls():
    jobs = JDLCreator("condocker")
    jobs.SetExecutable("../../job_plot_full.sh")
    liste=['']     ## fake arguments
    jobs.SetArguments(liste)
    jobs.SetFolder("../full_workdir/plots/")
    jobs.SetWalltime(8*60)
    jobs.requirements = "TARGET.ProvidesEKPResources && TARGET.ProvidesCPU"
    jobs.SetMemory(1500)
       #jobs.PrintJDL()
    jobs.WriteJDL()     # write JDL file
    #jobs.Submit()



def merge(i):
    jobs = JDLCreator("condocker")
    jobs.SetExecutable("../job_merge.sh")
    liste = [i]
    jobs.SetArguments(liste)
    jobs.SetWalltime(10*60)
    jobs.requirements = "TARGET.ProvidesEKPResources && TARGET.ProvidesIO"
    jobs.SetMemory(2000)
    jobs.SetFolder("../full_workdir/"+str(i)+"/")
    jobs.WriteJDL()
    jobs.Submit()

def asym(i):
    jobs = JDLCreator("condocker")
    jobs.SetExecutable("../../job_asympt.sh")
    liste = [i]
    jobs.SetArguments(liste)
    jobs.SetWalltime(10*60)
    jobs.requirements = "TARGET.ProvidesEKPResources && TARGET.ProvidesCPU"
    jobs.SetMemory(1500)
    jobs.SetFolder("../full_workdir/"+str(int(i))+"/")
    jobs.WriteJDL()
    jobs.Submit()

def asym_3m(i):
    jobs = JDLCreator("condocker")
    jobs.SetExecutable("../../job_asympt_3m.sh")
    liste = [i]
    jobs.SetArguments(liste)
    jobs.SetWalltime(10*60)
    jobs.requirements = "TARGET.ProvidesEKPResources && TARGET.ProvidesCPU"
    jobs.SetMemory(1500)
    jobs.SetFolder("../full_workdir/"+str(int(i))+"_3m/")
    jobs.WriteJDL()
    jobs.Submit()

def asym_4m(i):
    jobs = JDLCreator("condocker")
    jobs.SetExecutable("../../job_asympt_4m.sh")
    liste = [i]
    jobs.SetArguments(liste)
    jobs.SetWalltime(10*60)
    jobs.requirements = "TARGET.ProvidesEKPResources && TARGET.ProvidesCPU"
    jobs.SetMemory(1500)
    jobs.SetFolder("../full_workdir/"+str(int(i))+"_4m/")
    jobs.WriteJDL()
    jobs.Submit()




def fit(i):
    jobs = JDLCreator("condocker")
    jobs.SetExecutable("../job_fit.sh")
    liste = []
    liste.append(str(i)+" --grid=tHq_merge.root")
    for limit in ['0.025', '0.16', '0.5', '0.84', '0.975']:
        liste.append(str(i)+" --grid=tHq_merge.root --expectedFromGrid "+str(limit))
    jobs.SetArguments(liste)
    jobs.requirements = "TARGET.ProvidesEKPResources && TARGET.ProvidesCPU"
    jobs.SetWalltime(10*60)
    jobs.SetMemory(6200)
    jobs.AddExtraLines('request_disk=300000')
    jobs.SetFolder("../full_workdir/"+str(i)+"/")
    jobs.WriteJDL()
    jobs.Submit()

def calc(i):
    jobs = JDLCreator("condocker")
    jobs.SetExecutable("../job_th_comb.sh")
    liste=['a','b','c','4','5','6']     ## fake arguments
    jobs.SetArguments(liste)
    jobs.SetFolder("/usr/users/dschaefer/how-to_jdl_creator/fullCLs/")
    #jobs.SetFolder("../full_workdir/"+str(int(i))+"/")
    jobs.requirements = "TARGET.ProvidesEKPResources && TARGET.ProvidesCPU"
    jobs.SetWalltime(8*60)
    jobs.SetMemory(1500)
       #jobs.PrintJDL()
       #jobs.Submit()
    jobs.WriteJDL()     # write JDL file
    ListOfSteps(i)      # overwrite file with list of arguments

def test_stat(i):
    jobs = JDLCreator("condocker")
    jobs.SetExecutable("../job_test_stat.sh")
    liste=['a','b','c','4','5','6']     ## fake arguments
    jobs.SetArguments(liste)
    jobs.SetFolder("../full_workdir/"+str(int(i))+"/")
    jobs.SetWalltime(3*60)
    jobs.requirements = "TARGET.ProvidesEKPResources && TARGET.ProvidesCPU"
    jobs.SetMemory(1500)
       #jobs.PrintJDL()
       #jobs.Submit()
    jobs.WriteJDL()     # write JDL file
    ListOfSteps(i)      # overwrite file with list of arguments



def calc_3m(i):
    jobs = JDLCreator("condocker")
    jobs.SetExecutable("../../job_th_comb_3m.sh")
    liste=['a','b','c','4','5','6']     ## fake arguments
    jobs.SetArguments(liste)
    jobs.SetFolder("../full_workdir/"+str(int(i))+"_3m/")
    jobs.SetWalltime(8*60)
    jobs.requirements = "TARGET.ProvidesEKPResources && TARGET.ProvidesCPU"
    jobs.SetMemory(1500)
       #jobs.PrintJDL()
       #jobs.Submit()
    jobs.WriteJDL()     # write JDL file
    ListOfSteps(i)      # overwrite file with list of arguments

def calc_4m(i):
    jobs = JDLCreator("condocker")
    jobs.SetExecutable("../../job_th_comb_4m.sh")
    liste=['a','b','c','4','5','6']     ## fake arguments
    jobs.SetArguments(liste)
    jobs.SetFolder("../full_workdir/"+str(int(i))+"_4m/")
    jobs.requirements = "TARGET.ProvidesEKPResources && TARGET.ProvidesCPU"
    jobs.SetWalltime(8*60)
    jobs.SetMemory(1500)
       #jobs.PrintJDL()
       #jobs.Submit()
    jobs.WriteJDL()     # write JDL file
    ListOfSteps(i)      # overwrite file with list of arguments


def calc_remote(i):
    jobs = JDLCreator()
    jobs.universe = 'vanilla'
    jobs.SetExecutable("../job_th_comb_remote.sh")
    liste=['a','b','c','4','5','6']     ## fake arguments
    jobs.SetArguments(liste)
    jobs.SetFolder("../full_workdir/"+str(int(i))+"/")
    jobs.SetWalltime(23*60*60)
    #jobs.requirements = "TARGET.ProvidesCPU"
    jobs.requirements = '(TARGET.CLOUDSITE=="BWFORCLUSTER" ) '
    jobs.input_files = "../../setup.sh,../../pack.sh,tH_3m_"+str(int(i))+".root,tH_3m_"+str(int(i))+".txt,tH_4m_"+str(int(i))+".root,tH_4m_"+str(int(i))+".txt,tH_comb_"+str(int(i))+".txt"

    # start at the end a script to pack the results in an tar file
    jobs.AddExtraLines('+PreCmd = "setup.sh"')
    jobs.AddExtraLines('+PreArguments = ""')
    jobs.AddExtraLines("+RemoteJob=True")
    jobs.AddExtraLines("+ExperimentalJob=True")
    jobs.AddExtraLines('+PostCmd = "pack.sh"')
    jobs.AddExtraLines('+PostArguments = "$(Process)"')

#    jobs.AddExtraLines('use_x509userproxy = True')
#    jobs.AddExtraLines('x509UserProxyVOName = "cms"')
#    jobs.AddExtraLines('x509userproxysubject = "/C=DE/O=GermanGrid/OU=KIT/CN=Matthias Schnepf"')
#    jobs.AddExtraLines('x509UserProxyEmail = "matthias.jochen.schnepf@cern.ch"')
#    jobs.AddExtraLines('x509UserProxyFQAN = "/C=DE/O=GermanGrid/OU=KIT/CN=Matthias Schnepf,/cms/dcms/Role=NULL/Capability=NULL,/cms/Role=NULL/Capability=NULL"')
#    jobs.AddExtraLines('x509userproxy = "/usr/users/mschnepf/.globus/usercert.pem"')

    jobs.output_files = "sample_$(Process).tar"
    jobs.SetMemory(2000)
    jobs.WriteJDL()     # write JDL file
    ListOfSteps(i)      # overwrite file with list of arguments




def main():
    ListOfSteps(4000)
    #calc_remote(44)
    #merge(43)

    calc(4000)
    #for i in range(7,12):
		#calc(i)
		#merge(i)
        #calc_remote(i)
		#fit(i)
	    #asym(i)
    #plot_asym()
    #plot_fullcls()

if __name__ == "__main__":
        main()



