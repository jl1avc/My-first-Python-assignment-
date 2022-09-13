# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 20:05:24 2022

@author: Jon Leory
My first Python assignment!
"""

def payment(pv, rAPR, nMonths):
    """
    

    Parameters
    ----------
    pv : TYPE = float
        DESCRIPTION. = how much $ I barrow
    rAPR : TYPE = float
        DESCRIPTION. = annual percentage rate
    nMonth : TYPE = int
        DESCRIPTION. = term- Length of the Loan

    Returns
    -------
    Pmt: TYPE = float
        DESCRIPTION. = monthly payment
   

    """
    Pmt =  rAPR/1200*pv/(1-(1+(rAPR/1200))**(-nMonths)) 
    
    return Pmt

#pv = 41000
#pv = 39000
#n = 48
#n = 72
#rAPR = 7

#paymentDollars = payment(float(input('input pv ')),6, 38)
#pv = input("Enter amount to barrow $ ")
#print(pv)

#carPayment = payment(pv, rAPR, n)
#carPayment = payment(41232, 3.5, 36)


#print("my payment is :${:.2f}".format(round(carPayment,2)))
#print("my payment is :${:.2f}".format(carPayment))
#print("my payment is :${:.2f}".format(paymentDollars))

while(1):
    pv = float(input('input pv '))
    if float(pv) == 0:
        break
    #print(pv)
    n = int(input('input number of months '))
    rAPR = float(input('input APR '))
    
    paymentDollars = payment(pv ,rAPR , n)
    print("my payment is :${:.2f}".format(paymentDollars))
print('out of the loop')


#paymentDollars = payment(float(input('input pv ')),6, 38)
#print("my payment is :${:.2f}".format(paymentDollars))
