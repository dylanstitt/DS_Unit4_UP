import time, pyautogui

# THIS IS THE SOLUTION SET FOR 5 BLOCKS

moves = [
  ("A", "C"),
  ("A", "B"),
  ("C", "B"),
  ("A", "C"),
  ("B", "A"),
  ("B", "C"),
  ("A", "C"),
  ("A", "B"),
  ("C", "B"),
  ("C", "A"),
  ("B", "A"),
  ("C", "B"),
  ("A", "C"),
  ("A", "B"),
  ("C", "B"),
  ("A", "C"),
  ("B", "A"),
  ("B", "C"),
  ("A", "C"),
  ("B", "A"),
  ("C", "B"),
  ("C", "A"),
  ("B", "A"),
  ("B", "C"),
  ("A", "C"),
  ("A", "B"),
  ("C", "B"),
  ("A", "C"),
  ("B", "A"),
  ("B", "C"),
  ("A", "C")
]

time.sleep(5)
for move in moves:
    i, j = move[0], move[1]
    pyautogui.press(i)
    #time.sleep(.05)
    pyautogui.press('enter')
    #time.sleep(.05)
    pyautogui.press(j)
    #time.sleep(.05)
    pyautogui.press('enter')