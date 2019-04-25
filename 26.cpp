#include <fstream>
#include <iostream>
#include <random>
#include <cmath>
#include <string.h>
#include <stdlib.h>


using namespace std; 

void explicito(float paso, int sup, int w, string archivo);
void runge(float paso, int sup, int w, string archivo);
void rana(float paso, int sup, int w, string archivo);


int main()
{ 
  explicito(0.01, 30, 1, "explicito_001.dat");
  explicito(0.1, 30, 1, "explicito_01.dat");
  explicito(1, 30, 1, "explicito_1.dat"); 
  runge(0.01, 30, 1, "runge_001.dat");
  runge(0.1, 30, 1, "runge_01.dat");
  runge(1, 30, 1, "runge_1.dat");
  rana(0.01, 30, 1, "rana_001.dat");
  rana(0.1, 30, 1, "rana_01.dat");
  rana(1, 30, 1, "rana_1.dat");   
  return 0;
}

void explicito(float paso, int sup, int w, string archivo)
{
  float yn1;
  float yn;
  float zn1;
  float zn;  
  float tn;
  float tn1;  
  int limo;
  float lim; 
  yn=1;
  tn=0;
  zn=0;  
  lim=sup/(w*paso);
  limo=static_cast<int>(lim);
  ofstream outfile;
  outfile.open(archivo);  
  for (int i=0;i<limo;i++)
  {
    float f;
    f=-(w*w)*yn;
    zn1=zn+(paso*f);   
    yn1=yn+(paso*zn); 
    tn1=tn+paso; 
    outfile << tn << " " << zn << " " << yn << endl;
    yn=yn1;
    zn=zn1;  
    tn=tn1;  
  }
}

void runge(float paso, int sup, int w, string archivo)
{
    float tn;
    float yn;
    float zn;
    float tn1;
    float yn1;
    float zn1;
    float x;
    float x0;
    float x1;
    float x2;
    float x3;
    int limo;
    float lim; 
    yn=1;
    tn=0;
    zn=0; 
    lim=sup/(w*paso);
    limo=static_cast<int>(lim);
    ofstream outfile;
    outfile.open(archivo);

    for (int i=0;i<limo;i++)
    {
        x0=-pow(w,2)*yn;
        x1=-pow(w,2)*(yn+(paso*x0/2));
        x2=-pow(w,2)*(yn+(paso*x1/2));
        x3=-pow(w,2)*(yn+(paso*x2/2));
        x=(x0+2*x1+2*x2+x3)/6;
        zn1=zn+(paso*x);
        yn1=yn+(paso*zn);
        tn1=tn+paso;
        outfile << tn << " " << zn << " " << yn << endl;
        yn=yn1;
        zn=zn1;
        tn=tn1;
    }
}

void rana(float paso, int sup, int w, string archivo)
{
  float yn1;
  float yn;
  float zn12;
  float zn22;  
  float zn;  
  float tn;
  float tn1;  
  int limo;
  float lim; 
  yn=1;
  tn=0;
  zn=0;  
  lim=sup/(w*paso);
  limo=static_cast<int>(lim);
  ofstream outfile;
  outfile.open(archivo);  
  for (int i=0;i<limo;i++)
  {
    zn12=zn-((paso/2)*w*w*yn);   
    yn1=yn+(paso*zn12);
    zn22=zn12-((paso/2)*w*w*yn1);  
    tn1=tn+paso; 
    outfile << tn << " " << zn << " " << yn << endl;
    yn=yn1;
    zn=zn22;  
    tn=tn1;  
  }
}