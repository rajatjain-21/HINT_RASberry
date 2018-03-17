from bs4 import BeautifulSoup
import urllib.request
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
davaiyan = {}
cause = {}
complication = {}
symptom = {}
diagnose = {}
def disease_finder():
    opts = Options()
    opts.set_headless()
    assert opts.headless
    import time
    browser = Firefox(options=opts)
    browser.get('https://www.drugs.com/')
    medicine = []
    search_form = browser.find_element_by_id('livesearch-main')
    choice = input('Enter the disease')
    search_form.send_keys(choice)
    search_form.submit()
    time.sleep(5)
    medication_link = browser.find_element_by_css_selector('div.snippet:nth-child(2) > h3:nth-child(1) > a:nth-child(1)')
    medication_link.click()
    time.sleep(6)
    page = browser.page_source
    soup  = BeautifulSoup(page,'html.parser')
    dava = []
    for row in soup.findAll('table')[0].tbody.findAll('tr'):
        medicine = row.find_all('a',{'class':'condition-table__drug-name__link'})
        if len(medicine)>0:
            dava.append(medicine[0].text)

    davaiyan[choice]=dava
    # for k,v in davaiyan.items():
    #     for values in v:
    #         print(k,":",values)
    return davaiyan

site = "https://www.nhp.gov.in"
def symptoms():
    input_disease = input('Enter the name of the disease: ')
    page = urllib.request.urlopen(site+'/disease/'+input_disease)
    soup = BeautifulSoup(page,'html.parser')
    symptom[input_disease] = soup.find('div',{'id':'Symptoms'}).text.strip().replace('\n\n','\n')
    # for k,v in symptom.items():
    #     print(k,":",v)
    return symptoms

def causes():
    input_disease = input('Enter the name of the disease: ')
    page = urllib.request.urlopen(site + '/disease/' + input_disease)
    soup = BeautifulSoup(page, 'html.parser')
    cause[input_disease] = soup.find('div', {'id': 'Causes'}).text.strip().replace('\n\n', '\n')
    return causes

def diagnosis():
    input_disease = input('Enter the name of the disease: ')
    page = urllib.request.urlopen(site + '/disease/' + input_disease)
    soup = BeautifulSoup(page, 'html.parser')
    diagnose[input_disease] = soup.find('div', {'id': 'Diagnosis'}).text.strip().replace('\n\n', '\n')
    return diagnosis

def complications():
    input_disease = input('Enter the name of the disease: ')
    page = urllib.request.urlopen(site + '/disease/' + input_disease)
    soup = BeautifulSoup(page, 'html.parser')
    complication[input_disease] = soup.find('div', {'id': 'Complications'}).text.strip().replace('\n\n', '\n')
    return complications

def get_location():
    import requests
    import json
    send_url = 'http://api.zippopotam.us/IN/492001'
    r = requests.get(send_url)
    r = r.json();
    a = []
    for i in r:
        for j in r['places']:
            lat = j['latitude']
            lon = j['longitude']
            a.append(lat)
            a.append(lon)
            break
        break
    return a

def get_doctor():
    latlon = get_location()
    lat = latlon[0]
    lon = latlon[1]
    import requests
    send_url = 'https://api.betterdoctor.com/2016-03-01/doctors?location='+lat+'%2C'+lon+'%2C100&skip=0&limit=10&user_key=3e793332c913070b13242550b61af2c3'
    r = requests.get(send_url)
    r = r.json()
    for i in r['data']:
        for j in i['practices']:
            return j['name']

get_doctor()