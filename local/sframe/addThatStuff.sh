#!/bin/bash

echo "hadd -f tmp.root ExoDiBosonAnalysis.Data1.flatTuple_1.VVdijet.root ExoDiBosonAnalysis.Data1.flatTuple_2.VVdijet.root"

for i in `seq 1 10`;
do 
    echo "hadd -k -f tmpnew.root tmp.root ExoDiBosonAnalysis.Data1.flatTuple_${i}.VVdijet.root"
    echo "mv tmpnew.root tmp.root"
done
echo "mv tmp.root ExoDiBosonAnalysis.Data1.VVdijet.root"