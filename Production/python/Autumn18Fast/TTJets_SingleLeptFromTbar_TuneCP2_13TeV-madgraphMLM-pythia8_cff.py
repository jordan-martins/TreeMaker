import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/0BAB7F1E-07CC-3146-8B62-FC357F685855.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/0F4CE883-BDC4-B24A-910E-FD483A93BF0F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/187ACBA5-BF73-6842-A70F-0271C8E0F0A6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/2036D887-05E3-9842-9D7F-7ABA63F70D97.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/225EB880-D7B2-6949-9CD9-509088105225.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/225FB1D5-918B-0349-907F-DBD2A1F7F51C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/24ACF44A-87FA-EE45-B560-A2D7412193B8.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/29F1151D-D9D1-CF40-BF9B-966D1AF1FDA9.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/2AAA2A9A-9781-3145-9955-6E88439D4C8F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/338D001C-BCCB-9044-AABF-FE4D5838211E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/38BB8117-CF23-3B4E-87A0-EE85CF5BC03D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/3E809C03-773D-3C45-89BE-1653F13CCE10.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/3EB4E209-5078-A74B-B362-A4D251AE8D79.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/43B9A9E5-74E4-0545-BA38-C494EA623E17.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/48E79ED9-7E7E-714C-83A2-6B97472B990A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/4D053CA9-834A-C045-B169-740E0E46D811.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/512B85BE-1A30-FE41-ABC7-9C30CEBEF659.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/5278EE0B-5B60-494F-B02A-9A21403DEA53.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/5A725AA7-F1F0-8842-BB48-D297F52EBFA0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/5B84F8B4-7010-E146-969F-18CD5AF362DA.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/5F1B40A4-3E6C-1542-B78D-D1F289D3FC6B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/61700704-D933-294F-9DDC-4B47C85653DB.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/6760B89F-E9C3-6442-A39E-82D30F79609C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/67F98B3F-8EEE-F646-88B3-24DC546CC008.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/6BABFDE1-B18D-004D-8A2C-A15C6C7C53A8.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/6C750376-EBE9-374B-8793-5774382F1BAF.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/6FCD83C0-862D-104F-84D2-AE69F1E44466.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/7C5CBAB6-3EBF-494F-BEB6-9531310A7D06.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/82764179-836C-9949-A224-C2CAF97666AC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/90010084-6915-984A-B42E-1BAA1BC5D983.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/90F4F0D1-5775-BA48-B0B4-5DE37B148787.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/9BB2C675-A0A8-DD4D-BD99-326FB25387B4.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/AC18016F-ADB0-A949-B38D-B5C27AE757D2.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/AF91B294-6829-C848-956A-072364A71D03.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/B304C080-3858-804A-81DD-0E0A0E001008.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/B4A3BBE4-0198-B145-AE6B-D636F3D4EE96.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/B7EFDE5B-FDDA-8C42-BAC7-08BF8B346277.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/B94DB85D-19A8-0743-9982-BBE9CBB51C9D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/BA525983-F904-4F49-80EA-DC10DA3778CF.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/BB02D9E3-C6BE-1841-992D-238E06AC2FF3.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/C3A0A405-AD4A-8A4A-8F29-D0572571C4A3.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/C77CDDE7-BE4B-8F42-8717-8523A3EF3D0D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/C9ED9B92-3BA8-8645-A931-D35E3F26B841.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/D0E4BAF7-8B77-7D40-97A8-D6453B636259.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/D82A2110-8EBA-6940-8B32-7CAD0B66C94A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/E0B6DE7E-507D-844C-8E19-195C4071B4D1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/E26734CC-9329-D646-9E34-457F3783421B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/E4979C1E-F3D9-8742-9408-E4E1A0CCC622.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/F1F41180-3433-7043-9F05-479DBDB9C929.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/F52D0F51-3848-AF48-933F-FDD1C77025F3.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/F533D0DB-B75A-E148-B495-CE5A9B6E3F26.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/F59CAA81-286B-EC41-AF6C-2BBE25AD32ED.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/FB1B439F-72F8-BA4E-91BF-8FE10E93CCAD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/10000/FEBFF024-6F7F-E241-A16A-D4A9B4DEC4F6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/03E6281F-36EC-2C41-8C5C-4471D2860E59.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/058C4A3F-A41F-3948-BB7B-C64E075725FD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/06F17D88-11F9-0546-868C-F54976BCE5E2.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/08373A15-47C0-6740-BCEF-DB76D28E35D8.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/0CDCF731-4CA6-824D-8859-0E35E9E5A30F.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/0F0AC870-2F02-1949-8CAC-09C1639A9AF6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/152C2D7E-E005-264E-9327-591B99E801C9.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/196EC094-ECDC-424E-AB1F-0BDF42CD0248.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/19C7E827-3E77-6848-9270-BB1A7FCA55C0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/1A397653-97F8-DD49-8BD0-51A6726F60E8.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/1F3DA834-323C-8741-8C7C-0B18EF9A4A3C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/25AB6899-B8CE-F447-8209-601475D7D49D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/2A86E2B4-794B-0F45-8128-6BA7448A9D76.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/2BCF1254-B41C-2A4C-89F6-0C960DCE4AD4.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/2CF0D522-0A0E-C84E-A5B0-D8098CD1F627.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/3424BE76-A888-1240-810C-CA3E3D2A4061.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/3D9E089E-323B-9144-A9D1-4AF6EEEC6258.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/428A88D3-41F3-224C-9802-E98F5F8D5078.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/474DE3E6-E150-454F-BDC0-120E58CCA6F7.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/4D2F580B-9583-AA4A-8956-5A5761C24279.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/4FA045FD-7D66-ED4D-904E-9E6FE37B9556.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/5DBED508-6E35-B74D-9054-413EBBA382AF.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/5E55C979-85B5-3541-83F8-11E26D42CCAD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/63A314B2-5554-154C-B166-AFE164F629AC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/63F2295F-B5EE-C94F-9899-DD9A9DDDE995.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/689CBE1C-86AF-C746-9A85-8DEAAA9CCD11.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/716B43C4-7800-B649-9808-7169B2137EE4.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/722A0E9C-4209-6149-8F46-4271D45C1B95.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/7476F6A5-6660-8B43-BAC9-F0F5D820D406.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/758AD50C-6663-1B4D-B893-DC90832B46B9.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/773D6435-11AF-E640-9357-D3EFEABB37AC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/7F8C7BB5-9014-A241-90DC-356A068121E1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/803AE032-0633-8043-AA89-EB70C41B45BC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/8276AD73-335F-DD4C-8669-ABE45FA62DE8.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/864992C4-D795-F349-8313-F6D822BE98B3.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/897D286B-1C89-7D4A-8FCE-BD3E0DBB6F26.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/8A25C0BF-EFAE-2C40-9A02-FBB78BE91259.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/8D52CEEB-B81E-A64A-9DBA-E3D0BBA1A969.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/8F134850-3388-8E41-8BE6-5E002EF18D45.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/96FC39A3-708B-D74A-910E-550A70DE7FA3.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/97AB24E1-7640-944C-9380-BD15BD51BA40.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/A1224469-4854-6C42-A383-D252576F4849.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/A2C05A12-03B7-C84F-918B-41413628F91B.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/A56A5732-2164-2D4C-AA6D-CC2FF07D0D44.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/ABCB065F-9BDF-3348-B6BA-3218B979820E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/B96FA34C-1621-4B45-9025-3CA9637E7399.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/BC76D89C-CBF8-CF42-84D7-8DA41BC1C5FD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/C1FC4E6D-8DDF-B944-BF2F-C8802348E0E0.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/C2989F18-EBBB-8642-A50C-5EC918630DCD.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/C2A500EC-C226-5E4C-B8FA-02D1FDECFFE8.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/C6DA429C-7819-5942-BEF1-F26F80EF4235.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/CA9B88AC-9CAE-4044-8EBB-64C33890C513.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/CCE9A557-471B-6940-BF8E-3907AF103030.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/CDD90971-B2E9-574D-9783-5185233B3234.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/CEB27F60-1A5E-B745-A950-D3A406FB3D4C.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/CF62ACDB-A9B7-8041-8067-28DC261F3AD5.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/D1AC0D10-6F9D-4449-883C-A530A04E5BA5.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/D55F57B7-BF55-B241-A533-95562CD64CF6.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/E33381E4-F387-7444-A88D-49CC44264BFA.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/EE34A528-3C06-4742-8085-5AE8B1896DAB.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/EE6813FB-EE1C-0347-9044-EA27DFFB935A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/F0E3D1F3-5EF6-6541-9FAB-470E00AA3D8D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/F13A5BE1-84B5-9047-A396-17510E6CC384.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/F395FC5F-C074-664B-9595-4AFC8B15454D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/F3E82407-A1BE-6241-BFE0-8787B781CEC1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/F4B667AC-97D2-B544-B4EB-BC30A500BC3D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/F4FA27BE-8D03-254E-840F-2FF3BC369D61.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/F648AEA0-B329-5D43-9C87-5A6665CE0332.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/F64CF4A4-E6E5-1D45-BBDB-D462CEDD6B28.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/F685AB5A-9079-9346-AC6F-77616CD29116.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/FBA6F04D-ABEF-EE44-B78C-2D8761EBA5CC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/50000/FFB9C2FF-8BF7-DF41-8025-856D0D1DC500.root',
] )