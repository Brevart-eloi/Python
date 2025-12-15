a = int(input("entrer un nombre : "))
b = int(input("entrer un deuxième nombre : "))
print("La somme est :", a + b)

'''
code pour IATP2 partie web : 
const input1 = document.createElement('input');
const input2 = document.createElement('input');
const bouton = document.createElement('button');

input1.id = 'input1';
input2.id = 'input2';
bouton.id = 'boutonAddition';
bouton.textContent = "Additionner";

document.body.appendChild(input1);
document.body.appendChild(input2);
document.body.appendChild(bouton);

bouton.onclick = () => {
  const valeur1 = Number(input1.value);
  const valeur2 = Number(input2.value);
  const addition = valeur1 + valeur2;
  console.log("Résultat de la somme des valeurs :", addition);
};


'''