import sys

import ROOT

if len(sys.argv)<2:
    print("\nUsage: python dump_and_plot.py <ROOT FILE>\n") 
    print("Must pass in a ROOT file\n")
    exit(-1)


infilename = sys.argv[1]

f = ROOT.TFile(infilename)

f.ls()

t = f.Get('Events')

# Comment out this line if you don't want to see all the output
# of what is in the tree
t.Print()

#################################################################
# Draw a single plot
#
# We will plot the pT of one of the muons
#################################################################

# To uncomment this, put a # in front of the following '''
# and a # in front of the matching ''' surrounding this section.

'''

# Create a canvas to draw on
# canvas(name, title, x (upper corner), y (upper corner), width (pixels), height (pixels))
canvas = ROOT.TCanvas("canvas","canvas",10,10,400,400)

# Divide it into 1x1 grid
canvas.Divide(1,1)

# Create a histogram to fill for the 
# TH1F(name, title, # of bins, lo edge, hi edge)
hpt_1 = ROOT.TH1F("hpt_1","Muon pT",30,0,100)

# Get the number of entries in this file
nentries = t.GetEntries()

# Loop over the entries (events/collisions)
for i in range(nentries):

    # Get each entry and fill the TTree
    t.GetEvent(i)

    # Fill the histogram with each event
    hpt_1.Fill(t.pt_1)


# Go to the first block on the canvas
canvas.cd(1)
# Draw the histogram on there
hpt_1.Draw()

# We need this line for the plot to stay active sometimes
ROOT.gPad.Update()

# Save the plot as an image. This is useful in case our 
# canvas doesn't stay active
canvas.SaveAs("plots/TEST_pt_1.png")
'''
################################################################################

    

#################################################################
# Draw a four plots
#
# We will plot the pT,eta,phi, and charge of one of the muons
#################################################################

# To uncomment this, put a # in front of the following '''
# and a # in front of the matching ''' surrounding this section.

'''
# Create a canvas to draw on
# canvas(name, title, x (upper corner), y (upper corner), width (pixels), height (pixels))
canvas = ROOT.TCanvas("canvas","canvas",10,10,1200,800)

# Divide it into 1x1 grid
canvas.Divide(2,2)

# Create some histograms to fill for the 
# TH1F(name, title, # of bins, lo edge, hi edge)
hpt_1 = ROOT.TH1F("hpt_1","Muon pT",50,0,100)
heta_1 = ROOT.TH1F("heta_1","Muon eta",50,-3,3)
hphi_1 = ROOT.TH1F("hphi_1","Muon phi",50,-4,4)
hq_1 = ROOT.TH1F("hq_1","Muon charge",5,-2.5,2.5)

# Get the number of entries in this file
nentries = t.GetEntries()

# Loop over the entries (events/collisions)
for i in range(nentries):

    # Get each entry and fill the TTree
    t.GetEvent(i)

    # Fill the histograms as we loop over each event
    hpt_1.Fill(t.pt_1)
    heta_1.Fill(t.eta_1)
    hphi_1.Fill(t.phi_1)
    hq_1.Fill(t.q_1)


# Go to each block on the canvas and draw a histogram
canvas.cd(1)
hpt_1.Draw()

canvas.cd(2)
heta_1.Draw()

canvas.cd(3)
hphi_1.Draw()

canvas.cd(4)
hq_1.Draw()

# We need this line for the plot to stay active sometimes
ROOT.gPad.Update()

# Save the plot as an image. This is useful in case our 
# canvas doesn't stay active
canvas.SaveAs("plots/TEST_muon_plots.png")

'''    





