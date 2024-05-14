# OpenTTD Server Config File Editor

This software is a work-in-progress tool designed for OpenTTD server administrators to edit server configuration files conveniently through a graphical user interface (GUI). It aims to simplify the process of configuring and managing OpenTTD server settings by providing an intuitive interface for editing configuration files.

## How It Works

The OpenTTD Server Config File Editor is built using Python an PyQt5.
We open the folder with your config files and create tabs for each file found (including custom cfg files) and from there
we create sub-tabs for each section of a given config file.

It gives you a nice and easy gui to quickly navigate to and change sections. I'd like to eventually set this up so that the max values, bool and such have drop down boxes and value enforcement.
I'd also like to add a section to handle server-specific stuff from multiple files.

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


