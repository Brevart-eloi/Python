
import IATP3EXO4_fonction
num1 = input("Entrez le premier nombre : ")
num2 = input("Entrez le deuxième nombre : ")
num3 = input("Entrez le troisième nombre : ")
max = IATP3EXO4_fonction.maximum(num1, num2, num3)
print("Le maximum de", num1, ",", num2, ",", num3, "est :", max)


''' 
code pour IATP3 partie web :
function maximum(a, b, c) {
    if (a >= b && a >= c) {
        return a;
    } else if (b >= a && b >= c) {
        return b;
    } else {
        return c;
    }
}
const input1 = document.createElement('input');
const input2 = document.createElement('input');
const input3 = document.createElement('input');
const bouton = document.createElement('button');
input1.id = 'input1';
input2.id = 'input2';
input3.id = 'input3';
bouton.id = 'bouton';
bouton.textContent = "bouton : maximum de 3 nombres";
document.body.appendChild(input1);
document.body.appendChild(input2);
document.body.appendChild(input3);
document.body.appendChild(bouton);
bouton.onclick = () => {
  const num1 = Number(input1.value);
  const num2 = Number(input2.value);
  const num3 = Number(input3.value);
  const max = maximum(num1, num2, num3);
  console.log("Le maximum de", num1, ",", num2, ",", num3, "est :", max);
};
'''
