import requests
from urllib3.exceptions import InsecureRequestWarning
import os
# Function to delete a PDF file
def delete_pdf_file(file_url):
    try:
        # Ensure the file URL points to a valid PDF file
        if file_url.lower().endswith('.pdf'):
            requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
            response = requests.delete(file_url, verify=False)
            
            if response.status_code == 200:
                print(f"File at '{file_url}' has been deleted.")
            else:
                print(f"Failed to delete file at '{file_url}'. Status code: {response.status_code}")
        else:
            print(f"File URL '{file_url}' does not point to a PDF file.")
    except Exception as e:
        print(f"An error occurred while attempting to delete the file: {str(e)}")

# Connect to PostgreSQL database
