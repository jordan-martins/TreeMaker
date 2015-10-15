import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/020DA37C-AB66-E511-8214-002590D9D8C0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/0662F6F4-A966-E511-9EFD-002590D9D9E4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/0667CA88-AB66-E511-A5E4-0025901FB438.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/0C275E6F-A766-E511-BC4C-0002C94CDAF6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/186191A5-A766-E511-9711-00259048AE50.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/1C9A907F-AA66-E511-94BD-002590D9D8C0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/22BB628F-AB66-E511-90EC-0CC47A0AD6C4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/3443517F-AB66-E511-829A-0025907D1FF8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/5605701D-AB66-E511-864A-0025901FB188.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/5A2DB18C-AB66-E511-8CED-00259029ECEA.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/6A96367E-A766-E511-B988-0002C90B7484.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/6C5F4D7F-AB66-E511-B246-0025907D1FF8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/70348B7D-AA66-E511-817F-00259048AE50.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/74955C82-AB66-E511-963E-00259048A860.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/7696A355-A766-E511-9673-0002C90B7F3A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/7A6DFA21-A966-E511-A27C-002590D9D822.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/7ADAF0D8-A766-E511-93C1-002590D9D822.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/7E13C9CF-AA66-E511-9198-002590FD5122.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/8096A355-A766-E511-99AC-0002C90B7F3A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/80F82911-A966-E511-B662-00259048AE50.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/84AFEA7E-AB66-E511-A7D0-0025907D1FF8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/84CB1E3F-AA66-E511-A120-002590D9D822.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/8C1A5E6F-A766-E511-96ED-0002C94CDAF6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/8EC8D268-A766-E511-8D65-0002C90F80D6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/BC20148D-A766-E511-9594-0002C90A36FE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/BE08495A-A766-E511-925A-0002C94CD1E4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/C08E6060-A766-E511-BEA9-0002C90B73F2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/C63EAA84-AB66-E511-9050-00259029E66E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/CCA5865E-AB66-E511-A602-002590D9D822.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/CCA99072-A766-E511-8128-0002C90A351C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/CEB60D55-A766-E511-986C-0002C90A3678.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/D8869026-AB66-E511-9224-002590D9D9E4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/D8BE5383-A866-E511-A7D9-0025901FB188.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/DEC4CF74-A766-E511-9B91-0002C90F808C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/E0AF0386-A766-E511-A0D5-0002C90A37B6.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/E0B58071-A766-E511-B306-0002C90B7F4E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/E0C06775-A766-E511-A9D0-0002C95A02D0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/EC18E49F-AB66-E511-8020-002590812700.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/EC889D85-AB66-E511-86B3-00304867FF03.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/F06D828F-AB66-E511-8FC2-0030485FC291.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/F0BA448A-AB66-E511-AF54-0025907793F4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/F4F54CC2-A966-E511-B659-0025901FB188.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/FA596F7E-A766-E511-A0D6-0002C90F809E.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/FABECC85-AB66-E511-A870-002590D9D980.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/FC0F1A8B-AB66-E511-B9EB-00259048A8F4.root' ] );


secFiles.extend( [
               ] )

