// Copy in your bigint.cpp (overwrite this file)
//  and then add the appropriate code
#include <iostream>
#include "bigint.h"
#include <string>

using namespace std;

// Write your implementation below
void BigInt::removeLeadingZeroes() {
  // loop through the whole vector except the 0th index
  // so that the number 0 would just be left as a single digit 0
  size_t len = numList.size();
  for (size_t i = 0; i < len - 1; i++) {
    // when the leading number is zero, remove it
    if (numList[len - 1 - i] == 0) {
      // the digit of the number is in reverse order, so use pop_back()
      numList.pop_back();
    }
    // when first noticing the leading number is not zero
    // leave the loop and leave the number as it is
    else {
      break;
    }
  }

}

// convert string to BigInt
BigInt::BigInt(string s, int base) {
  add_base = base;  // update the base
  int x;
  // loop through each char of the string and convert it into the digit number
  for (unsigned int i = 0; i < s.size(); i++) {
    char c = s[s.size()-1-i];  // reverse the char in string
    if (c >= '0' && c <= '9') {
      x = static_cast<int>(c) - '0';
    }
    else if (c >= 'A' && c <= 'Z') {
      x = 10 + static_cast<int>(c) - 'A';
    }
    numList.push_back(x);  // add the converted digit into the vector
  }

  removeLeadingZeroes();  // remove the leading zeros by calling the helper function

}

// get string representation
string BigInt::to_string() const {
  string s = "";  // create an empty string variable
  // loop through the vector to convert each int digit into a character
  // and finally convert the int vector into a string
  for (unsigned int i = 0; i < numList.size(); i++) {
    int digit = numList[numList.size()-1-i];
    char c;
    if (digit >= 10) {
      c = (char)(digit - 10 + 'A');
    }
    else {
      c = (char)(digit + '0');
    }
    s += c;
  }
  return s;
}

// add two BigInts
void BigInt::add(BigInt b) {
  // add zeros if the two bigint vector not in the same size
  if (b.numList.size() < numList.size()) {
    for (unsigned int i = b.numList.size(); i < numList.size(); i++) {
      b.numList.push_back(0);
    }
  }
  else if (b.numList.size() > numList.size()) {
    for (unsigned int i = numList.size(); i < b.numList.size(); i++) {
      numList.push_back(0);
    }
  }

  // do addition of each digit
  unsigned int size1 = numList.size();
  for (unsigned int i = 0; i < size1; i++) {
    numList[i] += b.numList[i];
    if (numList[i] >= add_base) {  // add with a carry (when exceeding the base)
      int temp1 = numList[i] / add_base;
      int temp2 = numList[i] % add_base;
      numList[i] = temp2;
      if ((i+1) < size1) {
        numList[i+1] += temp1;
      }
      else {  // add without exceeding the base
        numList.push_back(temp1);
      }
    }
  }

  this->removeLeadingZeroes();
}

// returns the sum of this BigInt and rhs
BigInt BigInt::operator+(const BigInt& rhs) const {
  BigInt temp = *this;  // create a temp BigInt so that the orginal bigints won't be changed
  temp.add(rhs);
  return temp;
}

// returns the true if this BigInt is less than rhs
bool BigInt::operator<(const BigInt& rhs) const {
  if (numList.size() < rhs.numList.size()) {
    return true;
  }
  else if (numList.size() > rhs.numList.size()) {
    return false;
  }
  else {
    size_t len = numList.size();
    for (size_t i = 0; i < len; i++) {
      if (numList[len - 1 - i] > rhs.numList[len - 1 - i]) {
        return false;  // when this BigInt is greater than rhs, return false
    }
      else if (numList[len - 1 - i] < rhs.numList[len - 1 - i]) {
        return true;  // when this BigInt is less than rhs, return true
      }
    }
    return false;  // when this BigInt is equal to rhs, return false
  }
}

// returns the difference of this BigInt minus rhs
BigInt BigInt::operator-(const BigInt& rhs) const {
  BigInt temp1 = *this;
  BigInt temp2 = rhs;
  // add zeros if the two bigint vector not in the same size
  if (temp1.numList.size() < temp2.numList.size()) {
    for (unsigned int i = temp1.numList.size(); i < temp2.numList.size(); i++) {
      temp1.numList.push_back(0);
    }
  }
  else if (temp1.numList.size() > temp2.numList.size()) {
    for (unsigned int i = temp2.numList.size(); i < temp1.numList.size(); i++) {
      temp2.numList.push_back(0);
    }
  }
  // do subtraction of each digit
  unsigned int size1 = temp1.numList.size();
  if (temp1 < temp2) {  // when lhs is smaller than rhs (call operator< function)
    for (size_t i = 0; i < size1; i++) {
      if (temp2.numList[i] < temp1.numList[i]) {  // subtraction with borrow
        temp2.numList[i] = temp2.numList[i] - temp1.numList[i] + add_base;
        temp2.numList[i + 1] -= 1;
      }
      else {  // subtraction without borrow
        temp2.numList[i] = temp2.numList[i] - temp1.numList[i];
      }
    }
    temp2.removeLeadingZeroes();  // remove leading zeros
    return temp2;
  }
  else {  // when lhs is not smaller than rhs
    for (size_t i = 0; i < size1; i++) {
      if (temp1.numList[i] < temp2.numList[i]) {  // subtraction with borrow
        temp1.numList[i] = temp1.numList[i] - temp2.numList[i] + add_base;
        temp1.numList[i + 1] -= 1;
      }
      else {  // subtraction without borrow
        temp1.numList[i] = temp1.numList[i] - temp2.numList[i];
      }
    }
    temp1.removeLeadingZeroes();  // remove leading zeros
    return temp1;
  }
}