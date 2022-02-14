import webbrowser as link
digita_via = print ('digita qui sotto la via')
nome_via = input('inserisci il nome della via')
numero_civico = input('inserisci il numero civico')
URL = ('https://www.google.com/maps/place/'+'Via'+'_'+(nome_via)+'_'+(numero_civico)+'/@'+ '4')
link.open(URL)