import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class ConfigEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Config Editor")
        self.tabs = ttk.Notebook(master)
        self.tabs.pack(expand=1, fill='both')

        self.load_button = ttk.Button(master, text="Select Config Folder", command=self.load_config_folder)
        self.load_button.pack(pady=10)

    def load_config_folder(self):
        folder_path = filedialog.askdirectory(title="Select Config Folder")
        if not folder_path:
            return

        cfg_files = [f for f in os.listdir(folder_path) if f.endswith('.cfg')]
        for cfg_file in cfg_files:
            tab = ttk.Frame(self.tabs)
            self.tabs.add(tab, text=cfg_file)

            file_path = os.path.join(folder_path, cfg_file)
            with open(file_path, 'r') as file:
                config_data = file.readlines()

            options = {}
            entry_widgets = {}  # Dictionary to store entry widgets with their corresponding keys
            current_section = None
            for line in config_data:
                line = line.strip()
                if line.startswith("[") and line.endswith("]"):
                    current_section = line[1:-1]
                elif '=' in line and current_section:
                    key, value = line.split("=", 1)
                    options[key.strip()] = value.strip()

            row_counter = 0
            col_counter = 0
            for option, value in options.items():
                if row_counter >= 35:
                    row_counter = 0
                    col_counter += 1

                label = ttk.Label(tab, text=option)
                label.grid(row=row_counter, column=col_counter * 2, sticky="w", padx=5, pady=2)
                entry = ttk.Entry(tab, width=20)
                entry.insert(0, value)
                entry.grid(row=row_counter, column=col_counter * 2 + 1, padx=5, pady=2)
                # Store entry widget with its corresponding key
                entry_widgets[option] = entry
                row_counter += 1

            save_button = ttk.Button(tab, text="Save",
                                     command=lambda file_path=file_path, entry_widgets=entry_widgets: self.save_config(
                                         file_path, entry_widgets))
            save_button.grid(row=row_counter, columnspan=col_counter * 2 + 2, pady=10)

    def save_config(self, file_path, entry_widgets):
        new_options = {}
        for key, entry in entry_widgets.items():
            value = entry.get()
            new_options[key] = value

        with open(file_path, 'r') as file:
            config_data = file.readlines()

        with open(file_path, 'w') as file:
            for line in config_data:
                if "=" in line:
                    key, _ = line.split("=", 1)
                    key = key.strip()
                    if key in new_options:
                        file.write(f"{key} = {new_options[key]}\n")
                    else:
                        file.write(line)
                else:
                    file.write(line)


def main():
    root = tk.Tk()
    app = ConfigEditor(root)
    root.mainloop()


if __name__ == "__main__":
    main()
