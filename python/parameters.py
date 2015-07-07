### Parameters to be used in the configuration files
import FWCore.ParameterSet.Config as cms

_DiPhotonTag				=	cms.untracked.InputTag('flashggDiPhotons')
_JetTag						=	cms.untracked.InputTag('flashggJets')
_rhoFixedGridCollection		=	cms.untracked.InputTag('fixedGridRhoAll')
#0: Pho1, 1: Pho2
_PhotonPtOverDiPhotonMass	=	cms.untracked.vdouble( 0.333, 0.25 )
#0: First upper boundary (EB), 1: second upper boundary (EE) (only (1) is used to cut on both)
_PhotonEta					=	cms.untracked.vdouble(1.479, 2.50)
#0: Pho1 EB, 1: Pho1 EE, 2: Pho2 EB, 3: Pho2 EE
_PhotonHoverE				=	cms.untracked.vdouble(0.012, 0.023, 0.012, 0.023 )
#0: Pho1 EB, 1: Pho1 EE, 2: Pho2 EB, 3: Pho2 EE
_PhotonSieie				=	cms.untracked.vdouble(0.0100, 0.0267, 0.0100, 0.0267 )
#0: Pho1 EB, 1: Pho1 EE, 2: Pho2 EB, 3: Pho2 EE
_PhotonR9					=	cms.untracked.vdouble(0., 0.)
#0: Pho1 EB, 1: Pho1 EE, 2: Pho2 EB, 3: Pho2 EE
_PhotonChargedIso			=	cms.untracked.vdouble(1.79, 1.09, 1.79, 1.09 )
#0: Pho1 EB, 1: Pho1 EE, 2: Pho2 EB, 3: Pho2 EE
_PhotonNeutralIso			=	cms.untracked.vdouble(0.16, 4.31, 0.16, 4.31)
#0: Pho1 EB, 1: Pho1 EE, 2: Pho2 EB, 3: Pho2 EE
_PhotonPhotonIso			=	cms.untracked.vdouble(1.90, 1.90, 1.90, 1.90)
#0: Pho1, 1: Pho2
_PhotonElectronVeto			=	cms.untracked.vint32(1, 1)
#0: Pho1, 1: Pho2
_PhotonDoID					=	cms.untracked.vint32(0 , 0)
#0: Pho1, 1: Pho2
_PhotonDoISO				=	cms.untracked.vint32(0 , 0)
#0: lower boundary for dipho pt
_DiPhotonPt					=	cms.untracked.vdouble(0.)
#0: upper boundary
_DiPhotonEta				=	cms.untracked.vdouble(2.5)
#0: DiPhoton mass window lower boundary, 1: upper boundary
_DiPhotonMassWindow			=	cms.untracked.vdouble(80., 165.)
#If you only want to look at first diphoton pair: 1; if all: 0
_DiPhotonOnlyFirst			=	cms.untracked.uint32(1)
#0: jet1, 1: jet2
_JetPtOverDiJetMass			=	cms.untracked.vdouble(25., 25.)
#0: jet1, 1: jet2
_JetEta						=	cms.untracked.vdouble(2.5, 2.5)
#0: lowest b-tag requirement for any jet (default 0), standard b-tag cut (loose, medium, tight) 
_JetBDiscriminant			=	cms.untracked.vdouble(-50., 0.87)
#0: jet1, 1: jet2
_JetDoPUID					=	cms.untracked.vint32(1, 1)
#Number of required jets passing requirements in JetBDiscriminant
_n_bJets					=	cms.untracked.uint32(0)
#0: lower boundary for dijet pt
_DiJetPt					=	cms.untracked.vdouble(10.)
#0: upper boundary for dijet pt
_DiJetEta					=	cms.untracked.vdouble(20.)
#0: DiJet mass window lower boundary, 1: upper boundary
_DiJetMassWindow			=	cms.untracked.vdouble(40., 200.)
#0: 4-candidate mass window lower boundary, 1: upper boundary
_CandidateMassWindow		=	cms.untracked.vdouble(0, 9000.)
#0 4-candidate pt lower bound
_CandidatePt				=	cms.untracked.vdouble(0.)
#0 4-candidate eta upper bound
_CandidateEta				=	cms.untracked.vdouble(20.)
#string for btag algorithm
_bTagType					=	cms.untracked.string('pfCombinedInclusiveSecondaryVertexV2BJetTags')