# import urllib
# import urllib.request
import requests
from bs4 import BeautifulSoup


def get_listing_data(listing_url):
    # Check if url is empty
    if not listing_url:
        raise Exception("Empty URL")
        print("Empty URL")

    # Creates dictionary for listing data
    listing_data = {
        "title": "",
        "type_o": "",
        "size": "",
        "size_l": "",
        "year": "",
        "short": "",
        "long": "",
        "images_array": []
    }

    # Reverse Proxy
    listing_url = listing_url.replace("https://www.nepremicnine.net", "https://nepremicnine.sajtr.ga")
    print(listing_url)
    # Creates new request with the given listing URL
    listing_page = requests.get(listing_url)
    print("got listing")
    soup = BeautifulSoup(listing_page.content, 'html.parser')
    print("made soup")

    # Gets listing's heading get basic  info
    listing_heading = ""
    try:
        listing_heading = soup.find("h1", {"class": "podrobnosti-naslov"}).text
    except:
        print("basic info")
        pass

    # Gets listing's title
    listing_title = ""
    try:
        listing_title = listing_heading.split(": ")[1]
        listing_title = listing_title.split(",")[0]
        listing_title = listing_title.title()
    except:
        print("listing title")
        pass

    # Gets listing's offer type
    listing_offer_type = ""
    try:
        listing_offer_type = listing_heading.split(", ")[1]
    except:
        print("offer type")
        pass

    # Gets listing's size
    listing_size = ""
    try:
        listing_size = listing_heading.split(", ")[-1]
    except:
        print("listing size")
        pass

    # Gets listing's short description text
    listing_short_description = ""
    try:
        listing_short_description = soup.find("div", {"class": "kratek"}).text
    except:
        print("listing short")
        pass

    # Gets listing's year of construction from short description
    listing_year = ""
    try:
        listing_year = listing_short_description.split(" l. ")[1]
        listing_year = listing_year.split(",")[0]
    except:
        print("listing short year")
        pass
    # listing_year = ""

    # Gets listing's land size
    listing_size_land = ""
    try:
        listing_size_land = ""
    except:
        print("listing land size")
        pass

    # Gets listing's price
    listing_price = ""
    try:
        listing_price = listing_short_description.split("Cena: ")[1]
    except:
        print("listing size")
        pass

    # Gets listing's long description

    # Gets all HTML tags in listing's long description
    listing_long_description_tags_list = ""
    try:
        listing_long_description_tags_list = soup.find("div", {"class": "web-opis"}).find("div", {
            "itemprop": "disambiguatingDescription"}).findAll("p")
    except:
        print("listing tags")
        pass
    listing_long_description = ""
    # Adds text from tags to listing's long description
    try:
        for p in listing_long_description_tags_list:
            listing_long_description += p.text
            listing_long_description += "\n"
    except:
        print("add tags")
        pass

    # Creates images array
    # Gets all HTML tags with images links
    listing_images_tags_list = soup.find("div", {"id": "galerija"}).findAll("a", {"class": "rsImg"})
    # Fills the list of listing's images and changes the famous "I" to "l"
    listing_images_links_list = []
    for tag in listing_images_tags_list:
        image_id = tag.get("data-rsbigimg").split("/")[-1]
        image_link = "https://picbase.turbosist.si/slonep_oglasi2/" + image_id
        listing_images_links_list.append(image_link)

    # Update the dictionary
    listing_data["title"] = listing_title
    listing_data["type_o"] = listing_offer_type
    listing_data["size"] = listing_size
    listing_data["size_l"] = listing_size_land
    listing_data["year"] = listing_year
    listing_data["price"] = listing_price
    listing_data["short"] = listing_short_description
    listing_data["long"] = listing_long_description
    listing_data["images_array"] = listing_images_links_list

    print(listing_data["title"])
    print(listing_data["type_o"])
    print(listing_data["size"])
    print(listing_data["size_l"])
    print(listing_data["year"])
    print(listing_data["price"])
    print(listing_data["short"])
    print(listing_data["long"])

    return listing_data
