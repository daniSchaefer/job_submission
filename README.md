# job_submission

Scripts used to submit jobs to the desktop-cloud in karlsruhe


1) submit sframe jobs with: py batchsubmission.py --sframe -j submissionfile.py
2) submit various limits/ old workspace josbs using the various options and setting the models, categories, directories to run 
over in datacard.cfg
3) submit jobs for 3D limits: --limits3D
4) submit jobs for bias tests:
      4.1) scan significance over signal strenght: py batchsubmission.py --scanSig -t 100
          in between here the scans must be written into a root file using py /home/dschaefer/Limits3D/biasTest/scanSignalStrength.py 
          --mass 1200,1300,1400,1500,1700,1800,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3100,2100,3200,3300
          ,3400,3500,3600,3700,3800,3900,4000,4100,4200,4300,4400,1900,1600

      4.2) make signal+background fits for given signal strength : py batchsubmission.py --injectSig --toys 200
      --signal /home/dschaefer/Limits3DFit/biasTest/scanSignalStrength.root
