# dng_extractor
Search DNG (or other types) in folders by pattern and transfer them to other directory

This program allows you to find files based on a specified pattern within a given directory. The found files are then moved to a target directory for storage.

Initially, the program was designed to optimize the extraction of DNG files after transporting them via AirDrop. In its original state, a DNG file is contained within a directory that also contains other file types. iOS refers to these as assets. Typically, all assets (or folders) after transfer have names starting with IMG_*.
The program eliminates the need to manually go into each folder by gathering these folders.
P.S. The folder search pattern in this version is hardcoded. The reason is that the program was written for the Apple ecosystem, where file naming is quite stable.

The program has a simple graphical interface.
Global settings are set through the configuration file config.ini.

Main window with default settings:
![Main window](/assets/images/main_window.png)
