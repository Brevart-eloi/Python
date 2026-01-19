
import IATP3EXO4_fonction
num1 = 10
num2 = 25
num3 = 15
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

const num1 = 10;
const num2 = 25;
const num3 = 15;
const max = maximum(num1, num2, num3);
console.log("Le maximum de", num1, ",", num2, "et", num3, "est :", max);
'''
