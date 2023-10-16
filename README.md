# Clipboard Monitor
This is a simple Python program that monitors the system clipboard for changes and displays the new contents in a scrollable text box. When the clipboard changes, the program will also play a notification sound and bring the window to the front.

## Installation

1.  Install Python 3.x on your system if you haven't already done so.
2.  Install the required Python packages using pip:
```
pip install tkinter pyperclip
```
## Usage

1.  Run the program by executing the `clipboard_monitor.py` script using Python:
`python clipboard_monitor.py` 
2.  The program window will appear, displaying the current contents of the clipboard (if any).
3.  Copy some text to the clipboard (e.g. using Ctrl+C).
4.  The new clipboard contents will be displayed in the text box, and a notification sound will be played. The program window will also be brought to the front.
