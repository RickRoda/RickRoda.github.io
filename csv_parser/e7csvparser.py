import csv
import json 
from collections import defaultdict

"""HOW TO RUN

1. Have Python installed on your machine
2. From Command Line, go to directory continaing this file.
3. Place CSV in SAME DIRECTORY as this Python file.
4. In Command Line, type 'python e7parser.py'
5. Wait for completion
"""

#Open CSV File. MUST be in same directory as this python script
csvfile = open('TheHolyGrail.csv', 'r')

#Create JSON File
jsonfile = open('e7json.json', 'w')

#Fieldnames for JSON
fieldnames = (
    'character',
    'skill',
    'att_rate',
    'soul_burn_att_rate',
    'Bonus_Dmg1_atk%',
    'Bonus_Dmg1_Conditions',
    'Bonus_Dmg2',
    'Bonus_Dmg2_Conditions',
    'secondary_scaling%',
    'secondary_stat',
    'secondary_stat_burn%',
    'Beneficial_Effect',
    'Soulburn_Beneficial_Effect',
    'Soulburn_Secondary_Stat%',
    'Soulburn_Secondary_Stat%2',
    'MULT',
    'ATK',
    'HP',
    'DEF')

#Initialize Dictionary Reader with CSV and Fieldnames
reader = csv.DictReader(csvfile, fieldnames)

#Initiate empty Array that will contain all the JSON Elements as we go through the CSV
output = []

#Skip header Row
next(reader,None)

#Until we reach the end of the CSV...
for row in reader:
#Initialize empty JSON Element Dictionary that will be reused to insert each JSON element to output Array    
    record = {}

    record['character'] = row['character']
    record['ATK'] = row['ATK']
    record['HP'] = row['HP']
    record['DEF'] = row['DEF']
    record['SPD'] = ""

#Initialize Nested JSON Element for Skill 1 
    record['skill_1'] = {}

#Find each Skill 1 value from each row and add them to the JSON Element
    record['skill_1']['att_rate'] = row['att_rate']
    record['skill_1']['soul_burn_att_rate'] = row['soul_burn_att_rate']
    record['skill_1']['Bonus_Dmg1_atk%'] = row['Bonus_Dmg1_atk%']
    record['skill_1']['Bonus_Dmg1_Conditions'] = row['Bonus_Dmg1_Conditions']
    record['skill_1']['Bonus_Dmg2'] = row['Bonus_Dmg2']
    record['skill_1']['Bonus_Dmg2_Conditions'] = row['Bonus_Dmg2_Conditions']
    record['skill_1']['secondary_scaling'] = row['secondary_scaling%']
    record['skill_1']['secondary_stat'] = row['secondary_stat']
    record['skill_1']['secondary_stat_burn'] = row['secondary_stat_burn%']
    record['skill_1']['Beneficial_Effect'] = row['Beneficial_Effect']
    record['skill_1']['Soulburn_Beneficial_Effect'] = row['Soulburn_Beneficial_Effect']
    record['skill_1']['Soulburn_Secondary_Stat'] = row['Soulburn_Secondary_Stat%']
    record['skill_1']['Soulburn_Secondary_Stat'] = row['Soulburn_Secondary_Stat%2']
    record['skill_1']['MULT'] = row['MULT']

#Next Row for Skill 2
    skill_2_row = next(reader)

#Initialize Nested JSON Element for Skill 2 
    record['skill_2'] = {}

#Find each Skill 2 value from each row and add them to the JSON Element    
    record['skill_2']['att_rate'] = skill_2_row['att_rate']
    record['skill_2']['soul_burn_att_rate'] = skill_2_row['soul_burn_att_rate']
    record['skill_2']['Bonus_Dmg1_atk%'] = skill_2_row['Bonus_Dmg1_atk%']
    record['skill_2']['Bonus_Dmg1_Conditions'] = skill_2_row['Bonus_Dmg1_Conditions']
    record['skill_2']['Bonus_Dmg2'] = skill_2_row['Bonus_Dmg2']
    record['skill_2']['Bonus_Dmg2_Conditions'] = skill_2_row['Bonus_Dmg2_Conditions']
    record['skill_2']['secondary_scaling'] = skill_2_row['secondary_scaling%']
    record['skill_2']['secondary_stat'] = skill_2_row['secondary_stat']
    record['skill_2']['secondary_stat_burn'] = skill_2_row['secondary_stat_burn%']
    record['skill_2']['Beneficial_Effect'] = skill_2_row['Beneficial_Effect']
    record['skill_2']['Soulburn_Beneficial_Effect'] = skill_2_row['Soulburn_Beneficial_Effect']
    record['skill_2']['Soulburn_Secondary_Stat'] = skill_2_row['Soulburn_Secondary_Stat%']
    record['skill_2']['Soulburn_Secondary_Stat'] = skill_2_row['Soulburn_Secondary_Stat%2']
    record['skill_2']['MULT'] = skill_2_row['MULT']

#Next row for Skill 3
    skill_3_row = next(reader)

#Initialize Nested JSON Element for Skill 3    
    record['skill_3'] = {}

#Find each Skill 3 value from each row and add them to the JSON Element    
    record['skill_3']['att_rate'] = skill_3_row['att_rate']
    record['skill_3']['soul_burn_att_rate'] = skill_3_row['soul_burn_att_rate']
    record['skill_3']['Bonus_Dmg1_atk%'] = skill_3_row['Bonus_Dmg1_atk%']
    record['skill_3']['Bonus_Dmg1_Conditions'] = skill_3_row['Bonus_Dmg1_Conditions']
    record['skill_3']['Bonus_Dmg2'] = skill_3_row['Bonus_Dmg2']
    record['skill_3']['Bonus_Dmg2_Conditions'] = skill_3_row['Bonus_Dmg2_Conditions']
    record['skill_3']['secondary_scaling'] = skill_3_row['secondary_scaling%']
    record['skill_3']['secondary_stat'] = skill_3_row['secondary_stat']
    record['skill_3']['secondary_stat_burn'] = skill_3_row['secondary_stat_burn%']
    record['skill_3']['Beneficial_Effect'] = skill_3_row['Beneficial_Effect']
    record['skill_3']['Soulburn_Beneficial_Effect'] = skill_3_row['Soulburn_Beneficial_Effect']
    record['skill_3']['Soulburn_Secondary_Stat'] = skill_3_row['Soulburn_Secondary_Stat%']
    record['skill_3']['Soulburn_Secondary_Stat'] = skill_3_row['Soulburn_Secondary_Stat%2']
    record['skill_3']['MULT'] = skill_3_row['MULT']

#Sven has 4 Skills
    if record['character'] == 'Sven':
        skill_4_row = next(reader)
        record['skill_4'] = {}
        record['skill_4']['att_rate'] = skill_4_row['att_rate']
        record['skill_4']['soul_burn_att_rate'] = skill_4_row['soul_burn_att_rate']
        record['skill_4']['Bonus_Dmg1_atk%'] = skill_4_row['Bonus_Dmg1_atk%']
        record['skill_4']['Bonus_Dmg1_Conditions'] = skill_4_row['Bonus_Dmg1_Conditions']
        record['skill_4']['Bonus_Dmg2'] = skill_4_row['Bonus_Dmg2']
        record['skill_4']['Bonus_Dmg2_Conditions'] = skill_4_row['Bonus_Dmg2_Conditions']
        record['skill_4']['secondary_scaling'] = skill_4_row['secondary_scaling%']
        record['skill_4']['secondary_stat'] = skill_4_row['secondary_stat']
        record['skill_4']['secondary_stat_burn'] = skill_4_row['secondary_stat_burn%']
        record['skill_4']['Beneficial_Effect'] = skill_4_row['Beneficial_Effect']
        record['skill_4']['Soulburn_Beneficial_Effect'] = skill_4_row['Soulburn_Beneficial_Effect']
        record['skill_4']['Soulburn_Secondary_Stat'] = skill_4_row['Soulburn_Secondary_Stat%']
        record['skill_4']['Soulburn_Secondary_Stat'] = skill_4_row['Soulburn_Secondary_Stat%2']
        record['skill_4']['MULT'] = skill_4_row['MULT']
#Append the json entry we just created to the JSON file 
    output.append(record)

#Create the final JSON    
json.dump(output, jsonfile, indent=4)

print("All Done!")