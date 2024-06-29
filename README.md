# File-Organizer
## Overview

This Python script organizes files in a directory based on their file extensions into separate subdirectories for Music, Videos, Documents, Images, and Others using the `os`, `sys`, and `shutil` libraries.

## Features

- **File Type Detection**: Automatically identifies file types based on their extensions (.mp3, .mp4, .pdf, etc.).
- **Directory Creation**: Creates new directories for each file type if they don't already exist.
- **File Movement**: Moves files from the original directory to their respective subdirectories.
- **Summary**: Provides a summary of the number of files processed and directories created.

## Requirements

- Python 3.x
- Libraries used: `os`, `sys`, `shutil`

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository

2. **Run the Script**:
   ```bash
   python file_organizer.py

Please follow the prompts to enter the absolute path of the directory you'd like to organize.

3. **Expected Output**:
- Directories created: Music, Videos, Documents, Images, Other
- Files moved into their respective directories based on their file types.

## Example

Assume you have a directory `~/directory` with various files:

    File Organizer started. Organizing files in directory(Absolute Path): /path/to/your/directory
    Creating directories for file types:
    - Created Directory: /path/to/your/directory/Images
    - Created Directory: /path/to/your/directory/Documents
    - Created Directory: /path/to/your/directory/Videos
    - Created Directory: /path/to/your/directory/Music
    - Created Directory: /path/to/your/directory/Other
    Moving files...
    - Moving file: example1.mp3 to /path/to/your/directory/Music
    - Moving file: example2.mp4 to /path/to/your/directory/Videos
    - Moving file: example3.pdf to /path/to/your/directory/Documents
    - Moving file: example4.jpg to /path/to/your/directory/Images
    - Moving file: example5.py to /path/to/your/directory/Other
    - Moving file: example6.txt to /path/to/your/directory/Other
    File organization completed successfully.
    Summary:
    - 6 files processed.
    - 6 Files categorized into 5 directories.

## Troubleshooting

- **Path Validation**: Ensure you provide an absolute path to a valid directory.
- **File Permissions**: Make sure you have permission to read/write files in the specified directory.

## Contributing

Feel free to fork this repository, submit issues, or create pull requests for improvements.
