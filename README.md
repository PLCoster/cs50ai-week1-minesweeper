# CS50AI Week 1 - Minesweeper

## Task:

Write an AI to play Minesweeper.


## Background:

Minesweeper is a puzzle game that consists of a grid of cells, where some of the cells contain hidden “mines.” Clicking on a cell that contains a mine detonates the mine, and causes the user to lose the game. Clicking on a “safe” cell (i.e., a cell that does not contain a mine) reveals a number that indicates how many neighboring cells – where a neighbor is a cell that is one square to the left, right, up, down, or diagonal from the given cell – contain a mine.

The goal of the game is to flag (i.e., identify) each of the mines. In many implementations of the game, including the one in this project, the player can flag a mine by right-clicking on a cell (or two-finger clicking, depending on the computer).


## Knowledge Representation:

The AI's knowledge is represented as the following logical sentence:

{A, B, C, D, E, F, G, H} = 1

where {A, B, C etc.} are a set of cells, and the number 1 is the count of mines among those cells. This representation allows the following inferences to be made, e.g.:

{D, E} = 0
This implies that none of D, E contain mines, i.e. all are safe cells.

{A, B, C} = 3
This implies that all cells A, B, C contain a mine.

Furthermore, in general when we have two sentences where sentence A is a subset of sentence B, a new sentence can be infered:

setB - setA = countB - countA

Hence while playing minesweeper and clicking on cells, logical sentences are added to the AI's knowledge base. Often as a new sentence is added to the knowledge base, further inferences can be made allowing the identification of mines or safe spaces.


## Specification:

Complete the implementations of the Sentence class and the MinesweeperAI class in minesweeper.py.

In the Sentence class, complete the implementations of known_mines, known_safes, mark_mine, and mark_safe.

* The known_mines function should return a set of all of the cells in self.cells that are known to be mines.
* The known_safes function should return a set of all the cells in self.cells that are known to be safe.
* The mark_mine function should first check to see if cell is one of the cells included in the sentence.
  * If cell is in the sentence, the function should update the sentence so that cell is no longer in the sentence, but still represents a logically correct sentence given that cell is known to be a mine.
  * If cell is not in the sentence, then no action is necessary.
* The mark_safe function should first check to see if cell is one of the cells included in the sentence.
  * If cell is in the sentence, the function should update the sentence so that cell is no longer in the sentence, but still represents a logically correct sentence given that cell is known to be safe.
  * If cell is not in the sentence, then no action is necessary.

In the MinesweeperAI class, complete the implementations of add_knowledge, make_safe_move, and make_random_move.

* add_knowledge should accept a cell (represented as a tuple (i, j)) and its corresponding count, and update self.mines, self.safes, self.moves_made, and self.knowledge with any new information that the AI can infer, given that cell is known to be a safe cell with count mines neighboring it.
  * The function should mark the cell as one of the moves made in the game.
  * The function should mark the cell as a safe cell, updating any sentences that contain the cell as well.
  * The function should add a new sentence to the AI’s knowledge base, based on the value of cell and count, to indicate that count of the cell’s neighbors are mines. Be sure to only include cells whose state is still undetermined in the sentence.
  * If, based on any of the sentences in self.knowledge, new cells can be marked as safe or as mines, then the function should do so.
  * If, based on any of the sentences in self.knowledge, new sentences can be inferred (using the subset method described in the Background), then those sentences should be added to the knowledge base as well.
* make_safe_move should return a move (i, j) that is known to be safe.
  * The move returned must be known to be safe, and not a move already made.
  * If no safe move can be guaranteed, the function should return None.
  * The function should not modify self.moves_made, self.mines, self.safes, or self.knowledge.
* make_random_move should return a random move (i, j).
  * This function will be called if a safe move is not possible: if the AI doesn’t know where to move, it will choose to move randomly instead.
  * The move must not be a move that has already been made.
  * The move must not be a move that is known to be a mine.
  * If no such moves are possible, the function should return None.


## Usage:

Requires Python(3) and Python package installer pip(3) to run:

Install requirements:
$pip3 install -r requirements.txt

Run Game:
$python3 runner.py


## Further Ideas:

* Adding the option to choose the size of minefield grid and number of mines up to some reasonable limits.
* An option to give the AI knowledge of the number of mines in the grid, which would let it start with a knowledge base of {all grid cells} = number of mines, which would allow additional inferences to be made during play. It would also allow the AI to automatically mark all remaining cells as safe once all mines have been found.