# gd_piano_player
Project that converts sheet music files to Geometry Dash SFX triggers using SPWN and Python. Contributions are welcome!

## Prerequisites
- Make sure you have Geometry Dash 2.2, SPWN, Python 3.10+ and Git installed.
- Install the `music21` python library using `pip install music21`.

## Installation
Clone the repository and open it:
```
$ git clone https://github.com/yees7/gd_piano_player
$ cd gd_piano_player
```
## Usage
```sh
$ py run.py [file_name] [level_name (optional)]
```
### Examples
```sh
$ py run.py At_The_Speed_Of_Light.mxl # converts 'At_The_Speed_Of_Light.mxl' to SFX triggers and places them in the topmost level in your 'Created' tab
$ py run.py At_The_Speed_Of_Light.mxl atsolpiano # converts 'At_The_Speed_Of_Light.mxl' to SFX triggers and places them in the level called 'atsolpiano' in your 'Created' tab
```