import requests
from bs4 import BeautifulSoup

def extract_links(url):
  try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    for index, link in enumerate(links, start=1):
      print(f"{index}. {link.get('href')}")
  except Exception as e:
    print(f"An error occurred : {e}")
    
if __name__ == "__main__":
  url = "yourlinkto_enum"
  extract_links(url)