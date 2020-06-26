
''' Sample URL = http://receipts.cmdrf.kerala.gov.in/index.php/Settings/PrintReceipt/B2SF36VWtW4NZwzXvblkFAeKCnyqD.Em5j8Xwr0Mw1n6pyM83yKh7S8OnJHXq1~JwSj94fS~fGHen4BwFYkpjQ__/cEh6lXh0fPPWg3bMgGzu2OmTqgWVgSpJE0ujFZ2VPwqJCIoLlG12wc2Pfr1rL884K0PwtL5flm~o.gITF05QJQ__/Rs~X.pjt7V1.1xnuC~Oob66atga6hI3lLDv1DGHcqnu~ih5vtTBve8YYConqWPf8Vbn58dtmxQa5eoOALGSz5w__/U9vIP81W1C3GRHjM0f3hEixLoO6naGjQ6hN~LiB2ekRhU4es85pcpkX.Kk6fTou3NZh3QfBaEewVI.CBmaT4sQ__/h1oosj.sVlrmXr8cotfTBUEzWl4Qb.1SBLUlXQNDHgSwrm6VjG42pxAOWs2Bj.RUhPPy8ojuD.KHRNLlEILm9A__/am8okCAt08j2har.qKlvvEH1HWy.S0OQeALeTzdaagm3aWtF3aRx4D4z2pWQEIhO7OQGmFwuT9cTHO9VI8crtg__/VN4PL63~dHjmpd2CubUH6ki9sbyFHM5KnLJCNXRxl1WODZuK1mUq2i6yxRyg1bAC0.5GzZ1mR2rUlkRm7I6KHw__/1'''


import itertools, string
'''
comb_list = itertools.permutations(['a-zA-Z0-9'])

for i in list(comb_list):
    print(i)

'''


# try 2

import itertools
res = itertools.combinations( string.ascii_letters + string.digits , 8) # 3 is the length of your result.
words = open(r'E:\words.txt','w')
for i in res:
    a = ''.join(i)
    print(a)
    words.write(a+'\n')
words.close()
 
