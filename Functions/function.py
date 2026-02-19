# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalamu alaykum!")
#
# salom_ber()

def salom_ber(name):
    """Foydalanuvchidan ismini qabul qilib,
    unga salom beruvchi funksiya"""
    print(f"Assalamu alaykum, hurmatli {name.title()}!")

salom_ber('muhammadaziz')
salom_ber('muhammadyusuf')

print(salom_ber.__doc__)
print(print.__doc__)
print(max.__doc__)