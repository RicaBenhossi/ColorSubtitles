# Color Subtitles

This project processes `.srt` subtitle files and adds a specified color to the subtitle text. The processed subtitle
files are saved in the `output` directory.

## Features

- Reads subtitle files from the `resources` directory.
- Supports UTF-8 and Windows-1252 encodings.
- Adds a specified color to the subtitle text.
- Saves the processed subtitle files in the `output` directory.
- Handles errors for files that cannot be opened with the specified encodings.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/RicaBenhossi/color_subtitles.git
    cd color_subtitles
    ```

2. Ensure you have Python 3.x installed on your system.

## Usage

1. Place your `.srt` subtitle files in the `resources` directory.

2. Run the script:
    ```sh
    python3 color_subtitles.py
    ```

3. The processed subtitle files will be saved in the `output` directory.

## Configuration

- You can change the subtitle color by modifying the `SUBTITLE_COLOR_YELLOW` variable in the `color_subtitles.py` file.

## Error Handling

- If the script encounters files that cannot be opened with UTF-8 or Windows-1252 encodings, it will list these files
  and display an error message.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
