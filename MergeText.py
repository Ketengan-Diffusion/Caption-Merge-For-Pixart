import argparse
import os

# set up argument parser
parser = argparse.ArgumentParser(description='Merge .txt and .caption files into a single .txt file.')
parser.add_argument('-s', '--source', required=True, help='Source directory with .txt and .caption files to merge.')
parser.add_argument('-d', '--destination', required=True, help='Destination directory to save merged .txt files.')
args = parser.parse_args()

# function to merge files
def merge_files(txt_file, caption_file, output_file):
    with open(txt_file, 'r', encoding='utf-8') as f_txt, open(caption_file, 'r', encoding='utf-8') as f_caption:
        txt_content = f_txt.read().strip()
        caption_content = f_caption.read().strip()
    
    with open(output_file, 'w', encoding='utf-8') as f_output:
        f_output.write(txt_content + '\n' + caption_content + '\n')

# check if the source and destination directories exist
if not os.path.exists(args.source):
    raise Exception(f"Source directory '{args.source}' does not exist.")
if not os.path.exists(args.destination):
    os.makedirs(args.destination)

# iterate over files in the source directory
for file in os.listdir(args.source):
    if file.endswith('.txt'):
        base_name = os.path.splitext(file)[0]
        txt_file = os.path.join(args.source, file)
        caption_file = os.path.join(args.source, base_name + '.caption')
        output_file = os.path.join(args.destination, file)
        
        # check if the corresponding .caption file exists
        if not os.path.exists(caption_file):
            print(f"Warning: The corresponding caption file for '{txt_file}' is missing.")
        else:
            merge_files(txt_file, caption_file, output_file)
            print(f"Merged file {output_file} created successfully.")