# Google-Images-Downloader
Google Images Downloader is a program to dowload images from google.

## How to install?
1. Clone the repo
```bash
git clone https://github.com/JPCLima/Google-Images-Downloader.git
```
2. Create a virtual env
```bash
python -m venv env
```
3. Activate the virtual env
```bash
.\env\Scripts\activate
```
4. Run the program
```bash
python gi_downloader.py
```

## Usage
Download 5 pictures of cats 
```bash
python gi_downloader.py -k cats -n 5
```
Define the path
```bash
python gi_downloader.py -f folder_to_save -k cats -n 5
```
```bash
python gi_downloader.py -f C:\Users\User1\Desktop\Dowloads -k cats -n 5
```
Define the size
```bash
python gi_downloader.py -f folder_to_save -k cats -n 5 -s large
