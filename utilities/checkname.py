import requests
import re 
from bs4 import BeautifulSoup as parser

class Check:
  def __init__(self) ->None:
    pass
  def checkavailability(url):
    return parser(requests.get(url).content,'html.parser').find('title').text