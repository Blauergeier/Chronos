import json
import argparse

debug = True

def save_in_file(data, filename):
    save_file = open(filename, 'w+')
    save_file.write(json.dumps(data))
    save_file.close()
    return

def read_save_file(filename):
    try:
        save_file = open(filename,'r')
        dictionary = json.loads(save_file.read())
        save_file.close()
    except IOError:
        dictionary = {}
    return dictionary

#TODO: add Logger
def custom_print(text):
    if debug:
        print text
    return

print "[#] Welcome to Chronos!"
custom_print("[*] Reading from storage.")

names = read_save_file('names.txt')
time = read_save_file('time.txt')


#handle commandline input
parser = argparse.ArgumentParser(description="You can add or remove tasks or time as well as display your current status.")
parser.add_argument('-d', '--display', action="store_true", help="This option displays your current status.")
parser.add_argument('-a', '--add', action="store_true", help="Starts the menu for adding tasks")
parser.add_argument('-r', "--remove", action="store_true", help="Starts the process of deleting tasks")
args = parser.parse_args()

if args.display:
    print json.dumps(names)
    print json.dumps(time)

elif args.add:
    display_name = raw_input("[!] Please specify the full name of the task: ")
    handle = raw_input("[!] Please specify a short handle for the task: ")

    names[handle] = display_name
    time[handle] = 0
    print "[#] Task was added!"

elif args.remove:
    user_input = raw_input("[!] Please input the full name or handle of the tasks you want to delete: ")
    for e in names:
        #TODO: Improve code
        if e == user_input:
            del names[e]
            del time[e]
            break
        elif names[e] == user_input:
            del time[e]
            del names[e]
            break
    print "[#] Task was removed!"

#TODO: add options for adding and removing tasks as well as time

custom_print("[*] Saving.")
save_in_file(names, "names.txt")
save_in_file(time, "time.txt")

print "[#] Goodbye!"
