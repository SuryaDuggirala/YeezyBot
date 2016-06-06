##Base URL is test 

##Bear in mind that this is not functional yet. Still needs to be finished. Just storing it on Github to 
###have a record of it outside my hardrive 

#Python Bot for buying Yeezys

#Requires Time Stamp 


#import selenium

##ADBLOCK extension to WebDriver Object
""""from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chop = webdriver.ChromeOptions()
chop.add_extension('Adblock-Plus_v1.4.1.crx')
driver = webdriver.Chrome(chrome_options = chop)""""


browser = Browser('chrome')
main_url = 'http://usonline.apc.fr/'

#Basic Information required in fields 

name_of_shoe = input('Type in name of shoe, the program will automatically place this in the search bar so be as precise as possible: ')
card_number = input('write your card number her: ')
first_name = input('First name (case sensitive): ')
last_name = input('Last Name (case sensitive): ')
street = input('Street Name (case sensitive): ')
apt_num = input('apartment number, suite, unit, etc... (optional): ')
zipcode = input('zip code: ')
phone_number = input('phone number: ')
email = input('email address: ')




    
    


class Bot():
    
    def __init__(self, name_of_shoe, card_num, first_name, last_name, street, apt_num=None, zipcode, phone_number, email):
        self.name_of_shoe = name_of_shoe
        self.car_num = card_num
        self.first_name = first_name
        self.last_name = last_name
        self.street = street
        self.apt_num = apt_num
        self.zipcode = zipcode
        self.phone_number = phone_number
        self.email = email 
        
        
    def main(self):
        
        browser = Browser('chrome')
        browser.visit(main_url)
        
        
    
    

            
            
            
            
        else:
            main(input('Website is faulty, please enter a new url in the format "https://www.xyz.com" : '))
            
        
        
x = Bot(name_of_shoe, card_number, first_name, last_name, street, apt_num, zipcode, phone_number, email, url) 

x.main(main_url)


    
    
        
    
            
            
         
  







    
