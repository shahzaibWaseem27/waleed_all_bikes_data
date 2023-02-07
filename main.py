from allData import getAllData

bikeCategory = input("enter merida or norco\n")
first_page_URL = input("please enter the first page url of the bike category, showing 108 items per page\n")
second_page_URL = input("please enter the second page url of the bike category, showing 108 items per page\n")

is_bikeCategory_Valid = bikeCategory == "merida" or bikeCategory == "norco"

while True:
    if(is_bikeCategory_Valid):
        getAllData(bikeCategory, first_page_URL, second_page_URL)
        print("got all data\n")
        break
    else:
        print("invalid input, try again\n")
        bikeCategory = input("enter merida or norco\n")
        first_page_URL = input("please enter the first page url of the bike category, showing 108 items per page\n")
        second_page_URL = input("please enter the second page url of the bike category, showing 108 items per page\n")
        is_bikeCategory_Valid = bikeCategory == "merida" or bikeCategory == "norco"
