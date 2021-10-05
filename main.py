from selenium import webdriver
import csv
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.614 Yowser/2.5 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}


def get_data_file(headers):
    """Get data from site"""
    start_time = time.time()

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(
        executable_path="chromedriver.exe",
        options=options
    )

    with open("maps_collection.csv", 'r') as fd:
        hotel_codes = csv.reader(fd)
        for hotel_code_row in hotel_codes:
            for_start_time = time.time()
            hotel_code = hotel_code_row[0]
            url = "https://ostrovok.ru/rooms/" + hotel_code
            driver.get(url=url)

            try:
                value = driver.find_element_by_class_name("zenroomspageperks-rating-info-total-value")
                result_text = hotel_code + "; " + value.text + "\n"
            except:
                result_text = hotel_code + "; " + "null\n"

            with open("code_with_rating.txt", "a", encoding='utf-8') as file:
                file.write(result_text)

            print(f"loading {hotel_code} got {(time.time() - for_start_time)} seconds")

    driver.close()
    print(f"loading {hotel_code} got {(time.time() - start_time)} seconds")


def main():
    get_data_file(headers=headers)


if __name__ == "__main__":
    main()
