# My own sum function as rename summa()
def summa(*sonlar):
    """Kiritilgan sonlarni yig'indisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

print(summa(40, 20, 40))