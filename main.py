import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QTabWidget, QWidget, QVBoxLayout, QLabel, \
    QPushButton, QLineEdit, QHBoxLayout, QScrollArea
from configparser import ConfigParser


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.tabs_info = {}  # Dictionary to store file path and section name associated with each tab

    def initUI(self):
        self.setWindowTitle('OpenTTDConfig')
        self.setGeometry(100, 100, 800, 500)


        open_action = QAction('Open Config Directory', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.openFile)


        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)

        # Create file menu and add actions
        file_menu = self.menuBar().addMenu('File')
        file_menu.addAction(open_action)
        file_menu.addAction(exit_action)

        self.main_tabs = QTabWidget(self)
        self.setCentralWidget(self.main_tabs)

    def openFile(self):
        options = QFileDialog.Options()
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", options=options)
        if folder_path:
            cfg_files = [file for file in os.listdir(folder_path) if file.endswith('.cfg')]
            for cfg_file in cfg_files:
                cfg_tabs = QTabWidget()
                config = ConfigParser(strict=False)
                try:
                    file_path = os.path.join(folder_path, cfg_file)
                    print("Reading file:", file_path)
                    config.read(file_path)
                    print("Sections in {}: {}".format(cfg_file, config.sections()))

                    for section in config.sections():
                        tab = QWidget()
                        layout = QVBoxLayout()
                        seen_options = set()  # To track duplicate options within a section
                        for key, value in config.items(section):
                            # Skip duplicate options within a section
                            if key.lower() in seen_options:
                                continue
                            seen_options.add(key.lower())
                            field_layout = QHBoxLayout()
                            label = QLabel(key)
                            field_layout.addWidget(label)
                            line_edit = QLineEdit(value)
                            field_layout.addWidget(line_edit)
                            layout.addLayout(field_layout)
                        save_button = QPushButton("Save")
                        save_button.clicked.connect(
                            lambda _, s=section, f=cfg_file, t=tab, p=file_path: self.saveConfig(f, s, t, p))
                        layout.addWidget(save_button)
                        tab.setLayout(layout)

                        # Add scroll area to the tab
                        scroll_area = QScrollArea()
                        scroll_area.setWidgetResizable(True)
                        scroll_area.setWidget(tab)

                        cfg_tabs.addTab(scroll_area, section)

                        # Store file path and section name directly with the scroll area widget
                        self.tabs_info[scroll_area] = {'file': file_path, 'section': section}
                        print("Tab added:", cfg_file, section)

                    self.main_tabs.addTab(cfg_tabs, cfg_file)
                    print("Added tabs for:", cfg_file)
                except Exception as e:
                    print("Error while processing {}: {}".format(cfg_file, str(e)))

    def saveConfig(self, cfg_file, section, tab, file_path):
        config = ConfigParser()
        try:
            if file_path and section:
                config.read(file_path)

                # Print out sections to debug
                print("Sections in {}: {}".format(cfg_file, config.sections()))

                layout = tab.layout()
                for i in range(layout.count() - 1):  # Exclude save button
                    field_layout = layout.itemAt(i).layout()
                    label = field_layout.itemAt(0).widget()
                    line_edit = field_layout.itemAt(1).widget()
                    # Check if the value has been modified
                    original_value = config.get(section, label.text(), fallback=None)
                    new_value = line_edit.text()
                    if original_value != new_value:
                        config.set(section, label.text(), line_edit.text())

                # Print out sections again just before saving
                print("Sections before saving in {}: {}".format(cfg_file, config.sections()))

                with open(file_path, 'w') as f:
                    config.write(f)
                print("Saved changes to", file_path)
            else:
                print("Error: No file path or section name found for the current tab")
        except Exception as e:
            print("Error while saving {}: {}".format(cfg_file, str(e)))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
