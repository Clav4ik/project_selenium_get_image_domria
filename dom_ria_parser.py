
import time
import urllib.request
import pathlib
from selenium import webdriver
import requests



def get_foto():
    url = input(
        "Ссылку сверху такого типа скопировать=https://dom.ria.com/uk/realty-prodaja-kvartira-odessa-kievskiy-iekokaya-lia-22333623.html\n")

    options = webdriver.ChromeOptions()

    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36" )
    way = pathlib.Path(__file__).parent.resolve()
    w = str(way) + '\\hromebrouser\\chromedriver.exe'

    driver = webdriver.Chrome(
        executable_path=w,
        options=options
    )

    post_url = 'https://e.clarity.ms/collect'

    try:
        headers = {'cookie': "MUID=315CC60519096D26103ECBF31D096EBC",
                   'referer': url}
        driver.get(url)
        time.sleep(2)
        response = requests.post(post_url  , data=headers)
        print(response.text)
        time.sleep(2)

        driver.refresh()
        time.sleep(5)
        driver.refresh()
        time.sleep(2)
        try:
            page = driver.find_element_by_css_selector('div.gallery-tabs').find_elements_by_tag_name('label')
            page[1].click()
        except Exception as ex:
            print(ex)
        num_page = driver.find_element_by_css_selector('div.count-photo.flex.f-center.label-item').text
        list_page = num_page.split(' ')
        max_page = int(list_page[-1])
        min_page = int(list_page[-3])
        image = driver.find_element_by_css_selector('div.photo-.bg_white').find_elements_by_css_selector(
            'img')
        for i in range(1, max_page-min_page+2):


            urllib.request.urlretrieve(image[i-1].get_attribute("src"), f"foto number {i}.jpg")



    except Exception as ex:
        print(ex)

    finally:
        time.sleep(2)
        driver.close()
        driver.quit()


if __name__ == "__main__":
    get_foto()