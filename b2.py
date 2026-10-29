def ar_pvn(cena, likme=21):
    return cena * (1 + likme /100)

print(ar_pvn(100))
print(ar_pvn(100, 12))
