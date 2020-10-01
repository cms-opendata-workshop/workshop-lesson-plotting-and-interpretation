import sys

import ROOT

if len(sys.argv)<3:
    print("\nUsage: python dump_and_plot.py <ROOT FILE #1> <ROOT FILE #2>\n") 
    print("Must pass in 2 ROOT files\n")
    exit(-1)


infilenames = sys.argv[1:3]

# Create a canvas to draw on
# canvas(name, title, x (upper corner), y (upper corner), width (pixels), height (pixels))
canvas = ROOT.TCanvas("canvas","canvas",10,10,1200,800)

# Divide it into 1x1 grid
canvas.Divide(2,2)

#################################################################
# We will plot the pT,eta,phi, and charge of one of the muons
# We need histograms for each plot
#################################################################
# Create some histograms to fill for the 
# TH1F(name, title, # of bins, lo edge, hi edge)
#
# When we make them, we need to give them unique names
hpt_1 = []
heta_1= []
hphi_1= []
hq_1= []

hpt_1.append(ROOT.TH1F("hpt_1_0","Muon pT",50,0,150))
hpt_1.append(ROOT.TH1F("hpt_1_0","Muon pT",50,0,150))

heta_1.append(ROOT.TH1F("heta_1_0","Muon eta",50,-3,3))
heta_1.append(ROOT.TH1F("heta_1_1","Muon eta",50,-3,3))

hphi_1.append(ROOT.TH1F("hphi_1_0","Muon phi",50,-4,4))
hphi_1.append(ROOT.TH1F("hphi_1_1","Muon phi",50,-4,4))

hq_1.append(ROOT.TH1F("hq_1_0","Muon charge",5,-2.5,2.5))
hq_1.append(ROOT.TH1F("hq_1_1","Muon charge",5,-2.5,2.5))

for idx,infilename in enumerate(infilenames):
    f = ROOT.TFile(infilename)

    f.ls()

    t = f.Get('Events')

    # Get the number of entries in this file
    nentries = t.GetEntries()

    # Loop over the entries (events/collisions)
    for i in range(nentries):

        # Get each entry and fill the TTree
        t.GetEvent(i)

        # Fill the histograms as we loop over each event
        hpt_1[idx].Fill(t.pt_1)
        heta_1[idx].Fill(t.eta_1)
        hphi_1[idx].Fill(t.phi_1)
        hq_1[idx].Fill(t.q_1)


# Normalize the histograms so you can compare them directly
# Also set the line colors to distinguish them
hpt_1[0].Scale(1.0/hpt_1[0].GetEntries())
hpt_1[1].Scale(1.0/hpt_1[1].GetEntries())

hpt_1[0].SetLineColor(ROOT.kRed)
hpt_1[1].SetLineColor(ROOT.kBlack)

heta_1[0].Scale(1.0/heta_1[0].GetEntries())
heta_1[1].Scale(1.0/heta_1[1].GetEntries())

heta_1[0].SetLineColor(ROOT.kRed)
heta_1[1].SetLineColor(ROOT.kBlack)

hphi_1[0].Scale(1.0/hphi_1[0].GetEntries())
hphi_1[1].Scale(1.0/hphi_1[1].GetEntries())

hphi_1[0].SetLineColor(ROOT.kRed)
hphi_1[1].SetLineColor(ROOT.kBlack)

hq_1[0].Scale(1.0/hq_1[0].GetEntries())
hq_1[1].Scale(1.0/hq_1[1].GetEntries())

hq_1[0].SetLineColor(ROOT.kRed)
hq_1[1].SetLineColor(ROOT.kBlack)



# Go to each block on the canvas and draw a histogram
canvas.cd(1)
hpt_1[0].Draw()
hpt_1[1].Draw("same")

canvas.cd(2)
heta_1[0].Draw()
heta_1[1].Draw("same")

canvas.cd(3)
hphi_1[0].Draw()
hphi_1[1].Draw("same")

canvas.cd(4)
hq_1[0].Draw()
hq_1[1].Draw("same")

# We need this line for the plot to stay active sometimes
ROOT.gPad.Update()

# Save the plot as an image. This is useful in case our 
# canvas doesn't stay active
canvas.SaveAs("plots/comparison_plots.png")

        





