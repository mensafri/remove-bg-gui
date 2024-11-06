# Remove Background GUI Tool

A simple GUI tool for removing the background from images using Python. The application is built with Tkinter for the graphical interface and uses the `rembg` library to remove the background from images.

## Features
- Upload an image.
- Remove the background from the uploaded image.
- Save the resulting image with a transparent background.

## Requirements
- Python 3.8+

Install all required dependencies using:
```sh
pip install -r requirements.txt
```

## How to Run
To run the application, simply use the following command:
```sh
python main.py
```

## Usage
1. Launch the application using the command above.
2. Click on **Pilih Gambar** to select an image from your computer.
3. Click on **Hapus Latar Belakang** to remove the background of the image.
4. Click on **Simpan Hasil** to save the image without the background.

## Libraries Used
- **Tkinter**: For creating the graphical user interface.
- **Pillow**: For image manipulation and handling.
- **rembg**: To remove the background from images.

## Notes
- The tool only supports image files with the extension `.jpg`, `.jpeg`, and `.png`.
- Make sure to have an active internet connection, as `rembg` requires a pre-trained model which may need to be downloaded.