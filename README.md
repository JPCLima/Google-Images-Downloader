# Google-Images-Downloader

Google Images Downloader is a Python program that allows you to easily download images from Google for various purposes. It leverages the power of Python along with libraries such as `argparse`, `os`, `requests`, and `BeautifulSoup` to provide a versatile and user-friendly image-downloading solution.

## Features

The Google Images Downloader offers the following features:

- **Define a number of pictures**: With a simple command, you can download a specified number of cat images from Google. For example:
  ```bash
  python gi_downloader.py -k cats -n 5
  ```

- **Define the path to save images**: You have the flexibility to specify the destination folder where the downloaded images will be saved. By providing the path, you can organize your downloaded images easily. For example:
  ```bash
  python gi_downloader.py -f folder_to_save -k cats -n 5
  ```
  You can even specify an absolute path like this:
  ```bash
  python gi_downloader.py -f C:\Users\User1\Desktop\Downloads -k cats -n 5
  ```

- **Define the size of the images**: You can filter the downloaded images based on their size. For example, if you want large images, you can specify the size option:
  ```bash
  python gi_downloader.py -f folder_to_save -k cats -n 5 -s large
  ```

## Getting Started

To get started with the Google Images Downloader project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/JPCLima/Google-Images-Downloader.git
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   ```

3. Activate the virtual environment:
   - For Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the program:
   ```bash
   python gi_downloader.py
   ```

The Google Images Downloader project provides a convenient and efficient way to download images from Google, offering customization options for both the quantity and size of the images. It serves as a valuable tool for various applications such as data collection, machine learning, content creation, and more.
