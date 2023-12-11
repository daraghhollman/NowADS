import ads
import datetime
from dateutil import relativedelta
import random
import time

r = ads.RateLimits("SearchQuery")

# Import token from file (to exclude from script)
with open("./token.txt") as file:
    token = file.read()
    token = token.strip()
    ads.config.token = token

# Get today's date
today = str(datetime.date.today())[0:-3]
pastMonth = str(datetime.date.today() - relativedelta.relativedelta(months=1))[0:-3]
threeMonths = str(datetime.date.today() - relativedelta.relativedelta(months=3))[0:-3]


def SlowPrint(string, speed=0.01, isInput=False):
    for character in string:
        print(character, end="", flush=True)
        time.sleep(speed)

    if isInput:
        output = input("")
        return output



search = SlowPrint("What would you like to learn about today? (Leave blank for random) ", isInput=True)

papers = list(ads.SearchQuery(q=f"{search} pubdate:[{threeMonths} TO {today}]",
                              sort="citation_count",
                              rows=50,
                              fl=["id",
                                  "title",
                                  "author",
                                  "bibcode",
                                  "abstract",
                                  "first_author"]))

#print(r.limits)

random.seed()

chosenPaper = random.choice(papers)
authors = chosenPaper.author

slowPrint = True


if slowPrint:
    print("\n")
    SlowPrint(f"The paper randomly selected today (out of {len(papers)}),\n")
    SlowPrint("with search criterae:\n")
    SlowPrint(f"    [{search}],\n")
    SlowPrint(f"found between now and {threeMonths} is:\n")
    print("\n")
    SlowPrint(f"TITLE: {chosenPaper.title}\n")

    if len(authors) > 1:
        SlowPrint(f"AUTHOR: {chosenPaper.first_author} and others\n")

    else:
        SlowPrint(f"AUTHOR: {chosenPaper.author}\n")

    SlowPrint(f"BIBCODE: {chosenPaper.bibcode}\n")
    print("\n")
    SlowPrint(f"ABSTACT: {chosenPaper.abstract}\n", speed=0.005)
