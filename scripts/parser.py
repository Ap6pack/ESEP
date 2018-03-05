''' This is a script to apply a regular expression
to parse the information from twitter_pull.py'''
import re
import argparse
import json
import pprint

parser = argparse.ArgumentParser(description='Enter a file name/path.')

def main():
    file = raw_input("Enter a file name or path to parse the file\t\t\t")
    out = raw_input("Enter a file name or path to write to\t\t\t\t")
    filename = open(file, "r")
    intermediate = open("intermediate.txt", "w")
    filename2 = open(out, "w")
    array = []
    array2 = []
    i = 0
    pat = re.compile(r"\w{3}\s(?P<date>\w{3}\s\d{1,2})\s(?P<time>\d\d:\d\d:\d\d)\s\+0000\s\d{4}[^2017]:\s(?P<message>\S.+)")
    tap = re.compile(r"\S.+\@(?P<contacts>\S+)\s\S.+")
    pprint.pprint("[('date', 'time', 'tweet')]")
    pprint.pprint("[mention(s)]")
        
    for l in filename:
        p = pat.findall(l)
        if p:
            print p
            p2 = str(p)
            intermediate.write(p2)
            with open(intermediate, "w") as outfile:
                p3 = json.dump(out, outfile)
                filename2.write(p3)
            t = tap.findall(l)
            if t:
                print t
                t2 = str(t)
                intermediate.write(t2)
                with open(intermediate, "w") as outfile:
                    t3 = json.dump(out, outfile)
                    filename2.write(t3)
        else:
            filename.close()
            filename2.close()            
            exit()

main()
