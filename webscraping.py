from bs4 import BeautifulSoup
import requests
import time
import xlsxwriter
import os
import smtplib
from email.message import EmailMessage
from typing import Optional
from xlsxwriter.worksheet import (
    Worksheet, cell_number_tuple, cell_string_tuple)

def get_column_width(worksheet: Worksheet, column: int) -> Optional[int]:
    #Get the max column width in a `Worksheet` column.
    strings = getattr(worksheet, '_ts_all_strings', None)
    if strings is None:
        strings = worksheet._ts_all_strings = sorted(
            worksheet.str_table.string_table,
            key=worksheet.str_table.string_table.__getitem__)
    lengths = set()
    for row_id, colums_dict in worksheet.table.items():  # type: int, dict
        data = colums_dict.get(column)
        if not data:
            continue
        if type(data) is cell_string_tuple:
            iter_length = len(strings[data.string])
            if not iter_length:
                continue
            lengths.add(iter_length)
            continue
        if type(data) is cell_number_tuple:
            iter_length = len(str(data.number))
            if not iter_length:
                continue
            lengths.add(iter_length)
    if not lengths:
        return None
    return max(lengths)


def set_column_autowidth(worksheet: Worksheet, column: int, max_length):
    aasheet.set_column(column,column,max_length)


aa=xlsxwriter.Workbook("aa.xlsx")
aasheet=aa.add_worksheet()
aasheet.write("A1","Company")
aasheet.write("B1","Skills")
aasheet.write("C1","Published on")

print('Write all skill that you are familiar with no spaces and separated by a comma: ')
familiar_skills=input('>')
familiar_skills_list=familiar_skills.split(',')
print(f'Filtering by : {familiar_skills}')

def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
    for index,job in enumerate(jobs):
        published_date= job.find('span',class_='sim-posted').span.text
        #if '1' in published_date or '2' in published_date or '3' in published_date:
        company_name= job.find('h3',class_='joblist-comp-name').text.replace(' ','')
        required_skills= job.find('span',class_='srp-skills').text.replace(' ','').split()
        required_skills_list=(required_skills[0]).split(',')
        description_link=job.header.h2.a['href']
        html_description=requests.get(description_link).text
        soup_2 = BeautifulSoup(html_description,'lxml')
        description= soup_2.find('div',class_="jd-desc job-description-main").text
        published_date= job.find('span',class_='sim-posted').span.text
        #applications_received=''
        #try:
        #    applications_received=soup_2.find('strong',class_='ng-binding').text
        #except:
        #    pass
        #check = all(item in familiar_skills_list for item in required_skills_list)
        #if check is True:
            #with open (f'posts/{index}.txt','w') as f:                    
                #f.write('')
                #f.write(f'JOB NO.{index} \n')
                #f.write(f'Company name: {company_name.strip()} \n')
                #f.write(f'Required skills: {required_skills[0]} \n')
                #f.write(f'Published Date: {published_date.strip()} \n')
                #f.write(f'Description: {description}')
                #f.write('')
            #print(f'File Saved: {index}')
            #print(company_name.strip())
            #print(required_skills[0])
            #print(published_date.strip())
        aasheet.write(index+1,0,company_name.strip())
        aasheet.write(index+1,1,required_skills[0])
        aasheet.write(index+1,2,published_date.strip())
        #aasheet.write(index+1,3,html_description)
        #aasheet.write(index+1,4,applications_received)
        #aasheet.write(index+1,3,description)
        print(f'File Saved: {index}')
        print(html_description)
        
    for i in range(3):
        max_length=get_column_width(aasheet,i)
        try:
            set_column_autowidth(aasheet,i, max_length+1)
        except:
            pass
    aa.close()

    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


#NEXT STEPS : DESCRIPTION COLUMN (LINK TO IT); QUESTIONS AT THE BEGINNING (SELECT COUNTRIES TO WORK AT) (SELECT CURRENCY) (RANGE OF SALARY) (WORDS YOU WANT INCLUDED IN THE DESCRIPTION)

    msg = EmailMessage()
    msg['Subject'] = 'Test'
    msg['From'] = EMAIL_USER
    msg['To'] = 'insertemail@oftheadreesee.here'

    #msg.set_content('This is a plain text email')

    #files=['resume.pdf']

    #for file in files:
    with open('aa.xlsx','rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name) 


    #msg.add_alternative("""\
    #<!DOCTYPE html>
    #<html>
    #    <body>
    #        <h1 style="color:SlateGray;">test passed successfully!</h1>
    #    </body>
    #</html>
    #""", subtype='html')



    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)





if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait*60)
