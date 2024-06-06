import probability_laws as pl

def main():
    while True:
        print("Choisissez la loi de probabilité :")
        print("1. Loi Normale")
        print("2. Loi de Poisson")
        print("3. Loi Binomiale")
        print("4. Loi de Bernoulli")
        print("5. Loi Géométrique")
        print("6. Loi Uniforme Continue")
        print("7. Loi Exponentielle")
        print("8. Quitter")
        
        choice = input("Entrez votre choix (1-8) : ")
        
        if choice == '1':
            mean = float(input("Entrez la moyenne : "))
            stddev = float(input("Entrez l'écart type : "))
            n = int(input("Entrez le nombre de simulations : "))
            data = pl.normal_simulation(mean, stddev, n)
        elif choice == '2':
            lam = float(input("Entrez la valeur de lambda : "))
            n = int(input("Entrez le nombre de simulations : "))
            data = pl.poisson_simulation(lam, n)
        elif choice == '3':
            n_trials = int(input("Entrez le nombre d'essais (n) : "))
            p = float(input("Entrez la probabilité de succès (p) : "))
            n = int(input("Entrez le nombre de simulations : "))
            data = pl.binomial_simulation(n_trials, p, n)
        elif choice == '4':
            p = float(input("Entrez la probabilité de succès (p) : "))
            n = int(input("Entrez le nombre de simulations : "))
            data = pl.bernoulli_simulation(p, n)
        elif choice == '5':
            p = float(input("Entrez la probabilité de succès (p) : "))
            n = int(input("Entrez le nombre de simulations : "))
            data = pl.geometric_simulation(p, n)
        elif choice == '6':
            a = float(input("Entrez la borne inférieure (a) : "))
            b = float(input("Entrez la borne supérieure (b) : "))
            n = int(input("Entrez le nombre de simulations : "))
            data = pl.uniform_simulation(a, b, n)
        elif choice == '7':
            lam = float(input("Entrez la valeur de lambda : "))
            n = int(input("Entrez le nombre de simulations : "))
            data = pl.exponential_simulation(lam, n)
        elif choice == '8':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
            continue
        
        print("Données générées : ", data[:20])  # Affiche les 20 premières valeurs
        print("")

if __name__ == "__main__":
    main()
