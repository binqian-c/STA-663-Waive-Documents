/*********************************************************************
 File:     chromakey.cpp

 Author:   Binqian Chai

 Email address: binqianc@usc.edu

 Usage: program_name in.bmp background.bmp dist_threshold out1.bmp out2.bmp

 Notes:
 This program performs the chroma key operation on an input 
 using two different methods.

 Method 1 Utilize a user-defined distance threshold from the
          chromakey value as a discriminator

 Method 2 Devise a method that to determine the chromakey mask
          that doesn't require a user-input threshold

********************************************************************/

#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include "bmplib.h"

using namespace std;

// Prototypes
// IMPORTANT: you must exactly use these input types, function names, and 
// return types. Otherwise the grader can't test them.
void method1(unsigned char inImage[][SIZE][RGB], 
	     bool mask[][SIZE],
	     double threshold);

void method2(unsigned char inImage[][SIZE][RGB], 
	     bool mask[][SIZE]);

void replace(bool mask[][SIZE],
	     unsigned char inImage[][SIZE][RGB],
	     unsigned char bgImage[][SIZE][RGB],
	     unsigned char outImage[][SIZE][RGB]);

int main(int argc, char *argv[])
{
  // Image data array
  // Note:  DON'T use the static keyword except where we expressly say so.
  //        It puts the large array in a separate, fixed, area of memory. 
  //        It is bad practice. But useful until we have dynamic allocation.
  static unsigned char inputImage[SIZE][SIZE][RGB];
  static unsigned char bgrndImage[SIZE][SIZE][RGB];
  static unsigned char outputImage[SIZE][SIZE][RGB];
  static bool chromaMask[SIZE][SIZE];

  double threshold;

  if (argc < 6) {
    cerr << "usage: program_name in.bmp background.bmp dist_threshold " 
         << "out1.bmp out2.bmp" << endl;
    return 0;
  }
	
  if (readRGBBMP(argv[1], inputImage)) {
    cerr << "Error reading file: " << argv[1] << endl;
    return 1;
  }

  if (readRGBBMP(argv[2], bgrndImage)) {
    cout << "Error reading file: " << argv[2] << endl;
    return 1;
  }
  
  // Write code to convert the threshold (argv[3])
  //  from string format to a double and assign the 'threshold'
  threshold = atof(argv[3]);


  // Call Method 1 Function
  method1(inputImage, chromaMask, threshold);

  // Produce the output by calling replace()
  replace(chromaMask, inputImage, bgrndImage, outputImage);


  // Write the output image to a file using the filename argv[4]
  if (writeRGBBMP(argv[4], outputImage)) {
    cout << "Error writing file: " << argv[4] << endl;
    exit(1);
  }	

  // Call Method 2 Function
  method2(inputImage, chromaMask);

  // Produce the output by calling replace()
  replace(chromaMask, inputImage, bgrndImage, outputImage);

  // Write the output image to a file using the filename argv[5]
  if (writeRGBBMP(argv[5], outputImage)) {
    cout << "Error writing file: " << argv[5] << endl;
    exit(1);
  }	

  return 0;
}



// Use user-provided threshold for chroma-key distance
// The "output" of this method is to produce a valid mask array
//  where entries in the mask array are 1 for foreground image
//  and 0 for 'background'
void method1(unsigned char inImage[][SIZE][RGB], 
	     bool mask[][SIZE],
	     double threshold)
{
  // set three variables to store each total RGB values of the green-background
  int red_total = 0;
  int green_total = 0;
  int blue_total = 0;
  // set a variable to count the number of pixels the loops go through to find the average RGB values
  int count = 0;

  // loop through the 0th row
  for (int col1 = 0; col1 < SIZE; col1++) {
    // add up each rgb values of each pixel to rgb total
    red_total += inImage[0][col1][0];
    green_total += inImage[0][col1][1];
    blue_total += inImage[0][col1][2];
    count += 1;
  }

  // loop through the 0th column
  for (int row1 = 0; row1 < SIZE; row1++) {
    // add up each rgb values of each pixel to rgb total
    red_total += inImage[row1][0][0];
    green_total += inImage[row1][0][1];
    blue_total += inImage[row1][0][2];
    count += 1;
  }

  // average the RGB values；cast rgb totals to double to make the average value more precise
  double red_avg = static_cast<double>(red_total)/count;
  double green_avg = static_cast<double>(green_total)/count;
  double blue_avg = static_cast<double>(blue_total)/count;

  // loop through each pixel of the input image and create the mask
  for (int row = 0; row < SIZE; row++) {
    for(int col = 0; col < SIZE; col++) {
      // set three varibales to hold the rgb values separately
      int red = inImage[row][col][0];
      int green = inImage[row][col][1];
      int blue = inImage[row][col][2];
      // calculate the distance of each pixel to the average rgb values
      double distance = sqrt(pow(red-red_avg,2) + pow(green-green_avg,2) + pow(blue-blue_avg,2));
      // when the distance is inside the threshold
      if (distance < threshold) {
        // mask the pixel as 0
        mask[row][col] = 0;
      }
      // when the distance is outside the threshold
      else {
        // mask the pixel as 0
        mask[row][col] = 1;
      }
    }
  }

}

// Devise a method to automatically come up with a threshold
//  for the chroma key determination
// The "output" of this method is to produce a valid mask array
//  where entries in the mask array are 1 for foreground image
//  and 0 for 'background'
void method2(unsigned char inImage[][SIZE][RGB], 
	     bool mask[][SIZE])  
{
  // set [0][0] pixel as the base point and set three variables to hold each rgb values
  int r_initial = inImage[0][0][0];
  int g_initial = inImage[0][0][1];
  int b_initial = inImage[0][0][2];
  // set three variables to hold for the maximum differences 
  // between the based point rgb values and the assumed green-background rgb values
  // initialize them as 0.0; the type double helps to make them more precise
  double diff_r = 0.0;
  double diff_g = 0.0;
  double diff_b = 0.0;

  // loop through the top-most rows (assumed green-background)
  // the limit for row1 is found "safe" based on the seven pictures given
  for (int row1 = 0; row1 < 3; row1++) {
    for (int col1 = 0; col1 < SIZE; col1++) {
      // do absolute difference calculation to find the maximum difference
      double r1 = inImage[row1][col1][0];
      double g1 = inImage[row1][col1][1];
      double b1 = inImage[row1][col1][2];
      double diff_r1 = abs(r1 - r_initial);
      double diff_g1 = abs(g1 - g_initial);
      double diff_b1 = abs(b1 - b_initial);
      // when the "new" difference is greater than the current difference max
      // update the difference max value to the current "new" difference
      if (diff_r1 > diff_r) {
        diff_r = diff_r1;
      }
      if (diff_g1 > diff_g) {
        diff_g = diff_g1;
      }
      if (diff_b1 > diff_b) {
        diff_b = diff_b1;
      }
    }
  }

  // loop through the left-most columns (assumed green-background)
  // the limit for col2 is found "safe" based on the seven pictures given
  for (int col2 = 0; col2 < 10; col2++) {
    for (int row2 = 0; row2 < SIZE; row2++) {
      // do absolute difference calculation to find the maximum difference
      double r2 = inImage[row2][col2][0];
      double g2 = inImage[row2][col2][1];
      double b2 = inImage[row2][col2][2];
      double diff_r2 = abs(r2 - r_initial);
      double diff_g2 = abs(g2 - g_initial);
      double diff_b2 = abs(b2 - b_initial);
      // when the "new" difference is greater than the current difference max
      // update the difference max value to the current "new" difference
      if (diff_r2 > diff_r) {
        diff_r = diff_r2;
      }
      if (diff_g2 > diff_g) {
        diff_g = diff_g2;
      }
      if (diff_b2 > diff_b) {
        diff_b = diff_b2;
      }
    }
  }

  // loop through each pixel of the input image and create the mask
  for (int row = 0; row < SIZE; row++) {
    for(int col = 0; col < SIZE; col++) {
      // set three varibales to hold the rgb values separately
      int red = inImage[row][col][0];
      int green = inImage[row][col][1];
      int blue = inImage[row][col][2];
      // calculate the difference of each pixel to the base point rgb values
      double diff_r4 = abs(red - r_initial);
      double diff_g4 = abs(green - g_initial);
      double diff_b4 = abs(blue - b_initial);
      // when the difference for all three rgb values is within the max difference
      // the pixel should be marked as 0 (to be removed and be replaced by bgImage)
      if (diff_r4 <= diff_r && diff_g4 <= diff_g && diff_b4 <= diff_b) {
        mask[row][col] = 0;
      }
      // when the difference for all three rgb values is not within the max difference
      // the pixel should be marked as 1 (to be hold with inputImage)
      else {
        mask[row][col] = 1;
      }
    }
  }

}

// If mask[i][j] = 1 use the input image pixel for the output image
// Else if mask[i][j] = 0 use the background image pixel
void replace(bool mask[SIZE][SIZE],
	     unsigned char inImage[SIZE][SIZE][RGB],
	     unsigned char bgImage[SIZE][SIZE][RGB],
	     unsigned char outImage[SIZE][SIZE][RGB])
{
  // Create the output image using the mask to determine
  //  whether to use the pixel from the Input or Background image
  // loop through each grid of the mask
  for (int r = 0; r < SIZE; r++) {
    for (int c = 0; c < SIZE; c++) {
      // if mask as 0, use pixel from the background image
      if (mask[r][c] == 0) {
        outImage[r][c][0] = bgImage[r][c][0];
        outImage[r][c][1] = bgImage[r][c][1];
        outImage[r][c][2] = bgImage[r][c][2];
      }
      // if mask as 1, use pixel from the input image
      else {
        outImage[r][c][0] = inImage[r][c][0];
        outImage[r][c][1] = inImage[r][c][1];
        outImage[r][c][2] = inImage[r][c][2];   
      }
    }
  }

}
