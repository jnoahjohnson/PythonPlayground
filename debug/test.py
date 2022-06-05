# Ashley Denison, Noelia Root, Dave Shipley, Sam Jensen
# import random in order to generate random integers below
import random
class Order() :
    def __init__(self) :
        # calls randomBurgers() method to get burger count
        self.burger_count = self.randomBurgers()
    def randomBurgers(self) :
        # gets an integer 1-20
        return random.randint(1,20)
class Person ():
    def __init__(self) :
        # calls randomName() method to generate customer name
        self.customer_name = self.randomName()
    def randomName(self) :
        # given list of random names
        asCustomers = ["Jefe", "El Guapo", "Lucky Day",
                    "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman",
                    "Carmen", "Invisible Swordsman", "Singing Bush"]
        # generates a random number that will reference index of name list
        randNum = random.randint(0,8)
        # returns a random name from the list
        return asCustomers[randNum]

class Customer(Person) :
    def __init__(self):
        super().__init__()
        self.order = Order()
# Queue that will recieve items of type Customer
# Represents customer line
custQueue = []
# Dictionary for holding customer info
# Keys = strings
# Values = integers
custDict = {}
for lineNum in range(0,100) :
    oCustomer = Customer()
    # Create customer object and append it to the list
    custQueue.append(oCustomer)
    # is the person in dictionary?
    # if yes, increase count
    print(oCustomer.customer_name)
    if oCustomer.customer_name in custDict :
        custDict[oCustomer.customer_name] = custDict[oCustomer.customer_name] + oCustomer.order.burger_count
    # if not, add them to the dictionary
    else :
        custDict[oCustomer.customer_name] = oCustomer.order.burger_count

listSortedCustomers = sorted(custDict.items(), key = lambda x: x[1], reverse=True)

# print(listSortedCustomers)

for iCount in range(0,len(listSortedCustomers) - 1) :
    customer = listSortedCustomers[iCount]
    customerName = customer[0]
    print(customer[1])
    print(customer.ljust(19) + str(listSortedCustomers[iCount+1]) + "\n")
    iCount += 1


for customer in listSortedCustomers:
    print(customer[0] + ' ate ' + str(customer[1]))