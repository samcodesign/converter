import os
from pydub import AudioSegment
import string


def sanitize_filename(filename):
    # Replace special characters with underscores or remove them
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    sanitized_name = ''.join(c if c in valid_chars else '_' for c in filename)
    return sanitized_name

# Specify the source and target directories
source_directory = r'C:\Users\samyb\Desktop\Audio'
target_directory = r'C:\Users\samyb\Desktop\Final'

# Ensure the target directory exists
os.makedirs(target_directory, exist_ok=True)

# Convert all .opus files to .mp3
for filename in os.listdir(source_directory):
    if filename.endswith('.opus'):
        # Sanitize the file name
        safe_filename = sanitize_filename(filename)

        # Define full file paths
        opus_file_path = os.path.join(source_directory, filename)
        mp3_file_path = os.path.join(target_directory, safe_filename.replace('.opus', '.mp3'))

        # Load the opus file and export it as mp3
        try:
            audio = AudioSegment.from_file(opus_file_path, format='ogg')
            audio.export(mp3_file_path, format='mp3')
            print(f"Converted {filename} to mp3 and saved to {target_directory}")
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

print("Conversion complete.")