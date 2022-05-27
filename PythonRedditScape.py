# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:33:34 2022

@author: howel
"""

from IPython import display
import math
from pprint import pprint
import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid', context='talk', palette='Dark2')

import praw

reddit = praw.Reddit(client_id='Q7HUwrvzuMA-h14j2jQWmQ',
                     client_secret='elnJCI_3YaeBgFnR51kn3OwkVHFV0A',
                     user_agent='SkoodlyDitz')


ftm2 = set()

for submission in reddit.subreddit('ftm').new(limit=500):
    ftm2.add(submission.author)
    display.clear_output()
    print(len(ftm2))

ftm2 = list(ftm2)
    

FTMArray2 = []
FTMUser2 = []
FTMComments2 = []
FTMSubreddit2 = []

ftm2 = set(ftm2) - set(ftm)


for user in ftm2:
    FTMArray2.append(user.name)
    


for user in FTMArray2:
    for comment in reddit.redditor(user).comments.new(limit=1000):
        FTMUser2.append(comment.author.name)
        FTMComments2.append(comment.body)
        FTMSubreddit2.append(comment.subreddit_name_prefixed)


ls


FTMDF2 = pd.DataFrame(list(zip(FTMUser2,FTMSubreddit2,FTMComments2)), columns = ['User','Subreddit','Comments'])



FTMDF2.to_csv('FTMDFN2.csv',index=True, encoding='utf-8')
    














    
mtf2 = set()

for submission in reddit.subreddit('MtF').new(limit=500):
    mtf2.add(submission.author)
    display.clear_output()
    print(len(mtf2))

mtf2 = set(mtf2) - set(mtf)
    

MTFArray2 = []
MTFUser2 = []
MTFComments2 = []
MTFSubreddit2 = []

for user in mtf2:
    MTFArray2.append(user.name)



for user in MTFArray2:
    for comment in reddit.redditor(user).comments.new(limit=1000):
        MTFUser2.append(comment.author.name)
        MTFComments2.append(comment.body)
        MTFSubreddit2.append(comment.subreddit_name_prefixed)
    
MTFDF2 = pd.DataFrame(list(zip(MTFUser2,MTFSubreddit2,MTFComments2)), columns = ['User','Subreddit','Comments'])

MTFDF2.to_csv('MTFDFN2.csv',index=True, encoding='utf-8')

    
    

women = set()

for submission in reddit.subreddit('TwoXChromosomes').new(limit=300):
    women.add(submission.author)
    display.clear_output()
    print(len(women))

women = list(women)
    

WomenArray = []
WomenUser = []
WomenComments = []
WomenSubreddit = []

for user in women:
    WomenArray.append(user.name)
    
    

for user in WomenArray[53:283]:
    for comment in reddit.redditor(user).comments.new(limit=500):
        WomenUser.append(comment.author.name)
        WomenComments.append(comment.body)
        WomenSubreddit.append(comment.subreddit_name_prefixed)


WomenArray = pd.DataFrame(list(zip(WomenUser,WomenSubreddit,WomenComments)), columns = ['User','Subreddit','Comments'])


WomenArray.to_csv('WomenArray.csv',index=True, encoding='utf-8')

WomeanSuck = set(FTMComments)







url1 = "https://www.reddit.com/r/AskMen/comments/uf83cw/what_is_the_most_overrated_dating_advice_given_to/"
url2 = "https://www.reddit.com/r/AskMen/comments/uezfnm/what_can_a_girl_do_to_give_you_an_ick_feeling_and/"
url3 = "https://www.reddit.com/r/AskMen/comments/uf8o8z/what_was_something_you_thought_youd_never_do_but/"



men = set()

submission = reddit.submission(url=url1)

for top_level_comment in submission.comments:
    men.add(top_level_comment.author)

submission = reddit.submission(url=url2)

for top_level_comment in submission.comments:
    men.add(top_level_comment.author)
    
submission = reddit.submission(url=url3)

for top_level_comment in submission.comments:
    men.add(top_level_comment.author)




men = list(men)
    

menArray = []
menUser = []
menComments = []
menSubreddit = []

for user in men:
    menArray.append(user.name)
    


for user in menArray:
    for comment in reddit.redditor(user).comments.new(limit=500):
        menUser.append(comment.author.name)
        menComments.append(comment.body)
        menSubreddit.append(comment.subreddit_name_prefixed)


menArray = pd.DataFrame(list(zip(menUser,menSubreddit,menComments)), columns = ['User','Subreddit','Comments'])


menArray.to_csv('menArray.csv',index=True, encoding='utf-8')