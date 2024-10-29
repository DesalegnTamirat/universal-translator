# Necessary imports
import tkinter as tk
from tkinter import Tk, Label, Text, Button, StringVar, OptionMenu
from googletrans import Translator, LANGUAGES

# Create the main window
root = Tk()
root.title("Universal Translator")
root.geometry("700x500")
root.configure(bg="#2c3e50")  # Darker background color

# Center the window
root.eval('tk::PlaceWindow . center')

# Add a label and input field for entering the text
Label(root, text="Enter the text to be translated:", bg="#2c3e50", fg="white").grid(row=0, column=0, pady=5)
input_field = Text(root, height=8, width=45, bg="#34495e", fg="white", bd=0, highlightthickness=1, highlightbackground="#007bff")
input_field.grid(row=1, column=0, rowspan=4, padx=15)

# Add a label and output field to display the translation
Label(root, text="Translated Text:", bg="#2c3e50", fg="white").grid(row=6, column=0, pady=5)
output_field = Text(root, height=8, width=45, state=tk.DISABLED, bg="#34495e", fg="white", bd=0, highlightthickness=1, highlightbackground="#007bff")
output_field.grid(row=7, column=0, rowspan=4, padx=15)

# Add dropdown variables for Language selection
src_lang_var = StringVar(value="english") #Default: English
tgt_lang_var = StringVar(value="amharic")     # Default: Amharic

# Create a list of language names for dropdown
language_names = {code: name for code, name in LANGUAGES.items()}

# Add dropdown for source and target languages
Label(root, text="Select Source Language:", bg="#2c3e50", fg="white").grid(row=2, column=2)
src_dropdown = OptionMenu(root, src_lang_var, *language_names.values())
src_dropdown.config(bg="#007bff", fg="white", highlightbackground="#007bff", borderwidth=0)
src_dropdown.grid(row=2, column=1)

Label(root, text="Select Target Language:", bg="#2c3e50", fg="white").grid(row=8, column=2)
tgt_dropdown = OptionMenu(root, tgt_lang_var, *language_names.values())
tgt_dropdown.config(bg="#007bff", fg="white", highlightbackground="#007bff", borderwidth=0)
tgt_dropdown.grid(row=8, column=1)

# Initialize translator
def translate_text():
    input_text = input_field.get("1.0", tk.END).strip()
    if not input_text:
        output_field.config(state=tk.NORMAL)
        output_field.delete("1.0", tk.END)
        output_field.insert(tk.END, "Please enter text to translate.")
        output_field.config(state=tk.DISABLED)
        return None

    # Get selected languages from the dropdowns
    src_lang = list(language_names.keys())[list(language_names.values()).index(src_lang_var.get())]
    tgt_lang = list(language_names.keys())[list(language_names.values()).index(tgt_lang_var.get())]

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
translate_button = Button(root, text="Translate", command=translate_text, bg="#007bff", fg="white", bd=0)
translate_button.grid(row=5, column=0, pady=30)

# Run the app
root.mainloop()
