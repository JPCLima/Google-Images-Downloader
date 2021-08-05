import argparse
import os
import requests
from bs4 import BeautifulSoup

# Initiate argument parser
parser = argparse.ArgumentParser(
    description="Download Images from Google")

parser.add_argument("-f",
                    "--save_folder",
                    default='downloads',
                    help="path where images will be saved")

parser.add_argument("-k",
                    "--keyword",
                    type=str,
                    help="keyword to search")

parser.add_argument("-n",
                    "--num_images",
                    default=10,
                    type=int,
                    help="number of images to download")

parser.add_argument("-s",
                    "--size",
                    default=None,
                    type=str,
                    help="Size of the images to save")

args = parser.parse_args()

# Define the root url & user agent
GOOGLE_IMG = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
USER_AGENT = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}


def get_img_links(data, num_images, size=None):
    """
        This function is taking as parameter the keyword to be searched, the number of images to get the url
        and the size of the image. 
        The options of image size is: large, medium, icon or as default None
    """

    # Search url of image
    search_url = GOOGLE_IMG + 'q=' + data

    # Define the size of image
    if size == 'large':
        search_url += '&tbs=isz:l'
    elif size == 'medium':
        search_url += '&tbs=isz:m'
    elif size == 'icon':
        search_url += '&tbs=isz:i'

    # get all the HTML
    resp = requests.get(search_url, headers=USER_AGENT)
    html = resp.text

    # Parse the HTML & get all the images with class 'rg_i Q4LuWd'
    b_soup = BeautifulSoup(html, 'html.parser')
    results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})

    # Search the url of images and store in the img_links list
    count = 0
    img_links = []
    for res in results:
        try:
            if (count < int(num_images)):
                link = res['data-src']
                img_links.append(link)
                count = count + 1
        except KeyError:
            continue

    return img_links


def download_imgs(data, img_links):
    """
        This function as input is taking the keyword to rename the images files and the list of images
        to download.
    """
    for i, link in enumerate(img_links):
        resp = requests.get(link)
        img_name = args.save_folder + '/' + data + '-' + str(i+1) + '.jpg'

        # Save the img
        with open(img_name, 'wb') as file:
            file.write(resp.content)


def main():

    # Create a folder if doesnt exist
    if not os.path.exists(args.save_folder):
        os.mkdir(args.save_folder)

    # Get the list of links to download
    link_list = get_img_links(args.keyword, args.num_images, args.size)

    # Downlaod images
    download_imgs(args.keyword, link_list)


if __name__ == "__main__":
    try:
        main()
        print('Successfully downloaded!!!')
    except Exception as e:
        print(e)
