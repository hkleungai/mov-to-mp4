## A few words

Screen recording in MacOS is nice, 
but it also brings unnecessary huge mov files to the local file system.
This command line application aims to help
by having `ffmpeg` to convert any specfied `.mov` file to a smaller `.mp4` file 
while retaining most of the video quality.

## Installation

- Install Python3 and pip.
- Install `python-tk`.
    ```sh
    brew install python-tk
    ```
- Create a virtual environment if necessary.
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
- Install packages 
    ```sh
    pip install -r requirements.txt 
    ```

## Compilation

Run the main script with python.
```sh
python mov-to-mp4.py
```

## Remark
This is a quick dirty application done within hours, which leaves so many details (error handling, unit tests, customization, etc) worth for me to revisit later on.
