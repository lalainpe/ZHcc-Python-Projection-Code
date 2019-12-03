#vary c_tagging uncertainty 
# Eff_C set to 40% +/- unc_C
# Eff_B set to 25%
# EFF_L set to 10% 


def signal_significance_unc(Eff_C, Eff_B, Eff_L, err_Eff_C, err_Eff_B, err_Eff_L):
    
    efficiencies = {
    "cc" : Eff_C * Eff_C,
    "bb" : Eff_B * Eff_B,
    "ll" : Eff_L * Eff_L,
    "bc" : Eff_B * Eff_C,
    "bl" : Eff_B * Eff_L,
    "cl" : Eff_C * Eff_L,
    }
    
    err_efficiencies = {
    "cc" : (Eff_C + err_Eff_C) * (Eff_C + err_Eff_C),
    "bb" : (Eff_B + err_Eff_B) * (Eff_B + err_Eff_B),
    "ll" : (Eff_L + err_Eff_L) * (Eff_L + err_Eff_L),
    "bc" : (Eff_B + err_Eff_B) * (Eff_C + err_Eff_C),
    "bl" : (Eff_B + err_Eff_B) * (Eff_L + err_Eff_L),
    "cl" : (Eff_C + err_Eff_C) * (Eff_L + err_Eff_L),
    }
    
    bkgd_stack = ROOT.THStack()

    for b in sample: 

        hists_bkgd = hist_bkgd(b, efficiencies)

        bkgd_stack.Add(hists_bkgd)
        
    bkgd_stack_sum = bkgd_stack.GetStack().Last()
    
    bkgd_stack_up = ROOT.THStack()

    for c in sample: 

        hists_bkgd_up = hist_bkgd(c, err_efficiencies)

        bkgd_stack_up.Add(hists_bkgd_up)
        
    bkgd_stack_sum_up = bkgd_stack_up.GetStack().Last()
    

    hists_VHcc = hist_bkgd("VHcc_NLO", efficiencies)
    
    hists_VHcc_up = hist_bkgd("VHcc_NLO", err_efficiencies)

    hists_VHcc.SetLineColor(ROOT.kOrange)
    
    hists_VHcc_up.SetLineColor(ROOT.kOrange)

    signal = hists_VHcc.Integral(hists_VHcc.FindBin(110), hists_VHcc.FindBin(140))

    bkgd = bkgd_stack_sum.Integral(bkgd_stack_sum.FindBin(110), bkgd_stack_sum.FindBin(140))
    
    signal_up = hists_VHcc_up.Integral(hists_VHcc_up.FindBin(110), hists_VHcc_up.FindBin(140))

    bkgd_up = bkgd_stack_sum_up.Integral(bkgd_stack_sum_up.FindBin(110), bkgd_stack_sum_up.FindBin(140))
    
#     s = 100 
#     b = 1000
#     n_test = s + b
    
    unc = bkgd_up - bkgd
    
    n = signal + bkgd
    
    if n < bkgd: 
        
        if unc != 0: 
            
            print('test 1')
            
            s_sqrtb = - math.sqrt(2*(n * math.log((n * (bkgd + unc**2))/(bkgd**2 + n * (unc**2))) - (bkgd**2 / unc**2)*math.log(1 + (unc**2 * (n - bkgd))/(bkgd * (bkgd + unc**2)))))
        
        else: 
            
            print('test 2')
            
            s_sqrtb = - math.sqrt(2*(n * math.log(n/bkgd) - (n - bkgd)))
            
    if n >= bkgd: 
        
        if unc != 0: 
            
#             print('test 3')
#             print("unc>0 n = ", n)
#             print("unc>0 bkgd = ", bkgd)
#             print("unc>0 n/bkgd = ", n/bkgd)
            
            s_sqrtb = math.sqrt(2*(n * math.log((n * (bkgd + unc**2))/(bkgd**2 + n * (unc**2))) - (bkgd**2 / unc**2)*math.log(1 + (unc**2 * (n - bkgd))/(bkgd * (bkgd + unc**2)))))
        
        else:
            
#             print('test 4')
#             print("n = ", n)
#             print("bkgd = ", bkgd)
#             print("n/bkgd = ", n/bkgd)
            
            s_sqrtb = math.sqrt(2*(n * math.log(n/bkgd) - (n - bkgd)))
   
#     if int(n) >= int(bkgd) and unc == 0: 
        
#         s_sqrtb = math.sqrt(2*(n * math.log(n/bkgd) - (n - bkgd)))
        
#     if int(n) < int(bkgd) and unc == 0: 
        
#         s_sqrtb = - math.sqrt(2*(n * math.log(n/bkgd) - (n - bkgd)))
    
#     sig = s / math.sqrt(b)
    
#     print("realitic significance", s_sqrtb)
#     print("simple significance", sig)
    
    return signal, bkgd, s_sqrtb, bkgd_stack

 
    
# simple_sig =  signal_significance_unc(0.41, 0.25, 0.1, 0, 0, 0)   


gr_s_err_C = ROOT.TGraph()

gr_b_err_C = ROOT.TGraph()

gr_sb_err_C = ROOT.TGraph()

for err_C in [n/1000. for n in range(0,50,1)]:
    
    err_C_results = signal_significance_unc(0.4, 0.25, 0.10, err_C, 0, 0)
    
    gr_s_err_C.SetPoint(gr_s_err_C.GetN(), err_C, err_C_results[0])
    
    gr_b_err_C.SetPoint(gr_b_err_C.GetN(), err_C, err_C_results[1])
    
    gr_sb_err_C.SetPoint(gr_sb_err_C.GetN(), err_C, err_C_results[2])
     
#     if err_C == 0:
        
#         print("Sig when err_C = 0:", err_C_results[2])
    
gr_s_err_B = ROOT.TGraph()

gr_b_err_B = ROOT.TGraph()

gr_sb_err_B = ROOT.TGraph()

for err_B in [n/1000. for n in range(0,50,1)]:
    
    err_B_results = signal_significance_unc(0.4, 0.25, 0.10, 0, err_B, 0)
    
    gr_s_err_B.SetPoint(gr_s_err_B.GetN(), err_B, err_B_results[0])
    
    gr_b_err_B.SetPoint(gr_b_err_B.GetN(), err_B, err_B_results[1])
    
    gr_sb_err_B.SetPoint(gr_sb_err_B.GetN(), err_B, err_B_results[2])
    
#     if err_B == 0:
        
#         print("Sig when err_B = 0:", err_B_results[2])
        
gr_s_err_L = ROOT.TGraph()

gr_b_err_L = ROOT.TGraph()

gr_sb_err_L = ROOT.TGraph()

for err_L in [n/1000. for n in range(0,50,1)]:
    
    err_L_results = signal_significance_unc(0.4, 0.25, 0.10, 0, 0, err_L)
    
    gr_s_err_L.SetPoint(gr_s_err_L.GetN(), err_L, err_L_results[0])
    
    gr_b_err_L.SetPoint(gr_b_err_L.GetN(), err_L, err_L_results[1])
    
    gr_sb_err_L.SetPoint(gr_sb_err_L.GetN(), err_L, err_L_results[2])    
    
#     if err_L == 0:
        
#         print("Sig when err_L = 0:", err_L_results[2])
        
gr_s_err = ROOT.TGraph()

gr_b_err = ROOT.TGraph()

gr_sb_err = ROOT.TGraph()

for err in [n/1000. for n in range(0,50,1)]:
    
    err_results = signal_significance_unc(0.4, 0.25, 0.10, err, err, err)
    
    gr_s_err.SetPoint(gr_s_err.GetN(), err, err_results[0])
    
    gr_b_err.SetPoint(gr_b_err.GetN(), err, err_results[1])
    
    gr_sb_err.SetPoint(gr_sb_err.GetN(), err, err_results[2])  

#     if err == 0:
        
#         print("Sig when all err = 0:", err_results[2])  
        
gr_sb_c_zero_err = ROOT.TGraph()

for eff_C in [n/100. for n in range(0,101,1)]:
    
    results_c_zero_err = signal_significance_unc(eff_C, 0.25, 0.10, 0, 0, 0)
    
    gr_sb_c_zero_err.SetPoint(gr_sb_c_zero_err.GetN(), eff_C, results_c_zero_err[2])    
    
#     if eff_C == 0.4: 
        
#         print("Sig when eff_C = 0.4 and all err set constant to 0:", results_c_zero_err[2])

# my_canvas9 = TCanvas()
# gr_s_err_C.Draw('ap')
# gr_s_err_C.GetYaxis().SetTitle('Signal')
# gr_s_err_C.GetXaxis().SetTitle('c-tagging eff uncertainty')
# gr_s_err_C.SetMarkerStyle(8)
# gr_s_err_C.SetMarkerSize(0.5)
# gr_s_err_C.SetMarkerColor(46)
# my_canvas9.Draw()

# my_canvas10 = TCanvas()
# gr_b_err_C.Draw('ap')
# gr_b_err_C.GetYaxis().SetTitle('Background')
# gr_b_err_C.GetXaxis().SetTitle('c-tagging eff uncertainty')
# gr_b_err_C.SetMarkerStyle(8)
# gr_b_err_C.SetMarkerSize(0.5)
# gr_b_err_C.SetMarkerColor(46)
# my_canvas10.Draw()

my_canvas11 = TCanvas()
gr_sb_err_C.Draw('ap')
gr_sb_err_C.Draw("L")
gr_sb_err_C.SetTitle('Significance vs c-tagging eff uncertainty')
gr_sb_err_C.GetYaxis().SetTitle('Significance')
gr_sb_err_C.GetXaxis().SetTitle('c-tagging eff uncertainty')
gr_sb_err_C.SetMarkerStyle(8)
gr_sb_err_C.SetMarkerSize(0.75)
gr_sb_err_C.SetMarkerColor(32)
gr_sb_err_C.SetLineColor(32)
my_canvas11.Draw()

my_canvas12 = TCanvas()
gr_sb_err_B.Draw('ap')
gr_sb_err_B.Draw("L")
gr_sb_err_B.SetTitle('Significance vs b-tagging eff uncertainty')
gr_sb_err_B.GetYaxis().SetTitle('Significance')
gr_sb_err_B.GetXaxis().SetTitle('b-tagging eff uncertainty')
gr_sb_err_B.SetMarkerStyle(8)
gr_sb_err_B.SetMarkerSize(0.75)
gr_sb_err_B.SetMarkerColor(38)
my_canvas12.Draw()

my_canvas13 = TCanvas()
gr_sb_err_L.Draw('ap')
gr_sb_err_L.Draw("L")
gr_sb_err_L.SetTitle('Significance vs l-tagging eff uncertainty')
gr_sb_err_L.GetYaxis().SetTitle('Significance')
gr_sb_err_L.GetXaxis().SetTitle('l-tagging eff uncertainty')
gr_sb_err_L.SetMarkerStyle(8)
gr_sb_err_L.SetMarkerSize(0.75)
gr_sb_err_L.SetMarkerColor(46)
my_canvas13.Draw()

my_canvas14 = TCanvas()
gr_sb_err.Draw('ap')
gr_sb_err.Draw("L")
gr_sb_err.SetTitle('Significance vs all eff uncertainty')
gr_sb_err.GetYaxis().SetTitle('Significance')
gr_sb_err.GetXaxis().SetTitle('all eff uncertainty')
gr_sb_err.SetMarkerStyle(8)
gr_sb_err.SetMarkerSize(0.75)
gr_sb_err.SetMarkerColor(52)
my_canvas14.Draw()

my_canvas15 = TCanvas()
gr_sb_c_zero_err.Draw('ap')
gr_sb_c_zero_err.SetTitle('Significance w/ no eff uncertainty')
gr_sb_c_zero_err.GetYaxis().SetTitle('Significance')
gr_sb_c_zero_err.GetXaxis().SetTitle('c-tagging eff')
gr_sb_c_zero_err.SetMarkerStyle(8)
gr_sb_c_zero_err.SetMarkerSize(0.75)
gr_sb_c_zero_err.SetMarkerColor(32)
my_canvas15.Draw()
