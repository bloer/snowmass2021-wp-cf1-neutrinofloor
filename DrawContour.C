#include "TH2D.h"
#include "TCanvas.h"
#include <fstream>
#include <vector>
#include <iostream>

TH2D* GetContour()
{
  double readval;
  std::vector<double> mass, sigma;
  
  std::ifstream fmass("IndexMass.txt");  
  while(fmass >> readval) mass.push_back(readval);
  std::ifstream fsigma("IndexSig.txt");
  while(fsigma >> readval) sigma.push_back(readval);

  std::cout<<mass.size()<<" "<<sigma.size()<<std::endl;
  TH2D* hist = new TH2D("index", "Index of discovery limit",
                        mass.size()-1, &mass[0], sigma.size()-1, &sigma[0]);
  std::ifstream findex("IndexValues.txt");
  for(size_t y=0; y<sigma.size(); ++y){
    for(size_t x=0; x<mass.size(); ++x){
      findex >> readval;
      std::cout<<mass[x]<<" "<<sigma[y]<<" "<<readval<<std::endl;
      hist->SetBinContent(x+1, y+1, readval);
    }
  }
  return hist;
}

void DrawContour()
{
  TCanvas* can = new TCanvas;
  can->SetLogy();
  can->SetLogx();
  GetContour()->Draw("colz");
}
