import discord
import os
import requests
import json
from keep_alive import keep_alive

client = discord.Client()

dog_words = ["puppy", "pup", "dog", "woofer", "woof", "bork", "borker", "good boy", "good girl", ":dog:"]

dog_breeds = [ 
  'affenpinscher',
  'african',
  'airedale',
  'akita',
  'appenzeller',
  'australian',
  'basenji',
  'beagle',
  'bluetick',
  'borzoi',
  'bouvier',
  'boxer',
  'brabancon',
  'briard',
  'buhund',
  'bulldog',
  'bullterrier',
  'cairn',
  'cattledog',
  'chihuahua',
  'chow',
  'clumber',
  'cockapoo',
  'collie',
  'coonhound',
  'corgi',
  'cotondetulear',
  'dachshund',
  'dalmatian',
  'dane',
  'deerhound',
  'dhole',
  'dingo',
  'doberman',
  'elkhound',
  'entlebucher',
  'eskimo',
  'finnish',
  'frise',
  'germanshepherd',
  'greyhound',
  'groenendael',
  'havanese',
  'hound',
  'husky',
  'keeshond',
  'kelpie',
  'komondor',
  'kuvasz',
  'labrador',
  'leonberg',
  'lhasa',
  'malamute',
  'malinois',
  'maltese',
  'mastiff',
  'mexicanhairless',
  'mix',
  'mountain',
  'newfoundland',
  'otterhound',
  'ovcharka',
  'papillon',
  'pekinese',
  'pembroke',
  'pinscher',
  'pitbull',
  'pointer',
  'pomeranian',
  'poodle',
  'pug',
  'puggle',
  'pyrenees',
  'redbone',
  'retriever',
  'ridgeback',
  'rottweiler',
  'saluki',
  'samoyed',
  'schipperke',
  'schnauzer',
  'setter',
  'sheepdog',
  'shiba',
  'shihtzu',
  'spaniel',
  'springer',
  'stbernard',
  'terrier',
  'vizsla',
  'waterdog',
  'weimaraner',
  'whippet',
  'wolfhound'
]

sub_breeds = {
  'australian': [
  "shepherd"
  ],
  'buhund': [
  "norwegian"
  ],
  'bulldog': [
  "boston",
  "english",
  "french"
  ],
  'bullterrier': [
  "staffordshire"
  ],
  'cattledog': [
  "australian"
  ],
  'collie': [
  "border"
  ],
  'corgi': [
  "cardigan"
  ],
  'dane': [
  "great"
  ],
  'deerhound': [
  "scottish"
  ],
  'elkhound': [
  "norwegian"
  ],
  'finnish': [
  "lapphund"
  ],
  'frise': [
  "bichon"
  ],
  'greyhound': [
  "italian"
  ],
  'hound': [
  "afghan",
  "basset",
  "blood",
  "english",
  "ibizan",
  "plott",
  "walker"
  ],
  'mastiff': [
  "bull",
  "english",
  "tibetan"
  ],
  'mountain': [
  "bernese",
  "swiss"
  ],
  'ovcharka': [
  "caucasian"
  ],
  'pinscher': [
  "miniature"
  ],
  'pointer': [
  "german",
  "germanlonghair"
  ],
  'poodle': [
  "miniature",
  "standard",
  "toy"
  ],
  'retriever': [
  "chesapeake",
  "curly",
  "flatcoated",
  "golden"
  ],
  'ridgeback': [
  "rhodesian"
  ],
  'schnauzer': [
  "giant",
  "miniature"
  ],
  'setter': [
  "english",
  "gordon",
  "irish"
  ],
  'sheepdog': [
  "english",
  "shetland"
  ],
  'spaniel': [
  "blenheim",
  "brittany",
  "cocker",
  "irish",
  "japanese",
  "sussex",
  "welsh"
  ],
  'springer': [
  "english"
  ],
  'terrier': [
  "american",
  "australian",
  "bedlington",
  "border",
  "dandie",
  "fox",
  "irish",
  "kerryblue",
  "lakeland",
  "norfolk",
  "norwich",
  "patterdale",
  "russell",
  "scottish",
  "sealyham",
  "silky",
  "tibetan",
  "toy",
  "westhighland",
  "wheaten",
  "yorkshire"
  ],
  'waterdog': [
  "spanish"
  ],
  'wolfhound': [
  "irish"
  ]
  }

def get_dog():
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  json_data = json.loads(response.text)
  url = json_data['message']
  return(url)

def get_breed_pic(word):
  breed = word.strip('/').strip(' ')
  response = requests.get("https://dog.ceo/api/breed/{breed}/images/random".format(breed=breed))
  json_data = json.loads(response.text)
  dog_pic = json_data['message']
  return(dog_pic)

def get_sub_pic(string):
  breed = ''
  sub_breed = ''
  url = ''
  words = string.split(' ')
  sub_breed_keys = sub_breeds.keys()

  for word in words:
    if word in sub_breed_keys:
      breed = word
  
  for name in sub_breeds[breed]:
    for word in words:
      if name == word:
        sub_breed = name
        url = "https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random".format(breed=breed, sub_breed=sub_breed)
      else:
        url = "https://dog.ceo/api/breed/{breed}/images/random".format(breed=word)
  
  
  response = requests.get(url)
  json_data = json.loads(response.text)
  dog_pic = json_data['message']
  return(dog_pic)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return 

  msg = message.content

  if msg.startswith('//'):
    if any(word in msg for word in sub_breeds):
      string = msg
      pic = get_sub_pic(string)
      await message.channel.send(pic)

  if msg.startswith('//'):
    if any(word in msg for word in dog_breeds):
      if any(word in msg for word in sub_breeds):
        return
      else:
        breed = msg
        pic = get_breed_pic(breed)
        await message.channel.send(pic)
    
  if msg.startswith('//'):
    if any(word in msg for word in dog_words):
      if any(word in msg for word in dog_breeds) and any(word in msg for word in sub_breeds):
        return
      else:
        dog = get_dog()
        await message.channel.send(dog)


keep_alive()
client.run(os.getenv('TOKEN'))  