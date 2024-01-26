import os
import requests
from PIL import Image
from io import BytesIO

def download_and_upload_images(input_folder, output_folder, max_images):
    text_files = [file for file in os.listdir(input_folder) if file.endswith('.txt')]

    for file_name in text_files:
        input_file_path = os.path.join(input_folder, file_name)
        output_folder_path = os.path.join(output_folder, file_name.replace('.txt', '').replace('urls_', ''))
        os.makedirs(output_folder_path, exist_ok=True)  # Create output folder for each text file

        with open(input_file_path, 'r') as input_file:
            lines = input_file.readlines()

        valid_image_count = 0  # Counter for valid images

        for image_index, url in enumerate(lines, start=1):
            if valid_image_count >= max_images:
                break  # Break the loop after reaching the desired number of valid images

            url = url.strip()

            try:
                response = requests.get(url)
                response.raise_for_status()

                image_data = BytesIO(response.content)
                image = Image.open(image_data)

                # Save the image to the output folder with a unique name
                image_filename = f"image_{valid_image_count + 1}.png"
                image_path = os.path.join(output_folder_path, image_filename)
                image.save(image_path, 'PNG', icc_profile='')

                print(f"Image from URL in {file_name}, line {image_index} downloaded and saved: {image_path}")

                valid_image_count += 1  # Increment the valid image counter

            except requests.exceptions.RequestException as e:
                print(f"URL in {file_name}, line {image_index} is not working and will be skipped: {url}")
                print(f"Error: {e}")

if __name__ == "__main__":
    input_folder = "/Users/rohitjadhav/Desktop/Personal/nsfw-image-detection/raw_data"
    output_folder = "/Users/rohitjadhav/Desktop/Personal/nsfw-image-detection/clean_data"

    download_and_upload_images(input_folder, output_folder, max_images=200)
