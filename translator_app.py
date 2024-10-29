# neccesary imports
import tkinter as tk
from tkinter import Tk, Label, Text, Button
from googletrans import Translator, LANGUAGES

#create the main window
root = Tk()
root.title("Universal Translator")
root.geometry("600x400")

# Add a label and input field for entering the text
Label(root, text="Enter the statement to be translated:").pack(pady=10)
input_field = Text(root, height=5, width=50)
input_field.pack(padx=10, pady=10)


# Add a label and output field to display the translation
Label(root, text="Translated Text: ").pack(pady=10)
output_field = Text(root, height=5, width=50, state=tk.DISABLED)
output_field.pack(padx=10, pady=10)

# Add dropdown variables for Language selection
src_lang_var = tk.StringVar(value="auto") # Default: auto-detect
tgt_lang_var = tk.StringVar(value="en") # Default: English

# Add dropdown for source and target languages
Label(root, text="Seclect source Language: ").pack(pady=10)
src_dropdown = tk.OptionMenu(root, src_lang_var, *LANGUAGES.keys())
src_dropdown.pack(pady=10)

Label(root, text="Select the target Language: ").pack(pady=10)
src_dropdown = tk.OptionMenu(root, tgt_lang_var, *LANGUAGES.keys())
src_dropdown.pack(pady=10)

# Initialize translator
def translate_text():
  input_text = input_field.get("1.0", tk.END).strip()
  if not input_text:
    output_field.config(state=tk.NORMAL)
    output_field.delete("1.0", tk.END)
    output_field.insert(tk.END, "please enter text to translate.")
    output_field.config(state=tk.DISABLED)
    return None
  
  #Get selected languages from the dropdowns
  src_lang = src_lang_var.get()
  tgt_lang = tgt_lang_var.get()

  try:
    translated = Translator().translate(input_text, src=src_lang, dest=tgt_lang)
    output_field.config(state=tk.NORMAL)
    output_field.delete("1.0", tk.END)
    output_field.insert(tk.END, translated.text)
    output_field.config(state=tk.DISABLED)
  except Exception as err:
    output_field.config(state=tk.NORMAL)
    output_field.delete("1.0", tk.END)
    output_field.insert(tk.END, f"Error: {str(err)}")
    output_field.config(state=tk.DISABLED)

# Connect the translate button with the function
Button(root, text="Translate", command=translate_text).pack(pady=15)



#run the app
root.mainloop()