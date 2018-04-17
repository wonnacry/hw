xa = int(input())
ya = int(input())
xb = int(input())
yb = int(input())
xc = int(input())
yc = int(input())
ab = (xb - xa)**2+(yb-ya)**2
bc = (xb - xc)**2+(yb-yc)**2
ac = (xc - xa)**2+(yc-ya)**2
if ac  == bc + ab :
    print('yes')
elif ac == bc + ac :
    print('yes')
elif ac == bc + ac:
    print('yes')
else:
    print('no')