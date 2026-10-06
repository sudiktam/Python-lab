# import json



# with open('election_result.json', 'r', encoding='utf-8') as file_obj:
#     election_data = json.load(file_obj)


# # total_vote = 0 
# # for candidate in election_data:
# #     vote_received = candidate.get('TotalVoteReceived')
# #     total_vote = total_vote + vote_received

# # average_vote = total_vote / len(election_data)
# # print(average_vote)
# # print(total_vote)

# hightest_vote = 0

            

import json
import csv

with open('election_result.json', 'r', encoding='utf-8') as file_obj:
    election_data = json.load(file_obj)

with open('election_result.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=election_data[0].keys())

    writer.writeheader()
    writer.writerows(election_data)

print('CSV file created successfully')