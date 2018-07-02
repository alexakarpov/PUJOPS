from pyvirtualdisplay import Display
from xvfbwrapper import Xvfb
from selenium import webdriver

vdisplay = Xvfb()
vdisplay.start()

# launch stuff inside virtual display here
browser = webdriver.Firefox()
browser.get('http://localhost:80')
assert 'Django' in browser.title

browser.quit()

vdisplay.stop()
