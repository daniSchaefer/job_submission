loadLibs=[
  "libGoodRunsLists",
  "libExoDiBosonAnalysis",
  "libLHAPDF",
  ]


loadPacks=["SFrameCore.par",
	   "ExoDiBosonAnalysis.par",
	   ]

compilePacks=[
  "../ExoDiBosonAnalysis",
  ]

AddUserItems = [
 ["InputTreeName","tree"],
 ["OutputTreeName","tree"],
 ["usePuppiSD","true"],
 ["GenStudies","true"],
 ["LeptPtCut","30"],
 ["LeptEtaCut","2.4"],
 ["AleptPtCut","30"],
 ["AleptEtaCut","2.4"],
 ["METCut","80"],
 ["dEtaCut","1.3"], 
 ["JetPtCutLoose","30."],
 ["JetPtCutTight","200."],
 ["JetEtaCut","2.5"],
 ["Tau21Cut","true"],
 ["Tau21HPLow","0.00"],
 ["Tau21HPHigh","0.35"],     
 ["Tau21Low","0.35"],
 ["Tau21High","0.75"],  
 ["mWLow","65."],
 ["mWHigh","85."],
 ["mZLow","85."],
 ["mZHigh","105."],
 ["xSec","1."],
 ["genEvents","1."],
 ["Lumi","1."],
 ["PUdata","data/DataPUDistribution.root"],
 ["JSONfile","No"],
 ["BTagEff4vetoData" ,"data/TT_CT10_TuneZ2star_8TeV-powheg-tauola_AK5PF_CSVM_bTaggingEfficiencyMap.root" ],
 ["BTagEff4fatjetData","data/BtagEfficienciesMap_fatjets_Wp.root" ],
 ["BTagEff4subjetData","data/btag-efficiency-maps.root"],
 ["PUPPIJEC" ,"data/puppiCorr.root"], # old one from thea found here: "/mnt/t3nfs01/data01/shome/dschafer/ExoDiBosonAnalysis/data/puppiCorr_thea.root"
 ["PUPPIJMR" ,"data/puppiSoftdropResol.root"],
 ["JMS" ,"1.0"], #ICHEP 0.999
 ["JMSunc" ,"0.0094"],
 ["JMR" ,"1.0"], #ICHEP 1.079
 ["JMRunc" ,"0.2"],
]

#End
#["JSONfile","/mnt/t3nfs01/data01/shome/dschafer/ExoDiBosonAnalysis/data/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt"],
#["JSONfile","No"] put this for data! since the JSON has already been used on the promtreco data!!!
# for pileup old file in data/biasXsec_69200.root 
