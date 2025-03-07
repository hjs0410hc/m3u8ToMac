# M3U8ToMac

This project is designed to manage and manipulate playlists.

Read Mac's Music Library and relocate existing M3U8 playlist's filepath to corresponding path.


## Files

### `createFile.py`

This script is responsible for creating M3U8 playlist's metadata

### `loadFile.py`

This script loads created metadata and locating existing track in target playlist to Mac's path.

## Usage

1. **Creating a Metadata:**
    - Edit `createFile.py` to use your Music Library path, and run `createFile.py` to initialize and save a metadata.

2. **Loading a Playlist:**
    - Edit `loadFile.py` to indicate your existing playlist folder and converting destination folder, and Use `loadFile.py` to read metadata and convert your existing playlist.

## Requirements

- Python 3.x

## Installation

Clone the repository or download ZIP from GitHub Repository

## Running the Scripts

- To create a new playlist:
  ```sh
  python createFile.py
  ```

- To load an existing playlist:
  ```sh
  python loadFile.py
  ```

# License

No License since it's very simple Python scripts. Please steal.