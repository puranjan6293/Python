"""
grocery=["Bhendi","sabji","Rice","Dall",94]
print(grocery[3])

#output is Dall

numbers=[1,2,4,6,8,9,10]
#print(numbers)

#output is [1,2,4,6,8,,9,10]

numbers.sort()
numbers.reverse()
print(numbers)

#output is [10,9,8,6,4,2,1]


#advance lists slicing

numbers=[2,7,9,11,3]
print(numbers[::])

#defult parameters that is [0:length:1]

numbers=[2,7,9,11,3]
numbers.insert(3,90)
print(numbers)

#output is [2,7,9,90,11,3]

numbers=[2,7,9,11,3]
numbers.append(100)
print(numbers)
#output is [2,7,9,11,3,100]
#100 will added in the end

numbers=[2,7,9,11,3]
numbers.pop()
print(numbers)

#output is [2,7,9,11,3]
#it will leave one number from the last

numbers=[2,7,9,11,3]
numbers.reverse()
print(numbers)

#the output is [3,11,9,7,2]
#it just reverse the list


#Tapple function

tp=(1,3,5,6)
tp[1]=10
print(tp)

#output is ERROR
#we cant interchange tapple function


numbers=[2,7,9,11,3]
numbers[1]=25
print(numbers)

#output is [2,25,9,11,3]
#it will just interchange the 1st position in the list with 25


numbers=[2,7,9,11,3]
numbers.clear()
print(numbers)
#output is []
#it will just clear everything


numbers=[2,7,9,11,3]
numbers.copy()
print(numbers)
#the output is [2,7,9,11,3]
#it will just copy everything

numbers=[2,7,9,11,3]
numbers.remove(2)
print(numbers)
#output is [7,9,11,3]
#it will just remove the 2 from the list

"""
numbers=[2,7,9,11,3]
numbers.pop(3)
print(numbers)
#output is [2,7,9,3]
#it will just remove the 3rd plce from this list



