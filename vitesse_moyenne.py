# Calcul de la vitesse moyenne d'un déplacement

# Saisie des données
distance_km = float(input("Entrez la distance parcourue (en km) : "))
temps_min = float(input("Entrez le temps mis (en min) : "))

# 1. Conversion : km -> m et min -> s
distance_m = distance_km * 1000
temps_s = temps_min * 60

print("Distance :", distance_m, "m")
print("Temps :", temps_s, "s")

# 2. Calcul et affichage de la vitesse moyenne en m/s
if temps_s <= 0:
    print("Erreur : le temps doit être strictement positif.")
else:
    vitesse = distance_m / temps_s
    print("Vitesse moyenne :", round(vitesse, 2), "m/s")

    # 3. Message selon la vitesse
    if vitesse > 10:
        print("déplacement rapide")
    else:
        print("déplacement modéré")
