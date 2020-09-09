#!bin/bash

# merge root files

name="higgsCombineBulkWW_sp"

one=0.37
two=0.36
hadd temp.root $name$one*T500.mH4000.root $name$two*T500.mH4000.root


#sp=(0.45  0.40  0.35  0.30  0.25  0.20  0.15)
#sp=(0.0 0.03 0.05 0.08 0.1 0.13 0.15 0.18 0.2 0.23 0.25 0.28 0.3 0.33)
sp=(0.01 0.02 0.04 0.06 0.07 0.09 0.12 0.14 0.16 0.17 0.19 0.21 0.22 0.24 0.26 0.27 0.29 0.31 0.32 0.34)
for i in  "${sp[@]}"; do
     #rm tempnew.root
     hadd tempnew.root temp.root $name$i*T500.mH4000.root
     mv tempnew.root temp.root
done;
