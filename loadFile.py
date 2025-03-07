import os
import json

def load_json_file(json_file_path):
    global metadata
    with open(json_file_path, 'r', encoding='utf-8') as f:
        metadata = json.load(f)

def convert_playlist(convert_target_file_path, output_file):
    with open(convert_target_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        for line in lines:
            if "\n" in line:
                line = line[:-1]
            if line in metadata:
                f.write(line+"\n")
                if len(metadata[line]) > 1:
                    print(f"Multiple files found for {line}")
                    for i, file in enumerate(metadata[line]):
                        print(line)
                        print(file['filepath']+"\n")
                    print("Please select the file you want to add to the playlist")
                    selected_file = int(input())
                    f.write(metadata[line][selected_file]['filepath']+"\n")
                else:
                    f.write(metadata[line][0]['filepath']+"\n")

if __name__ == "__main__":
    json_file_path = "mp3_metadata.json"
    load_json_file(json_file_path)
    src_folder = "./src"
    cvt_folder = "./converted"
    for root,_,files in os.walk(src_folder):
        for file in files:
            if file.endswith(".m3u8"):
                output_file = os.path.join(cvt_folder, file)
                convert_playlist(os.path.join(root,file), output_file)
                print(f"Metadata saved to {output_file}")