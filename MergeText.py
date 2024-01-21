import argparse
import os

def read_file(file_path):
    try:
        # First attempt to read with utf-8
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except UnicodeDecodeError:
        # If utf-8 fails, attempt to read with 'windows-1252' encoding which covers ANSI
        with open(file_path, 'r', encoding='windows-1252') as f:
            return f.read().strip()

def merge_files(txt_file, caption_file, output_file):
    txt_content = read_file(txt_file)
    caption_content = read_file(caption_file)
    
    if txt_content is not None and caption_content is not None:
        with open(output_file, 'w', encoding='utf-8') as f_output:
            f_output.write(txt_content + '\n' + caption_content + '\n')
            print(f"Merged file {output_file} created successfully.")
    else:
        print("Failed to merge files due to an encoding error.")

# Parse command line arguments
parser = argparse.ArgumentParser(description='Merge .txt and .caption files into a single .txt file.')
parser.add_argument('-s', '--source', required=True, help='Source directory with .txt and .caption files to merge.')
parser.add_argument('-d', '--destination', required=True, help='Destination directory to save merged .txt files.')
args = parser.parse_args()

if not os.path.exists(args.source):
    raise Exception(f"Source directory '{args.source}' does not exist.")
if not os.path.exists(args.destination):
    os.makedirs(args.destination)

for file in os.listdir(args.source):
    if file.endswith('.txt'):
        base_name = os.path.splitext(file)[0]
        txt_file = os.path.join(args.source, file)
        caption_file = os.path.join(args.source, base_name + '.caption')
        output_file = os.path.join(args.destination, file)
        
        if not os.path.exists(caption_file):
            print(f"Warning: The corresponding caption file for '{txt_file}' is missing.")
        else:
            merge_files(txt_file, caption_file, output_file)
