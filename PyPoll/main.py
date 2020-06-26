import os

import csv

votes = []
candidates = []
can_votes = []
khan = 0
correy = 0
li = 0
otooley = 0
# winner = []

# all_info = ["Khan", khan, "Correy", correy, "Li", li, "O'Tooley", otooley]

pypoll_csv = os.path.join('Resources', 'election_data.csv')

with open(pypoll_csv) as csvfile:
    pypollreader = csv.reader(csvfile, delimiter = ",")
    next(pypollreader)

    for row in pypollreader:
        votes.append(row[2])
        if row[2] not in candidates:
            # complete list of candidates
            candidates.append(row[2])
        if row[2] == "Khan":
            khan += 1
            # percent vote won
            khan_perc = '{:.3f}'.format((khan/len(votes))*100)
        if row[2] == "Correy":
            correy += 1
            # percent vote won
            correy_perc = '{:.3f}'.format((correy/len(votes))*100)
        if row[2] == "Li":
            li += 1
            # percent vote won
            li_perc = '{:.3f}'.format((li/len(votes))*100)
        if row[2] == "O'Tooley":
            otooley += 1
            # percent vote won
            otooley_perc = '{:.3f}'.format((otooley/len(votes))*100)
        # total number of votes
        total_votes = len(votes)
        can_votes = [khan, correy, li, otooley]
        # can_position = candidates.idex("Khan")
        if khan >= max(can_votes):
            winner = "Khan"
        if correy >= max(can_votes):
            winner = "Correy"
        if li >= max(can_votes):
            winner = "Li"
        if otooley >= max(can_votes):
            winner = "O'Tooley"

    print(f"""
    ELection Results
    -------------------------
    Total Votes: {total_votes}
    -------------------------
    {candidates[0]}: {khan_perc}% ({khan})
    {candidates[1]}: {correy_perc}% ({correy})
    {candidates[2]}: {li_perc}% ({li})
    {candidates[3]}: {otooley_perc}% ({otooley})
    -------------------------
    Winner: {winner}""")