#!/usr/bin/env python3

import os
import random
import requests
import json
import csv

from .arguments import args
from .logger import logger

TEXT_GEN_API_VAR = 'DEEP_AI_KEY'
DEFAULT_KEY = '9d414130-ca3d-4169-ab5e-0c0c2f17b65f'

words = [
  'The', 'he', 'at', 'but', 'there', 'of', 'was', 'be', 'not', 'use', 'and', 'for', 'this', 'what', 'an', 'a', 'on', 'have', 'all', 'each',
  'to', 'are', 'from', 'were', 'which', 'in', 'as', 'or', 'we', 'she', 'is', 'with', 'ine', 'when', 'do', 'you', 'his', 'had', 'your',
  'how', 'that', 'they', 'by', 'can', 'their', 'it', 'I', 'word', 'said', 'if'
]

with open(os.path.join(os.path.dirname(__file__), './data/cities.json')) as cities_file:
  cities = json.load(cities_file)

gop_members = [
  'Gary VanDeaver', 'Bryan Slaton', 'Cecil Bell Jr.', 'Keith Bell', 'Cole Hefner', 'Matt Schaefer', 'Jay Dean', 'Cody Harris',
  'Chris Paddie', 'Travis Clardy', 'Kyle Kacal', 'Ben Leman', 'John N. Raney', 'Steve Toth', 'Will Metcalf', 'John Cyrier', 'Ernest Bailes',
  'James White', 'Terry Wilson', 'Dade Phelan', 'Mayes Middleton', 'Greg Bonnen', 'Cody Vasut', 'Brooks Landgraf', 'Tom Craddick',
  'Dustin Burrows', 'John Frullo', 'Phil Stephenson', 'John T. Smithee', 'Four Price', 'Ken King', 'Candy Noble', 'Stephanie Klick',
  'Jeff Cason', 'Matt Krause', 'Tony Tinderholt', 'David Cook', 'Craig Goldman', 'Giovanni Capriglione', 'Charlie Geren', 'Sam Harless',
  'Dan Huberty', 'Briscoe Cain', 'Dennis Paul', 'Tom Oliverson', 'Mike Schofield'
]

with open(os.path.join(os.getcwd(), "bot", "data", "firstnameGirl.json")) as fng:
  firstNames = json.loads(fng.read())
  firstNames = firstNames["names"]

with open(os.path.join(os.getcwd(), "bot", "data", "firstnameBoy.json")) as fnb:
  maleFirstNames = json.loads(fnb.read())
  maleFirstNames = maleFirstNames["names"]

with open(os.path.join(os.getcwd(), "bot", "data", "lastname.json")) as ln:
  lastNames = json.loads(ln.read())
  lastNames = lastNames["names"]
  
# Seeds for text body generation
gpt2_prompts = [
  'My neighbor got an illegal abortion.', 'I suspect my father has violated the abortion ban.',
  random.choice(firstNames) + ' ' + random.choice(lastNames) + ' is helping people get abortions.',
  random.choice(gop_members) + ' has been sneaking around the abortion clinic in ' + random.choice(list(cities)) + '.'
]

info_location = [
  'A friend saw them', 'I work at the clinic', 'I know his secretary', 'He told me at the club', 'The police report', 'His wife told me',
  'From a coworker', 'From a neighbor', 'From a family member.', 'Heard from a friend', 'a relative told me', 'a private source',
  'A confession at church', 'I know their cousin', 'a taxi driver', 'From a cashier', 'Got a confidential tip', 'From a fellow parent',
  'a concerned citizen', 'From a relative.', 'A PP volunteer', 'A charity worker', 'A social worker', 'From my friend who knows cops',
  'from a lawyer', 'From a government employee'
]

zip_codes = [
  75001,
  75006,
  75011,
  75014,
  75015,
  75016,
  75017,
  75019,
  75030,
  75038,
  75039,
  75040,
  75041,
  75042,
  75043,
  75044,
  75045,
  75046,
  75047,
  75048,
  75048,
  75049,
  75050,
  75051,
  75052,
  75053,
  75054,
  75060,
  75061,
  75062,
  75063,
  75080,
  75081,
  75082,
  75083,
  75085,
  75088,
  75089,
  75104,
  75106,
  75115,
  75116,
  75123,
  75134,
  75137,
  75138,
  75141,
  75146,
  75149,
  75150,
  75159,
  75159,
  75172,
  75180,
  75180,
  75181,
  75182,
  75182,
  75185,
  75187,
  75201,
  75202,
  75203,
  75204,
  75205,
  75206,
  75207,
  75208,
  75209,
  75210,
  75211,
  75212,
  75214,
  75215,
  75216,
  75217,
  75218,
  75219,
  75220,
  75221,
  75222,
  75223,
  75224,
  75225,
  75226,
  75227,
  75228,
  75229,
  75230,
  75231,
  75232,
  75233,
  75234,
  75234,
  75235,
  75236,
  75237,
  75238,
  75239,
  75240,
  75241,
  75242,
  75243,
  75244,
  75244,
  75245,
  75246,
  75247,
  75248,
  75249,
  75250,
  75251,
  75253,
  75254,
  75258,
  75260,
  75261,
  75262,
  75263,
  75264,
  75265,
  75266,
  75267,
  75270,
  75295,
  75313,
  75315,
  75336,
  75339,
  75342,
  75354,
  75355,
  75356,
  75357,
  75359,
  75360,
  75367,
  75370,
  75371,
  75372,
  75374,
  75376,
  75378,
  75379,
  75380,
  75381,
  75382,
  75398,
]

# TX IPs gathered from here: https://www.xmyip.com/ip-addresses/united--states/texas
ips = [
  "24.27.72.", # Allen
  "65.65.132.", # Alpine
  "50.175.228.", # Alvin
  "50.175.229.", # Alvin
  "23.117.126.", # Arlington
  "24.153.156.", # Austin
  "66.193.112.", # Austin
  "66.193.113.", # Austin
  "50.94.23.", # Austin
  "24.173.59.", # Beaumont
  "63.174.138.", # Beaumont
  "24.219.225.", # Benbrook
  "50.15.108.", # Conroe
  "50.21.240.", # Conroe
  "32.144.6.", # Dallas
  "32.144.7.", # Dallas
  "17.253.118.", # Dallas
  "67.216.80.", # Dallas
  "67.216.81.", # Dallas
  "67.216.82.", # Dallas
  "67.216.83.", # Dallas
  "67.216.84.", # Dallas
  "67.216.85.", # Dallas
  "67.216.86.", # Dallas
  "67.216.87.", # Dallas
  "67.216.88.", # Dallas
  "67.216.89.", # Dallas
  "67.216.90.", # Dallas
  "67.216.91.", # Dallas
  "67.216.92.", # Dallas
  "67.216.93.", # Dallas
  "67.216.94.", # Dallas
  "67.216.95.", # Dallas
  "23.119.13.", # Dallas
  "23.119.14.", # Dallas
  "23.119.15.", # Dallas
  "64.197.59.", # Dallas
  "32.153.78.", # Dallas
  "32.153.79.", # Dallas
  "32.153.80.", # Dallas
  "32.153.81.", # Dallas
  "32.153.82.", # Dallas
  "32.153.83.", # Dallas
  "32.153.84.", # Dallas
  "32.153.85.", # Dallas
  "32.153.86.", # Dallas
  "32.153.87.", # Dallas
  "32.153.88.", # Dallas
  "32.153.89.", # Dallas
  "32.153.90.", # Dallas
  "32.153.91.", # Dallas
  "32.153.92.", # Dallas
  "32.153.93.", # Dallas
  "32.153.94.", # Dallas
  "32.153.95.", # Dallas
  "32.153.96.", # Dallas
  "32.153.97.", # Dallas
  "32.153.98.", # Dallas
  "4.68.19.", # Dallas
  "63.133.167.", # Dallas
  "66.155.134.", # Dallas
  "66.155.135.", # Dallas
  "68.109.248.", # Dallas
  "64.56.170.", # Dallas
  "32.149.194.", # Dallas
  "32.149.195.", # Dallas
  "32.149.196.", # Dallas
  "32.149.197.", # Dallas
  "32.168.139.", # Dallas
  "68.90.101.", # Dallas
  "24.242.248.", # Dallas
  "23.33.244.", # Dallas
  "23.33.245.", # Dallas
  "23.33.246.", # Dallas
  "23.33.247.", # Dallas
  "66.106.98.", # Dallas
  "47.184.118.", # Denton
  "47.184.119.", # Denton
  "47.184.120.", # Denton
  "47.184.121.", # Denton
  "24.206.145.", # Denton
  "12.184.253.", # Fort Worth
  "47.32.223.", # Fort Worth
  "12.203.146.", # Fort Worth
  "12.203.147.", # Fort Worth
  "12.184.254.", # Fort Worth
  "12.90.92.", # Fort Worth
  "50.207.209.", # Friendswood
  "64.134.76.", # Grapevine
  "66.169.188.", # Haltom City
  "66.169.189.", # Haltom City
  "66.78.229.", # Houston
  "66.78.230.", # Houston
  "66.78.231.", # Houston
  "66.161.197.", # Houston
  "66.3.44.", # Houston
  "66.3.45.", # Houston
  "66.3.46.", # Houston
  "50.162.44.", # Houston
  "45.17.135.", # Houston
  "68.91.35.", # Hurst
  "64.129.174.", # Irving
  "50.84.165.", # Irving
  "64.195.138.", # Irving
  "64.195.139.", # Irving
  "64.195.140.", # Irving
  "64.195.141.", # Irving
  "64.195.142.", # Irving
  "64.195.143.", # Irving
  "47.187.76.", # Lewisville
  "12.38.125.", # Lubbock
  "24.243.98.", # McAllen
  "67.10.39.", # McAllen
  "24.243.150.", # McAllen
  "24.243.151.", # McAllen
  "24.243.152.", # McAllen
  "47.185.248.", # Plano
  "63.199.94.", # Richardson
  "63.203.212.", # Richardson
  "63.203.213.", # Richardson
  "67.38.82.", # Richardson
  "66.137.185.", # Richardson
  "68.72.157.", # Richardson
  "68.72.158.", # Richardson
  "65.68.3.", # Richardson
  "64.218.64.", # Richardson
  "65.68.4.", # Richardson
  "65.64.221.", # Richardson
  "65.64.222.", # Richardson
  "65.64.223.", # Richardson
  "47.186.233.", # Richardson
  "66.136.184.", # Richardson
  "66.136.185.", # Richardson
  "66.136.186.", # Richardson
  "66.136.187.", # Richardson
  "64.252.212.", # Richardson
  "64.252.213.", # Richardson
  "64.252.214.", # Richardson
  "64.252.215.", # Richardson
  "64.252.216.", # Richardson
  "64.252.217.", # Richardson
  "64.252.218.", # Richardson
  "64.252.219.", # Richardson
  "64.252.220.", # Richardson
  "64.252.221.", # Richardson
  "64.252.222.", # Richardson
  "64.252.223.", # Richardson
  "64.252.224.", # Richardson
  "64.252.225.", # Richardson
  "64.252.226.", # Richardson
  "64.252.227.", # Richardson
  "64.252.228.", # Richardson
  "64.252.229.", # Richardson
  "64.252.230.", # Richardson
  "64.252.231.", # Richardson
  "64.252.232.", # Richardson
  "64.252.233.", # Richardson
  "64.252.234.", # Richardson
  "64.252.235.", # Richardson
  "64.252.236.", # Richardson
  "64.252.237.", # Richardson
  "64.252.238.", # Richardson
  "66.142.202.", # Richardson
  "66.235.81.", # Rosenberg
  "15.252.43.", # San Antonio
  "15.150.168.", # San Antonio
  "15.150.169.", # San Antonio
  "40.141.126.", # San Antonio
  "15.138.0.", # San Antonio
  "15.138.1.", # San Antonio
  "15.154.136.", # San Antonio
  "15.154.137.", # San Antonio
  "15.131.196.", # San Antonio
  "15.131.197.", # San Antonio
  "15.131.198.", # San Antonio
  "15.131.199.", # San Antonio
  "15.131.200.", # San Antonio
  "15.143.78.", # San Antonio
  "15.160.200.", # San Antonio
  "15.160.201.", # San Antonio
  "15.160.202.", # San Antonio
  "15.193.69.", # San Antonio
  "15.193.70.", # San Antonio
  "15.211.169.", # San Antonio
  "15.132.71.", # San Antonio
  "15.132.72.", # San Antonio
  "15.190.132.", # San Antonio
  "15.156.247.", # San Antonio
  "15.156.248.", # San Antonio
  "15.219.34.", # San Antonio
  "15.176.79.", # San Antonio
  "15.176.80.", # San Antonio
  "15.176.81.", # San Antonio
  "15.133.222.", # San Antonio
  "12.207.43.", # San Antonio
  "15.235.202.", # San Antonio
  "15.235.203.", # San Antonio
  "15.243.228.", # San Antonio
  "15.243.229.", # San Antonio
  "15.162.246.", # San Antonio
  "15.162.247.", # San Antonio
  "15.162.248.", # San Antonio
  "15.162.249.", # San Antonio
  "12.7.34.", # San Antonio
  "12.7.35.", # San Antonio
  "15.128.234.", # San Antonio
  "15.128.235.", # San Antonio
  "15.134.233.", # San Antonio
  "15.134.234.", # San Antonio
  "15.117.166.", # San Antonio
  "15.159.219.", # San Antonio
  "15.160.97.", # San Antonio
  "15.160.98.", # San Antonio
  "15.160.99.", # San Antonio
  "15.189.87.", # San Antonio
  "15.189.88.", # San Antonio
  "15.120.172.", # San Antonio
  "15.181.151.", # San Antonio
  "15.181.152.", # San Antonio
  "15.237.79.", # San Antonio
  "15.157.163.", # San Antonio
  "24.155.227.", # San Marcos
  "45.21.35." # Schertz
  "67.78.77.", # Seguin
]

# random element from each list

# Randomize doctor name format
# Read in first names and pick one
with open('bot/data/fns.csv') as fns:
	reader2 = csv.reader(fns)
	chosen_first=random.choice(list(fns))
# Read in last names and pick one
with open('bot/data/lns.csv') as lns:
	reader3=csv.reader(lns)
	chosen_last=random.choice(list(lns))
# Choose a name format
nF = random.choice(['FL','DL','L,F','L', 'DLF', 'IL', 'DIL'])

if nF == 'FL':
	dr = " ".join([chosen_first,chosen_last])
elif nF == 'DL':
	dr = " ".join(["Dr.",chosen_last])
elif nF == 'L,F':
	dr = ", ".join([chosen_last,chosen_first])
elif nF == 'L':
	dr = chosen_last
elif nf == 'DLF':
	dr = " ".join(["Dr.",chosen_first,chosen_last])
elif nf == 'IL':
	dr = "".join([chosen_first[0],". ",chosen_last])
elif nf == 'DIL':
	dr = "".join("Dr. ",[chosen_first[0],". ",chosen_last])

# Chose a state format
stateName = random.choice(['TX','Texas','TEXAS','texas','tx','Tx'])

# Read in zip code / city / county combos and select one to populate the form
with open('bot/data/TX_Zips.csv') as zf:
	reader = csv.reader(zf)
	chosen_row=random.choice(list(reader))
	
def anonymous_form():
  while True:
    city, county = random.choice(list(cities.items()))
    form_data = {
      'textarea-1': get_tip_body(),
      'text-1': random.choice(info_location),
      'text-6': dr,
      'text-2': chosen_row[1],
      'text-3': stateName,
      'text-4': chosen_row[0],
      'text-5': chosen_row[2],
      'hidden-1': random.choice(ips) + str(random.randint(0, 255)),
      'checkbox-1[]': 'no',
    }
    yield form_data

def sign_up_page():
  raise NotImplementedError()

def get_tip_body():
  rv = ''
  # If we have an API key for GPT2, use it
  if args.generate:
    key = DEFAULT_KEY
    if TEXT_GEN_API_VAR in os.environ:
      key = os.environ[TEXT_GEN_API_VAR]
      logger.info('Using key from environment: ' + key)
    else:
      logger.info('Using default key.')
    prompt = random.choice(gpt2_prompts)
    r = requests.post(
      "https://api.deepai.org/api/text-generator", data={
        'text': prompt,
      }, headers={'api-key': key}
    )
    rv = str(r.json()['output'].encode('utf-8'))
    # cut out the prompt, which comes from a limited set and can be filtered on
    rv = rv.replace(prompt, '').lstrip()
    # take string up through last complete sentence since we occasionally get trailing words
    if '.' in rv:
      rv = rv[0:rv.rindex('.')] + '.'
  else:
    # standard tip body generation
    rv = random.choice(gop_members) + ' took their mistress ' + random.choice(firstNames) + ' ' + random.choice(
      lastNames
    ) + ' to get an abortion after their affair.'
  logger.info('Generated text:\n' + rv)
