#https://www.instagram.com/share/BBMP8sejMw
#https://www.instagram.com/share/_yz61lrSL

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_original_instagram_link(share_link):
    # Chrome WebDriver için seçenekler
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Tarayıcıyı arka planda çalıştırır
    options.add_argument('--disable-gpu')
    
    # WebDriver başlat
    driver = webdriver.Chrome(options=options)
    driver.get(share_link)
    
    time.sleep(5)  # Dinamik yüklemeler için bekleme süresi
    
    # Orijinal URL'yi çek
    original_url = driver.current_url
    print("Orijinal Link:", original_url)
    
    driver.quit()
    return original_url

# Share linki buraya yapıştır
share_link = "https://www.instagram.com/share/_yz61lrSL"
get_original_instagram_link(share_link)
