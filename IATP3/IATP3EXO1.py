nombre = int(input("entrer un nombre entier : "))
if (nombre % 2) == 0:
    print("Le nombre ", nombre, "est pair")
else:
    print("Le nombre ",nombre, "est impair")


'''
code pour IATP3 partie web :
const input = document.createElement('input');
const bouton = document.createElement('button');
input.id = 'input';
bouton.id = 'bouton';
bouton.textContent = "bouton : pair ou impair";
document.body.appendChild(input);
document.body.appendChild(bouton);
bouton.onclick = () => {
  const nombre = Number(input.value);
  if ((nombre % 2) == 0) {
    console.log("Le nombre ", nombre, "est pair");
  } else {
    console.log("Le nombre ", nombre, "est impair");
  }
};
'''