tab = [] *20
moy = 0
for i in range(20+1):
    tab.append(i)
print(tab)
for i in range(20):
    moy += tab[i]
moy = moy / 20
print("La moyenne est :", moy)

"""
code pour IATP3 partie web :
const tab = [];
let moy = 0;
for (let i = 0; i <= 20; i++) {
    tab.push(i);
}
console.log(tab);
for (let i = 0; i < 20; i++) {
    moy += tab[i];
}
moy = moy / 20;
console.log("La moyenne est :", moy);
"""

