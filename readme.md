# OpenTTD Server Config File Editor

This software is a work-in-progress tool designed for OpenTTD server administrators to edit server configuration files conveniently through a graphical user interface (GUI). It aims to simplify the process of configuring and managing OpenTTD server settings by providing an intuitive interface for editing configuration files.

## How It Works

The OpenTTD Server Config File Editor is built using Python and utilizes the Tkinter library for creating the graphical user interface. It allows users to select a folder containing OpenTTD server configuration files (`*.cfg`), and then displays each configuration file in a separate tab within the application.

For each configuration file, the editor parses the file to extract the configuration options and their corresponding values. It then presents these options and values in a structured format within the GUI, allowing users to easily view and modify them.

Users can modify the values of configuration options directly within the application's interface. Once modifications are made, they can save the changes back to the original configuration file. The editor ensures that the modified configuration file retains its original formatting and comments while updating the values of the specified configuration options.

![Demo Gif](https://github.com/SarahRoseLives/PyOpenTTDConfig/blob/master/demo.gif?raw=true)

## Features (Work in Progress)

- Select folder containing OpenTTD server configuration files.
- View and edit configuration options and their values.
- Save modifications back to the original configuration files.
- Retain original formatting and comments of configuration files.
- Support for various configuration file formats.

## Usage

1. Run the application.
2. Click on the "Select Config Folder" button to choose the folder containing your OpenTTD server configuration files.
3. Once the folder is selected, the editor will display each configuration file in a separate tab.
4. Modify the values of configuration options as needed.
5. Click the "Save" button to save the modifications back to the original configuration files.

## Future Improvements

- Improved error handling and validation.
- Clean-up code and resolve GUI layout issues.
- Enhanced user interface with more features and customization options.

## Contributions

Contributions to this project are welcome! If you have any suggestions, bug reports, or feature requests, please feel free to open an issue or submit a pull request on the GitHub repository.


