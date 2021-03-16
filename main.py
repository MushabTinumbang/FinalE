from wrds import ctg1, ctg2, wr, tr, ta
x = int(input())
lst = []
st = ""
ch = []
chb = []
chbmax = 0
chm = []
chmmax = 0
pp = 0
tl = 0
am = 0
end = 0
if x >= 1 and x <= 50:
  for p in range (x+1):
    if p < x:
      y = input().split(",")
      lst.append(y)
    else : 
      ctg = input().upper()
      print("\n")
      if not ctg == ctg1 and not ctg == ctg2:
        print(wr)
        end = 1
  if end == 0 :
    for xx in range (0,x):
      for m in range(0,3):
        ch.append(lst[xx][m])
    for p in range (0, x*3):
      if ch[p] == ctg1 :
        chb.append(int(p/3))
      if ch[p] == ctg2 :
        chm.append(int(p/3))
    for xp in range (0,len(chb)):
      chbmax = chb[xp]
    for xy in range (0,len(chm)):
      chmmax = chm[xy]
    for yx in range(0,x):
      if ctg == ctg1:
        if lst[yx][0] == ctg1:
          for z in range(0,3):
            if z<2:
              st += lst[yx][z] + " "
            elif yx == chbmax and z==2:
              st += lst[yx][z] + " "
              tl +=1
              am += int(lst[yx][2])
            elif z==2:
              st += lst[yx][z] + " "
              st += "\n"
              tl += 1
              am += int(lst[yx][2])
      else:
        if lst[yx][0] == ctg2:  
          for z in range(0,3):
            if z<2:
              st += lst[yx][z] + " "
            elif yx == chmmax and z==2:
              st += lst[yx][z] + " "
              tl +=1
              am += int(lst[yx][2])
            else :
              st += lst[yx][z] + " "
              st += "\n"  
              tl += 1
              am += int(lst[yx][2])  
    print(st)
    print(f"{tr}{tl}")
    print(f"{ta}{am}")