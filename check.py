import sys
sys.path.insert(0, 'instagram-check/lib/python3.9/site-packages')
# adds the igramscraper module to PATH

from igramscraper.instagram import Instagram  # type: ignore 
# imports the Instagram class from the module, allows for usage 
# type: ignore, removes the pylance false error

from time import sleep
# sleep to mimic user latency

instagram = Instagram()

instagram.with_credentials('username', 'password', 'cachepath')
# gets the authentication to allow API calls: username, password, cache path of browser, which i think is optional
instagram.login(force=False, two_step_verificator=False)
# logs in to instagram, force decides between whether to refresh the current session, true is refresh allowed
# two step verification for enabled accounts, if there is two step verification you need to do it via CLI, then you can access

# suggestion: create a feeder account for login purposes, to allow for full security
# note: you need to be following the account under inspection, in case the account is private

sleep(2) 

username = str(input("Enter Username of The Account You Wish to Check: "))
# username for the account under inspection

followerList = []
followingList = []
# declares the list for followers and followings

account = instagram.get_account(username)
# gets the instagram account of the specified user

sleep(1)

followerList = instagram.get_followers(account.identifier, 200, 100, delayed=True) 
# parameters: a/c ID, user limit, page data limit, delay between requests
# get x followers of user, y a time with random delay between requests [in order of occurance]

sleep(1)

followingList = instagram.get_following(account.identifier, 200, 100, delayed=True) 

followings = []
followers = []
# declares the list for comparision

for following in followingList['accounts']:
    followings.append(following.username)
# adds the username of each account you follow into a list

for follower in followerList['accounts']:
    followers.append(follower.username)
# adds the username of each account that follows you into a list

unfollowList = []
followBackList = []
# declares the final list for output

def unfollow():
    for person in followings:
        if person not in followers:
            unfollowList.append(person)
    return unfollowList
# checks who doesn't follow back

def followBack():
    for person in followers:
        if person not in followings:
            followBackList.append(person)
    return followBackList
# checks who you don't follow back

unfollow()
followBack()
# calls the comparision functions

print("People Who Don't Follow Back: ", unfollowList)
print("People Who You Don't Follow Back: ", followBackList)
# outputs the final data