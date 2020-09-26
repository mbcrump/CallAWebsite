## Day 5 - Make a call to an API or scrap web data

import requests
#from bs4 import BeautifulSoup as soup 
import bs4

def main():
    print_the_header()
    city = input("What is your city?\t")
    state = input("What state (use state code such as AL, WA, TX)\t")

    html = get_html(state, city)
    report = get_weather_from_html(html)
    

def print_the_header():
    print("--------------------------")
    print("Welcome to the Weather App")
    print("--------------------------")

## understand the format the url has been created in 

def get_html(state, city):
    url = "https://www.wunderground.com/weather/us/{}/{}".format(state.lower().strip(), city.lower().strip())
    response = requests.get(url)
    #print(response.status_code)
    #print(response.text)
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    #data = soup(html, "html.parser")
    ## 62
    ##test-true wu-unit wu-unit-temperature is-degree-visible ng-star-inserted
    #wu-value wu-value-to
    #temp = soup.find(class_='wu_unit_temperature').findall(class_='wu_value').get_text()
    temp = soup.find('span', {'class' : 'wu-value wu-value-to'}).get_text() # First degree only
    temp1 = soup.find('span', {'class' : 'wu-label'}).find('span', {'class' : 'ng-star-inserted'}).get_text() # perfect
    #temp1 = soup.find('span', {'class' : 'ng-star-inserted'}).get_text() # perfect
    message = soup.find('p', {'class' : 'weather-quickie'}).get_text()

    print(temp + temp1)
   
    print(message)
    # find_all('span', {'class' : 'wu-value wu-value-to'})






## call to the site and scrap data or api

## return to the console


main()