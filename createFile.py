import os
import json
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB

def get_mp3_metadata(file_path):
    audio = MP3(file_path, ID3=ID3)
    title = "#EXTINF:"+str(int(audio.info.length))+","+str(audio.get("TPE1", "Unknown Artist"))+" - "+ str(audio.get("TIT2", "Unknown Title"))
    metadata = {
        "filepath": file_path,
        "length": int(audio.info.length)
    }
    return title, metadata

def walk_through_folder(folder_path):
    mp3_files_metadata = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".mp3"):
                file_path = os.path.join(root, file)
                title, metadata = get_mp3_metadata(file_path)
                if title not in mp3_files_metadata:
                    mp3_files_metadata[title]=[]
                mp3_files_metadata[title].append(metadata)
    return mp3_files_metadata

def save_metadata_to_file(metadata, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    folder_path = "/Users/!Username!/Music/Music/Media.localized/Music"
    output_file = "mp3_metadata.json"
    metadata = walk_through_folder(folder_path)
    save_metadata_to_file(metadata, output_file)
    print(f"Metadata saved to {output_file}")