"""
# FIRST EXAMPLE

from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content=html_file.read()
    print(content)
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
# THIRD EXAMPLE

from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content=html_file.read()
    
    soup=BeautifulSoup(content,'lxml')
    tags=soup.find('h3')
    print(tags)
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


#"""

# 9TH EXAMPLE

from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
count=0
for job in jobs:
    published_date= job.find('span',class_='sim-posted').span.text
    if '1' in published_date or '2' in published_date or '3' in published_date:
        count+=1
        company_name= job.find('h3',class_='joblist-comp-name').text.replace(' ','')
        required_skills= job.find('span',class_='srp-skills').text.replace(' ','')
        published_date= job.find('span',class_='sim-posted').span.text
        print(f'JOB NO.{count}.')
        print(f'Company name: {company_name.strip()}')
        print(f'Required skills: {required_skills.strip()}')
        print(f'Published Date: {published_date.strip()}')
        print('')
        


######
        
#"""


"""

# 6TH EXAMPLE


######
        
#"""


"""

# 6TH EXAMPLE


######
        
#"""


"""

# 6TH EXAMPLE


######
        
#"""


"""

# 6TH EXAMPLE


######
        
#"""