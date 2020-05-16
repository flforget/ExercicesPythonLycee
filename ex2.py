import math as m

def factorielle(n):
  resultat = 1
  ### Votre code va ici 
  # 
  # Vous devez programmer la fonction qui calcule 
  # la factorielle d'un nombre
  #
  # Pour rappel : factoriel(0) = 1
  #               factoriel(1) = 1
  #               factoriel(2) = 1*2 = 2
  #               factoriel(3) = 1*2*3 = 6 
  #               ...
  ###


  
  ### ne modifiez rien en dessous de cette ligne ###
  return resultat







































def ex2():
  correct = True
  string = ""
  for n in [2,0,5,20,23]:
    if(factorielle(n) == m.factorial(n)):
      string += "CORRECT - "
    else :
      correct = False
      string += "FAUX    - "
    string += "Ta réponse : "+ str(factorielle(n))+ " - " + "Réponse attendue : "+ str(m.factorial(n))
    string += "\n"

  if(correct):
    print("### EXERCICE 2 ### CORRECT")
  else:
    print("### EXERCICE 2 ### FAUX")
  print(string[:-1])
