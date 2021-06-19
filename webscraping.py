from bs4 import BeautifulSoup
import requests
import time

print('Write all skill that you are familiar with no spaces and separated by a semi-colon: ')
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
        check = all(item in familiar_skills_list for item in required_skills_list)
        if check is True:
            with open (f'posts/{index}.txt','w') as f:                    
                f.write('')
                f.write(f'JOB NO.{index} \n')
                f.write(f'Company name: {company_name.strip()} \n')
                f.write(f'Required skills: {required_skills[0]} \n')
                f.write(f'Published Date: {published_date.strip()} \n')
                f.write(f'Description: {description}')
                f.write('')
            print(f'File Saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait*60)
