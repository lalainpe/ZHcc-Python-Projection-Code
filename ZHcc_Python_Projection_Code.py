#only need hi/2tag


import ROOT 
from ROOT import TCanvas, TString, TFile, TGraph, TF1, TH1D, TLine, TLegend

# step 1: load in the data 
myFile = ROOT.TFile("ZHccProjection.root")

# step 2: define efficiencies and flavour options 
Eff_C = 0.20
Eff_B = 0.25
Eff_L = 0.10 

flav = ["cc", "bb", "ll", "bc", "bl", "cl"]

sample = ["ttbar_PwPy8_DiLep", "ZZ", "WZ", "Zjets", "VHcc_NLO", "VHbb_NLO"]

file = "h_Clone_2L_CTagLooseCut_Nominal_Higgs_Mass_inc_hi_xt2pj"
index1 = file.find("inc")
index2 = file.find("hi")

# step 3: organize data by flavour and scale with efficiencies

def hist_cc(sample):
     
    hists_cc = []
    
    outputs_cc = []

    for i in range(0,5):
        
        output_cc_line = file[:index1] + sample[i] + "_" + file[index1:index2] + "cc"  + "_" + file[index2:]
        
        outputs_cc.append(output_cc_line)
        
    
    for k in range(0,5):
        
        Eff_Scale_cc = Eff_C * Eff_C
        
        hists_cc_hi = myFile.Get(outputs_cc[k])
        
        hists_cc_scaled = hists_cc_hi.Clone()
        
        hists_cc_scaled.Scale(Eff_Scale_cc)

        hists_cc.append(hists_cc_scaled)
     
    hists_cc_map = {hists_cc}
    
    return hists_cc_map


def hist_bb(sample):
 
    hists_bb = []

    outputs_bb = []

    for i in range(0,5):

        output_bb_line = file[:index1] + sample[i] + "_" + file[index1:index2] + "bb"  + "_" + file[index2:]

        outputs_bb.append(output_bb_line)


    for k in range(0,5):

        hists_bb_hi = myFile.Get(outputs_bb[k])

        Eff_Scale_bb = Eff_B * Eff_B

        hists_bb_scaled = hists_bb_hi.Clone()

        hists_bb_scaled.Scale(Eff_Scale_bb)

        hists_bb.append(hists_bb_scaled)
    
    hists_bb_map = {hists_bb}
    
    return hists_bb_map


def hist_ll(sample):

    hists_ll = []

    outputs_ll = []

    for i in range(0,5):

        output_ll_line = file[:index1] + sample[i] + "_" + file[index1:index2] + "ll"  + "_" + file[index2:]

        outputs_ll.append(output_ll_line)


    for k in range(0,5):

        hists_ll_hi = myFile.Get(outputs_ll[k])

        Eff_Scale_ll = Eff_L * Eff_L

        hists_ll_scaled = hists_ll_hi.Clone()

        hists_ll_scaled.Scale(Eff_Scale_ll)

        hists_ll.append(hists_ll_scaled)
    
    hists_ll_map = {hists_ll}
    
    return hists_ll_map 


def hist_bc(sample):

    hists_bc = []

    outputs_bc = []

    for i in range(0,5):

        output_bc_line = file[:index1] + sample[i] + "_" + file[index1:index2] + "bc"  + "_" + file[index2:]

        outputs_bc.append(output_bc_line)


    for k in range(0,5):

        hists_bc_hi = myFile.Get(outputs_bc[k])

        Eff_Scale_bc = Eff_B * Eff_C

        hists_bc_scaled = hists_bc_hi.Clone()

        hists_bc_scaled.Scale(Eff_Scale_bc)

        hists_bc.append(hists_bc_scaled)

    hists_bc_map = {hists_bc}    
        
    return hists_bc_map


def hist_bl(sample):

    hists_bl = []

    outputs_bl = []

    for i in range(0,5):

        output_bl_line = file[:index1] + sample[i] + "_" + file[index1:index2] + "bl"  + "_" + file[index2:]

        outputs_bl.append(output_bl_line)


    for k in range(0,5):

        hists_bl_hi = myFile.Get(outputs_bl[k])

        Eff_Scale_bl = Eff_B * Eff_L

        hists_bl_scaled = hists_bl_hi.Clone()

        hists_bl_scaled.Scale(Eff_Scale_bl)

        hists_bl.append(hists_bl_scaled)
    
    hists_bl_map = {hists_bl}
    
    return hists_bl


def hist_cl(sample):

    hists_cl = {}

    outputs_cl = []

    for i in range(0,5):

        output_cl_line = file[:index1] + sample[i] + "_" + file[index1:index2] + "cl"  + "_" + file[index2:]

        outputs_cl.append(output_cl_line)


    for k in range(0,5):

        hists_cl_hi = myFile.Get(outputs_cl[k])

        Eff_Scale_cl = Eff_C * Eff_L 

        hists_cl_scaled = hists_cl_hi.Clone()

        hists_cl_scaled.Scale(Eff_Scale_cl)

        hists_cl.append(hists_cl_scaled)

    hists_cl_map = {hists_cl}    
        
    return hists_cl


# step 4: use THStack to recompile scaled histograms based on sample type, not flavour 

def hist_ttbar(flav):
     
    hists_ttbar = ROOT.THStack()
    
    outputs_ttbar = []

    for i in range(0,5):
        
        output_ttbar_line = file[:index1] + "ttbar_PwPy8_DiLep" + "_" + file[index1:index2] + flav[i]  + "_" + file[index2:]
        
        outputs_ttbar.append(output_ttbar_line)
    
    for k in range(0,5):
        
        hists_ttbar_cc = hists_cc[outputs_ttbar[k]]
        hists_ttbar_bb = hists_bb[outputs_ttbar[k]]
        hists_ttbar_ll = hists_ll[outputs_ttbar[k]]
        hists_ttbar_bc = hists_bc[outputs_ttbar[k]]
        hists_ttbar_bl = hists_bl[outputs_ttbar[k]]
        hists_ttbar_cl = hists_cl[outputs_ttbar[k]]
        
        hists_ttbar.Add(hists_ttbar_cc)
        hists_ttbar.Add(hists_ttbar_bb)
        hists_ttbar.Add(hists_ttbar_ll)
        hists_ttbar.Add(hists_ttbar_bc)
        hists_ttbar.Add(hists_ttbar_bl)
        hists_ttbar.Add(hists_ttbar_cl)
        
    hists_ttbar.SetFillColor(kOrange)
        
    return hists_ttbar

                       
def hist_ZZ(flav):
     
    hists_ZZ = ROOT.THStack()
    
    outputs_ZZ = []

    for i in range(0,5):
        
        output_ZZ_line = file[:index1] + "ZZ" + "_" + file[index1:index2] + flav[i]  + "_" + file[index2:]
        
        outputs_ZZ.append(output_ZZ_line)
    
    for k in range(0,5):
        
        hists_ZZ_cc = hists_cc.GetHists(outputs_ZZ[k])
        hists_ZZ_bb = hists_bb.GetHists(outputs_ZZ[k])
        hists_ZZ_ll = hists_ll.GetHists(outputs_ZZ[k])
        hists_ZZ_bc = hists_bc.GetHists(outputs_ZZ[k])
        hists_ZZ_bl = hists_bl.GetHists(outputs_ZZ[k])
        hists_ZZ_cl = hists_cl.GetHists(outputs_ZZ[k])
        
        hists_ZZ.Add(hists_ZZ_cc)
        hists_ZZ.Add(hists_ZZ_bb)
        hists_ZZ.Add(hists_ZZ_ll)
        hists_ZZ.Add(hists_ZZ_bc)
        hists_ZZ.Add(hists_ZZ_bl)
        hists_ZZ.Add(hists_ZZ_cl)
    
    hists_ZZ.SetFillColor(kGray+2)
    
    return hists_ZZ

def hist_WZ(flav):
     
    hists_WZ = ROOT.THStack()
    
    outputs_WZ = []

    for i in range(0,5):
        
        output_WZ_line = file[:index1] + "WZ" + "_" + file[index1:index2] + flav[i]  + "_" + file[index2:]
        
        outputs_WZ.append(output_WZ_line)
    
    for k in range(0,5):
        
        hists_WZ_cc = hists_cc.GetHists(outputs_WZ[k])
        hists_WZ_bb = hists_bb.GetHists(outputs_WZ[k])
        hists_WZ_ll = hists_ll.GetHists(outputs_WZ[k])
        hists_WZ_bc = hists_bc.GetHists(outputs_WZ[k])
        hists_WZ_bl = hists_bl.GetHists(outputs_WZ[k])
        hists_WZ_cl = hists_cl.GetHists(outputs_WZ[k])
        
        hists_WZ.Add(hists_WZ_cc)
        hists_WZ.Add(hists_WZ_bb)
        hists_WZ.Add(hists_WZ_ll)
        hists_WZ.Add(hists_WZ_bc)
        hists_WZ.Add(hists_WZ_bl)
        hists_WZ.Add(hists_WZ_cl)
     
    hists_WZ.SetFillColor(kGray+3)
    
    return hists_WZ

def hist_Zjets(flav):
    
    hists_Zjets = ROOT.THStack()
    
    outputs_Zjets = []

    for i in range(0,5):
        
        output_Zjets_line = file[:index1] + "Zjets" + "_" + file[index1:index2] + flav[i]  + "_" + file[index2:]
        
        outputs_Zjets.append(output_Zjets_line)
    
    for k in range(0,5):
        
        hists_Zjets_cc = hists_cc.GetHists(outputs_Zjets[k])
        hists_Zjets_bb = hists_bb.GetHists(outputs_Zjets[k])
        hists_Zjets_ll = hists_ll.GetHists(outputs_Zjets[k])
        hists_Zjets_bc = hists_bc.GetHists(outputs_Zjets[k])
        hists_Zjets_bl = hists_bl.GetHists(outputs_Zjets[k])
        hists_Zjets_cl = hists_cl.GetHists(outputs_Zjets[k])
        
        hists_Zjets.Add(hists_Zjets_cc)
        hists_Zjets.Add(hists_Zjets_bb)
        hists_Zjets.Add(hists_Zjets_ll)
        hists_Zjets.Add(hists_Zjets_bc)
        hists_Zjets.Add(hists_Zjets_bl)
        hists_Zjets.Add(hists_Zjets_cl)
    
    hists_Zjets.SetFillColor(kAzure-4)
    
    return hists_Zjets

def hist_VHcc_NLO(flav):
    
    hists_VHcc_NLO = ROOT.THStack()
    
    outputs_VHcc_NLO = []

    for i in range(0,5):
        
        output_VHcc_NLO_line = file[:index1] + "VHcc_NLO" + "_" + file[index1:index2] + flav[i]  + "_" + file[index2:]
        
        outputs_VHcc_NLO.append(output_VHcc_NLO_line)
    
    for k in range(0,5):
        
        hists_VHcc_NLO_cc = hists_cc.GetHists(outputs_VHcc_NLO[k])
        hists_VHcc_NLO_bb = hists_bb.GetHists(outputs_VHcc_NLO[k])
        hists_VHcc_NLO_ll = hists_ll.GetHists(outputs_VHcc_NLO[k])
        hists_VHcc_NLO_bc = hists_bc.GetHists(outputs_VHcc_NLO[k])
        hists_VHcc_NLO_bl = hists_bl.GetHists(outputs_VHcc_NLO[k])
        hists_VHcc_NLO_cl = hists_cl.GetHists(outputs_VHcc_NLO[k])
        
        hists_VHcc_NLO.Add(hists_VHcc_NLO_cc)
        hists_VHcc_NLO.Add(hists_VHcc_NLO_bb)
        hists_VHcc_NLO.Add(hists_VHcc_NLO_ll)
        hists_VHcc_NLO.Add(hists_VHcc_NLO_bc)
        hists_VHcc_NLO.Add(hists_VHcc_NLO_bl)
        hists_VHcc_NLO.Add(hists_VHcc_NLO_cl)
    
    hists_VHcc_NLO.SetLineColor(kRed)
    hists_VHcc_NLO.SetLineWidth(2)
    
    return hists_VHcc_NLO

def hist_VHbb_NLO(flav):
    
    hists_VHbb_NLO = ROOT.THStack()
    
    outputs_VHbb_NLO = []

    for i in range(0,5):
        
        output_VHbb_NLO_line = file[:index1] + "VHbb_NLO" + "_" + file[index1:index2] + flav[i]  + "_" + file[index2:]
        
        outputs_VHbb_NLO.append(output_VHbb_NLO_line)
    
    for k in range(0,5):
        
        hists_VHbb_NLO_cc = hists_cc.GetHists(outputs_VHbb_NLO[k])
        hists_VHbb_NLO_bb = hists_bb.GetHists(outputs_VHbb_NLO[k])
        hists_VHbb_NLO_ll = hists_ll.GetHists(outputs_VHbb_NLO[k])
        hists_VHbb_NLO_bc = hists_bc.GetHists(outputs_VHbb_NLO[k])
        hists_VHbb_NLO_bl = hists_bl.GetHists(outputs_VHbb_NLO[k])
        hists_VHbb_NLO_cl = hists_cl.GetHists(outputs_VHbb_NLO[k])
        
        hists_VHbb_NLO.Add(hists_VHbb_NLO_cc)
        hists_VHbb_NLO.Add(hists_VHbb_NLO_bb)
        hists_VHbb_NLO.Add(hists_VHbb_NLO_ll)
        hists_VHbb_NLO.Add(hists_VHbb_NLO_bc)
        hists_VHbb_NLO.Add(hists_VHbb_NLO_bl)
        hists_VHbb_NLO.Add(hists_VHbb_NLO_cl)
     
    hists_VHbb_NLO.SetFillColor(kRed)
    
    return hists_VHbb_NLO

# step 5: plot the new histogram. Only interested in hi 2_tag case

#gathering the signal and bkgd values in the range we want to use in plot  

hists_cc = hist_cc(sample)
hists_bb = hist_bb(sample)
hists_ll = hist_ll(sample)
hists_bc = hist_bc(sample)
hists_bl = hist_bl(sample)
hists_cl = hist_cl(sample)

hists_ttbar = hist_ttbar(flav)
# hists_VHcc = hist_VHcc_NLO(flav)

# signal = hists_VHcc_NLO.Integral(hists_VHcc_NLO.FindBin(110), hists_VHcc_NLO.FindBin(140))



bkgd_ttbar = hists_ttbar.Integral(hists_ttbar.FindBin(110), hists_ttbar.FindBin(140))

# bkgd_ZZ = hists_ZZ.Integral(hists_ZZ.FindBin(110), hists_ZZ.FindBin(140))

# bkgd_WZ = hists_WZ.Integral(hists_WZ.FindBin(110), hists_WZ.FindBin(140))

# bkgd_Zjets = hists_Zjets.Integral(hists_Zjets.FindBin(110), hists_Zjets.FindBin(140))

# bkgd_VHbb_NLO = hists_VHbb_NLO.Integral(hists_VHbb_NLO.FindBin(110), hists_VHbb_NLO.FindBin(140))

# bkgd = bkgd_ttbar + bkgd_ZZ + bkgd_WZ + bkgd_Zjets + bkgd_ZZ_VHbb_NLO 



print("signal = ", signal)
print("background = ", bkgd_ttbar)

# cc_hists = hist_cc(sample)

# my_canvas = TCanvas()
# cc_hists.Draw("hist")
# my_canvas.Draw()
# my_canvas.Print("out.pdf")

# bb_hists = hist_bb(sample)

# my_canvas1 = TCanvas()
# bb_hists.Draw("hist")
# my_canvas1.Draw()
# my_canvas1.Print("out.pdf")

#making the signal/bkgd vs. efficiency plots 
