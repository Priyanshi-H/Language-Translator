import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from googletrans import Translator, LANGUAGES

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multilingual Translator App")
        
        self.translator = Translator()
        
        # Language selection frames
        self.src_lang_frame = ttk.Frame(self.root)
        self.dest_lang_frame = ttk.Frame(self.root)
        
        self.src_lang_frame.grid(row=0, column=0, padx=10, pady=10)
        self.dest_lang_frame.grid(row=0, column=1, padx=10, pady=10)
        
        self.src_lang_label = ttk.Label(self.src_lang_frame, text="Source Language:")
        self.src_lang_label.pack(anchor=tk.W)
        self.src_lang_combobox = ttk.Combobox(self.src_lang_frame, values=list(LANGUAGES.values()), state="readonly")
        self.src_lang_combobox.pack(fill=tk.X)
        
        self.dest_lang_label = ttk.Label(self.dest_lang_frame, text="Destination Language:")
        self.dest_lang_label.pack(anchor=tk.W)
        self.dest_lang_combobox = ttk.Combobox(self.dest_lang_frame, values=list(LANGUAGES.values()), state="readonly")
        self.dest_lang_combobox.pack(fill=tk.X)
        
        # Text input and output frames
        self.input_frame = ttk.Frame(self.root)
        self.output_frame = ttk.Frame(self.root)
        
        self.input_frame.grid(row=1, column=0, padx=10, pady=10)
        self.output_frame.grid(row=1, column=1, padx=10, pady=10)
        
        self.input_label = ttk.Label(self.input_frame, text="Enter text to translate:")
        self.input_label.pack(anchor=tk.W)
        self.input_text = tk.Text(self.input_frame, height=10, width=40)
        self.input_text.pack(fill=tk.BOTH, expand=True)
        
        self.output_label = ttk.Label(self.output_frame, text="Translated text:")
        self.output_label.pack(anchor=tk.W)
        self.output_text = tk.Text(self.output_frame, height=10, width=40, state="disabled")
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        # Browse button to load text from file
        self.browse_button = ttk.Button(self.root, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=2, column=0, pady=10)
        
        # Translate button
        self.translate_button = ttk.Button(self.root, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=2, column=1, pady=10)
        
        # Copy button to copy translated text to clipboard
        self.copy_button = ttk.Button(self.root, text="Copy", command=self.copy_to_clipboard)
        self.copy_button.grid(row=3, column=0, columnspan=2, pady=10)
    
    def translate_text(self):
        src_lang = self.src_lang_combobox.get()
        dest_lang = self.dest_lang_combobox.get()
        text = self.input_text.get("1.0", tk.END).strip()
        
        if not src_lang or not dest_lang or not text:
            messagebox.showerror("Error", "Please fill all fields.")
            return
        
        src_lang_code = self.get_language_code(src_lang)
        dest_lang_code = self.get_language_code(dest_lang)
        
        try:
            translation = self.translator.translate(text, src=src_lang_code, dest=dest_lang_code)
            self.output_text.config(state="normal")
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translation.text)
            self.output_text.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def get_language_code(self, lang_name):
        for code, name in LANGUAGES.items():
            if name == lang_name:
                return code
        return None
    
    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                self.input_text.delete("1.0", tk.END)
                self.input_text.insert(tk.END, text)
    
    def copy_to_clipboard(self):
        translated_text = self.output_text.get("1.0", tk.END).strip()
        if translated_text:
            self.root.clipboard_clear()
            self.root.clipboard_append(translated_text)
            messagebox.showinfo("Info", "Translated text copied to clipboard.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
