#include "digitblob.h"
#include <iostream>
// Add more includes if necessary
#include <vector>
#include <cmath>

using namespace std;

// TO DO - Complete this function
bool Location::operator<(const Location& other) const
{
    if (col < other.col) {  // when lhs's col is less than rhs's col
        return true;
    }
    else if (col == other.col) {  // when lhs's col is equal to rhs's col
        if (row < other.row) {  // when lhs's row is less than rhs's row
            return true;
        }
    }
    // when lhs's col is greater than rhs's col
    // or when equal col condition, lhs's row is not less than rhs's row
    return false;

}

// TO DO - Complete this function
DigitBlob::DigitBlob()
{
    img_ = NULL;
    digit_ = '!'; // dummy value
    bq0_ = bq1_ = bq2_ = bq3_ = bq4_ = bqd_ = 0;
    euler_ = -2;

    // ul_'s Location default constructor already initializes it to -1,-1

    // Initilaize h_ and w_ and any other data members
    h_ = 0;
    w_ = 0;
    aspect_r = -1;
    vertical_cm = horizontal_cm = -1;
    vertical_sy = horizontal_sy = -1;

}

// TO DO - Complete this function
DigitBlob::DigitBlob(uint8_t** img, Location upperleft, int height, int width)
{
    img_ = img;
    digit_ = '!'; // dummy value

    bq0_ = bq1_ = bq2_ = bq3_ = bq4_ = bqd_ = 0;
    euler_ = -2;

    // Initilaize ul_, h_ and w_ and any other data members
    ul_ = upperleft;
    h_ = height;
    w_ = width;

}

// TO DO - Complete this function if necessary
DigitBlob::~DigitBlob()
{
    // Add code if it is necessary

}

// TO DO - Complete this function
void DigitBlob::classify()
{
    calc_bit_quads();
    calc_euler_number();
    // Call helper functions to calculate features
    calc_aspect_ratio();
    calc_vertical_centroid();
    calc_horizontal_centroid();
    calc_vertical_symmetry();
    calc_horizontal_symmetry();
    calc_vert_lines();

    // TO DO: use the results of helper functions to calculate features
    //    We suggest starting with the Euler number but you are free to
    //    change our structure
    if (euler_ == -1) {  // only 8
        digit_ = '8';
    }
    else if (euler_ == 0) {  // 0 4 6 9
        if (vertical_sy >= 0.8 && horizontal_sy >= 0.8) {
            digit_ = '0';
        }
        else {
          if (vert == true) {
            digit_ = '4';
          }
          else {
            if (abs(horizontal_sy - vertical_sy) > 0.09) {
              if (horizontal_sy - vertical_sy < 0) {
                digit_ = '9';
              }
              else {
                digit_ = '4';
              }
            }
            else {
              digit_ = '6';
            }
          }
        }
    }
    else if (euler_ == 1) {  // 1 2 3
      if (horizontal_sy > 0.6) {
        if (vert == true) {
          digit_ = '1';
        }
        else {
          if (horizontal_sy < 0.625) {
            digit_ = '2';
          }
          else {
            digit_ = '3';
          }
        }
      }
      else {
        if (vertical_cm < 0.4) {
          digit_ = '7';
        }
        else {
          digit_ = '5';
        }
      }
    }

}

// Complete - Do not alter
char DigitBlob::getClassification() const
{
    return digit_;
}

// TO DO - Complete this function
void DigitBlob::printClassificationResults() const
{
    cout << "Digit blob at " << ul_.row << "," << ul_.col << " h=" << h_ << " w=" << w_ << endl;
    cout << "Bit quads: 1, 2, D, 3, 4:";
    cout << " " << bq1_ << " " << bq2_ << " " << bqd_;
    cout << " " << bq3_ << " " << bq4_ << endl;
    cout << "Euler number is " << euler_ << endl;
    // TO DO: Add any other couts to print classification test data
    cout << "Vertical center of mass is " << vertical_cm << endl;
    cout << "Horizontal center of mass is " << horizontal_cm << endl;
    cout << "Vertical symmetry is " << vertical_sy << endl;
    cout << "Horizontal symmetry is " << horizontal_sy << endl;
    cout << "Aspect ratio is " << aspect_r << endl;
    cout << "Vert line? " << vert << endl;

    cout << "****Classified as: " << digit_ << "\n\n" << endl;

}

// Complete - Do not alter
const Location& DigitBlob::getUpperLeft() const
{
    return ul_;
}

// Complete - Do not alter
int DigitBlob::getHeight() const
{
    return h_;
}

// Complete - Do not alter
int DigitBlob::getWidth() const
{
    return w_;
}

// Complete - Do not alter
bool DigitBlob::operator<(const DigitBlob& other)
{
    // Use Location's operator< for DigitBlob operator<
    return ul_ < other.ul_;
}

// Complete - Do not alter
void DigitBlob::calc_euler_number()
{
    euler_ = (bq1_ - bq3_ - 2*bqd_) / 4;
}

// TO DO - Complete this function to set bq1_, bq2_, etc.
void DigitBlob::calc_bit_quads()
{
    for (int i = ul_.row - 1; i < ul_.row + h_; i++) {
        for (int j = ul_.col - 1; j < ul_.col + w_; j++) {
            // update the number of bq0
            if (img_[i][j] == 255 && img_[i][j+1] == 255 && img_[i+1][j] == 255 && img_[i+1][j+1] == 255) {
                bq0_ += 1;
            }
            // update the number of bq1
            if (img_[i][j] == 0 && img_[i][j+1] == 255 && img_[i+1][j] == 255 && img_[i+1][j+1] == 255) {
                bq1_ += 1;
            }
            else if (img_[i][j] == 255 && img_[i][j+1] == 0 && img_[i+1][j] == 255 && img_[i+1][j+1] == 255) {
                bq1_ += 1;
            }
            else if (img_[i][j] == 255 && img_[i][j+1] == 255 && img_[i+1][j] == 0 && img_[i+1][j+1] == 255) {
                bq1_ += 1;
            }
            else if (img_[i][j] == 255 && img_[i][j+1] == 255 && img_[i+1][j] == 255 && img_[i+1][j+1] == 0) {
                bq1_ += 1;
            }
            // update the number of bq2
            if (img_[i][j] == 0 && img_[i][j+1] == 0 && img_[i+1][j] == 255 && img_[i+1][j+1] == 255) {
                bq2_ += 1;
            }
            else if (img_[i][j] == 255 && img_[i][j+1] == 0 && img_[i+1][j] == 255 && img_[i+1][j+1] == 0) {
                bq2_ += 1;
            }
            else if (img_[i][j] == 0 && img_[i][j+1] == 255 && img_[i+1][j] == 0 && img_[i+1][j+1] == 255) {
                bq2_ += 1;
            }
            else if (img_[i][j] == 255 && img_[i][j+1] == 255 && img_[i+1][j] == 0 && img_[i+1][j+1] == 0) {
                bq2_ += 1;
            }
            // update the number of bq3
            if (img_[i][j] == 0 && img_[i][j+1] == 0 && img_[i+1][j] == 0 && img_[i+1][j+1] == 255) {
                bq3_ += 1;
            }
            else if (img_[i][j] == 0 && img_[i][j+1] == 0 && img_[i+1][j] == 255 && img_[i+1][j+1] == 0) {
                bq3_ += 1;
            }
            else if (img_[i][j] == 255 && img_[i][j+1] == 0 && img_[i+1][j] == 0 && img_[i+1][j+1] == 0) {
                bq3_ += 1;
            }
            else if (img_[i][j] == 0 && img_[i][j+1] == 255 && img_[i+1][j] == 0 && img_[i+1][j+1] == 0) {
                bq3_ += 1;
            }
            // update the number of bq4
            if (img_[i][j] == 0 && img_[i][j+1] == 0 && img_[i+1][j] == 0 && img_[i+1][j+1] == 0) {
                bq4_ += 1;
            }
            // update the number of bqd
            if (img_[i][j] == 0 && img_[i][j+1] == 255 && img_[i+1][j] == 255 && img_[i+1][j+1] == 0) {
                bqd_ += 1;
            }
            else if (img_[i][j] == 255 && img_[i][j+1] == 0 && img_[i+1][j] == 0 && img_[i+1][j+1] == 255) {
                bqd_ += 1;
            }          
        }
    }

}

// Add more private helper function implementations below
// calculate aspect ratio
void DigitBlob::calc_aspect_ratio() {
    aspect_r = h_ / w_;
}

// calculate vertical center of mass
void DigitBlob::calc_vertical_centroid() {
    double numerator = 0;
    double denominator = 0;
    for (int i = ul_.row; i < ul_.row + h_; i++) {
        for (int j = ul_.col; j < ul_.col + w_; j++) {
            if (img_[i][j] == 0) {
                numerator = numerator + (i - ul_.row) * 1;
                denominator += 1;
            }
        }
    }
    vertical_cm = (numerator / denominator) / h_;  // normalize the vertical center of mass by dividing height
}

// calculate the horizontal center of mass
void DigitBlob::calc_horizontal_centroid() {
    double numerator = 0;
    double denominator = 0.0;
    for (int i = ul_.row; i < ul_.row + h_; i++) {
        for (int j = ul_.col; j < ul_.col + w_; j++) {
            if (img_[i][j] == 0) {
                numerator = numerator + (j - ul_.col) * 1;
                denominator += 1;
            }
        }
    }
    horizontal_cm = (numerator / denominator) / w_;  // normalize the horizontal center of mass by dividing the width
}

// calcualte the percentage of vertical symmetry
void DigitBlob::calc_vertical_symmetry() {
    double symmetry = 0.0;
    int num = 0;
    for (int i = ul_.row; i < ul_.row + h_; i++) {
        for (int j = 0; j < w_ / 2; j++) {  // loop through half of the col
            // compare the left with the right
            if (img_[i][j + ul_.col] == img_[i][ul_.col + w_ - 1 - j]) {
                symmetry += 1;
            }
            num += 1;
        }
    }
    vertical_sy = symmetry / num;
}

// calculate the percentage of horizontal symmetry
void DigitBlob::calc_horizontal_symmetry() {
    double symmetry = 0;
    int num = 0;
    for (int i = 0; i < h_ / 2; i++) {  // loop through half of the row
        for (int j = ul_.col; j < ul_.col + w_; j++) {
            // compare the upper half with the lower half
            if (img_[i + ul_.row][j] == img_[ul_.row + h_ - 1 - i][j]) {
                symmetry += 1;
            }
            num += 1;
        }
    }
    horizontal_sy = symmetry / num;
}

// if there exists vertical line in the digit (like 1, 4)
void DigitBlob::calc_vert_lines() {
  vert = false;
  for (int j = ul_.col; j < ul_.col + w_; j++) {
    double black = 0.0;
    double total = 0.0;
    double percent = 0.0;
    for (int i = ul_.row; i < ul_.row + h_; i++) {
      total += 1;
      if (img_[i][j] == 0) {
        black += 1;
      }
    }
    percent = black / total;
    // if the vertical line is 82% of the height of the bounding box
    // mark vert as true
    if (percent > 0.82) {
      vert = true;
      break;
    }
  }
}
