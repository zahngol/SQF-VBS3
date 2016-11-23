# SQF for VBS3
SQF Syntax Highlighting and Enhancement Features for Bohemia Interactive Simulations' [VBS3](https://bisimulations.com/virtual-battlespace-3)

## Table of Contents
- [Features](#features)
- [Installation](#installation)
    + [Using Package Control](#using-package-control-recommended)
    + [Manual Install](#manual-install)
- [Usage](#usage)
    + [Snippets](#snippets)
    + [Search Resources](#search-resources)
    + [Color Picker](#color-picker)
    + [Keyboard Shortcuts](#keyboard-shortcuts)
    + [Open Report File](#open-report-file)
- [Support](#support)

## Features:
* Syntax highlighting
* Autocomplete for commands and functions
* Snippets for autoformating code blocks for common functions
    * e.g. `while`, `waitUntil`, and `diagMessage`
* Search shortcuts for the BIS Wiki, Developers Reference, and VBS Forums
* Color picker that returns VBS compatible values (Modification of [ColorPicker](https://packagecontrol.io/packages/ColorPicker) by [Weslly](https://github.com/weslly))

## Installation:

### Using [Package Control](https://packagecontrol.io/) (_Recommended_)

For all Sublime Text 2/3 users we recommend install via [Package Control](https://packagecontrol.io/).

1. [Install](https://packagecontrol.io/installation) Package Control if you haven't yet.
1. Use `Ctrl+Shift+P` then `Package Control: Install Package`
1. Look for `SQF for VBS3` and install it.

### Manual Install

1. Click the `Preferences > Browse Packages…` menu
1. Browse up a folder and then into the `Installed Packages/` folder
1. Download [zip package](https://github.com/zahngol/SQF-VBS3/archive/master.zip) rename it to `SQF-VBS3.sublime-package` and copy it into the `Installed Packages/` directory
1. Restart Sublime Text

## Usage

### Snippets
- As you type out a command that has a snippet created for it, you will see it as an autocomplete option. 
- If you hit `Enter` with the snippet option highlighted, the rest of the code will be filled in.
- Once the code has been added, you can hit `Tab` to move to each of the key input areas for that command/code block 

![VBS3 Snippets](demo/vbs3_snippets.gif)

### Search Resources
- You can search various development resources by highlighting a word, and then either right-clicking and selecting the resource you want to search from the context menu, or by pressing the corresponding [keyboard shortcut](#keyboard-shortcuts).

### Color Picker
- You can retrive a formated color value from a color picker GUI by either right-clicking and selecting `Color Picker - VBS Format` from the context menu, or by pressing the corresponding [keyboard shortcut](#keyboard-shortcuts).
- The color will be returned in R,B,G format, with each value being calculated within a range of 0-1

### Keyboard Shortcuts

- Search VBS3 Wiki
    + `Ctrl+Shift+F1`
    + `Ctrl+Shift+'`
- Search VBS3 Developers Reference
    + `Ctrl+Shift+F2`
- Search VBS Forums
    + `Ctrl+Shift+F3`
- Open Color Picker
    + `Ctrl+Shift+C`

### Open Report File
- You can open the VBS3_64.RPT file without having to navigate to the proper folder by going to `Tools -> VBS Resources -> Open VBS RPT File`
    + Any errors that you see show up in VBS should be near the bottom of this file

## Support:
* Any bugs about SQF for VBS3 please feel free to report [here](https://github.com/zahngol/SQF-VBS3/issues).
* And you are welcome to fork and submit pullrequests.
