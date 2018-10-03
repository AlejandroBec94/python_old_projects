import re





cadena = "hola!!! como estas?"
c=cadena.split()
s="_"
c=s.join(c)
cadena = re.sub("\W", "", c)
print cadena