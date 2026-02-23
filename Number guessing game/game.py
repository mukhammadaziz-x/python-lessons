import random as r

from django.db.models.expressions import result

print("Keling o'ylagan sonni topish o'ynaymiz!")
def son_top(x):
    son = r.randint(1, x)
    return son
tax_son = son_top(10)

while True:
    son = int(input("1 dan 10 gacha son o'yladim. Topa olasizmi?:\n>>"))
    for urunish in range(10):
        urunish += 1
        if son == tax_son:
            print(f"TOPDINGIZ! {tax_son} sonini o'ylagan edim. {urunish} ta tahmin bilan topdingiz. Tabriklayman!")
            break
        elif tax_son > son:
            son = int(input(f"Xato, men o'ylagan son bundan kattaroq. Yana xarakat qiling:\n>>"))
        else:
            son = int(input(f"Xato, men o'ylagan son bundan kichikroq. Yana xarakat qiling:\n>>"))
    print(f"1 dan 10 gacha son o'ylang. Men topishga xarakat qilaman.")
    for pc_urunish in range(10):
        pc_urunish += 1
        son = int(input("Son o'ylagan bo'lsangiz istalgan tugmani bosing:\n>>"))
        pc_son = input(f"Siz {tax_son} sonini o'yladingiz: to'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)??\n>>")
        if pc_son == '-':
            pc_son = input(f"Siz {tax_son-1} sonini o'yladingiz: to'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)??\n>>")
            continue
        if pc_son == '+':
            pc_son = input(f"Siz {tax_son+1} sonini o'yladingiz: to'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)??\n>>")
            continue
        if pc_son == 't':
            print(f"Soningizni {pc_urunish} urunish bilan topdim!")
            break
    result = input("Yana o'ynaymizmi: ha(1) / yo'q (0): ")
    if result != 'ha':
        break





