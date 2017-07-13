x = "there are %d types of people." % 10
binary = "binary"
not_binary = "don't"
y = "those who know %s and those who %s" %(binary,not_binary)

print x
print y

print "i said %s ." %x
print "i also said %s." %y


hilarious = False
joke = "Isn't that joke so funny? %r"

print joke % hilarious

w = "this is left side of..... "
e = "of this string "

print w+e