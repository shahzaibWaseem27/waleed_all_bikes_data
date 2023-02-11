def getAllData(bikeBrand, first_page_URL, second_page_URL=""):
    
    all_URLs = [first_page_URL, second_page_URL]

    from bs4 import BeautifulSoup
    import requests

    print("working on getting all data ...\n")

    allDataCategories = ['SKU', 'Season', 'Click & Collect', 'Frame', 'Frame Material', 'Fork', 'Fork Brand', 'Front Travel', 'Speeds', 'Front Gear', 'Groupset Brand', 'Groupset', 'Rear Gears', 'Crankset', 'Pedals', 'Chain', 'Brake Type', 'Brakes', 'Shifters', 'Brake Levers', 'Derailleur Front', 'Derailleur Rear', 'Cassette', 'Wheel Size', 'Tyres', 'Rims', 'Colour', 'Bottom Bracket', 'Handlebar', 'Headset', 'Grips', 'Stem', 'Hubs', 'Saddle', 'Seatpost', 'Spokes', 'Sizing SKUs', 'eBike Drive System', 'Motor Brand', 'Motor Model', 'Motor Torque (Nm)', 'Battery', 'Battery Brand', 'Battery Model', 'Assist Modes', 'Charge Time (Hours)', 'Front Gears', 'Display', 'Motor/Drive Unit', 'Weight', 'Battery Size (Watt-Hours)', 'Fork Material']

    
    all_txt_paths = []

    for category in allDataCategories:
        if("/" in category):
            category = category.replace("/", "")
        current_txt_path = "./" + bikeBrand + "/" + category + ".txt"
        all_txt_paths.append(current_txt_path)

    allFiles = []

    for txt_path in all_txt_paths:
        currentFile = open(txt_path, "a")
        allFiles.append(currentFile)
    
    file_descr = open("./" + bikeBrand + "/description.txt", "a")
    file_fullPrice = open("./" + bikeBrand + "/fullPrice.txt", "a")
    file_clubPrice = open("./" + bikeBrand + "/clubPrice.txt", "a")

    dataCategory_to_file = {}

    for i in range(len(allFiles) - 1):
        dataCategory_to_file[allDataCategories[i]] = allFiles[i]

    for url in all_URLs:
        mainPage_response = requests.get(url)
        mainPage_soup = BeautifulSoup(mainPage_response.content, "html.parser")

        allBikesLinks = mainPage_soup.find_all("a", class_="product-item-link")

        for link in allBikesLinks:
            eachBike_URL = link.get("href")
            eachBike_response = requests.get(eachBike_URL)
            eachBikeSoup = BeautifulSoup(eachBike_response.content, "html.parser")

            descr_soup = eachBikeSoup.find("span", class_="base")
            descr_text = descr_soup.text
            descr = str(descr_text) + "\n"
            file_descr.write(descr)

            full_price_soup = eachBikeSoup.find("span", class_="full-price")
            club_price_soup = eachBikeSoup.find("span", class_="special-price")
            full_price_text = full_price_soup.find("span", class_="price").text
            club_price_text = club_price_soup.find("span", class_="price").text
            full_price = str(full_price_text) + "\n"
            club_price = str(club_price_text) + "\n"
            file_fullPrice.write(full_price)
            file_clubPrice.write(club_price)

            table = eachBikeSoup.find("table", class_="data table additional-attributes")
            table_body = table.find("tbody")
            table_body_rows = table_body.find_all("tr")
            
            

            for i in range(len(allDataCategories) - 1):
                foundData = False
                for row in table_body_rows:
                    bikeDataTitle_soup = row.find("th")
                    bikeDataValue_soup = row.find("td")
                    bikeDataTitle = str(bikeDataTitle_soup.text)
                    if(bikeDataTitle == allDataCategories[i]):
                        foundData = True
                        bikeDataValue = str(bikeDataValue_soup.text) + "\n"
                        for char in bikeDataValue:
                            currentCharASCII = ord(char)
                            isValidChar = currentCharASCII >= 0 and currentCharASCII <= 127
                            if(not isValidChar):
                                bikeDataValue = bikeDataValue.replace(char, "")
                        allFiles[i].write(bikeDataValue)
                        break
                if(not foundData):
                    allFiles[i].write("not listed\n")

            
    for file in allFiles:
        file.close()
    
