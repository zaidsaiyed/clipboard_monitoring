import tkinter as tk
import tkinter.scrolledtext as st
import time, threading, pyperclip

def clipboard_monitor(text_box):
    # Initialize last_value to the current value of the clipboard
    last_value = pyperclip.paste()
    separator = '-' * 50
    while True:
        
        current_value = pyperclip.paste()
        # If the value has changed, update the text box and notify the user
        if current_value != last_value:
            last_value = current_value
            text_box.configure(state=tk.NORMAL)
            text_box.insert(tk.END, f"{separator}\n{last_value}\n")
            text_box.see(tk.END)
            text_box.configure(state=tk.DISABLED) 
            # Bring the window to the front so that the user sees it
            root.attributes("-topmost", True)
            # Reset the topmost attribute after idle to prevent locking the window on top
            root.after_idle(root.attributes, '-topmost', False)
            root.bell()
        
        time.sleep(0.1)

# Main entry point for the program
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Clipboard Monitor")
    root.geometry("400x300")

    text_box = st.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
    text_box.pack(fill=tk.BOTH, expand=True)

    # Start a background thread to monitor the clipboard
    monitor_thread = threading.Thread(target=clipboard_monitor, args=(text_box,), daemon=True)
    monitor_thread.start()

    # Handle the case where the user closes the window
    root.protocol("WM_DELETE_WINDOW", root.quit)
    
    root.mainloop()
