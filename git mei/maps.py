import webbrowser as link
digita_citta = print('digita la città che vuoi visitare')
citta = input()
URL = ('https://www.google.com/maps/place/'+(citta)+'/@'+ '4')
link.open(URL)