def main():
    start_app()
    input_file = obtain_input_path()
    output_file = obtain_output_path()  
    process_files_with_ffmpeg(input_file, output_file)
    end_app()

def start_app():
    print("This application converts a mov file to a (smaller) mp4 file.")
    start_on_user_command()

def start_on_user_command(): 
    start_key = None
    while start_key != 'y' and start_key != 'n':
        start_key = input("Click \'y\' to start, or \'n\' to quit the application. ")
    if (start_key == 'n'):
        import sys
        print("Application terminated.")
        print("Exiting...")
        sys.exit()

def obtain_input_path():
    try: 
        import tkinter as tk
        from tkinter import filedialog
        tk.Tk().withdraw()
        input_file = filedialog.askopenfilename()
        if (input_file == ''):
            raise Exception("No file is selected for conversion.")
        if (input_file[-4:] != '.mov'):
            raise Exception("Selected file is not a mov file.")
        return input_file
    except Exception:
        raise

def obtain_output_path():
    try: 
        import os
        output_file = input("Enter a file name for output (without .mp4 prefix): ")
        if (output_file == ''):
            raise Exception('Output file path is not specified for conversion.')
        # TODO: Allow further customization of output file path
        home_path = os.path.expanduser('~')
        return os.path.join(home_path, 'Desktop', f'{output_file}.mp4')
    except Exception:
        raise

def process_files_with_ffmpeg(input_file, output_file):
    import ffmpeg
    stream = ffmpeg.input(input_file)
    stream = ffmpeg.output(stream, output_file, vcodec = "h264", acodec = "aac")
    ffmpeg.run(stream)

def end_app():
    print("Conversion completed.")
    print("Exiting...")

main()
