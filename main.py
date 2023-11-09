import os, openai, json
import tkinter as tk
import tkinter.scrolledtext as st
import time, datetime
import threading
import pyperclip
import tkinter.filedialog as fd

openai.api_key = json.load(open("key.json"))["openAiKey"]
def openai_api(prompt):
    # Use the openai API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{prompt}",
        max_tokens=1024,
        temperature=0.5
    )
    # Return the generated response
    return response["choices"][0]["text"]

def clipboard_monitor(text_box, clipboard_history):
    # Initialize last_value to the current value of the clipboard
    last_value = pyperclip.paste()
    separator = '-' * 50
    while True:

        current_value = pyperclip.paste()
        # If the value has changed, update the text box and notify the user
        if current_value != last_value:
            last_value = current_value
            clipboard_history.append(last_value)
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
    
def save_file_dialog():
    filetypes = (("Text files", "*.txt"), ("All files", "*.*"))
    now = datetime.datetime.now().strftime("%B %d, %Y  %I-%M %p")
    default_filename = f"history_{now}.txt"
    
    # get directory path of main.py file
    main_dir = os.path.dirname(os.path.abspath(__file__))
    
    file_input = fd.asksaveasfilename(title="Save Clipboard History As", filetypes=filetypes, defaultextension="", initialfile=default_filename, initialdir=main_dir)
    # if user cancels save dialog, file_input will be empty string
    file_name = file_input[:-4] + f"_{now}.txt"
    return file_name     

def save_to_file(clipboard_history):
    file_name = save_file_dialog()
    if not file_name:
        return
    with open(file_name, 'w') as file:
        for item in clipboard_history:
            file.write(item + '\n' + '-' * 50 + '\n')



# Main entry point for the program
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Clipboard Monitor")
    root.geometry("400x300")

    text_box = st.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
    text_box.pack(fill=tk.BOTH, expand=True)

    # Start a background thread to monitor the clipboard
    clipboard_history = []
    monitor_thread = threading.Thread(target=clipboard_monitor, args=(text_box, clipboard_history), daemon=True)
    monitor_thread.start()

    def on_closing():
        save_to_file(clipboard_history)
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()
