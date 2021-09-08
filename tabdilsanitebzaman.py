

sani = int(input(" saniye ra vared konid: "))

saat = sani // 3600
b=sani-3600*saat
min = sani % 60
sec = b-sani*min

print ( saat , ":" , min, ":", sec) 



