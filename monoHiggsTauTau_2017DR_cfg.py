# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein file:monoHiggs_tautau_2017.root --fileout file:monoHiggs_2017DR_step1.root --pileup_input dbs:/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v2/GEN-SIM-RAW --mc --eventcontent FEVTDEBUGHLT --pileup AVE_25_BX_25ns,{'N': 20} --datatier GEN-SIM-DIGI-RAW --conditions 94X_mc2017_realistic_v17 --step DIGI,L1,DIGI2RAW,HLT:@relval2017 --nThreads 8 --geometry DB:Extended --era Run2_2017 --python_filename monoHiggsTauTau_2017DR_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_Fake2_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('file:monoHiggs_tautau_2017.root'),
    inputCommands = cms.untracked.vstring(
        'keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:monoHiggs_2017DR_step1.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(20.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/523E1286-F76B-EA11-A1C7-0CC47A57CB62.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/24190951-F76B-EA11-B073-0CC47AC17502.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/0245D1AB-F76B-EA11-BC84-0CC47A2B03A2.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/30AD3C9B-F76B-EA11-9685-0CC47AD98B94.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/EAD85CA9-F76B-EA11-8003-0CC47A2B04DE.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/78BD7DF2-F76B-EA11-8F77-0CC47A13CB36.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/EE7F5493-F76B-EA11-AE16-0CC47ADAF60A.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/028C0588-F56B-EA11-8D6A-0CC47A13CC7A.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/642E82E6-F76B-EA11-B1F1-0CC47A13CCEE.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/D0409EA6-F76B-EA11-9DF1-0CC47A13CC7E.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/0AF0E0FD-F16B-EA11-A810-0CC47AD98B94.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/E0F44443-F56B-EA11-97F6-002590489776.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/9AE18CAB-F36B-EA11-96F0-0242AC130002.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/6E023F99-816C-EA11-A8B3-001E674FBF1D.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/924874F6-F36B-EA11-BE86-20040FF474C8.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/5C04A1E4-F36B-EA11-9D7D-1866DAEA79D4.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/3C6937EB-F36B-EA11-972C-141877410B85.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/009A7F17-F46B-EA11-BABB-1866DAEA6C40.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/9E598AFF-F36B-EA11-8DAF-782BCB20E8A3.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/DEE0732B-F46B-EA11-9166-001EC94BF70E.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/66F05376-F56B-EA11-99BA-20040FE8E8A4.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/7A972EA4-F56B-EA11-87C0-B083FED3F2E8.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/F474CB8F-F26B-EA11-8A74-801844DEDF08.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/E86D057A-F06B-EA11-822D-20040FF46E04.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/D4008E22-F56B-EA11-83EF-1418774120C3.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/16DA1C2D-F56B-EA11-B80E-842B2B1810D3.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/1CD44AD6-F56B-EA11-9B88-EC0D9A0B3340.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/0251B213-EE6B-EA11-ACA4-001E67A400F0.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/B6982C25-EE6B-EA11-90DD-001E67DDC4AC.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/CEAB63C9-F16B-EA11-83CD-24BE05C4D821.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/06E9964A-F56B-EA11-B470-E0071B697BF1.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/A2F73A1D-F76B-EA11-97A7-24BE05CEDC81.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/3CDB36F0-F56B-EA11-97E9-0CC47A7C3430.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/18CBF7A8-F66B-EA11-B9EA-0CC47A4D7698.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/9213C992-F66B-EA11-89E8-0CC47A4C8EB6.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/AC42EEF7-F56B-EA11-886B-0025905B85D2.root', '/store/mc/RunIIFall17DRPremix/MinBias_NoFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8/GEN-SIM-RAW/PU2017_94X_mc2017_realistic_v11-v2/20000/9246D5FF-F46B-EA11-A0A6-0025905A607A.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_v17', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.FEVTDEBUGHLToutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
