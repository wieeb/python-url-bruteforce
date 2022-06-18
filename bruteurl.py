import requests
def mostrar_menu():
    url = input("URL: ")
    wordlist = input("Wordlist: ")
    hacer_peticion(url,wordlist)
def hacer_peticion(url,wordlist):
    open_wordlist = open(wordlist,"r")
    for l in open_wordlist:
        response = requests.get(url + "/" + l)   
        print(response)
mostrar_menu()
