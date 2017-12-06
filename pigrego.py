div = 3.0
segno = 1
tot = 0
num = input("Quanti termini vuoi utilizzare: ")

pig=4.0-(4.0/div)
tot=pig;

for i in range(2, num ):
    div=div+2
    segno = -segno
    tot=tot-((4.0/div)*segno)

print ("Approssimato: "), tot
