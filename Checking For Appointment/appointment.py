import requests
from bs4 import BeautifulSoup
import smtplib
import getpass

website = # write here the website in that you want to get an appointment

response = requests.get(website)

smtp_object = smtplib.SMTP('smtp.gmail.com',587)

smtp_object.ehlo()

smtp_object.starttls()

# Write your own E-mail to send message and use here your App Password that you can get from your Gmail account.
email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
smtp_object.login(email,password)

from_address = email
to_address = email
subject = "New Appointment"
message = "Be fast and get your appointment in"
msg = "Subject : "+subject+'\n'+message+'\n'+website+"!"


if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Looking for a div element with a specific class
    specific_div = soup.find('div', class_='fix_ul')
    
    # Check if the div element was found
    if specific_div:
        # Find ul element with a specific class within the div
        ul_element = soup.find('ul',class_='list')

        # Check if the ul element was found
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
    
                # Print the extracted information
                print(f"Text: {anchor_text}")
                print(f"Additional Info: {additional_info_text}")
                print("------")

                # Check if there is an available appointment
                if additional_info_text == "Termin buchen":
                    # Send Email and inform to get that appointment
                    smtp_object.sendmail(from_address,to_address,msg)

    
        else:
            print('Ul element with class "list" not found.')

    else:
        print('Div element with class "your-class-name" not found.')
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
