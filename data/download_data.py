import gdown
import requests
from bs4 import BeautifulSoup
import os
import zipfile

# List of Google Drive shareable links
google_drive_links = [
    "https://drive.google.com/file/d/1tElBfaidS3Ufe548SE6I1604rtOtu9zm/view?usp=drive_link" # "hogskoleprovet_questions.zip
]

def get_file_name_from_google_drive(share_link):
    # Send a request to the Google Drive shareable link
    response = requests.get(share_link)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the file name from the <title> tag or <meta> tags
    file_name = soup.title.text.strip() if soup.title else "downloaded_file.zip"
    
    # Sometimes the title might include "Google Drive", we can refine further
    if "Google Drive" in file_name:
        meta_tag = soup.find("meta", {"property": "og:title"})
        if meta_tag:
            file_name = meta_tag["content"].strip()
    
    return file_name

def download_file_from_google_drive(share_link):
    # Get the file name by parsing the HTML
    output_file_name = get_file_name_from_google_drive(share_link)
    
    # Extract the file ID from the shareable link
    file_id = share_link.split('/')[-2]
    
    # Construct the download URL
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

    current_directory: str = str(os.path.dirname(os.path.realpath(__file__)))
    output_file_name: str = current_directory + "/" + output_file_name

    print (f"Downloading {output_file_name} from {download_url}")

    # Verify if the file already exists
    if os.path.exists(output_file_name):
        print(f"File {output_file_name} already exists")
        return

    # Download the file using gdown
    gdown.download(download_url, output_file_name, quiet=False)

# unzip all files in the current directory
def unzip_files_in_current_directory():
    # Get the absolute path of the current script directory
    current_directory = os.path.abspath(os.path.dirname(__file__))

    # List all files in the current directory
    files_in_directory = os.listdir(current_directory)

    # Iterate over the files
    for file_name in files_in_directory:
        if file_name.endswith(".zip"):
            # Construct the full path to the file
            file_path = os.path.join(current_directory, file_name)

            # Check if the directory already exists
            directory_name = file_name.replace(".zip", "")
            directory_path = os.path.join(current_directory, directory_name)
            if os.path.exists(directory_path):
                print(f"Directory {directory_name} already exists")
                continue
            
            # Extract the zip file
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                # Extract all the contents into the current directory
                zip_ref.extractall(current_directory)
                print(f'Extracted: {file_name}')


if __name__ == "__main__":
    # Iterate over all the Google Drive links and download the files
    for share_link in google_drive_links:
        download_file_from_google_drive(share_link)

    # Unzip all the files in the current directory
    unzip_files_in_current_directory()