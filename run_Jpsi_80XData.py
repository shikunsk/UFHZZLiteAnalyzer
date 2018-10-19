import os, time

dataInfos = [
        [
            "root://cmsio5.rc.ufl.edu//store/user/t2/users/archived/dsperka/Run2/HZZ4l/SubmitArea_13TeV/rootfiles_Data80X_4lskim_M17_Feb21/",
            ["Data_Run2016-03Feb2017_4l"],
        ],
        ]

# ____________________________________________________________________________________________________________ ||
# Configuration
infos            = dataInfos
outputDir       = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180914/SkimTree_Jpsi_Run2016Data_v1/"

if not os.path.exists(os.path.abspath(outputDir)):
    os.makedirs(outputDir)

njobs = 1
if njobs > 6: raise RuntimeError, "Too many resources required"
for inputDir,inputSamples in infos:
    for job in range(1,njobs+1):
        for sample in inputSamples:
            cmd = './Jpsi_Ana.exe '+inputDir+'/'+sample+' '+outputDir+sample+' 1 '+str(job)+' '+str(njobs)
            os.system(cmd)
