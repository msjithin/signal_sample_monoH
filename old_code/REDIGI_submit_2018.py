# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --fileout file:SUS-RunIIAutumn18DRPremix-00019_step1.root --pileup_input pileup.root --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 102X_upgrade2018_realistic_v15 --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:@relval2018 --procModifiers premix_stage2 --nThreads 8 --geometry DB:Extended --datamix PreMix --era Run2_2018 --python_filename try.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
from Configuration.ProcessModifiers.premix_stage2_cff import premix_stage2

process = cms.Process('HLT',eras.Run2_2018,premix_stage2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.DigiDM_cff')
process.load('Configuration.StandardSequences.DataMixerPreMix_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorDM_cff')
process.load('Configuration.StandardSequences.DigiToRawDM_cff')
process.load('HLTrigger.Configuration.HLT_2018v32_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
                            fileNames = cms.untracked.vstring($inputFileNames),
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

process.PREMIXRAWoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
                                           fileName = cms.untracked.string('$outputFileName'),
    outputCommands = process.PREMIXRAWEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mixData.input.fileNames = cms.untracked.vstring(['/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/00002/1C56C5CD-24BC-A841-A5D5-FD70C468F890.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/00003/ED3110CF-AF42-A94C-B382-E7620DF2EAF1.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/007B12AA-FFA8-CE4F-A039-6E89B4417C3A.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/0095A820-DC36-184B-84E3-5B9814E93A54.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/00B0F18D-6603-7C4E-89C2-93D1A99D513A.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/00B64D15-D716-9F4E-8747-7750A581D665.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/011DCAE7-23A1-5F4D-851E-4D0BE2F2C7F6.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/012AC93B-0518-3444-A65D-A4953CB94A5A.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/016FA077-2F96-D249-ACFE-626AEE45CE5B.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/01E1B3E1-810A-5449-8020-98B8DCC7BFDB.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/021CC002-B7CA-1C44-BE1B-7ABC6147E7E1.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/02416FB3-9475-114D-8C75-EDE0A961424F.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/02ABE723-AB52-8A43-A949-F2970710592F.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/02BDF04B-B507-8E44-846E-725EE4FEA6EF.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/02CDC0A1-4898-2D4C-BB1C-85D06CD5783A.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/02D1ECDC-7899-6F47-839E-43A4D9DD9CC3.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/031E2532-D6A3-3549-BD42-D6F9256B9837.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/03491A85-48C1-FC46-B7D3-0552B92C0041.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/03CDCDD0-B9F7-6944-B5D9-3EDC96FC3ADD.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/04092424-8346-D64A-98EF-4EFC783D8DE3.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/045A2FB3-1527-4B4B-89FB-613E753C403F.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/04B18EC4-6C03-2D4F-AA7D-4605C3329A25.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/04CC8746-CA7F-3B46-8D81-8E141B3A46D1.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/04F7A2DE-16FE-5B47-AFD9-5775AEBF7DD9.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/04FAA85C-42E4-F047-AAFD-EB33E6E9EE5E.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/04FCF5CB-ED27-F941-B74F-DC57826A8AB4.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/053F8078-3B41-6248-A4A6-C5ED08D9F1F3.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/05990F68-1FD4-A846-9CCB-0CF7B410281E.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/05B9E1EC-F61B-DC43-B777-550A7CF986C5.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/05F0C8E2-E7EB-5240-A41F-0A9341971F5B.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/06035A37-6DEC-C144-AC4B-7BE20D074D16.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/063AA3EE-82BD-F74F-B218-23C8B2B5A4FD.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/063F47DA-8822-4D47-9B36-BEF01AF10D6A.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/066F17CE-A667-8844-965C-DCF7AA012754.root',
                                                         '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/100000/06B58C9B-1432-7741-811B-3D734BAE0328.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v20', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.PREMIXRAWoutput_step = cms.EndPath(process.PREMIXRAWoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.datamixing_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.PREMIXRAWoutput_step])
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
