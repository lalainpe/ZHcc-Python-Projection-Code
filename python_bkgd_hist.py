import math
import ROOT 
from ROOT import TCanvas, TString, TFile, TGraph, TF1, TH1D, TLine, TLegend

myFile = ROOT.TFile("ZHccProjection.root")


flav = ["cc", "bb", "ll", "bc", "bl", "cl"]

sample = ["ttbar_PwPy8_DiLep", "ZZ", "WZ", "Zjets", "VHcc_NLO", "VHbb_NLO"]

file = "h_Clone_2L_CTagLooseCut_Nominal_Higgs_Mass_inc_hi_xt2pj"
index1 = file.find("inc")
index2 = file.find("hi")


def hist_bkgd(sample, efficiencies):


    hists_stack = None
    
    for flav in efficiencies:
        
        output_line = file[:index1] + sample + "_" + file[index1:index2] + flav  + "_" + file[index2:]
        
        hists_hi = myFile.Get(output_line)
        
        hists_scaled = hists_hi.Clone()
        
        hists_scaled.Scale(efficiencies[flav])
        
        #print("efficiencies", efficiencies[flav])
    
        if hists_stack == None:
            
            hists_stack = hists_scaled
            
        else:
            
            hists_stack.Add(hists_scaled)
    
    return hists_stack

Eff_C = 0.41
Eff_B = 0.25
Eff_L = 0.10 
    
efficiencies = {
    "cc" : Eff_C * Eff_C,
    "bb" : Eff_B * Eff_B,
    "ll" : Eff_L * Eff_L,
    "bc" : Eff_B * Eff_C,
    "bl" : Eff_B * Eff_L,
    "cl" : Eff_C * Eff_L,
}


bkgd_label_stack = ROOT.THStack()

hists_ttbar = hist_bkgd("ttbar_PwPy8_DiLep", efficiencies)
hists_ZZ = hist_bkgd("ZZ", efficiencies)
hists_WZ = hist_bkgd("WZ", efficiencies)
hists_Zjets = hist_bkgd("Zjets", efficiencies)
hists_VHbb = hist_bkgd("VHbb_NLO", efficiencies)

signal_VHcc = hist_bkgd("VHcc_NLO", efficiencies)

hists_ttbar.SetFillColor(33)
hists_ZZ.SetFillColor(34)
hists_WZ.SetFillColor(30)
hists_Zjets.SetFillColor(40)
hists_VHbb.SetFillColor(29)

signal_VHcc.SetLineColor(2)
signal_VHcc.SetLineWidth(4)
signal_VHcc.Scale(100)  #signal scaled by 100 to show up on plot

bkgd_label_stack.Add(hists_ttbar)
bkgd_label_stack.Add(hists_ZZ)
bkgd_label_stack.Add(hists_WZ)
bkgd_label_stack.Add(hists_Zjets)
bkgd_label_stack.Add(hists_VHbb)

Leg = ROOT.TLegend(0.64,0.9,0.84,0.9-7*0.05)

Leg.SetTextFont(42)
Leg.SetTextSize(0.04)
Leg.SetBorderSize(0)
Leg.SetFillStyle(0)

Leg.AddEntry(hists_ttbar, "ttbar")
Leg.AddEntry(hists_ZZ, "ZZ")
Leg.AddEntry(hists_WZ, "WZ")
Leg.AddEntry(hists_Zjets, "Zjets")
Leg.AddEntry(hists_VHbb, "VHbb")
Leg.AddEntry(signal_VHcc, "VHcc")


bkgd_canvas = TCanvas()
bkgd_label_stack.Draw("hist")
signal_VHcc.Draw('same')
Leg.Draw()
bkgd_label_stack.GetYaxis().SetTitle('Events / 10 GeV')
bkgd_label_stack.GetXaxis().SetTitle('m_{cc} [GeV]')
bkgd_label_stack.SetTitle("hi_2tag")
bkgd_canvas.Draw()
