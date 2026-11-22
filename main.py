import random


print("===❤️ TESTEUR D'AMOUR ❤️===")
print("Attention ! Ce testeur est faux, c'est complètement aléatoire, ce n'est pas ce testeur qui décidera votre amour !")
p1 = input("Quel est ton joli prénom ?")
print("Ok,", p1)
p2 = input("Quel est le joli prénom de ton ou ta crush ?")
print("Ok, ton crush est", p2)


score = random.randint(0, 100)
print(p1, "et", p2, "s'aime à", score, "% !")

if score >= 80:
  print("♥️L'amour pour la vie !")

elif score>= 50:
  print("🤗L'amour ca devient sérieux.")

else:
  print("😭Impossible...")
