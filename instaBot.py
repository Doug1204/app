from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import json
import time

class bot:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.browser = webdriver.Chrome("C:\\Users\\Rachel Greenwood\\Desktop\\Python code\\chromedriver_win32\\chromedriver.exe")

  def goToSite(self):
    self.browser.get('http://www.instagram.com')
  
  def logIn(self):
    time.sleep(0.5)
    o ="""
    self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[2]/p/a').click() # Log In button
    time.sleep(3)
    self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(self.username) # Username
    self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(self.password)# Password
    self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click() #Click submit
    """
    self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(self.username) # Username
    self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(self.password)# Password
    self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div[1]/div/form/div[4]/button/div').click()
    time.sleep(4)
    try:
      self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
    except:
      pass
    self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click() # remove pop up
  
  def profile(self):
    self.browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click() # Goes to profile
  
  def search(self, name):
    time.sleep(1)
    self.browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(name) # Search bar
    time.sleep(3)
    self.browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a').click()

  def open_foll(self, foll): # foll should = 'following' or 'followers'
    self.browser.find_element_by_xpath(f"//a[contains(@href,'/{foll}')]").click()
    if foll == 'following': self.following = self._get_names()
    else: self.followers = self._get_names()

  def _get_names(self):
      time.sleep(2)
      scrolly = self.browser.find_element_by_xpath('/html/body/div[4]/div/div[2]')
      box = self.browser.find_element_by_xpath("/html/body/div[4]/div/div[2]") # scrolling box
      while True:
        lst1 = box.find_elements_by_tag_name('a')
        self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",scrolly) #scroll
        time.sleep(2)
        lst2 = box.find_elements_by_tag_name('a')
        if lst1 == lst2: break # if page hasn't moved
      links = box.find_elements_by_tag_name('a')
      names = [name.text for name in links if name.text != '']
      self.browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click() # close button
      return names

  def unfollowFinder(self):
    self.unfollow = [i for i in self.following if i not in self.followers]
  
  def findPerson(self, username):
    self.browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
    time.sleep(1)
    self.browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/button').click()
    self.browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div/div[2]/input').send_keys(username)
    time.sleep(1.5)
    self.browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
    self.browser.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/div/button').click()

  def text(self, message):
    self.browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message)
    self.browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
  
  def spam(self, username, message, numberOfTimes):
    self.goToSite()
    time.sleep(3)
    self.logIn()
    time.sleep(1)
    self.findPerson(username)
    time.sleep(1)
    while True:
      for _ in range(numberOfTimes):
        self.text(message)
    self.browser.quit()

  def getUnfollow(self, username, save=False):
    self.goToSite()
    time.sleep(3)
    self.logIn()
    time.sleep(1)
    self.search(username)
    time.sleep(3)
    self.open_foll('following')
    self.open_foll('followers')
    self.unfollowFinder()
    if save:
      with open(f'unfollowers-{username}', 'w') as f:
        for person in self.unfollow:
          f.write(person + '\n')
    self.browser.quit()


