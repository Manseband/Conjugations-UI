import json

PROJECT_TOKEN = 'ta4TO7wT8gFJ'

def newUrl():

    verb = input("Enter name of new verb: ")

    nUrl = 'https://conjugator.reverso.net/conjugation-french-verb-' + str(verb) + '.html\n'

    with open('cahier.csv','a') as f:
        f.write(nUrl)
        f.close

    f = open('var.txt', 'r')
    count = int(f.read()) + 1
    f.close()

    dictionary = {verb:count}

    with open("dict.json", "r+") as file:
        data = json.load(file)
        data.update(dictionary)
        file.seek(0)
        json.dump(data, file)
        file.close()

    f = open('var.txt', 'w')
    f.write(str(count))
    f.close()

    #requests.post('https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/run')
    
newUrl()