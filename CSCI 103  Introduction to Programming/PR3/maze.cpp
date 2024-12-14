/*
maze.cpp
*/

#include <iostream>
#include "mazeio.h"
// #include "queue.h"
#include "queue.h"

using namespace std;

// Prototype for maze_search, which you will fill in below.
int maze_search(char**, int, int);

// Add other prototypes here for any functions you wish to use


// main function to read, solve maze, and print result
int main(int argc, char* argv[]) {
    int rows, cols, result;
    char** mymaze=NULL;
    const char* invalid_char_message = "Error, invalid character.";
    const char* invalid_maze_message = "Invalid maze.";
    const char* no_path_message = "No path could be found!";

    if(argc < 2)
    {
        cout << "Please provide a maze input file" << endl;
        return 1;
    }
    
    mymaze = read_maze(argv[1], &rows, &cols); // <---TASK: COMPLETE THIS FOR CHECKPOINT 1

    // For checkpoint 2 you should check the validity of the maze
    // You may do so anywhere you please and can abstract that
    // operation with a function or however you like.
    if (mymaze == NULL) {  // when unable to read the file or the rows and cols from the start of the file
        // print "Invalid maze" and return 1 indicating one error exist
        cout << invalid_maze_message << endl;
        return 1;
    }

    // call maze_search function and store the return value into result
    result = maze_search(mymaze, rows, cols);
    if (result == -1) {  // when the maze has more then one start or finish point
      cout << invalid_maze_message << endl;  // print "Invalid maze"
    }
    else if (result == 0) {  // when no path exists
      cout << no_path_message << endl;  // print "No path could be found"
    }
    else if (result == 1) {  // when successfully found the path
      //================================
      // When working on Checkpoint 4, you will need to call maze_search
      // and output the appropriate message or, if successful, print
      // the maze.  But for Checkpoint 1, we print the maze, regardless.
      print_maze(mymaze, rows, cols);
    }
    else {  // when the input maze contains characters other than ".#SF"
      cout << invalid_char_message << endl;  // print "Error, input format incorrect"
    }
    
    //================================
    // ADD CODE BELOW 
    // to delete all memory that read_maze allocated: CHECKPOINT 2
    for (int r = 0; r < rows; r++) {
        delete [] mymaze[r];
    }
    delete [] mymaze;

    return 0;
}

/**************************************************
 * Attempt to find shortest path and return:
 *  1 if successful
 *  0 if no path exists
 *
 * If path is found fill it in with '*' characters
 *  but don't overwrite the 'S' and 'F' cells
 * NOTE: don't forget to deallocate memory in here too!
 *************************************************/
int maze_search(char** maze, int rows, int cols)
{
    // *** You complete **** CHECKPOINT 4
    int num_start = 0;  // variable to store the number of start cells
    int num_finish = 0;  // variable to store the number of finish cells
    int num_odd = 0;  // variable to store the number of odd cells (characters other than ".#SF")
    Location startCell, loc, north, west, south, east;  // struct to find the start cell, current cell, neighbor cells
    Queue q(rows * cols);  // create queue with rows*cols size
    // dynamically allocate the predecessor array
    Location** pred = new Location*[rows];
    for (int r = 0; r < rows; r++) {
      pred[r] = new Location[cols];
    }
    // dynamically allocate the explored array
    int** explored = new int*[rows];
    for (int r = 0; r < rows; r++) {
      explored[r] = new int[cols];
    }
    // initialize the explored array with each cell as 0
    for (int r = 0; r < rows; r++) {
      for (int c = 0; c < cols; c++) {
        explored[r][c] = 0;
      }
    }

    // find the start and finish cells
    for (int r = 0; r < rows; r++) {
      for (int c = 0; c < cols; c++) {
        if (maze[r][c] == 'S') {
          num_start += 1;  // record the number of start cells of the input maze
          // find the start cell
          startCell.row = r;
          startCell.col = c;
          explored[r][c] = 1;  // mark the start location with 1 as explored
          q.add_to_back(startCell);  // add start location to q
        }
        else if (maze[r][c] == 'F') {
            num_finish += 1;  // record the number of finish cells of the input maze
        }
        else if (maze[r][c] != '.' && maze[r][c] != '#') {
            num_odd += 1;  // record the number of cells that have character other than ".#SF"
        }
      }
    }

    // check the validity of the maze
    if (num_start != 1 || num_finish != 1) {  // when there are more than one start and finish cell
      // delocate the explored array before ending the function
      for (int r = 0; r < rows; r++) {
        delete [] explored[r];
      }
      delete [] explored;
      // delocate the predecessor array before ending the function
      for (int r = 0; r < rows; r++) {
        delete [] pred[r];
      }
      delete [] pred;
      // return -1 for a badly-formatted maze
      return -1;
    }
    else if (num_odd != 0) {  // when the maze contains character other than ".#SF"
      // delocate the explored array before ending the function
      for (int r = 0; r < rows; r++) {
        delete [] explored[r];
      }
      delete [] explored;
      // delocate the predecessor array before ending the function
      for (int r = 0; r < rows; r++) {
        delete [] pred[r];
      }
      delete [] pred;
      // return 2 to distinguish from the badly-formatted maze of having more than one start and finish cells
      return 2;
    }

    // set a variable to record whether there exist a path
    // 0 for no path, 1 for there exists a path
    int path = 0;
    // Perform the breadth-first search algorithm
    while (not q.is_empty()) {
      loc = q.remove_from_front();  // extract the item from the front of q and store as the current location
      // check 1 step north of the current location
      north.row = loc.row - 1;
      north.col = loc.col;
      // when the north neightbor is valid, open, and not yet explored
      if (north.row >= 0 && north.row < rows && north.col >= 0 && north.col < cols) {
        if (maze[north.row][north.col] == '.' && explored[north.row][north.col] == 0) {
          explored[north.row][north.col] = 1;  // mark the north neighbor as explored
          q.add_to_back(north);  // add the north neighbor to the back of q
          pred[north.row][north.col] = loc;  // set the predecessor of the north neighbor to the current location
        }
        else if (maze[north.row][north.col] == 'F') {  // when the north neighbor is the finish cell
          path = 1;  // set path to 1 implying there exists a path
          break;  // stop and leave the loop
        }
      }
      // check 1 step west of the current location
      west.row = loc.row;
      west.col = loc.col - 1;
      // when the west neightbor is valid, open, and not yet explored
      if (west.row >= 0 && west.row < rows && west.col >= 0 && west.col < cols) {
        if (maze[west.row][west.col] == '.' && explored[west.row][west.col] == 0) {
          explored[west.row][west.col] = 1;  // mark the west neighbor as explored
          q.add_to_back(west);  // add the west neighbor to the back of q
          pred[west.row][west.col] = loc;  // set the predecessor of the west neighbor to the current location
        }
        else if (maze[west.row][west.col] == 'F') {  // when the west neighbor is the finish cell
          path = 1;  // set path to 1 implying there exists a path
          break;  // stop and leave the loop
        }
      }
      // check 1 step south of the current location
      south.row = loc.row + 1;
      south.col = loc.col;
      // when the south neightbor is valid, open, and not yet explored
      if (south.row >= 0 && south.row < rows && south.col >= 0 && south.col < cols) {
        if (maze[south.row][south.col] == '.' && explored[south.row][south.col] == 0) {
          explored[south.row][south.col] = 1;  // mark the south neighbor as explored
          q.add_to_back(south);  // add the south neighbor to the back of q
          pred[south.row][south.col] = loc;  // set the predecessor of the south neighbor to the current location
        }
        else if (maze[south.row][south.col] == 'F') {  // when the south neighbor is the finish cell
          path = 1;  // set path to 1 implying there exists a path
          break;  // stop and leave the loop
        }
      }
      // check 1 step east of the current location
      east.row = loc.row;
      east.col = loc.col + 1;
      // when the east neightbor is valid, open, and not yet explored
      if (east.row >= 0 && east.row < rows && east.col >= 0 && east.col < cols) {
        if (maze[east.row][east.col] == '.' && explored[east.row][east.col] == 0) {
          explored[east.row][east.col] = 1;  // mark the east neighbor as explored
          q.add_to_back(east);  // add the east neighbor to the back of q
          pred[east.row][east.col] = loc;  // set the predecessor of the east neighbor to the current location
        }
        else if (maze[east.row][east.col] == 'F') {  // when the east neighbor is the finish cell
          path = 1;  // set path to 1 implying there exists a path
          break;  // stop and leave the loop
        }
      }
    }

    // check whether there exists a path
    if (path == 0) {  // when no path
      // delocate the explored array before ending the function
      for (int r = 0; r < rows; r++) {
          delete [] explored[r];
      }
      delete [] explored;
      // delocate the predecessor array before ending the function
      for (int r = 0; r < rows; r++) {
        delete [] pred[r];
      }
      delete [] pred;
      // return 0 to indicate no path
      return 0;
    }
    else {  // when there exists a path
      // walk the predecessor array backwards from the finish location to the start location
      while (maze[loc.row][loc.col] != 'S') {  // when the start cell is not reached
        maze[loc.row][loc.col] = '*';  // fill in the intermediate locations of the maze with * to indicate the path
        loc = pred[loc.row][loc.col];  // update the current location to the one predecess to it
      }
      // delocate the explored array before ending the function
      for (int r = 0; r < rows; r++) {
          delete [] explored[r];
      }
      delete [] explored;
      // delocate the predecessor array before ending the function
      for (int r = 0; r < rows; r++) {
        delete [] pred[r];
      }
      delete [] pred;
      // return 1 to indicate successfully find the path
      return 1;
    }

   // DELETE this stub, it's just for Checkpoint 1 to compile.
}
