
import inquirer
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os




Cantrips= ['Fire Bolt','Mage Hand','Dancing Lights','Message','Mind Sliver','Prestidigitation','Sapping Sting',
           'Ray Of Frost','Minor Illusion','Green-Flame Blade','Booming Blade','Encode Thoughts']
Level_One= [
'Shield', 'Detect Magic', 'Disguise Self', 'Fog Cloud', 'Sleep', 'Ice Knife', 'Spiny Shield',
'Magic Missile', 'Tashas Hideous Laughter', 'Elevated Sight', 'Spiny Shield', 'Burning Hands', 'Alarm', 'Find Familiar',
'Comprehend Languages', 'Identify', 'Tensors Floating Disk', 'Unseen Servant','cure wounds','Gift of Alacrity']

Level_Two=['Eb And Flow','Mind Spike','Detect Thoughts','Suggestion','Fortunes Favor','Augury', 'Hold Person','Halaster image swap','Lesser Restoration','Invisibility','Immovable Object',
           'Scorching Ray','Acid Arrow','Gust of Wind','Skeemos Weird Bottle', 'Arcane Lock','Wrist Pocket','snowshoes', 'Enlarge Reduce','Misty Step']

Level_Three= ['Dispel Magic','Sending','Lightning Bolt','Fireball','Pulse Wave','Fly','Remove Curse',
             'Fear','Intellect fortress','Clairvoyance','Haste','Tidal Wave','Nondetection','Glyph of Warding','Gaseous Form','Wall of Water','Water Breathing',
              'Feign Death','Phantom Steed','Leomunds Tiny Hut','Counterspell', 'revivify','Continual Flame']

Level_Four= ['Polymorph','Wall of Fire','Evards Black Tentacles','Divination','Confusion','Locate Creature',
             'Dimension Door','Greater Invisibility','Fire Shield','Phantasmal Killer','Ice Storm',
             'Conjure Minor Elementals','Blight','Arcane Eye','Stellar Bodies']

Level_Five= ['Bigbys Hand','Teleportation Circle','Wall of Force','Dawn','Cone of Cold','Conjure Elemental','Dream',
             'Modify Memory','Scry','Legend Lore','Dominate Person','Dream','Rarys Telepathic Bond']

Level_Six= ['Mental Prison','Disintegrate','Gravity Fissure','Contingency','Create Undead','Globe of Invulnerability','Sunbeam','Soul Cage','Planar Ally']

Level_Seven=['Teleport','Whirlwind','Magnificent Mansion','Halaster Anti-scry chains','Symbol','Crown of Stars',]

Level_eight=['Mind Blank','antipathy/sympathy','dominate monster','control weather']

Level_nine=['Wish','Meteor Swarm']
questions = [
    inquirer.Checkbox('Cantrips',
                      message="Select 5 Cantrips",
                      choices= Cantrips,
                      ),
    inquirer.Checkbox('1st level',
                      message="what are you preparing",
                      choices=Level_One,
                      ),
    inquirer.Checkbox('2nd Level',
                      message="what are you preparing",
                      choices=Level_Two,
                      ),
    inquirer.Checkbox('3rd level',
                      message="what are you preparing",
                      choices=Level_Three
                      ),
    inquirer.Checkbox('4th level',
                      message="what are you preparing",
                      choices=Level_Four
                      ),
    inquirer.Checkbox('5th Level',
                      message="what are you preparing",
                      choices=Level_Five
                      ),
    inquirer.Checkbox('6th level',
                        message="what are you preparing",
                       choices=Level_Six
                       ),
    inquirer.Checkbox('7th level',
                        message="what are you preparing",
                       choices=Level_Seven
                       ),
    inquirer.Checkbox('8th level',
                        message="what are you preparing",
                       choices=Level_eight
                       ),
inquirer.Checkbox('pth level',
                        message="what are you preparing",
                       choices=Level_nine
                       ),
]
Prepared_Spells = inquirer.prompt(questions)


df = pd.DataFrame(list(Prepared_Spells.items()),columns = ['Spell Level','Spell'])
pd.set_option('display.max_colwidth', 1000)


f = open("df.txt","w")
f.write( str(df) )
f.close()




file = open('df.txt', 'r')
data= open('Prepared_Spells.txt', 'w')
for line in file:
    data.write(line.replace('[','').replace(']',''))




file.close()
data.close()


yeye= r'C:\Users\Mason\PycharmProjects\pythonProject\Prepared_Spells.txt'
os.startfile(yeye)


Values = Prepared_Spells.values()

v=open('values.txt','w')
v.write(str(Values))
v.close()

vin= open('values.txt','r')
vout=open('urlready.txt','w')

for line in vin:
    vout.write(line.replace('dict_values','').replace('[','').replace(']','').replace('(','').replace(')','').replace(',','\n')
               .replace("'",""))

vin.close()
vout.close()

valuelist=open('urlready.txt').read().splitlines()

url= 'http://dnd5e.wikidot.com/spell:'

URLList= [url + x for x in valuelist]

U=open('Urllist.txt','w')
U.write(str(URLList))
U.close()

Uin=open('Urllist.txt','r')
Uout= open('Urllist2.txt','w')
for line in Uin:
    Uout.write(line.replace(': ',':').replace(', ','\n').replace(' ','-').replace('[','').replace(']','').replace("'",""))
Uin.close()
Uout.close()

with open('Urllist2.txt','r') as f:
    urls = f.readlines()

urls = ([s.strip('\n') for s in urls])

alltext = []
for url in urls:
        page=requests.get(url)
        contents = page.content
        soup = BeautifulSoup(contents, 'html.parser')

        title = soup.find("div", {'class': "page-title page-header"})
        text = soup.find("div", {'id': "page-content"})

        alltext.append(title)
        alltext.append(text)


with open("soup.txt", "w", encoding='utf-8') as file:
    file.write(str(alltext))

with open('soup.txt','r') as file:
    filedata = file.read()

filedata = filedata.replace('/p','').replace('</strong>','').replace('<p>','').replace('<strong>','').replace('<em>',''
    ).replace('<br/>','\n').replace('</em>','').replace('<a % >','').replace('<title>','').replace('[',''
       ).replace('],','\n\n\n').replace(' DND 5th Edition</title>','').replace('<div class="page-title page-header"><span>',''
        ).replace('</span></div>, <div id="page-content">','').replace('<div class="content-separator" style="display: none:"></div>','').replace('<>','').replace('</div>','\n'
         ).replace(', The page does not (yet) exist.<p id="404-message">','').replace('The page spell you want to access does not exist.','').replace('<ul id="create-it-now-link">','').replace('<li><a href="javascript:;" onclick="WIKIDOT.page.listeners.editClick(event)">Create page</a></li>',''
           ).replace('</ul>','').replace('<a href="http://dnd5e.wikidot.com/spells:artificer">Artificer</a>','').replace('<a href="http://dnd5e.wikidot.com/spells:sorcerer">Sorcerer</a>','').replace('<a href="http://dnd5e.wikidot.com/spells:wizard">Wizard</a>',''
            ).replace('<a href="http://dnd5e.wikidot.com/spells:warlock">Warlock</a>','').replace('<a href="http://dnd5e.wikidot.com/spells:druid">Druid</a>','').replace('<a href="http://dnd5e.wikidot.com/spells:cleric">Cleric</a>','').replace('<a href="http://dnd5e.wikidot.com/spells:bard">Bard</a>','').replace('Spell Lists','\n').replace('The page spell:eb-and-flow you want to access does not exist.',''
              ).replace('<ul>','').replace('<li>','').replace('</li>','')

with open('spell_description.txt',"w", encoding='utf-8') as file:
    file.write(filedata)




