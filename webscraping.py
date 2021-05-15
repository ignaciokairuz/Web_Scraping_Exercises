

#"""

# 10TH and final EXAMPLE of the video course

from bs4 import BeautifulSoup
import requests
import time

print('Write all skill that you are familiar with no spaces and separated by a semi-colon: ')
familiar_skills=input('>')
familiar_skills_list=familiar_skills.split(';')
print(f'Filtering by : {familiar_skills}')

def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
    for index,job in enumerate(jobs):
        published_date= job.find('span',class_='sim-posted').span.text
        if '1' in published_date or '2' in published_date or '3' in published_date:
            company_name= job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            required_skills= job.find('span',class_='srp-skills').text.replace(' ','').split()
            required_skills_list=(required_skills[0]).split(',')
            more_info=job.header.h2.a['href']
            published_date= job.find('span',class_='sim-posted').span.text
            check = all(item in familiar_skills_list for item in required_skills_list)
            if check is True:
                with open (f'posts/{index}.txt','w') as f:                    
                    f.write('')
                    f.write(f'JOB NO.{index} \n')
                    f.write(f'Company name: {company_name.strip()} \n')
                    f.write(f'Required skills: {required_skills[0]} \n')
                    f.write(f'Published Date: {published_date.strip()} \n')
                    f.write(f'More info: {more_info}')
                    f.write('')
                print(f'File Saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait*60)


 
#"""


"""

# 9TH EXAMPLE

from bs4 import BeautifulSoup
import requests

print('Write all skill that you are familiar with separated by a semi-colon: ')
familiar_skills=input('>')
familiar_skills_list=familiar_skills.split(';')
print(f'Filtering by : {familiar_skills}')

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
count=0
indicator=0
for job in jobs:
    published_date= job.find('span',class_='sim-posted').span.text
    if '1' in published_date or '2' in published_date or '3' in published_date:
        company_name= job.find('h3',class_='joblist-comp-name').text.replace(' ','')
        required_skills= job.find('span',class_='srp-skills').text.replace(' ','')
        required_skills_list=required_skills.split(',')
        more_info=job.header.h2.a['href']
        published_date= job.find('span',class_='sim-posted').span.text
        for i in required_skills_list:
            if i in familiar_skills_list :
                indicator+=1
        if indicator==len(required_skills_list):
            count+=1
            print(f'JOB NO.{count}.')
            print(f'Company name: {company_name.strip()}')
            print(f'Required skills: {required_skills.strip()}')
            print(f'Published Date: {published_date.strip()}')
            print(f'More info: {more_info}')
            print('')
        


######
        
#"""




"""

# 8TH EXAMPLE

from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content=html_file.read()
    
    soup=BeautifulSoup(content,'lxml')
    discounts=soup.find_all('div',class_='item-description')
    for discount in discounts:
        try:
            product=discount.h4.text
            discount_amount=discount.h3.text.split()[0].split("%")[0]
            print(f' On {product} there is {discount_amount} percent off on discount')
        except: pass

######
        
#"""



"""

# 7TH EXAMPLE


from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content=html_file.read()
    
    soup=BeautifulSoup(content,'lxml')
    discounts=soup.find_all('div',class_='item-description')
    for discount in discounts:
        try:
            print("On "+discount.h4.text)
            print(discount.h3.text.split()[0].split("%")[0]+" discount")
        except: pass



######
        
#"""


"""

# 6TH EXAMPLE

from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content=html_file.read()
    
    soup=BeautifulSoup(content,'lxml')
    discounts=soup.find_all('div',class_='item-description')
    for discount in discounts:
        try:
            print(discount.h4.text)
            print(discount.h3.text)
        except: pass


######
        
#"""

"""

# 5TH EXAMPLE


from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content=html_file.read()
    
    soup=BeautifulSoup(content,'lxml')
    subtitle_tags=soup.find_all('h3')
    for subtitles in subtitle_tags:
        print(subtitles.text)
        
#"""

"""
# FOURTH EXAMPLE


from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content=html_file.read()
    
    soup=BeautifulSoup(content,'lxml')
    tags=soup.find_all('h3')
    print(tags)
#"""

"""
# THIRD EXAMPLE

from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content=html_file.read()
    
    soup=BeautifulSoup(content,'lxml')
    tags=soup.find('h3')
    print(tags)
#"""


"""
# SECOND EXAMPLE

from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content=html_file.read()
    
    soup=BeautifulSoup(content,'lxml')
    print(soup.prettify())
#"""



"""
# FIRST EXAMPLE

from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content=html_file.read()
    print(content)
#"""















