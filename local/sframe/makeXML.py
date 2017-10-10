#!/usr/bin/env python

import os, sys, re, optparse,shutil, pickle
from ROOT import *


argv = sys.argv
parser = optparse.OptionParser()   
parser.add_option("--sample",dest="sample",action="store",default="QstarQW")
parser.add_option("--region",dest="region",action="store",default="WW")
parser.add_option("--path",dest="path",action="store",default="/storage/b/psi_data/Summer16/")


(opts, args) = parser.parse_args(argv)  

#<In FileName="Summer16/WprimeToWZToWhadZhad_narrow_M-4000_13TeV-madgraph/WprimeToWZToWhadZhad_narrow_M-4000_13TeV-madgraph20170203_signal/170203_125733/0000/flatTuple_1.root" Lumi="1.0"/>


xmldir="/usr/users/dschaefer/job_submission/local/sframe/xml/"
for filename in os.listdir(opts.path):
    if filename.find(opts.sample)==-1:
        continue
    if filename.find(opts.region)==-1:
        continue
    print filename
    if opts.region.find("QCD")==-1 and opts.region.find("QQ")==-1:
        a,b = filename.split("M-")
        c, d = b.split("_13")
        if c.find("_T"):
            mass = int(c.split("_T")[0])
        else:
            mass = int(c)
    else:
        if opts.region.find("QCD")!=-1:
            a,b = filename.split("QCD_")
            c,d = b.split("_T")
            mass = c
        if opts.region.find("QQ")!=-1:
            mass = 0
        
    print mass
    name = xmldir+opts.sample+opts.region+"_M"+str(mass)+".xml"
    if opts.region.find("QQ")!=-1:
        name = xmldir+opts.sample+opts.region+".xml"
    print " output file saved to : "+name
    out = open(name,'w')
    
    for dir2 in os.listdir(opts.path+filename):
        for dir3 in os.listdir(opts.path+filename+"/"+dir2):
            #if opts.sample == "Bulk":
            #            out.write('<In FileName="')
            #            out.write(filename)
            #            out.write(filename+"/"+dir2+"/"+dir3)
            #            out.write('" Lumi="1.0"/>\n')
            #else:  
                for dir4 in os.listdir(opts.path+filename+"/"+dir2+"/"+dir3):
                    for flatTuple in os.listdir(opts.path+filename+"/"+dir2+"/"+dir3+"/"+dir4):
                        out.write('<In FileName="Summer16/')
                        out.write(filename)
                        out.write("/"+dir2+"/"+dir3+"/"+dir4+"/"+flatTuple)
                        out.write('" Lumi="1.0"/>\n')
    out.close()
