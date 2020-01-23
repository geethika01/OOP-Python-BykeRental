# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:57:42 2020

@author: Geethika.Wijewardena
"""
class Customer:
    def __init__(self, **kwargs):
        self._accNo = kwargs['accNo']
        self._firstName = kwargs['firstName']
        self._surname = kwargs['surname']
        self._dob = kwargs['dob']
       # self._phone = kwargs['phone']
        
    def acc_no(self, accNo = None):
        if accNo == None: 
            return(self._accNo)
        else:
            self._accNo = accNo
            return(self._accNo)
        
    def firstName(self, firstName):
        if firstName: self._firstName= firstName
        return(self._firstName)
        
    def surname(self, surname):
        if surname: self._surname= surname
        return(self._surname)
        
    def dob(self, dob):
        if dob: self._dob = dob
        return(self._dob)
        
    def __str__(self):
        msg = (f'Customer Account No:{self._accNo} \nCustomer Name:{self._firstName} {self._surname} \nDOB: {self._dob}')
        return(msg)
        
        
class BykeRental:
    
    def __init__(self, **kwargs):        
        self._bykeID = kwargs['bykeID'] if 'bykeID' in kwargs else 'BYK0001'
        #self._rentalType = kwargs['rentalType'] if 'rentalType' in kwargs else 'hourly'
        self._numUnits = kwargs['numUnits'] if 'numUnits' in kwargs else 1
        self._customer = kwargs['customerObj'] if 'customerObj' in kwargs else print('Error!! Missing customer')
        self._custAccNo = self._customer.acc_no()
    
    
    def numUnits (self, numofunits ):
        if numofunits: self._numUnits = numofunits 
        return(self._numUnits)
        
    def rentalType (self, newRentalType):
        if newRentalType: self._rentalType = newRentalType
        return (self._rentalType)
    
    def calcHours(self):
        if self._rentalType == 'hourly':
            totalHrs = self._numUnits * 1
        elif self._rentalType == 'daily':
             totalHrs = self._numUnits * 24
        else:
            totalHrs = self._numUnits * 24 * 7
        return(totalHrs)        
        
    
    def calcTotal(self) :
        total = self.calcHours() * self._ratePerHr
        return(total)
            
   
    def __str__ (self):
        msg = (f'Account ID:{self._custAccNo} \nBike ID: {self._bykeID} \nRental Type: {self._rentalType} \nTotal: {self.calcTotal()}')
        return(msg)
        
class BykeRentalWeekly(BykeRental):
    
    def __init__(self, **kwargs):
        self._rentalType = 'weekly'
        self._ratePerHr = 1.00
        #if 'rentalType' in kwargs: del kwargs['rentalType']
        super().__init__(**kwargs)
        
class BykeRentalDaily(BykeRental):
    
    def __init__(self, **kwargs):
        self._rentalType = 'daily'
        self._ratePerHr = 5.00
        #if 'rentalType' in kwargs: del kwargs['rentalType']
        super().__init__(**kwargs)
    
class BykeRentalHourly(BykeRental):
    
    def __init__(self, **kwargs):
        self._rentalType = 'hourly'
        self._ratePerHr = 10.00
        #if 'rentalType' in kwargs: del kwargs['rentalType']
        super().__init__(**kwargs)    
    
        
def main():
    # Create customer Account
    cust1 = Customer(accNo = '000001', firstName = 'Emily', surname = 'Smidth', dob = '12/12/1988')
    print(cust1)
    
    
    # Rent a bike for that customer 
    
    rentalType = "weekly"
    bykeIDInput = 'BYK002'
    numUnitsInput = 2
    #accNoInput = cust1.acc_no()
    
    # create object of the relavent class
    if rentalType == "weekly": bykerental = BykeRentalWeekly(
            bykeID = bykeIDInput , numUnits = numUnitsInput, customerObj = cust1)
    elif rentalType == "daily": bykerental = BykeRentalDaily(
            bykeID = bykeIDInput , numUnits = numUnitsInput, customerObj = cust1)
    else: bykerental = BykeRentalHourly(
            bykeID = bykeIDInput , numUnits = numUnitsInput, customerObj = cust1)
        
    
   # bykerental = BykeRental(bykeID = 'BYK002', rentalType = 'hourly', numUnits = 2, accNo = cust1.acc_no())
    #print(f'Current number of units = {byke1._numUnits}')
   # byke1.numUnits(3)
   # byke1.rentalType('daily')
   # print(f'New number of units = {byke1._numUnits}')
    print(bykerental)
    print('-----------------------------------------------------------------')
    
    cust2 = Customer(accNo = '000002', firstName = 'Jo', surname = 'White', dob = '14/02/1989')
    print(cust2)
    
    rentalType = "hourly"
    bykeIDInput = 'BYK005'
    numUnitsInput = 4
   
    if rentalType == "weekly": bykerental1 = BykeRentalWeekly(
            bykeID = bykeIDInput , numUnits = numUnitsInput, customerObj = cust2)
    elif rentalType == "daily": bykerental1 = BykeRentalDaily(
            bykeID = bykeIDInput , numUnits = numUnitsInput, customerObj = cust2)
    else: bykerental1 = BykeRentalHourly(
            bykeID = bykeIDInput , numUnits = numUnitsInput, customerObj = cust2)
    print(bykerental1)
    print('-----------------------------------------------------------------')
    
    # Extend cust1 for 4 more weeks
    bykerental.numUnits(4)
    print(bykerental)
    
    
if __name__ == '__main__': main()
            