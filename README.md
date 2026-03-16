## Amraj's Boogle Game (GUI Version)

This project is a simple **Boggle-style word game** with a graphical user interface built using `tkinter`.  
The program generates a 4x4 board of random letters and lets the player enter words they can form from the board.  
Valid words (according to `words.txt` and the game rules) earn points based on their length.

### Files
- **`Amraj_Dhanoa_Boogle_Game_Final_With_GUI.py`**: Main Python program that runs the GUI Boggle game.
- **`words.txt`**: Text file containing the dictionary of allowed words (one word per line, letters only).

### Requirements
- **Python 3** (recommended 3.8+)
- Standard Python library `tkinter` (included with most Python installations on macOS/Windows).
- A `words.txt` file in the **same folder** as the Python file.

### How to Run
1. Open a terminal and navigate to this folder:
   ```bash
   cd "/Users/amrajdhanoa/Computer Science Grade 11/Com Sci Summative"
   ```
2. Make sure `words.txt` is in this folder.
3. Run the game:
   ```bash
   python3 Amraj_Dhanoa_Boogle_Game_Final_With_GUI.py
   ```

### How to Play
- A 4x4 grid of random letters is displayed.
- Type a word into the input box and press **Submit**.
- You can submit multiple words for the same board.
- When you are done, click **Display My Score!** to:
  - See which of your words were valid.
  - See how many points each word earned.
  - See your **total score**.
- You can then choose to **play another round** (new board) or **quit**.

### Word and Scoring Rules
- Words must:
  - Appear in `words.txt`.
  - Use only letters that appear on the current 4x4 board.
  - Use each letter **at most once**.
  - Be formed by letters that are **touching** each other horizontally, vertically, or diagonally on the board.
- Scoring (based on word length):
  - 2 letters: 1 point
  - 3 letters: 2 points
  - 4 letters: 5 points
  - 5 letters: 7 points
  - 6 or more letters: 10 points

### Notes
- If `words.txt` cannot be found, the program will print `Not found` in the terminal.
