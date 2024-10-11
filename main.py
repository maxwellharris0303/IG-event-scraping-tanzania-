from selenium_driverless.sync import webdriver
from selenium_driverless.types.by import By
from time import sleep
from image_downloader import download_image
import openai_result
from event_date_comparison import comparison_event_date
import json
import quickstart
import google_maps_scrape
import add_event_bot

profile_directory = 'C:/Profile IG'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--user-data-dir={profile_directory}')

driver = webdriver.Chrome(max_ws_size=2**50, options=chrome_options)
# driver.maximize_window()

# USERNAME = "leveragestrategies.de"
# PASSWORD = "L$V$R@GE23"
USERNAME = "chiefdontrun56"
PASSWORD = "nakujawalete"

url = "https://instagram.com"
driver.get(url, wait_load=True)
sleep(5)

urls = []
with open('feeds.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    urls.append(line.strip())
print(urls)
urls = urls[:6]
for url in urls:

    driver.get(url, wait_load=True)
    sleep(5)


    event_parents = driver.find_elements(By.CSS_SELECTOR, "div[class=\"x1lliihq x1n2onr6 xh8yej3 x4gyw5p xfllauq xo2y696 x11i5rnm x2pgyrj\"]")
    print(len(event_parents))
    if len(event_parents) == 0:
        sleep(5)
        event_parents = driver.find_elements(By.CSS_SELECTOR, "div[class=\"x1lliihq x1n2onr6 xh8yej3 x4gyw5p xfllauq xo2y696 x11i5rnm x2pgyrj\"]")
        print(len(event_parents))
    event_parents = event_parents[:3]
    for event_parent in event_parents:
        try:
            img_url = event_parent.find_element(By.TAG_NAME, "img").get_attribute('src')
            print(img_url)
            post_url = event_parent.find_element(By.TAG_NAME, "a").get_attribute('href')
            print(post_url)
            caption = ""
            if "reel" not in post_url:
                #################### scrape cattion #######################
                event_parent.click()
                sleep(2)
                try:
                    caption = driver.find_element(By.CSS_SELECTOR, "h1[class=\"_ap3a _aaco _aacu _aacx _aad7 _aade\"]").text
                    print(caption)
                except:
                    pass
                close_button = driver.find_element(By.CSS_SELECTOR, "svg[aria-label=\"Close\"]")
                close_button.click()
                ###########################################################
                image_path = "image.jpg"
                download_image(img_url, image_path)
                result_1, result_2 = openai_result.transcribe_image(image_path, caption)
                json_result_1 = json.loads(result_1)
                json_result_2 = json.loads(result_2)
                print(json_result_1)
                print(json_result_2)
                # try:
                #     comparison_result = event_date_comparison_result = comparison_event_date(json_result_1['eventDate'], 2024, 8, 1)
                #     print(comparison_result)
                # except:
                #     pass
                # if comparison_result:
                if json_result_1['eventName'] != "" and json_result_1['eventDate'] != "":
                    location_url, accessibility, amenities, offers = google_maps_scrape.scrape_google_maps(json_result_1['eventLocation'])

                    data = []
                    data.append(json_result_1['eventName'])
                    data.append(img_url)
                    data.append(json_result_2['description'])
                    data.append(', '.join(amenities))
                    data.append(', '.join(offers))
                    data.append(json_result_2['musicPolicy'])
                    data.append(', '.join(accessibility))
                    data.append(json_result_1['eventDate'])
                    data.append(json_result_2['pricing'])
                    data.append(json_result_1['eventLocation'])
                    data.append(location_url)
                    data.append(json_result_1['websiteURL'])
                    data.append(json_result_1['phoneNumber'])
                    data.append(json_result_1['emailAddress'])
                    data.append(post_url)

                    quickstart.main()
                    index = quickstart.getColumnCount()
                    RANGE_DATA = f'Sheet1!A{index + 2}:O'
                    quickstart.insert_data(RANGE_DATA, data)

                    add_event_bot.main(json_result_1['eventName'], json_result_2['description'], amenities, offers, accessibility, json_result_2['musicPolicy'],
                                       json_result_2['pricing'], json_result_1['phoneNumber'], json_result_1['websiteURL'], json_result_1['emailAddress'], post_url)
        except:
            pass
            # else:
            #     break
