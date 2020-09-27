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

    print("Your weather forecast is : " + report)
    

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

    ##test-true wu-unit wu-unit-temperature is-degree-visible ng-star-inserted
    #wu-value wu-value-to

    degrees = soup.find('span', {'class' : 'wu-value wu-value-to'}).get_text() # First degree only
    scale = soup.find('span', {'class' : 'wu-label'}).find('span', {'class' : 'ng-star-inserted'}).get_text() # F or C
    quick_weather_info = soup.find('p', {'class' : 'weather-quickie'}).get_text()

    return degrees + "°" + scale


main()