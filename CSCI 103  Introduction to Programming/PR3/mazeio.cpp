/*
mazeio.cpp
*/

#include <iostream>
#include <fstream>
#include "mazeio.h"

using namespace std;

/*************************************************
 * read_maze:
 * Read the maze from the given filename into a
 *  2D dynamically  allocated array.
 *
 * Return the pointer to that array.
 * Return NULL (a special address) if there is a problem,
 * opening the file or reading in the integer sizes.
 *
 * The first argument is the filename of the maze input.
 *  You should use an ifstream to open and read from this
 *  file.
 *
 * We also pass in two pointers to integers. These are
 * output parameters (i.e. declared by the caller and
 * passed-by-reference for this function to fill in).
 * Fill the integers pointed to by these arguments
 * with the number of rows and columns
 * read (the first two input values).
 *
 *************************************************/
char** read_maze(char* filename, int* rows, int* cols)
{

    // *** You complete **** CHECKPOINT 1
  ifstream ifile(filename);  // open the file
  if (ifile.fail()) {  // able to open the file?
    return NULL;  // return NULL if the file does not exist
  }
  ifile >> *rows >> *cols;  // read the rows and cols from the start of the file
  if (ifile.fail()) {  // able to read the rows and cols?
    return NULL;  // return NULL if unable to read the rows and cols
  }
  // dynamically allocate a 2D array for the maze
  char** maze_2D = new char* [*rows];
  for (int r = 0; r < *rows; r++) {
    maze_2D[r] = new char[*cols];
  }
  // read in each cell of the file into the maze
  for (int r = 0; r < *rows; r++) {
    for (int c = 0; c < *cols; c++) {
      ifile >> maze_2D[r][c];
    }
  }
  // close the file
  ifile.close();
  // return the dynamically allocated 2D array
  return maze_2D;

}

/*************************************************
 * Print the maze contents to the screen in the
 * same format as the input (rows and columns, then
 * the maze character grid).
 *************************************************/
void print_maze(char** maze, int rows, int cols)
{

    // *** You complete **** CHECKPOINT 1
  // print out the first line of the file
  cout << rows << " " << cols << endl;
  // print out each cell of the maze
  for (int r = 0; r < rows; r++) {
    for (int c = 0; c < cols; c++) {
      cout << maze[r][c];
    }
    cout << endl;  // start a newline after looping through each row
  }

}

