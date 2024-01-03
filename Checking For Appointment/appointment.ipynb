{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fad625a6-3e78-46cf-8f71-24f2f68fc9e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import smtplib\n",
    "import getpass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5dc761c3-582d-4443-843f-f57a662490d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "website = # write here the website in that you want to get an appointment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3b7922b-a296-4293-9c6d-775511938019",
   "metadata": {},
   "outputs": [],
   "source": [
    "response = requests.get(website)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3257b591-60de-485c-afa1-0eec4f49fe2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "type(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a60636ab-c835-4a18-8f2d-6c587983bda2",
   "metadata": {},
   "outputs": [],
   "source": [
    "smtp_object = smtplib.SMTP('smtp.gmail.com',587)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a2a7cd7-d7b4-46a7-826b-dae2023470e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "smtp_object.ehlo()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f049daca-a88e-4f98-9177-d90c1a7067ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "smtp_object.starttls()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "91158ef0-add0-4af0-91ab-6bf79ffe8e81",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'getpass' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[1], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m email \u001b[38;5;241m=\u001b[39m getpass\u001b[38;5;241m.\u001b[39mgetpass(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEmail: \u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m      2\u001b[0m password \u001b[38;5;241m=\u001b[39m getpass\u001b[38;5;241m.\u001b[39mgetpass(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPassword: \u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m      3\u001b[0m smtp_object\u001b[38;5;241m.\u001b[39mlogin(email,password)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'getpass' is not defined"
     ]
    }
   ],
   "source": [
    "email = getpass.getpass(\"Email: \")\n",
    "password = getpass.getpass(\"Password: \")\n",
    "smtp_object.login(email,password)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0bc7d264-9914-4558-a547-f2de8ae9fce2",
   "metadata": {},
   "outputs": [],
   "source": [
    "from_address = email\n",
    "to_address = email\n",
    "subject = \"New Appointment\"\n",
    "message = \"Be fast and get your appointment in\"\n",
    "msg = \"Subject : \"+subject+'\\n'+message+'\\n'+website+\"!\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "207c21b5-e4a0-43a8-8818-c622ab5f7dbd",
   "metadata": {},
   "outputs": [],
   "source": [
    "if response.status_code == 200:\n",
    "    # Parse the HTML content of the page\n",
    "    soup = BeautifulSoup(response.text, 'html.parser')\n",
    "\n",
    "    specific_div = soup.find('div', class_='fix_ul')\n",
    "    i = 0\n",
    "    # Check if the div element was found\n",
    "    if specific_div:\n",
    "        # Find all li elements within the ul\n",
    "        ul_element = soup.find('ul',class_='list')\n",
    "\n",
    "        if ul_element:\n",
    "            # Find all li elements within the ul\n",
    "            li_elements = ul_element.find_all('li')\n",
    "\n",
    "            # Loop through the li elements and extract information\n",
    "            for li in li_elements:\n",
    "                # Extract the text content of the anchor tag within the li\n",
    "                anchor_text = li.find('a', class_='more').text\n",
    "    \n",
    "                # Extract additional information (if present)\n",
    "                additional_info = li.find('a', class_='direct')\n",
    "                if additional_info:\n",
    "                    additional_info_text = additional_info.text\n",
    "                else:\n",
    "                    additional_info_text = None\n",
    "    \n",
    "                # Print the extracted information\n",
    "                print(f\"Text: {anchor_text}\")\n",
    "                print(f\"Additional Info: {additional_info_text}\")\n",
    "                print(\"------\")\n",
    "                \n",
    "                if additional_info_text == \"Termin buchen\":\n",
    "                    smtp_object.sendmail(from_address,to_address,msg)\n",
    "\n",
    "    \n",
    "        else:\n",
    "            print('Ul element with class \"list\" not found.')\n",
    "\n",
    "    else:\n",
    "        print('Div element with class \"your-class-name\" not found.')\n",
    "else:\n",
    "    print('Failed to retrieve the webpage. Status code:', response.status_code)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
