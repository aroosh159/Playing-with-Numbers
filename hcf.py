numberLargest = int(input("Enter you highest number"))
numbersmallest = int(input("Enter you smallest number"))
while numbersmallest:
    numberStore= numbersmallest
    numbersmallest = numberLargest % numbersmallest
    numberLargest = numberStore

print("HCF IS:", numberLargest)