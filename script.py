import csv
from idlelib.iomenu import encoding
from pyexpat import errors
from builtins import round

with open('G:/Python Programs/stackOverFlowSurvey/survey_results_public.csv', errors='ignore') as f:
    csv_reader = csv.DictReader(f)

    yes_count = 0
    no_count = 0

    for line in csv_reader:
        if line['Hobbyist'] == 'Yes':
            yes_count += 1
        elif line['Hobbyist'] == 'No':
            no_count += 1
            
            
#     count_dict = {
#         'Yes': 0,
#         'No': 0
#         }
#     
#     for line in csv_reader:
#         count_dict[line['Hobbyist']] +=1
# Number of Yes_count and No_count here.             
# print(yes_count)        
# print(no_count)
 
total_count = yes_count + no_count
 
perc_yes_count = (yes_count/total_count)*100
perc_no_count = (no_count/total_count)*100
 
perc_yes_count = round(perc_yes_count, 2)
perc_no_count = round(perc_no_count, 2)
 
print(f'Yes : {perc_yes_count}%')
print(f'No : {perc_no_count}%')

# print(f'yes : {count_dict["Yes"]}%')
# print(f'no : {count_dict["No"]}%')





        
