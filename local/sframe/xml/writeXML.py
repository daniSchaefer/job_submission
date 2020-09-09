
import os
import glob
import math
import array
import ROOT
import ntpath
import sys
import subprocess
import time
import numpy
from subprocess import Popen
from optparse import OptionParser
from array import array

from ROOT import gROOT, TPaveLabel, gStyle, gSystem, TGaxis, TStyle, TLatex, TString, TF1,TFile,TLine, TLegend, TH1D,TH1F,TH2D,THStack,TChain, TCanvas, TMatrixDSym, TMath, TText, TPad

from array import array

#parser = OptionParser()

#parser.add_option('--filename', action="store",type="string",dest = "filename",default="../config/BulkWW_M1000.xml")
#parser.add_option('--outname',action="store",type="string",dest="outname",default="N")
#parser.add_option('--s',action="store",type="string",dest="suffix",default="")

#(options, args) = parser.parse_args()



def write(mass,model):
    suffix = ''
    if model.find('BulkWW')!=-1:
        suffix = 'BulkGravToWW'
    if model.find('BulkZZ')!=-1:
        suffix = 'BulkGravToZZToZhadZhad'
    if model.find('Zprime')!=-1:
        suffix = 'ZprimeToWW'
    if model.find('Wprime')!=-1:
        suffix = 'WprimeToWZToWhadZhad'
    if model.find('QstarQW')!=-1:
        suffix = 'QstarToQW'
    if model.find('QstarQZ')!=-1:
        suffix = 'QstarToQZ' 
        

    f = open(model+"_M"+str(int(mass))+".xml","w")
    if model.find('Qstar')==-1:
        f.write('  <In FileName="Summer16/jobtmp_'+suffix+'_narrow_M-'+str(int(mass))+'_13TeV-madgraph_RunIISummer16MiniAODv2_PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/'+suffix+'_narrow_M-'+str(int(mass))+'_13TeV-madgraph_RunIISummer16MiniAODv2_PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-1/flatTuple.root" Lumi="1.0"/>  \n')
        f.write('  <In FileName="Summer16/jobtmp_'+suffix+'_narrow_M-'+str(int(mass))+'_13TeV-madgraph_RunIISummer16MiniAODv2_PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/'+suffix+'_narrow_M-'+str(int(mass))+'_13TeV-madgraph_RunIISummer16MiniAODv2_PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-2/flatTuple.root" Lumi="1.0"/>  \n')
        f.write('  <In FileName="Summer16/jobtmp_'+suffix+'_narrow_M-'+str(int(mass))+'_13TeV-madgraph_RunIISummer16MiniAODv2_PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/'+suffix+'_narrow_M-'+str(int(mass))+'_13TeV-madgraph_RunIISummer16MiniAODv2_PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-3/flatTuple.root" Lumi="1.0"/>  \n')
    else:
        f.write('  <In FileName="Summer16/'+suffix+'_M_'+str(int(mass))+'_TuneCUETP8M1_13TeV_pythia8_GEN-SIM_DIGI80X_RECO80X_MiniAODv2_80X_MiniAODv2_PUSpring16RAWAODSIM/EXOVVTree_'+suffix+'_M_'+str(int(mass))+'_TuneCUETP8M1_13TeV_pythia8_GEN-SIM_DIGI80X_RECO80X_MiniAODv2_80X_MiniAODv2_PUSpring16RAWAODSIM_1.root" Lumi="1.0"/> \n') 
        
        
        
def write_Clemens(mass,model,direc,N):
    suffix = ''
    if model.find('BulkWW')!=-1:
        suffix = 'BulkGravToWW'
    if model.find('BulkZZ')!=-1:
        suffix = 'BulkGravToZZToZhadZhad'
    if model.find('Zprime')!=-1:
        suffix = 'ZprimeToWW'
    if model.find('Wprime')!=-1:
        suffix = 'WprimeToWZToWhadZhad'
    if model.find('QstarQW')!=-1:
        suffix = 'QstarToQW'
    if model.find('QstarQZ')!=-1:
        suffix = 'QstarToQZ' 
        

    f = open(model+"_M"+str(int(mass))+".xml","w")
    for n in range(1,N+1):
        if model.find('Qstar')==-1:
            f.write('  <In FileName="Summer16/'+suffix+'_narrow_M-'+str(int(mass))+'_13TeV-madgraph/'+suffix+'_narrow_M-'+str(int(mass))+'_13TeV-madgraph20170203_signal/'+direc+'/0000/flatTuple_'+str(n)+'.root" Lumi="1.0"/>  \n')
        
        else:
            f.write('  <In FileName="Summer16/'+suffix+'_M-'+str(int(mass))+'_TuneCUETP8M2T4_13TeV-pythia8/'+suffix+'_M-'+str(int(mass))+'_TuneCUETP8M2T4_13TeV-pythia820170203_signal/'+direc+'/0000/flatTuple_'+str(n)+'.root" Lumi="1.0"/> \n') 
        
    



    
 

    
#######################################
############ Main Code ################
#######################################

if __name__== '__main__':
  
  # masses=[1000,1200,1400,1600,1800,2000,2500,3500,4000,4500]
  # model = "BulkWW"
  # direc = ["170203_124015","170203_124102","170203_124212", "170203_124303","170203_124351", "170203_124445","170203_124543","170203_124637","170203_124725","170203_124815"]
  # for i in range(0,len(masses)):
  #     write_Clemens(masses[i],model,direc[i],5)
      
  # masses=[1000,1200,1400,1600,1800,2000,2500,3000,3500,4000]
  # model = "BulkZZ"
  # direc = ["170203_125950","170203_130046","170203_130217","170203_130307" ,"170203_130401","170203_130513" ,"170203_130602","170203_130656"  ,"170203_130746","170203_130836"]
  # for i in range(0,len(masses)):
  #     write_Clemens(masses[i],model,direc[i],5)
      
  # masses=[1000,1200,1400,1600,1800,2000,2500,3000,3500,4000,4500]
  # model = "Zprime"
  # direc = ["170203_123048","170203_123137","170203_123227","170203_123314","170203_123424","170203_123521","170203_123609","170203_123700","170203_123745","170203_123834","170203_123922"]
  # for i in range(0,len(masses)):
  #     write_Clemens(masses[i],model,direc[i],5)
      
  # masses=[1000,1200,1400,1600,1800,2000,2500,3000,3500,4000,4500]
  # model = "Wprime"
  # direc = ["170203_124859","170203_125002","170203_125054","170203_125147","170203_125242","170203_125329","170203_125437","170203_125537","170203_125638","170203_125733","170203_125842"]
  # for i in range(0,len(masses)):
  #     write_Clemens(masses[i],model,direc[i],5)    
      
  masses=[1000,1200,1400,1600,1800,2000,2500,3000,3500,4000,4500,5000,6000,7000]
  model = "QstarQW"
  direc = ["170203_131033","170203_131119","170203_131245","170203_131334","170203_131424","170203_131525","170203_131617","170203_131737","170203_131834","170203_131927","170203_132026", "170203_132144","170203_132239","170203_132327"]
  for i in range(0,len(masses)):
      write_Clemens(masses[i],model,direc[i],21)    
  
  
  masses=[1000,1200,1400,1600,1800,2000,2500,3000,4500,6000]
  model = "QstarQZ"
  direc = ["170203_132416", "170203_132501","170203_132550","170203_132643","170203_132755","170203_132843","170203_132932","170203_133028","170203_133122","170203_133213"]
  for i in range(0,len(masses)):
      write_Clemens(masses[i],model,direc[i],14)    
  
  
  
  #massesalt=[800,1000,1200,1400,1600,1800,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500]
  
  #for amodel in altmodels:
      #for am in massesalt:
          #write(263400,am,amodel)
  
