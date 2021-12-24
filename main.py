from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# link = 'https://www.instagram.com/marvel/'
# link = 'https://www.instagram.com/teamrrq/'
link = 'https://www.instagram.com/evos.luch/'


def scraping_data():
    output = ""
    driver = webdriver.Chrome()
    driver.get(link)
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')
    posts = soup.findAll('div', class_="v1Nh3")
    post_type = posts[0].findChildren('div', class_='CzVzU')
    link_post = "https://www.instagram.com" + posts[0].findChildren('a')[0].get('href')
    driver.get(link_post)
    content2 = driver.page_source.encode('utf-8').strip()
    soup2 = BeautifulSoup(content2, 'lxml')
    upload_time = soup2.findAll('time', class_='_1o9PC')[0].text
    description = soup2.findAll('div', class_='C4VMK')[0].findChildren('span', class_="")[0].text


    if len(post_type) == 0:
        view_or_like = soup2.findAll('div', class_='Nm9Fw')[0].text
        output = f'Content type : photo\n{description}\n{view_or_like}\n{upload_time}\nlink : {link_post}'
    else:
        post_type = post_type[0].findChildren('div',class_='qF0y9')[0].findChildren('svg')[0].get('aria-label')
        if post_type == 'Video':
            view_or_like = soup2.findAll('span', class_='vcOH2')[0].text
            views_button = driver.find_elements(By.CLASS_NAME, "vcOH2")[0]
            wait = 1
            while wait == 1:
                if views_button.is_displayed() and views_button.is_enabled():
                    driver.execute_script("window.scrollTo(0, 500)")
                    views_button.click()
                    wait = 0
            content3 = driver.page_source.encode('utf-8').strip()
            soup3 = BeautifulSoup(content3, 'lxml')
            likes = soup3.findAll('div', class_='vJRqr')[0].text
            output = f'Content type : {post_type} \n{view_or_like}\n{likes}\n{upload_time}\n{description}\nlink : {link_post}'
        elif post_type == 'Carousel':
            view_or_like = soup2.findAll('div', class_='Nm9Fw')[0].text
            output = f'Content type : {post_type}\n{description}\n{view_or_like}\n{upload_time}\nlink : {link_post}'
        elif post_type == 'Klip':
            view_or_like = soup2.findAll('div', class_='Nm9Fw')[0].text
            output = f'Content type : {post_type}\n{description}\n{view_or_like}\n{upload_time}\nlink : {link_post}'
        else:
            output = 'Content type : Unknown'

    print(output)

    # view_or_like = soup2.findAll('span', class_='vcOH2')[0].text
    # upload_time = soup2.findAll('time', class_='_1o9PC')[0].text
    # description = soup2.findAll('div', class_='C4VMK')[0].findChildren('span', class_="")[0].text
    # if view_or_like.find('views') != -1:
    #     print("post type is video!")
    #     views_button = driver.find_elements(By.CLASS_NAME, "vcOH2")[0]
    #     wait = 1
    #     while wait == 1:
    #         if views_button.is_displayed() and views_button.is_enabled():
    #             driver.execute_script("window.scrollTo(0, 500)")
    #             views_button.click()
    #             wait = 0
    #     content3 = driver.page_source.encode('utf-8').strip()
    #     soup3 = BeautifulSoup(content3, 'lxml')
    #     likes = soup3.findAll('div', class_='vJRqr')[0].text
    #     print(f'{view_or_like}\n{likes}\n{upload_time}\n{description}')
    # else:
    #     print("post type is image!")
    #     print(f'{view_or_like}\n{upload_time}\n{description}')

    # print(view_or_like)



    #
    #
    # likes = soup2.findAll('div', class_='vJRqr')
    # print(likes)

    # upload_time = soup2.findAll('time', class_='_1o9PC')[0].text
    # verified_status = soup2.findAll('span', class_='coreSpriteVerifiedBadgeSmall')[0].text
    # description = soup2.findAll('div', class_='C4VMK')[0].findChildren('span', class_="")
    # link_newest_posts = ""


if __name__ == '__main__':
    scraping_data()
