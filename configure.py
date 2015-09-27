import json, time

config = {'firstname': '', 
          'lastname': '',
          'ainame': '',
          'zip': ''
          }

# Creates the config file that holds information needed in later computations
# holds data including the ai's name, the user's name and the user's zip code

def createConfig():
    ainame = raw_input('Please enter the name for your personal assistant: ')
    check = 'n'
    while(check.lower() != 'y'):
        firstname = raw_input('Please enter your first name: ')
        check = raw_input('Is ' + firstname + ' right? (y/n):')
    check = 'n'
    while(check.lower() != 'y'):
        lastname = raw_input('Please enter your last name: ')
        check = raw_input('Is ' + lastname + ' right? (y/n):')
    zipcode = raw_input('Please enter your 5-digit zip code: ')

    if(len(zipcode) != 5):
        zipcode = raw_input('Please enter your 5-digit zip code: ')

    print('configuring...')
    time.sleep(1)
    print('done!')

    # input values into json file
    config['ainame'] = ainame
    config['firstname'] = firstname
    config['lastname'] = lastname
    config['zip'] = zipcode

    # write to the the config json
    with open('config.json', 'w') as f:
        json.dump(config, f)

def getConfigEntry(entry):
    # read the config json
    with open('config.json', 'r') as f:
        config = json.load(f)

    #edit the data
    return config[entry]

def setConfigEntry(entry, value):
    # read the config json
    with open('config.json', 'r') as f:
        config = json.load(f)

    #edit the data
    config[entry] = value

    #write it back to the file
    with open('config.json', 'w') as f:
        json.dump(config, f)

createConfig()
