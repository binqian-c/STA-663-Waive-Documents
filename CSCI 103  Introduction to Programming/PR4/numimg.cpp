#include "digitblob.h"
#include "numimg.h"
#include "bmplib.h"
#include <algorithm> // for std::sort
#include <deque>
#include <iomanip>
#include <iostream>

using namespace std;

// TO DO: Complete this function
NumImg::NumImg(const char* bmp_filename)
{
    //  Note: readGSBMP dynamically allocates a 2D array 
    //    (i.e. array of pointers (1 per row/height) where each  
    //    point to an array of unsigned char (uint8_t) pixels)

    // TO DO:
    // call readGSBMP to initialize img_, h_, and w_;
    img_ = readGSBMP(bmp_filename, h_, w_);



    // Leave this check
    if(img_ == NULL) {
        throw std::logic_error("Could not read input file");
    }
    
    // Convert to Black and White using a fixed threshold 
    for(int i =0; i < h_; i++){
        for(int j = 0; j < w_; j++){
            if(img_[i][j] > 150){
                img_[i][j] = 255;
            }
            else {
                img_[i][j] = 0;
            }
        }
    }
    // Perform any other initialization you need
}

// TO DO: Complete this function
NumImg::~NumImg()
{
    // Add code here if necessary
    // delocate the 2D array
    for (int i = 0; i < h_; i++) {
      delete [] img_[i];
    }
    delete [] img_;

}

// TO DO: Complete this function
size_t NumImg::findAndCreateDigitBlobs()
{
    // dynamically allocate a 2D array to remember the visited black pixel
    bool** visited = new bool*[h_];
    for (int i = 0; i < h_; i++) {
      visited[i] = new bool[w_];
    }

    // initialize the 2D array as unvisited
    for (int i = 0; i < h_; i++) {
        for (int j = 0; j < w_; j++) {
            visited[i][j] = false;
        }
    }

    // loop through the whole image to find each number's starting index
    for (int i = 0; i < h_; i++) {
        for (int j = 0; j < w_; j++) {
            // if the pixel is black and unvisited
            if (img_[i][j] == 0 && visited[i][j] != true) {
                // do BFS search
                DigitBlob db = createDigitBlob(visited, i, j);
                blobs_.push_back(db);
            }
        }
    }

    // sort the digit blobs
    sortDigitBlobs();

    // delocate the 2D array created above
    for (int i = 0; i < h_; i++) {
        delete [] visited[i];
    }
    delete [] visited;

    // return the number of digit blobs
    return blobs_.size();

}

// Complete - Do not alter
std::string NumImg::classify(bool withDebug)
{
    std::string res;
    for(size_t i = 0; i < blobs_.size(); i++){
        blobs_[i].classify();
        if(withDebug){
            blobs_[i].printClassificationResults();
        }
        char c = blobs_[i].getClassification();
        res += c;
    }
    return res;
}

// Complete - Do not alter
void NumImg::printBoundingBoxes() const
{
    cout << setw(2) << "i" << setw(6) << "ULRow" << setw(6) << "ULCol" << setw(4) << "Ht." << setw(4) << "Wi." << endl;
    for(size_t i = 0; i < blobs_.size(); i++){
        const DigitBlob& b = blobs_[i];
        cout << setw(2) << i << setw(6) << b.getUpperLeft().row << setw(6) << b.getUpperLeft().col 
        << setw(4) << b.getHeight() << setw(4) << b.getWidth()  << endl;
        // cout << "Blob " << i << " ul=(" << b.getUpperLeft().row << "," << b.getUpperLeft().col 
        //     << ") h=" << b.getHeight() << " w=" << b.getWidth() << endl;
    }

}

// Complete - Do not alter
const DigitBlob& NumImg::getDigitBlob(size_t i) const
{
    if(i >= blobs_.size()){
        throw std::out_of_range("Index to getDigitBlob is out of range");
    }
    return blobs_[i];
}

// Complete - Do not alter
size_t NumImg::numDigitBlobs() const
{
    return blobs_.size();
}

// Complete - Do not alter
void NumImg::sortDigitBlobs()
{
    std::sort(blobs_.begin(), blobs_.end());
}

// Complete - Do not alter
void NumImg::drawBoundingBoxesAndSave(const char* filename)
{
    for(size_t i=0; i < blobs_.size(); i++){
        Location ul = blobs_[i].getUpperLeft();
        int h = blobs_[i].getHeight();
        int w = blobs_[i].getWidth();
        for(int i = ul.row-1; i < ul.row + h + 1; i++){
            img_[i][ul.col-1] = 128;
            img_[i][ul.col+w] = 128;
        }
        for(int j = ul.col-1; j < ul.col + w + 1; j++){
            img_[ul.row-1][j] = 128;
            img_[ul.row+h][j] = 128;
        }
    }
    writeGSBMP(filename, img_, h_, w_);
}

// TO DO:
// Add other (helper) function definitions here

DigitBlob NumImg::createDigitBlob(bool** explored, int pr, int pc)
{
    // Arrays to help produce neighbors easily in a loop
    // by encoding the **change** to the current location.
    // Goes in order N, NW, W, SW, S, SE, E, NE
    int neighbor_row[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
    int neighbor_col[8] = {0, -1, -1, -1, 0, 1, 1, 1};

    // Add your code here
    explored[pr][pc] = true;
    deque<Location> q;  // create a queue
    q.push_back(Location(pr,pc));  // add the starting point to the queue
    Location loc;
    // initialize the max row and col and min row and col to the starting point
    int row_min = pr;
    int col_min = pc;
    int row_max = pr;
    int col_max = pc;

    while (!q.empty()) {  // when the queue is not empty
        loc = q.front();  // extract the item from the front of the queue
        q.pop_front();  // remove the front item
        // search each neighbor with the help of the neighbor arrays
        for (int i = 0; i < 8; i++) {
            int r = loc.row + neighbor_row[i];
            int c = loc.col + neighbor_col[i];
            if (img_[r][c] == 0 && explored[r][c] != true) {  // when the neighbor pixel is black and not visited
                explored[r][c] = true;  // mark as visited
                q.push_back(Location(r, c));  // add the neighbor to the back of the queue
                if (r < row_min) {
                    row_min = r;  // update the min row
                }
                if (r > row_max) {
                    row_max = r;  // update the max row
                }
                if (c < col_min) {
                    col_min = c;  // update the min col
                }
                if (c > col_max) {
                    col_max = c;  // update the max col
                }
            }
        }
    }

    // calculate the height and width of the bounding box
    Location up_le(row_min, col_min);
    int h = row_max - row_min + 1;
    int w = col_max - col_min + 1;

    // create the digit blob and return it
    DigitBlob blob(img_, up_le, h, w);
    return blob;
}

