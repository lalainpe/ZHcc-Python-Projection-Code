#only need hi/2tag

import math
import ROOT 
from ROOT import TCanvas, TString, TFile, TGraph, TF1, TH1D, TLine, TLegend

# step 1: load in the data 
myFile = ROOT.TFile("ZHccProjection.root")

# step 2: define efficiencies and flavour options 

flav = ["cc", "bb", "ll", "bc", "bl", "cl"]

sample = ["ttbar_PwPy8_DiLep", "ZZ", "WZ", "Zjets", "VHcc_NLO", "VHbb_NLO"]

file = "h_Clone_2L_CTagLooseCut_Nominal_Higgs_Mass_inc_hi_xt2pj"
index1 = file.find("inc")
index2 = file.find("hi")

# step 3: organize data by flavour and scale with efficiencies


def hist_bkgd(sample, efficiencies):


    hists_stack = None
    
    for flav in efficiencies:
        
        output_line = file[:index1] + sample + "_" + file[index1:index2] + flav  + "_" + file[index2:]
        
        Eff_Scale = efficiencies[flav]
        
        hists_hi = myFile.Get(output_line)
        
        hists_scaled = hists_hi.Clone()
        
        hists_scaled.Scale(Eff_Scale)
    
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

bkgd_stack = ROOT.THStack()

for b in sample: 

    hists_bkgd = hist_bkgd(b, efficiencies)

    bkgd_stack.Add(hists_bkgd)
    
canvas = TCanvas()
bkgd_stack.Draw('hist')
canvas.Draw()

def signal_significance(Eff_C):
    
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
    
    bkgd_stack = ROOT.THStack()

    for b in sample: 

        hists_bkgd = hist_bkgd(b, efficiencies)

        bkgd_stack.Add(hists_bkgd)

#     print(bkgd_stack)
        
    bkgd_stack_sum = bkgd_stack.GetStack().Last()
    
#     print(bkgd_stack_sum.GetSum())


    hists_VHcc = hist_bkgd("VHcc_NLO", efficiencies)

    hists_VHcc.SetLineColor(ROOT.kOrange)

    signal = hists_VHcc.Integral(hists_VHcc.FindBin(110), hists_VHcc.FindBin(140))

    bkgd = bkgd_stack_sum.Integral(bkgd_stack_sum.FindBin(110), bkgd_stack_sum.FindBin(140))
    
#     print(bkgd)

    s_sqrtb = signal/ math.sqrt(bkgd)

    canvas = TCanvas()
    bkgd_stack.Draw('hist nostack')
    canvas.Draw()

    return signal, bkgd, s_sqrtb, bkgd_stack


gr_s = ROOT.TGraph()

gr_b = ROOT.TGraph()

gr_sb = ROOT.TGraph()

for eff in [x/100. for x in range(0,101,1)]:
    
    x = signal_significance(eff)
    
    gr_s.SetPoint(gr_s.GetN(), eff, x[0])
    
    gr_b.SetPoint(gr_b.GetN(), eff, x[1])
    
    gr_sb.SetPoint(gr_sb.GetN(), eff, x[2])

    
  

my_canvas = TCanvas()
gr_s.Draw('ap')
gr_s.GetYaxis().SetTitle('Signal')
gr_s.GetXaxis().SetTitle('c-tagging eff')
my_canvas.Draw()

my_canvas1 = TCanvas()
gr_sb.Draw('ap')
gr_sb.GetYaxis().SetTitle('s/sqrt(b)')
gr_sb.GetXaxis().SetTitle('c-tagging eff')
my_canvas1.Draw()

my_canvas2 = TCanvas()
gr_b.Draw('ap')
gr_b.GetYaxis().SetTitle('Background')
gr_b.GetXaxis().SetTitle('c-tagging eff')
my_canvas2.Draw()

