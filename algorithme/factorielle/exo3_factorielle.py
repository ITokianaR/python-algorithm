n = int(input("Saisir un nombre : "))
if (n == 0) :
    F = 1
    print(n, "!=", F)
elif (n < 0) :
    print("Erreur")
    F = "impossible"
else :
    F = 1
    for m in range (1, n+1) :
        F = F*m
print("La factorielle de",n,"est",F)