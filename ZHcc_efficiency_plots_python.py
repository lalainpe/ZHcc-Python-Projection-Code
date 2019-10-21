#only need hi/2tag

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


def signal_significance(Eff_C, Eff_B, Eff_L):
    
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
        
    bkgd_stack_sum = bkgd_stack.GetStack().Last()

    hists_VHcc = hist_bkgd("VHcc_NLO", efficiencies)

    hists_VHcc.SetLineColor(ROOT.kOrange)

    signal = hists_VHcc.Integral(hists_VHcc.FindBin(110), hists_VHcc.FindBin(140))

    bkgd = bkgd_stack_sum.Integral(bkgd_stack_sum.FindBin(110), bkgd_stack_sum.FindBin(140))

    s_sqrtb = signal/math.sqrt(bkgd)


    return signal, bkgd, s_sqrtb, bkgd_stack



#vary c-tagging

gr_s_c = ROOT.TGraph()

gr_b_c = ROOT.TGraph()

gr_sb_c = ROOT.TGraph()

for eff_C in [n/100. for n in range(0,101,1)]:
    
    results_c = signal_significance(eff_C, 0.25, 0.10)
    
    gr_s_c.SetPoint(gr_s_c.GetN(), eff_C, results_c[0])
    
    gr_b_c.SetPoint(gr_b_c.GetN(), eff_C, results_c[1])
    
    gr_sb_c.SetPoint(gr_sb_c.GetN(), eff_C, results_c[2])


#vary b_tagging

gr_s_b = ROOT.TGraph()

gr_b_b = ROOT.TGraph()

gr_sb_b = ROOT.TGraph()

for eff_B in [n/100. for n in range(0,101,1)]:
    
    results_b = signal_significance(0.41, eff_B, 0.10)
    
    gr_s_b.SetPoint(gr_s_b.GetN(), eff_B, results_b[0])
    
    gr_b_b.SetPoint(gr_b_b.GetN(), eff_B, results_b[1])
    
    gr_sb_b.SetPoint(gr_sb_b.GetN(), eff_B, results_b[2])

    
#vary l-tagging
        
gr_s_l = ROOT.TGraph()

gr_b_l = ROOT.TGraph()

gr_sb_l = ROOT.TGraph()

for eff_L in [n/100. for n in range(0,101,1)]:
    
    results_l = signal_significance(0.41, 0.25, eff_L)
    
    gr_s_l.SetPoint(gr_s_l.GetN(), eff_L, results_l[0])
    
    gr_b_l.SetPoint(gr_b_l.GetN(), eff_L, results_l[1])
    
    gr_sb_l.SetPoint(gr_sb_l.GetN(), eff_L, results_l[2])
    


my_canvas = TCanvas()
gr_s_c.Draw('ap')
gr_s_c.GetYaxis().SetTitle('Signal')
gr_s_c.GetXaxis().SetTitle('c-tagging eff')
gr_s_c.SetMarkerStyle(8)
gr_s_c.SetMarkerSize(0.5)
gr_s_c.SetMarkerColor(32)
my_canvas.Draw()

my_canvas1 = TCanvas()
gr_sb_c.Draw('ap')
gr_sb_c.GetYaxis().SetTitle('S/\sqrt{B}')
gr_sb_c.GetXaxis().SetTitle('c-tagging eff')
gr_sb_c.SetMarkerStyle(8)
gr_sb_c.SetMarkerSize(0.5)
gr_sb_c.SetMarkerColor(32)
my_canvas1.Draw()

my_canvas2 = TCanvas()
gr_b_c.Draw('ap')
gr_b_c.GetYaxis().SetTitle('Background')
gr_b_c.GetXaxis().SetTitle('c-tagging eff')
gr_b_c.SetMarkerStyle(8)
gr_b_c.SetMarkerSize(0.5)
gr_b_c.SetMarkerColor(32)
my_canvas2.Draw()

my_canvas3 = TCanvas()
gr_s_b.Draw('ap')
gr_s_b.GetYaxis().SetTitle('Signal')
gr_s_b.GetXaxis().SetTitle('b-tagging eff')
gr_s_b.SetMarkerStyle(8)
gr_s_b.SetMarkerSize(0.5)
gr_s_b.SetMarkerColor(46)
my_canvas3.Draw()

my_canvas4 = TCanvas()
gr_sb_b.Draw('ap')
gr_sb_b.GetYaxis().SetTitle('S/\sqrt{B}')
gr_sb_b.GetXaxis().SetTitle('b-tagging eff')
gr_sb_b.SetMarkerStyle(8)
gr_sb_b.SetMarkerSize(0.5)
gr_sb_b.SetMarkerColor(46)
my_canvas4.Draw()

my_canvas5 = TCanvas()
gr_b_b.Draw('ap')
gr_b_b.GetYaxis().SetTitle('Background')
gr_b_b.GetXaxis().SetTitle('b-tagging eff')
gr_b_b.SetMarkerStyle(8)
gr_b_b.SetMarkerSize(0.5)
gr_b_b.SetMarkerColor(46)
my_canvas5.Draw()

my_canvas6 = TCanvas()
gr_s_l.Draw('ap')
gr_s_l.GetYaxis().SetTitle('Signal')
gr_s_l.GetXaxis().SetTitle('l-tagging eff')
gr_s_l.SetMarkerStyle(8)
gr_s_l.SetMarkerSize(0.5)
gr_s_l.SetMarkerColor(38)
my_canvas6.Draw()

my_canvas7 = TCanvas()
gr_sb_l.Draw('ap')
gr_sb_l.GetYaxis().SetTitle('S/\sqrt{B}')
gr_sb_l.GetXaxis().SetTitle('l-tagging eff')
gr_sb_l.SetMarkerStyle(8)
gr_sb_l.SetMarkerSize(0.5)
gr_sb_l.SetMarkerColor(38)
my_canvas7.Draw()

my_canvas8 = TCanvas()
gr_b_l.Draw('ap')
gr_b_l.GetYaxis().SetTitle('Background')
gr_b_l.GetXaxis().SetTitle('l-tagging eff')
gr_b_l.SetMarkerStyle(8)
gr_b_l.SetMarkerSize(0.5)
gr_b_l.SetMarkerColor(38)
my_canvas8.Draw()



