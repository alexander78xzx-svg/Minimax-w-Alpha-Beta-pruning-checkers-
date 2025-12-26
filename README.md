# Minimax Checkers

A fully functional Checkers engine built from scratch in Python, featuring an unbeatable AI powered by the Minimax Algorithm with  Alpha-Beta Pruning optimization.

![1226-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/653877a7-43e0-479c-b18f-307b57412f73)

## About The Project


This project is a complete implementation of the game of Checkers (Draughts) with a graphical user interface (GUI) and an intelligent "AI" opponent. 

It was built to explore game theory, recursive algorithms, and search optimization. The AI doesn't just play randomly; it thinks 5-6 turns ahead to trap the player, forcing captures and setting up multi-jump chains.

### Key Features
* **Minimax Algorithm:** The AI evaluates thousands of future board states to determine the optimal move.
* **Alpha-Beta Pruning:** Optimized the search algorithm to prune bad branches, significantly increasing performance and allowing for deeper search depths (Level 6+).
* **Recursive Logic:** Handles complex multi-hop double/triple jumps seamlessly.
* **Rule Compliance:** Enforces strict checkers rules, including mandatory capture (global priority) and King Promotion.
* **Pygame GUI:** A clean, responsive interface built with Python's Pygame library.

## How It Works (The "AI")

The core of this project is a decision engine that combines recursive search algorithms with heuristic evaluation.

### 1. The Minimax Algorithm

The AI uses the Minimax algorithm to look into the future. It builds a decision tree of possible board states:

-   **Root:** The current board.
    
-   **Depth 1:** All legal moves the AI can make.
    
-   **Depth 2:** All legal responses the human opponent can make.
    
-   **Depth 3+:** The AI continues this simulation up to a depth of 6 turns (Python performance limitations).
    

The algorithm assumes the opponent plays optimally (i.e., the "Minimizing" player tries to force the lowest possible score for the AI).2

### 2. Evaluation Function

At the maximum depth, the AI cannot predict further, so it calculates a "score" for the board state using a static evaluation function:

-   Piece Count: A basic piece is worth  1 point.
    
-   King Weight: A King is worth 3 points (prioritizing promotion).

The score is calculated as: `(White Score) - (Red Score)`. Positive values favor the player, negative values favor AI.

### 3. Alpha-Beta Pruning (Optimization)

To achieve a search depth of 6 without lag, I implemented Alpha-Beta pruning. This optimization significantly reduces the number of nodes the algorithm needs to evaluate.

-   Alpha ($\alpha$): The best score the human can guarantee.
    
-   Beta ($\beta$): The best score the AI can guarantee.
    

How it works: If the AI finds a move in one branch that is clearly worse than a move found in a previous branch, it strictly cuts off (prunes) the rest of that branch, this is a significant performance boost.
### 4. Complex Move Logic

The engine handles unique Checkers edge cases that standard Minimax implementations often miss:

-   Forced Captures (Global): Before generating moves, the engine scans the entire board to check for capture opportunities. If a capture exists, all non-capture moves are invalidated to enforce standard tournament rules.
    
-   Recursive Double Jumps: When a piece captures, the engine recursively calls the move function to check if the same piece can jump again. This allows the AI to "see" and execute multi-jump chains in a single turn.

