import csv
import time
import requests   #USED FOR HTML PARSING
from selenium import webdriver  #USED FOR DYNAMIC JS PARSING


INPUTFILE = "Input.csv"
OUTPUTFILE = "Output.csv"


options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

#USED FOR CHECKING THE URLS
def urlValidity(link):
    response = requests.get(link)
    if response.status_code==200:      #USED FOR MEGA AND UPTOBOX 
        driver.get(link)
        time.sleep(8)
        pageSource = driver.page_source
        if "The file you are trying to download is no longer available" in pageSource:  #USED FOR MEGA UPLOADS
            print("Link is invalid")
            return False
        elif "404" in pageSource:                     #USED FOR GOOGLE DRIVE
            print("Link is invalid")
            return False
                
        print("Link is valid")
        return True
    
    else:
        print("Link is invalid")
        return False


#WRITING THE BROKEN LINKS IN OUTPUT FILE
def writeCSV(row):
    with open(OUTPUTFILE, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(row)
    file.close()


#READING THE INPUT FILE FOR ENTRIES
def readCSV():
    with open(INPUTFILE, newline="") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)   
        rows = []
        for row in reader:
            name = row[0]       
            links = row[1:] 
            print(f"Name : {name}")
            for link in links:
                print(f"Link : {link}")
                print("Checking for validity...")
                if (urlValidity(link)):
                    continue
                else:
                    writeCSV(row)
        


#USED TO CLEAR OUTPUT FILE ON NEW PROGRAM RUN
with open(OUTPUTFILE,"w") as opFile:
    pass
opFile.close()


readCSV()
