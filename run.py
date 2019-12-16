from scrape_data.scrape_data import scrapped_data
from analysis.analysis import analysis_products

if __name__ == "__main__":
    # choice = int(input("\nPress 1 to scrap data from website\nPress 2 to do analysis on scrapped data \n"))

    # assign option 1 to choice to scrap data or assign 2 for analysis of data
    choice = 2

    if choice == 1:
        scrapped_data()

    elif choice == 2:
        analysis_products()

    else:
        print("\nYou selected the wrong option ")
