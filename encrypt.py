# Importe le module EnigmaMachine depuis enigma.machine
from enigma.machine import EnigmaMachine

# Demande les valeurs des rotors à l'utilisateur
rotinput=input("Quelles sont les valeurs des rotors ? (exemple : IV I V)\n")

# Boucle, pour les rotors, pour que l'utilisateur entre forcément une valeur 
while rotinput == "":
    rotinput=input("Entrez impérativement la postition des rotors !!!\n")

# Demande les position des anneaux à l'utilisateur
ringinput=input("Quelles sont les valeurs des anneaux ? (exemple : 20 5 10)\n")

# Boucle, pour les anneaux, pour que l'utilisateur entre forcément une valeur
while rotinput == "":
    rotinput=input("Entrez impérativement les valeurs des anneaux !!!\n")

# Demande les 10 pairs du tableau de connexion à l'utilisateur
plugboardinput=input("Quelles sont les 10 paires du tableau de connexion ?\nSi vous ne mettez rien, ces paramètres seront utilisés : SX KU QP VN JG TC LA WM OB ZF\n")

# Si l'utilisateur n'entre aucune paires, le programme utilise ceux de base
if plugboardinput == "":
    plugboardinput == "SX KU QP VN JG TC LA WM OB ZF"

# Mise en place de la machine Enigma
machine = EnigmaMachine.from_key_sheet(
    rotors=(rotinput),
    reflector='B',
    ring_settings=[int(n) for n in ringinput.split()], # Converti "string" (entrée utilisateur) en "int"
    plugboard_settings=(plugboardinput))

# Demande a l'utilisateur la position initale des rotors
displayinput=input("Quelle est la position initale des rotors ? (exemple FNZ)\n")

# Boucle, pour la position initale des rotors,
# pour que l'utilisateur entre forcément une valeur
while displayinput == "":
    displayinput=input("Entrez impérativement la postition initiale des rotors !!!\n")

# Mise en place de la position initiale des rotors
machine.set_display(displayinput)

# Encrypte le texte 'BFR' et l'enregistre dans une clé : msg_key
cle = input('Quelle clé souhaitez-vous pour encrypter le texte ?\n')
msg_key = machine.process_text(cle)
print(f"La clé de message est : {msg_key}")

# Réinitialise la position initiale des rotors avec la clé du message
machine.set_display(msg_key)

# Converti le texte de l'utilisateur et affiche le résultat
# après être converti en ciphertext
plaintext = input('Quel mot souhaitez-vous encrypter ?\n')
ciphertext = machine.process_text(plaintext)
print(f'Voici le texte codé : {ciphertext}')

# Message de fin du programme
print("Merci d'avoir utilisé notre programme !")