loadLibs=[
  "libSFramePlugIns",
  "libNtupleVariables",
  "libPileupReweightingTool",
  "libBTaggingTools",
  "libTreeAnalyzer",
  ]


loadPacks=["SFrameCore.par",
	   "TreeAnalyzer.par",
	   ]

compilePacks=[
  "../TreeAnalyzer",
  ]

AddUserItems = [
 ["RecoTreeName","tree"],
 ["PUPPIJEC","/usr/users/dschaefer/SFrame_setup/HadronicVV/TreeAnalyzer/weights/puppiCorr.root"],
 
 ["pileupReweighting_HistoPath" ,"$SFRAME_DIR/../HadronicVV/PileupReweightingTool/histograms/" ],
 ["pileupReweighting_DataRootFileName","DataPUDistribution.root" ],
 ["pileupReweighting_MCScenario","PUS25ns" ],

]
