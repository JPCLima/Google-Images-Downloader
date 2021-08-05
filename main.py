import os
import requests
from bs4 import BeautifulSoup


google_img = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
user_agent = u_agnt = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

SAVE_FOLDER = 'img_downloaded'

# Size
# &tbs=isz:l
# &tbs=isz:m
# &tbs=isz:i


def get_img_links(data, num_images, size=None):

    # Search url of image
    search_url = google_img + 'q=' + data

    # Define the size of image
    if size == 'large':
        search_url += '&tbs=isz:l'
    elif size == 'medium':
        search_url += '&tbs=isz:m'
    elif size == 'icon':
        search_url += '&tbs=isz:i'

    # get all the HTML
    response = requests.get(search_url, headers=user_agent)
    html = response.text

    # Parse the HTML & get all the images with class 'rg_i Q4LuWd'
    b_soup = BeautifulSoup(html, 'html.parser')
    results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})

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
    for i, link in enumerate(img_links):
        response = requests.get(link)
        img_name = SAVE_FOLDER + '/' + data + '-' + str(i) + '.jpg'

        # Save the img
        with open(img_name, 'wb') as file:
            file.write(response.content)


def main():

    data = 'cola-can'
    num_images = 3

    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)

    link_list = get_img_links(data, num_images, 'large')
    download_imgs(data, link_list)


if __name__ == "__main__":
    main()
