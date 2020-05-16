import math as m

def calcul(n):
  x,y,z,a,b = 0,0,0,0,0
  ### Votre code va ici 
  # 
  # Vous devez programmer la fonction qui calcule  :
  # 
  # Soustraire 3 à n et sauvegarder le résultat dans x. 
  # Multiplier x par 2 et sauvegarder le résultat dans y. Ensuite, afficher y
  # Mettre y au carré et sauvegarder le résultat dans z. Ensuite, afficher z
  # Diviser z par 10 et sauvegarder le résultat dans a.
  # Faites la somme de n, x, y, z et a et stockez la dans b
  # 
  ###
  


  ### ne modifiez rien en dessous de cette ligne ###
  return n,x,y,z,a,b




































def ex1():
  input = [2,0,5]
  ans = [
          (2, -1, -2, 4, 0.4, 3.4),
          (0, -3, -6, 36, 3.6, 30.6),
          (5, 2, 4, 16, 1.6, 28.6),
        ]
  correct = True
  string = "                       (n, x, y, z, a, b)                      (n, x, y, z, a, b)\n"
  for i in range(len(input)):
    if(calcul(input[i]) == ans[i]):
      string += "CORRECT - "
    else :
      correct = False
      string += "FAUX    - "
    string += "Ta réponse : "+str(calcul(input[i]))+ \
              " - " \
              "Réponse attendue : "+str(ans[i]) + "\n"

  if(correct):
    print("### EXERCICE 1 ### CORRECT")
  else:
    print("### EXERCICE 1 ### FAUX")
  print(string)
