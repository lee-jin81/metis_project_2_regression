import requests, bs4
from bs4 import BeautifulSoup as bs
import time
import random
import pickle
import pandas as pd

# get url for each page
def create_page_url(base_url):
    val = 0
    page_num_start = 15
    page_num = page_num_start
    page_url_list =[]

    while page_num > 0:
        if val == 0:
            page_url = base_url
            page_url_list.append(page_url)
            val += 96
            page_num -=1

        else:
            page_url = base_url + '&No=' + str(val) + '&Nrpp=96'
            page_url_list.append(page_url)
            val += 96
            page_num -=1
    
    # test that all pages url were extracted
    if page_num_start != len(page_url_list):
        print('not all url extracted')
        
    return page_url_list


# create soup for each page
# add pause
def get_page_soup(page_url_list):
    page_soup = []
    
    for page_num in page_url_list:
        response = requests.get(page_num)
        status = response.status_code
        if status == 200:
            page = response.text
            soup = bs(page, 'lxml')
            page_soup.append(soup)
            time.sleep(.5+2*random.random())
        else:
            print(f"Oops! Received status code {page, status}")
            return None        

    return page_soup

# get url of each product on a page
def create_product_url_list(pages_soup_list):
    products_url = []
    product_url_base = 'https://www.ulta.com'
    
    for page_soup in pages_soup_list:
        page_tag = page_soup.find_all('div', class_="quick-view-prod")

        for tags in page_tag:
            a_tag = tags.find('a')
            product_url_str = a_tag['href']
            product_url =  product_url_base + product_url_str
            products_url.append(product_url)
        
    return products_url

# get page for each product url, save output as pickle file
# parse later since it is easier to save a page than soup
def get_products_page(page_url_list, file_name):

    count_failed = 0 
    count_success = 0
    all_pages = []

    for i, url in enumerate(page_url_list):
        response = requests.get(url)
        status = response.status_code
        
        if status == 200:
            #page = response.text # do I need this text line?
            page = response
            all_pages.append(page)
            print("Progress " + str(count_success))
            count_success += 1
   
            # time.sleep(1+2*random.random())
            
            time.sleep(random.randint(2, 8) * random.random())
            
        else:
            count_failed += 1
            print(f"Oops! Received status code {product_url, status}")
            return None   
        
        # pause every 190 requests
        if (i+1) % 190 == 0:
            print('sleep')
            time.sleep(330) ## 5.5 min pause
            
    
    # save page in a pickle
    with open(file_name + ".pickle", "wb") as f:
        pickle.dump(all_pages, f)
    
    statement = "{} files success, {} failed".format(str(count_success), str(count_failed))
    return statement