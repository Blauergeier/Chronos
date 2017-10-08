import json

def save(data):
    save_file = open('data.txt', 'w+')
    save_file.write(json.dumps(data))
    save_file.close()
    return

def read_save_file():
    save_file = open('data.txt','r')
    dictionary = json.loads(save_file.read())
    save_file.close()
    return dictionary

def clear_stash():
    stash.clear()
    return

def add_subject(key):
    stash[key] = 0
    return

print "[*] Reading from storage."
stash = read_save_file()

print json.dumps(stash)

raw_input("")


print "[*] Saving."
save(stash)
