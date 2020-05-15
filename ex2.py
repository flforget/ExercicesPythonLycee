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
  

  return resultat










































def ex2():
  for n in [2,0,5,20,23]:
    if(factorielle(n) == m.factorial(n)):
      string = "Correct - "
    else :
      string = "Faux    - "
    string += "Ta réponse : "+str(factorielle(n))+ \
              " - " \
              "Réponse attendue : "+str(m.factorial(n))
    print(string)