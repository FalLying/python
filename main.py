l=input()
x = l.split(' ')

fl=int(x[0])
fw=int(x[1])

alph=['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if (fl*26 < fw) or (fl > fw) or (fl <= 0) or (fw <= 0):
  print('impossible')
else:
  word = ''
  i = 0

  while (i == 0):
    mod = (fw % fl)
    
    if mod == 0:
      mult = fl
      t = int(fw/fl)
    else:
      mult = fl-mod
      t=int(fw/fl)

    j = 0
    while (j < mult):
        word+=alph[t]
        j+=1

    fw-=(t*mult)
    fl-=mult

    if (fw <= 0):
      i = 1
  print(word)

