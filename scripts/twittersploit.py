# This script is heavily based upon Justin Seitz's scripts in his
# Learning OSINT course on automatingosint.com

import json
import sys
import pprint
import requests
from keys import oauth, url



# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
#
# Download Tweets from a user profile
#
def intro():
    print "                  (                     (    (   (   (       ) (            "
    print "  *   ) (  (      )\ )  *   )  *   )    )\ ) )\ ))\ ))\ ) ( /( )\ )  *   )  "
    print "` )  /( )\))(   '(()/(` )  /(` )  /((  (()/((()/(()/(()/( )\()|()/(` )  /(  "
    print " ( )(_)|(_)()\ )  /(_))( )(_))( )(_))\  /(_))/(_))(_))(_)|(_)\ /(_))( )(_)) "
    print "(_(_())_(())\_)()(_)) (_(_())(_(_()|(_)(_)) (_))(_))(_))   ((_|_)) (_(_())  "
    print "|_   _|\ \((_)/ /|_ _||_   _||_   _| __| _ \/ __| _ \ |   / _ \_ _||_   _|  "
    print "  | |   \ \/\/ /  | |   | |    | | | _||   /\__ \  _/ |__| (_) | |   | |    "
    print "  |_|    \_/\_/  |___|  |_|    |_| |___|_|_\|___/_| |____|\___/___|  |_|    "
    print " "
    print "\t\tCreated by Joe Gray (@C_3PJoe)"
    print " "

    intro2()

def intro2():
    print " #####                                      "
    print "#     # #####  ###### #####  # #####  ####  "
    print "#       #    # #      #    # #   #   #      "
    print "#       #    # #####  #    # #   #    ####  "
    print "#       #####  #      #    # #   #        # "
    print "#     # #   #  #      #    # #   #   #    # "
    print " #####  #    # ###### #####  #   #    #### "
    print "\n\n"
    print "I would like to thank the following people:"
    print " "
    print "Maddie\t\t@maddiestone"
    print "Justin\t\t@jms_dot_py"
    print "Shubham\t\t@upgoingstar"
    print "Zack\t\t@nvmb3r"
    print "Ben\t\t@bjg"
    print "Caroline\t@cxstephens"
    print "Kyle\t\t@cool_breeze26"
    print "Daniel\t\t@dmfroberson"
    print "Ryan\t\t@mrjester7521"
    print " "

    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8') # This setting is necessary to be able to pipe to a file

    application = raw_input("Continue to the Application? (y/n)\t")
    if application.lower() == str("y") or application.lower() == str("yes"):
        menu1()
    else:
        exit()

def menu1():
    specific = raw_input("Are you targeting a specific twitter handle? (y/n)?\t")
    if specific.lower() == str("y") or specific.lower() == str("yes"):
        menu2()
    elif specific.lower() == str("n") or specific.lower() == str("no"):
        coming_soon()
    else:
        exit()

def menu2():
    sname = raw_input("What target do you wish to evaluate? (OMIT the @ symbol)\t\t")
    screen_name = str(sname.lower())
    ch1 = raw_input("Do you wish to define how many tweets to query? (y/n)\t")
    if ch1.lower() == str('y') or ch1.lower() == str('yes'):
        count = int(raw_input("How many tweets to you want to evaluate? (Maximum: 3200)\t"))
        menu3(screen_name, count)
    else:
        print "Using the default value of 10"
        menu3(screen_name, 10)

def menu3(screen_name, count):
    verbosity = raw_input("Do you desire expanded verbosity\t\t")
    verbosity = str(verbosity.lower())
    if verbosity.lower() == str('y') or verbosity.lower() == str('yes'):
        verbose_main(screen_name, count)
    else:
        simple_main(screen_name, count)

def verbose_download_tweets(screen_name, count):
    api_url = '%s/statuses/user_timeline.json' % url
    params = {
        'screen_name':  screen_name,
        'count':        count,
    }
    # send request to Twitter
    response = requests.get(api_url, params=params, auth=oauth)
    if response.status_code == 200:
        tweets = pprint.pprint(json.loads(response.content))
        return tweets
    return None

def simple_download_tweets(screen_name, count):
    api_url = '%s/statuses/user_timeline.json' % url
    params = {
        'screen_name':  screen_name,
        'count':        count,
    }
    # send request to Twitter
    response = requests.get(api_url, params=params, auth=oauth)
    if response.status_code == 200:
        tweets = json.loads(response.content)
        return tweets
    return None

def simple_main(screen_name, count):
    # get a list of Tweets
    tweet_list = simple_download_tweets(screen_name, count)

    if tweet_list is not None:

        # loop over each Tweet and print the date and text
        for tweet in tweet_list:

            pprint.pprint('%s : %s' % (tweet['created_at'], tweet['text']))
            start_over()

    else:

        print '[*] No Tweets retrieved.'
        start_over()


def verbose_main(screen_name, count):
    # get a list of Tweets
    tweet_list = verbose_download_tweets(screen_name, count)

    if tweet_list is not None:

        # loop over each Tweet and print the date and text
        for tweet in tweet_list:

            pprint.pprint('%s : %s' % (tweet['created_at'], tweet['text']))
            start_over()
    else:

        print '[*] No Tweets retrieved.'
        start_over()

def coming_soon():
    print "This functionality is coming soon"
    exit()

def star_over():
    start_over = raw_input("Start Over?\t(y/n)")
    if start_over.lower() == str('y') or start_over.lower() == str('yes'):
        intro()
    else:
        exit()

intro()
