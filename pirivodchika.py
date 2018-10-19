from bs4 import BeautifulSoup
import requests
import webbrowser

def openff():
    # This def open firefox browser.
    Jpsen = input("ロシア語にしたい日本語を入力してください: ")
    url = "https://script.google.com/macros/s/AKfycbyIDKv7Mx1Ga_myI4hzuCDA-gTvLurfPgWlK39isQQyWUelhcEw/exec?text=" + Jpsen + "&source=ja&target=ru"
    browser = webbrowser.get('"/usr/bin/firefox" %s')
    browser.open(url)

openff()