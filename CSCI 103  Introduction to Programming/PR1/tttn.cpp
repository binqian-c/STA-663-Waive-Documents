// NxN tic-tac-toes
#include <iostream>
using namespace std;

// The following 3 functions are helper functions to convert
// between 1D and 2D array indices.  The grid itself is stored
// as a 1D array.  However, for printing, checking who won,
// etc. it may be easier to write loops that generate separate
// row/column indices (i.e. treating the array like a 2D array).
// The functions below should be written using the hints in the
// writeup for performing the appropriate arithmetic conversion
// between 1D- and 2D-indices, and can then be called in any
// of the other functions when you find yourself wanting to 
// convert one to the other.

/**
 * Helper function - Given the grid array and its dimension
 *    as well as a particular row (r) and column (c), this
 *    function performs the arithmetic to convert r and c
 *    to a 1D index and returns that character in the grid.
 *    For example, for dim = 3 and r = 2, c = 1, this function
 *    should compute the corresponding index: 7 and return
 *    grid[7].
 *
 * Use this function wherever you generate, row/column
 *    indices and want to access that element in the grid.
 *    Pass the row/column indices as r and c, respectively.
 *
 */
char getEntryAtRC(char grid[], int dim, int r, int c);

/**
 * Helper function - Given a 1D index returns the row
 * that corresponds to this 1D index.  Use this in
 * conjunction with idxToCol() anytime you have a 1D index
 * and want to convert to 2D indices.
 */
int idxToRow(int idx, int dim);

/**
 * Helper function - Given a 1D index returns the column
 * that corresponds to this 1D index.  Use this in
 * conjunction with idxToRow() anytime you have a 1D index
 * and want to convert to 2D indices.
 */
int idxToCol(int idx, int dim);


/** Should print the tic-tac-toe board in a nice grid
 *  format as shown below:
 *
 * Parameters:
 *   grid: Array of dim^2 characters representing the state
 *         of each square.  Each entry contains 'X', 'O'
 *         (the letter oh), or '?'.
 */
void printTTT(char grid[], int dim);

/** 
 * Should check if any player has won the game yet.
 *
 * Parameters:
 *   grid: Array of dim^2 characters representing the state
 *         of each square.  Each entry contains 'X', 'O', or '?'
 *
 * Return value:
 *   Should return 1 if 'X' has won, 2 if 'O' has won, or 0 (zero)
 *   if the game is still undecided.
 * 
 */
int checkForWinner(char grid[], int dim);


/** 
 * Should check if there is no possible way any player can win.
 * More specifically, if there does not exist a row, column,
 * or diagonal that can still have 3 of a kind, then the game
 * will be a draw.
 * 
 *
 * Parameters:
 *   grid: Array of dim^2 characters representing the state
 *         of each square.  Each entry contains 'X', 'O', or '?'
 *
 * Return value:
 *   Return true if no player can win given the current 
 *   game state, false otherwise.
 */
bool checkForDraw(char grid[], int dim);
 

/**********************************************************
 *  Write your implementations for each function prototyped
 *  above in the space below
 **********************************************************/

char getEntryAtRC(char grid[], int dim, int r, int c)
{
    int oneD = r * dim + c; // convert 2D index to 1D index
    return grid[oneD]; /* Convert r,c to 1D index here */
}

int idxToRow(int idx, int dim)
{
    int convertToRow = idx / dim; // convert 1D index to 2D index- row here
    return convertToRow; /* Add Expression here to convert idx to appropriate row */
}

int idxToCol(int idx, int dim)
{
    int convertToCol = idx % dim; // convert 1D index to 2D index- column here
    return convertToCol; /* Add Expression here to convert idx to appropriate column */;
}

void printTTT(char grid[], int dim)
{
  // the nested loop helps to loop through each 2D index position of the ttt board
  for(int r=0; r < dim; r++) { // loop through each row
    for(int c=0; c < dim; c++) { // loop through each column
      int one_idx = r * dim + c; // convert 2D index to 1D index
      cout << " " << grid[one_idx] << " "; // print the character on each position of the ttt board
      // does not need to print a "|" after the last character in each row
      if (c != dim -1) {
        cout << "|";
      }
    }
    cout << endl; // start a new line to print a line of "-"
    // does not need to print a line of "-" after the last row of the ttt board
    if (r < dim - 1) {
      // each character corresponds to 3 "-" and each "|" corresponds to 1 "-"
      int num = dim * 3 + (dim - 1);
      // loop through the total number of "-" needed and print one "-" at a time
      for (int i=0; i < num; i++) {
        cout << "-";
      }
      cout << endl; // start a new line to print the next row of characters
    }
  }
}

int checkForWinner(char grid[], int dim)
{
  // check each row;
  for (int r=0; r < dim; r++) { // loop through each row
    // the number of X's in each row will be stored in x_same1, initialize it to zero
    int x_same1 = 0;
    // the number of O's in each row will be stored in o_same1, initialize it to zero
    int o_same1 = 0;
    for (int c=0; c < dim; c++) { // loop through each column in a specific row
      // update the number of X's in this row if seeing an X
      if (getEntryAtRC(grid, dim, r, c) == 'X') {
        x_same1 += 1;
      }
      // update the number of O's in this row if seeing an O
      else if (getEntryAtRC(grid, dim, r, c) == 'O') {
        o_same1 += 1;
      }
    }
    // when this row only contains X, player X wins
    if (x_same1 == dim) {
      return 1;
    }
    // when this row only contains O, player O wins
    else if (o_same1 == dim) {
      return 2;
    }
  }

  // check each column;
  for (int c=0; c < dim; c++) { // loop through each column
    // the number of X's in each column will be stored in x_same2, initialize it to zero
    int x_same2 = 0;
    // the number of O's in each column will be stored in o_same2, initialize it to zero
    int o_same2 = 0;
    for (int r=0; r < dim; r++) { // loop through each row in a specific column
      // update the number of X's in this column if seeing an X
      if (getEntryAtRC(grid, dim, r, c) == 'X') {
        x_same2 += 1;
      }
      // update the number of O's in this column if seeing an O
      else if (getEntryAtRC(grid, dim, r, c) == 'O') {
        o_same2 += 1;
      }
    }
    // when this column only contains X, player X wins
    if (x_same2 == dim) {
      return 1;
    }
    // when this column only contains O, player O wins
    else if (o_same2 == dim) {
      return 2;
    }
  }
  
  // check top-left to bottom-right diagnol;
  // the number of X's in top-left to bottom-right diagnol will be stored in x_same3, initialize it to zero
  int x_same3 = 0;
  // the number of O's in top-left to bottom-right diagnol will be stored in o_same3, initialize it to zero
  int o_same3 = 0;
  // loop through each top-left to bottom-right diagnol position
  for (int n=0; n < dim; n++) {
    // update the number of X's in this diagnol if seeing an X
    if (getEntryAtRC(grid, dim, n, n) == 'X') {
      x_same3 += 1;
    }
    // update the number of O's in this diagnol if seeing an O
    else if (getEntryAtRC(grid, dim, n, n) == 'O') {
      o_same3 += 1;
    }
  }
  // when this diagnol only contains X, player X wins
  if (x_same3 == dim) {
    return 1;
  }
  // when this diagnol only contains O, player O wins
  else if (o_same3 == dim) {
    return 2;
  }

  // check top-right to bottom-left diagnol
  // the number of X's in top-right to bottom-left diagnol will be stored in x_same4, initialize it to zero
  int x_same4 = 0;
  // the number of O's in top-right to bottom-left diagnol will be stored in o_same4, initialize it to zero
  int o_same4 = 0;
  // loop through each top-right to bottom-left diagnol position
  for (int n=0; n < dim; n++) {
    // update the number of X's in this diagnol if seeing an X
    if (getEntryAtRC(grid, dim, n, dim-1-n) == 'X') {
      x_same4 += 1;
    }
    // update the number of O's in this diagnol if seeing an O
    else if (getEntryAtRC(grid, dim, n, dim-1-n) == 'O') {
      o_same4 += 1;
    }
  }
  // when this diagnol only contains X, player X wins
  if (x_same4 == dim) {
    return 1;
  }
  // when this diagnol only contains O, player O wins
  else if (o_same4 == dim) {
    return 2;
  }
  // when the game is undecided
  return 0;
}

bool checkForDraw(char grid[], int dim)
{
  // check each row;
  for (int r=0; r < dim; r++) { // loop through each row
    // the number of X's in each row will be stored in x_num1, initialize it to zero
    int x_num1 = 0;
    // the number of O's in each row will be stored in o_num1, initialize it to zero
    int o_num1 = 0;
    for (int c=0; c < dim; c++) { // loop through each column in a specific row
      // update the number of X's when seeing an X
      if (getEntryAtRC(grid, dim, r, c) == 'X') {
        x_num1 += 1;
      }
      // update the number of O's when seeing an O
      else if (getEntryAtRC(grid, dim, r, c) == 'O') {
        o_num1 += 1;
      }
    }
    // when this row contains zero X or zero O, this is not a draw
    if ((x_num1 == 0) || (o_num1 == 0)) {
      return false;
    }
  }

  // check each column;
  for (int c=0; c < dim; c++) { // loop through each column
    // the number of X's in each column will be stored in x_num2, initialize it to zero
    int x_num2 = 0;
    // the number of O's in each column will be stored in o_num2, initialize it to zero
    int o_num2 = 0;
    for (int r=0; r < dim; r++) { // loop through each row in a specific column
      // update the number of X's when seeing an X
      if (getEntryAtRC(grid, dim, r, c) == 'X') {
        x_num2 += 1;
      }
      // update the number of O's when seeing an O
      else if (getEntryAtRC(grid, dim, r, c) == 'O') {
        o_num2 += 1;
      }
    }
    // when this column contains zero X or zero O, this is not a draw
    if ((x_num2 == 0) || (o_num2 == 0)) {
      return false;
    }
  }
  
  // check top-left to bottom-right diagnol;
  // the number of X's in this diagnol will be stored in x_num3, initialize it to zero
  int x_num3 = 0;
  // the number of X's in this diagnol will be stored in x_num1, initialize it to zero
  int o_num3 = 0;
  for (int n=0; n < dim; n++) { // loop through each top-left to bottom-right position
    // update the number of X's when seeing an X
    if (getEntryAtRC(grid, dim, n, n) == 'X') {
      x_num3 += 1;
    }
    // update the number of O's when seeing an O
    else if (getEntryAtRC(grid, dim, n, n) == 'O') {
      o_num3 += 1;
    }
  }
  // when this diagnol contains zero X or zero O, this is not a draw
  if ((x_num3 == 0) || (o_num3 == 0)) {
    return false;
  }

  // check top-right to bottom-left diagnol;
  // the number of X's in this diagnol will be stored in x_num4, initialize it to zero
  int x_num4 = 0;
  // the number of O's in this diagnol will be stored in o_num3, initialize it to zero
  int o_num4 = 0;
  for (int n=0; n < dim; n++) { // loop through each top-right to bottom-left position
    // update the number of X's when seeing an X
    if (getEntryAtRC(grid, dim, n, dim-1-n) == 'X') {
      x_num4 += 1;
    }
    // update the number of O's when seeing an O
    else if (getEntryAtRC(grid, dim, n, dim-1-n) == 'O') {
      o_num4 += 1;
    }
  }
  // when this diagnol contains zero X or zero O, this is not a draw
  if ((x_num4 == 0) || (o_num4 == 0)) {
    return false;
  }
  // when each row, column, diagnol contains at least one X and one O, this is a draw
  return true;
}



/**********************************************************
 *  Complete the indicated parts of main(), below. 
 **********************************************************/
int main()
{
  // This array holds the actual board/grid of X and Os. It is sized 
  // for the biggest possible case (11x11), but you should only 
  // use dim^2 entries (i.e. if dim=3, only use 9 entries: 0 to 8)
  char tttdata[121];
    
  // dim stands for dimension and is the side length of the 
  // tic-tac-toe board i.e. dim x dim (3x3 or 5x5). 
  int dim;
  // Get the dimension from the user
  cin >> dim;
    
  int dim_sq = dim*dim;

  for(int i=0; i < dim_sq; i++){
    tttdata[i] = '?';
  }

  // Print one of these messages when the game is over
  // and before you quit
  const char xwins_msg[] = "X player wins!";
  const char owins_msg[] = "O player wins!";
  const char draw_msg[] =  "Draw...game over!";
  
  bool done = false;
  char player = 'X';
  // Show the initial starting board
  printTTT(tttdata, dim);

  while(!done){

    //**********************************************************
    // Get the current player's input (i.e. the location they want to
    // choose to place their mark [X or O]) and update the tttdata array.
    // Be sure to follow the requirements defined in the guide/writeup
    // for quitting immediately if the user input is out-of-bounds 
    // (i.e. not in the range 0 to dim_sq-1) as well as continuing to 
    // prompt for an input if the user chooses locations that have already
    // been chosen (already marked with an X or O).
    //**********************************************************

    // Add your code here for getting input
    if (player == 'X') { // when this is player X's turn
      // get the index to put X from the user
      int x_idx;
      cout << "Player X enter your square choice [0-" << dim_sq - 1 << "]: " << endl;
      cin >> x_idx;
      // when the input index is out-of-bound, quit the program without any further steps executed
      if (x_idx > dim_sq - 1) {
        break;
      }
      else { // when input index is in bound
        while (tttdata[x_idx] != '?') { // when the position has already been occupied
          // get index from the user again and update the index value
          cout << "Player X enter your square choice [0-" << dim_sq - 1 << "]: " << endl;
          cin >> x_idx;
          // when the input index is out-of-bound, quit the program
          if (x_idx > dim_sq - 1) {
            done = true; // change the value of done to stop the outer while-loop
            break; // end the current while loop of occupancy
          }
        }
        tttdata[x_idx] = 'X'; // update the board with player X's index choice
      }
      player = 'O'; // change to player O's turn
    }
    else { // when this is player O's turn
      // get the index to put O from the user
      int o_idx;
      cout << "Player O enter your square choice [0-" << dim_sq - 1 << "]: " << endl;
      cin >> o_idx;
      // when the input index is out-of-bound, quit the program without any further steps executed
      if (o_idx > dim_sq - 1) {
        break;
      }
      else { // when input index is in bound
        while (tttdata[o_idx] != '?') { // when the position has already been occupied
          // get index from the user again and update the index value
          cout << "Player O enter your square choice [0-" << dim_sq - 1 << "]: " << endl;
          cin >> o_idx;
          // when the input index is out-of-bound, quit the program
          if (o_idx > dim_sq - 1) {
            done = true; // change the value of done to stop the outer while-loop
            break; // end the current while loop of occupancy
          }
        }
        tttdata[o_idx] = 'O'; // update the board with player O's index choice
      }
      player = 'X'; // change to player X's turn
    }
    // quit the program because the index entered by the user is out-of-bound
    if (done == true) {
      break;
    }


    // Show the updated board if the user eventually chose a valid location
    // (i.e. you should have quit the loop and program by now without any 
    //  other output message if the user chosen an out-of-bounds input).
    printTTT(tttdata, dim);

    //**********************************************************
    // Complete the body of the while loop to process the input that was just
    //  received to check for a winner or draw and update other status, as 
    //  needed. 
    // 
    // To match our automated checkers' expected output, you must output 
    // one of the messages defined above using *one* of the cout commands 
    // (under the appropriate condition) below:
    //   cout << xwins_msg << endl;  OR
    //   cout << owins_msg << endl;  OR
    //   cout << draw_msg << endl;
    //
    // Note: Our automated checkers will examine a specific number of lines
    //  at the end of the program's output and expect to see the updated board
    //  and game status message.  You may certainly add some debug print  
    //  statements during development but they will need to be removed to 
    //  pass the automated checks.
    //**********************************************************
    // when player X wins, print the message and quit the program
    if (checkForWinner(tttdata, dim) == 1) {
      cout << xwins_msg << endl;
      break;
    }
    // when player O wins, print the message and quit the program
    else if (checkForWinner(tttdata, dim) == 2) {
      cout << owins_msg << endl;
      break;
    }
    // when there is a draw, print the message and quit the program
    else if (checkForDraw(tttdata, dim) == true) {
      cout << draw_msg << endl;
      break;
    }

  } // end while
  return 0;
}