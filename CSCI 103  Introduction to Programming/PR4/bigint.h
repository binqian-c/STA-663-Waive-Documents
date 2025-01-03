// Copy in your bigint.h (overwrite this file)
//  and then add the appropriate code
#ifndef BIGINT_H
#define BIGINT_H
#include <string>
#include <vector>

// Note: it is bad practice to have `using namespaces std;` in 
//       a header file.  So where we use C++ objects (cout, cin) 
//       and C++ class types (string, vector<int>), you should
//       precede them with `std::`.  

// In the .cpp implementation file, it is fine to have a 
//  `using namespace std;` statement. So you can put that in the
//  .cpp file and then avoid having to precede everything with `std::`

class BigInt {
public:
    BigInt(std::string s, int base=10); // convert string to BigInt
    std::string to_string() const; // get string representation
    // returns the sum of this BigInt and rhs
    BigInt operator+(const BigInt& rhs) const; 
    // returns the difference of this BigInt minus rhs
    BigInt operator-(const BigInt& rhs) const; 
    // returns the true if this BigInt is less than rhs
    bool operator<(const BigInt& rhs) const;
    // add another BigInt to this one
    void add(BigInt b);
private:
    // whatever you need
    int add_base;
    std::vector<int> numList;
    void removeLeadingZeroes();
};

#endif