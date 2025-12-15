somme = 0
N = int(input("Entrer un nombre entier N : "))
for i in range(N):
    somme += i

print("La somme des nombres de 0 à 0 est :", somme)



"""
code pour IATP3 partie web :
const input = document.createElement('input');
const bouton = document.createElement('button');
input.id = 'input';
bouton.id = 'bouton';
bouton.textContent = "bouton : somme de 0 à N";
document.body.appendChild(input);
document.body.appendChild(bouton);
bouton.onclick = () => {
  const nombre = Number(input.value);
    let somme = 0;
    for (let i = 0; i < nombre; i++) {
        somme += i;
    print("La somme des nombres de 0 à", nombre, "est :", somme);
    }
};
"""