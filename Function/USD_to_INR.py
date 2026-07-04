# USD to INR converter function
def usd_to_inr(usd_amount):
     conversion_rate = 91
     inr_amount = conversion_rate * usd_amount
     return inr_amount
     
print(usd_to_inr(2))     