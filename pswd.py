import random

import string
#print ','.join(random.sample('qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*',10)).replace(',','')
 
#rand = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*"

#password = random.sample(rand,10)

#print(password)

print ','.join(random.SystemRandom().sample(string.ascii_lowercase + string.ascii_uppercase + string.digits + '!@#$%^&*()',10)).replace(',','')
