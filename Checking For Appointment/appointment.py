import requests
from bs4 import BeautifulSoup
import smtplib
import getpass

# write here the website in that you want to get an appointment
website = "https://www.service.bremen.de/dienstleistungen/personalausweis-beantragen-8363"

response = requests.get(website)

smtp_object = smtplib.SMTP('smtp.gmail.com',587)

smtp_object.ehlo()

smtp_object.starttls()

# Write your own E-mail address to send message and use here your App Password that you can get from your Gmail account.
email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
smtp_object.login(email,password)

from_address = email
to_address = email
subject = "New Appointment"
message = "Be fast and get your appointment in"
msg = "Subject : "+subject+'\n'+message+'\n'+website+"!"

# Schedule the task to run every 5 minutes
schedule.every(5).minutes.do(sendMail)

while True:
    schedule.run_pending()
    time.sleep(1)

def sendMail():
    
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
    
        specific_div = soup.find('div', class_='fix_ul')
        
        isAppointment = 0
        
        # Check if the div element was found
        if specific_div:
            # Find all li elements within the ul
            ul_element = soup.find('ul',class_='list')
    
            if ul_element:
                # Find all li elements within the ul
                li_elements = ul_element.find_all('li')
    
                # Loop through the li elements and extract information
                for li in li_elements:
                    # Extract the text content of the anchor tag within the li
                    anchor_text = li.find('a', class_='more').text
        
                    # Extract additional information (if present)
                    additional_info = li.find('a', class_='direct')
                    if additional_info:
                        additional_info_text = additional_info.text
                    else:
                        additional_info_text = None
                    
                    if additional_info_text == "Termin buchen":
                        isAppointment += 1 

                if isAppointment > 0:
                    smtp_object.sendmail(from_address,to_address,msg)
                else:
                    print("There is no available appointment :(")
            else:
                print('Ul element with class "list" not found.')
    
        else:
            print('Div element with class "your-class-name" not found.')
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)
