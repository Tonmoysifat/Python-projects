print()
print()
print()
print()
print()
print()
import time
print("                                                    Welcome to INFOAPP")
time.sleep(3)
print()
print()
print()
print()
while(1):
  def getdate():
    import datetime
    return datetime.datetime.now().strftime("%c")
  print("  Press-1 for add or 2 for retrieve")
  d=int(input("   "))
  def add_retrieve(d):
    if d==1:
      z=input(" Enter file name:")
      a=input(" Enter customar name:")
      b=input(" Enter Date of birth(d.m.y):")
      c=input(" Enter phone number:")
      e=input(" Enter address:")
      g=input(" Enter product type:")
      h=input(" Enter number of product:")
      j=input(" Enter amount:")
      i=input(" Enter payment status:")
      f=open(z,"a")
      f.write("[")
      f.write(str(getdate()))
      f.write("]")
      f.write("\n")
      f.write("\n")
      f.write(" Customar info... ")
      f.write("\n")
      f.write("  Name:")
      f.write(a)
      f.write("\n")
      f.write("  DOB:")
      f.write(b)
      f.write("\n")
      f.write("  Phone:")
      f.write(c)
      f.write("\n")
      f.write("  Address:")
      f.write(e)
      f.write("\n")
      f.write("\n")
      f.write(" Product info... ")
      f.write("\n")
      f.write("  Product type:")
      f.write(g)
      f.write("\n")
      f.write("  NPS:")
      f.write(h)
      f.write("\n")
      f.write("\n")
      f.write("        Total paid amount:")
      f.write(j)
      f.write("        Payment status:")
      f.write(i)
      f.write("\n")
      f.write("\n")
      print("Successfully added")
      f.close()
    elif d==2:
      z=input("Enter file name:")
      print()
      f=open(z)
      print(f.read())
      f.close()
  add_retrieve(d)
  input()
        
