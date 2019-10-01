#only need hi/2tag


import ROOT 
from ROOT import TCanvas, TString, TFile, TGraph, TF1, TH1D, TLine, TLegend

# step 1: load in the data 
myFile = ROOT.TFile("ZHccProjection.root")

# step 2: define efficiencies and flavour options 
Eff_C = 0.41
Eff_B = 0.25
Eff_L = 0.10 

flav = ["cc", "bb", "ll", "bc", "bl", "cl"]

jet_type = ["ttbar_PwPy8_DiLep", "ZZ", "WZ", "Zjets", "VHcc_NLO", "VHbb_NLO"]

# step 3: organize data by flavour and scale with efficiencies

def hist_cc(jet_type):
    
    
    #need to get these into TH1D type 
    hists_cc = ROOT.THStack()
    
    outputs_cc = []

    for i in range(0,5):
        
        output_cc_line = file[:index1] + jet_type[i] + "_" + file[index1:index2] + "cc"  + "_" + file[index2:]
        
        outputs_cc.append(output_cc_line)
        
        
    for k in range(0,5):
        
        Eff_Scale_cc = Eff_C * Eff_C
        
        hists_cc_hi = myFile.Get(outputs_cc[k])
        
        hists_cc_scaled = hists_cc_hi * Eff_Scale_cc

        hists_cc.Add(hists_cc_scaled)
        
    return hists_cc
        
def hist_bb(jet_type):
    
    
    #need to get these into TH1D type 
    hists_bb = ROOT.THStack()
    
    outputs_bb = []

    for i in range(0,5):
        
        output_bb_line = file[:index1] + jet_type[i] + "_" + file[index1:index2] + "bb"  + "_" + file[index2:]
        
        outputs_bb.append(output_bb_line)
        
        
    for k in range(0,5):
        
        hists_bb_hi = myFile.Get(outputs_bb[k])

        hists_bb.Add(hists_bb_hi)

        
    Eff_Scale_bb = Eff_B * Eff_B
        
    hists_bb_scaled = hists_bb * Eff_Scale_bb
        
    return hists_bb_scaled
        
def hist_ll(jet_type):
    
    
    #need to get these into TH1D type 
    hists_ll = ROOT.THStack()
    
    outputs_ll = []

    for i in range(0,5):
        
        output_ll_line = file[:index1] + jet_type[i] + "_" + file[index1:index2] + "ll"  + "_" + file[index2:]
        
        outputs_ll.append(output_ll_line)
        
        
    for k in range(0,5):
        
        hists_ll_hi = myFile.Get(outputs_ll[k])

        hists_ll.Add(hists_ll_hi)

    
    Eff_Scale_ll = Eff_L * Eff_L
    
    hists_ll_scaled = hists_ll * Eff_Scale_ll
        
    return hists_ll_scaled 
        
def hist_bc(jet_type):
    
    
    #need to get these into TH1D type 
    hists_bc = ROOT.THStack()
    
    outputs_bc = []

    for i in range(0,5):
        
        output_bc_line = file[:index1] + jet_type[i] + "_" + file[index1:index2] + "bc"  + "_" + file[index2:]
        
        outputs_bc.append(output_bc_line)
        
        
    for k in range(0,5):
        
        hists_bc_hi = myFile.Get(outputs_bc[k])

        hists_bc.Add(hists_bc_hi)

     
    Eff_Scale_bc = Eff_B * Eff_C
    
    hists_bc_scaled = hists_bc * Eff_Scale_bc
        
    return hists_bc_scaled
        
def hist_bl(jet_type):
    
    
    #need to get these into TH1D type 
    hists_bl = ROOT.THStack()
    
    outputs_bl = []

    for i in range(0,5):
        
        output_bl_line = file[:index1] + jet_type[i] + "_" + file[index1:index2] + "bl"  + "_" + file[index2:]
        
        outputs_bl.append(output_bl_line)
        
        
    for k in range(0,5):
        
        hists_bl_hi = myFile.Get(outputs_bl[k])

        hists_bl.Add(hists_bl_hi)

     
    Eff_Scale_bl = Eff_B * Eff_L
    
    hists_bl_scaled = hists_bl * Eff_Scale_bl
        
    return hists_bl_scaled
        
def hist_cl(jet_type):
    
    
    #need to get these into TH1D type 
    hists_cl = ROOT.THStack()
    
    outputs_cl = []

    for i in range(0,5):
        
        output_cl_line = file[:index1] + jet_type[i] + "_" + file[index1:index2] + "cl"  + "_" + file[index2:]
        
        outputs_cl.append(output_cl_line)
        
        
    for k in range(0,5):
        
        hists_cl_hi = myFile.Get(outputs_cl[k])

        hists_cl.Add(hists_cl_hi)

        
    Eff_Scale_cl = Eff_C * Eff_L 
    
    hists_cl_scaled = hists_cl * Eff_Scale_cl
        
    return hists_cl_scaled 

#     hist_Zjets_cl_hi.SetLineWidth(1)
#     hist_Zjets_cl_hi.SetFillColor(6)

#     cl_canvas = TCanvas() 
#     hist_Zjets_cl_hi.Draw() 
#     cl_canvas.Draw()
        

# hist_Zjets_cc_hi = myFile.Get("h_Clone_2L_CTagLooseCut_Nominal_Higgs_Mass_Zjets_inc_cc_hi_xt2pj")

# hist_Zjets_cc_hi.SetLineWidth(1)
# hist_Zjets_cc_hi.SetFillColor(6)

# step 4: use THStack to recompile scaled histograms based on jet type, not flavour 

# step 5: plot the new histogram. Only interested in hi 2_tag case

#right now, just testing plotting ability of histograms as I go 

cc_hists = hist_cc(jet_type)

my_canvas = TCanvas() 
cc_hists.Draw()
my_canvas.Draw()

