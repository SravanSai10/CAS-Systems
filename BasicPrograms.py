exp = "111 + 4809"

line = "-"*10
space = " "
zero = "0"

def padd(l2):
    global zero
    #print(l2)
    if int(l2[0]) < int(l2[1]):
        temp = l2[0]
        l2[0] = l2[1]
        l2[1] = temp
    else: pass

    if len(l2[0]) != len(l2[1]):
        diff = (len(l2[0]) - len(l2[1]))
        if diff < 0:
            space_add = zero*abs(diff)
            l2[0] = space_add + l2[0]
        else:
            l2[1] = zero*diff + l2[1]

    print(l2)


def typeCheck(l2):
    #print(type(l2))
    list_elements = [str(x) for x in list(range(0,10))]

    for i in range(len(l2)):
        #print(type(l2[i]))
        if l2[i] not in list_elements:
            print("l2 is not a number!")
            break;
        else: continue

def cleanData(exp):
    l1 = []
    exp = exp.split("+")
    for element in exp:
        element = element.strip()
        typeCheck(element)
        l1.append(element)
    padd(l1)
    return l1

class Operations:

    @classmethod
    def addition(self,num1,num2):
        global line
        global space
        carry = "0"
        add = ""
        for i in range(num1.length):
            add_val = str(num1.integer[-1-i]+num2.integer[-1-i]+int(carry[-1-i]))
            if len(add_val) == 1:
                add = (add_val) + add
                carry = ('0') + carry
            else:
                print(add_val)
                add_val = add_val[1:]
                add = (add_val) + add
                carry = ('1') + carry
            print("{}\n{}\n{}\n{}\n{}\n".format(space*(10-len(carry))+carry,
                                            space*(10-num1.length)+num1.string,
                                            space*(10-num1.length)+num2.string,line,
                                            space*(10-len(add))+add))


    @classmethod
    def subtraction(self,num1,num2):
        global line
        global space
        carry = ""
        sub = ""
        for i in [((-1)*x-1) for x in range(num1.length)]:
            if num1.integer[i] < num2.integer[i]:
                if num1.integer[i] != 0:
                    diff = num1.integer[i]*10 - num2.integer[i]
                else:
                    diff = 10 - num2.integer[i]
                num1.integer[i-1] -= 1
                carry = "1" + carry
                sub = str(diff) + sub
            else:
                diff = num1.integer[i] - num2.integer[i]
                carry = "0" + carry
                sub = str(diff) + sub
            print("{}\n{}\n{}\n{}\n{}\n".format(space*(10-len(carry))+carry,
                                                space*(10-num1.length)+num1.string,
                                                space*(10-num1.length)+num2.string,line,
                                                space*(10-len(sub))+sub))

    @classmethod
    def multiplication(self,num1,num2):
        product = ""
        add_list = []
        for j in [((-1)*x-1) for x in range(num2.length)]:
            mul = 0
            product = "0"*(-j-1)
            for i in [((-1)*x-1) for x in range(num1.length)]:
                mul = str(num1.integer[i]*num2.integer[j])
                product = mul + product

            add_list.append(product)

        print(add_list)






class Numbers(Operations):
    def __init__(self,value):
        Operations.__init__(self)
        self.length = len(value)
        self.string = value
        self.integer = [int(x) for x in value]

expression = cleanData(exp)

expression1 = Numbers(expression[0])
expression2 = Numbers(expression[1])

##print(expression1.integer)
##print(type(expression1.integer))
##
##print(expression2.string)
##print(type(expression2.string))

Operations.addition(expression1,expression2)
print("----next----")
Operations.subtraction(expression1,expression2)
print("----next----")
Operations.multiplication(expression1,expression2)
