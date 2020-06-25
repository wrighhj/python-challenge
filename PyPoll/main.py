import os

import csv

votes = []
candidates = []
khan = 0
correy = 0
li = 0
otooley = 0

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
        # winner of election based on popular vote
        winner = max(set(candidates), key = candidates.count)
    
    # print(khan_perc)
    # print(len(votes))
    # print(winner)
    print(candidates)
    # print(correy)
    # print(li)
    # print(otooley)
    # print(f"""
    # ELection Results
    # -------------------------
    # Total Votes: {total_votes}
    # -------------------------
    # Khan: {khan_perc}% ({khan})
    # Correy: {correy_perc}% ({correy})
    # Li: {li_perc}% ({li})
    # O'Tooley: {otooley_perc}% ({otooley})
    # -------------------------
    # Winner: {winner}""")