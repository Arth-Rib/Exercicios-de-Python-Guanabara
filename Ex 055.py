map = 0
mep = 0
for c in range(1, 6):
    p = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        map = p
        mep = p
    else:
        if p > map:
            map = p
        if p < mep:
            mep = p
print('O maoir peso é {} e o menor peso é {}.'.format(map, mep))
