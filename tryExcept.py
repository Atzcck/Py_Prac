try:
  f = open("demofile.txt", "w")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  

try:
   print("try string")
except:
   print("except string")
else:
   print("else string")

