from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import requests

# Use MongoDB with Flask templating to create a new HTML page that displays all
# of the information that was scraped from the URLs above.

# Start by converting your Jupyter notebook into a Python script called
# scrape_mars.py with a function called scrape that will execute all of your
# scraping code from above and return one Python dictionary containing all of
# the scraped data.

def scrape():
    # NASA Mars News
    url = "https://mars.nasa.gov/news/"
    parser = bs(requests.get(url).text)
    news_title = parser.find_all("div", class_="content_title")[0].text.strip()
    news_p = parser.find_all("div", class_="rollover_description")[0].text.strip()
    
    # JPL Mars Space Images - Featured Image
    browser = Browser('chrome', headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    featured_image_url = "https://" + browser.url.split("/")[2] + soup.article.attrs["style"].split("'")[1]

    # Mars Weather
    url = "https://mobile.twitter.com/marswxreport?lang=en"
    parser = bs(requests.get(url).text)
    mars_weather = parser.find_all("div", class_="tweet-text")[0].text.strip()

    # Mars Facts
    url = "https://space-facts.com/mars/"
    parser = bs(requests.get(url).text)
    html_table = str(parser.table)
    mars_facts_df = pd.DataFrame(pd.read_html(html_table, flavor="html5lib")[0])
    mars_facts_html = mars_facts_df.to_html(index=False, header=False)
    
    # Mars Hemispheres
    hemisphere_image_urls = []
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    links = ["https://" + browser.url.split("/")[2] + tag.parent.attrs["href"] for tag in soup.find_all("h3")]
    for link in links:
        image = {}
        browser.visit(link)
        soup = bs(browser.html, 'html.parser')
        image["Title"] = str(soup.h2.text.rsplit(' ', 1)[0])
        # text changed from original (.tif) to sample (.jpg) 
        image["Link"] = str(soup.find_all("a", text="Sample")[0].attrs["href"])
        hemisphere_image_urls.append(image)
    browser.quit()

    data = {"news_title": news_title,
            "news_p": news_p,
            "featured_image_url": featured_image_url,
            "mars_weather": mars_weather,
            "mars_facts_html": mars_facts_html,
            "hemisphere_image_urls": hemisphere_image_urls}
    
    return data