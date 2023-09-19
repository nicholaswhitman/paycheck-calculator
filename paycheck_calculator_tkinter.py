# paycheck calculator
# Nicholas W
# 20 May 2023

import tkinter as tk
	
def getUserEntry():
	flag.set(True)
	value1 = entry1.get()
	value2 = entry2.get()
	print("Value entered:", value1)
	print("Value entered:", value2)
	return value1, value2

# main application window
root = tk.Tk()

# creates the window size
root.geometry("500x500")
# minimum window size
root.minsize(300, 300)
# Create a BooleanVar variable
flag = tk.BooleanVar()  

label = tk.Label(root, text = "What is your hourly pay? ")
label.pack()
entry1 = tk.Entry(root)
entry1.pack()
label = tk.Label(root, text = "How many hours a week do you work? ")
label.pack()
entry2 = tk.Entry(root)
entry2.pack()

# creating a button and adding it to the window
button = tk.Button(root, text="Calculate", command = getUserEntry )
button.pack()

# Wait for the flag to become True
root.wait_variable(flag)  


value1, value2 = getUserEntry()
grossHourly = float(value1)
hoursPerWeek = float(value2)


medicare = .0145 					# 1.45%
socialSecurity = .062 				# 6.2%
FICA = medicare + socialSecurity	# 7.65%
taxBracket1 = .10 					# 10%
taxBracket2 = .12 					# 12%
taxBracket3 = .22                   # 22%
taxBracket4 = .24                   # 24%
taxBracket5 = .32                   # 32%
taxBracket6 = .35                   # 35%
taxBracket7 = .37                   # 37% 

#impliment State and city taxes \\ last implimentation
grossWeekly = grossAnnual = 0.0

tempGrossWeekly = grossHourly * hoursPerWeek
tempGrossAnnual = grossHourly * hoursPerWeek * 52

grossWeekly += tempGrossWeekly
grossAnnual += tempGrossAnnual

print("Weekly gross income: ", grossWeekly)
print("Annual gross income: ", grossAnnual)

if grossAnnual <= 11000:
	temp = grossAnnual * (FICA + taxBracket1)
	netAnnual = grossAnnual - temp
	netWeekly = netAnnual/52
	print("Weekly net income: ", netWeekly)
	print("Annual net income: ", netAnnual)
	print("tax bracket 1")
	pass

elif 11001 <= grossAnnual <=  44725:
	temp = grossAnnual * FICA
	temp2 = (grossAnnual - 11000) * taxBracket2
	netAnnual = grossAnnual - (temp + temp2 + 1100)
	netWeekly = netAnnual/52
	print("Weekly net income: ", netWeekly)
	print("Annual net income: ", netAnnual)
	print("tax bracket 2")
	pass

elif 44756 <= grossAnnual <=  95375:
	temp = grossAnnual * FICA
	temp2 = (grossAnnual - 44725) * taxBracket3
	netAnnual = grossAnnual - (temp + temp2 + 5127)
	netWeekly = netAnnual/52
	print("Weekly net income: ", netWeekly)
	print("Annual net income: ", netAnnual)
	print("tax bracket 3")
	pass

elif 95376 <= grossAnnual <=  182100:
	temp = grossAnnual * FICA
	temp2 = (grossAnnual - 95375) * taxBracket4
	netAnnual = grossAnnual - (temp + temp2 + 16290)
	netWeekly = netAnnual/52
	print("Weekly net income: ", netWeekly)
	print("Annual net income: ", netAnnual)
	print("tax bracket 4")
	pass

elif 182101 <= grossAnnual <=  231250:
	temp = grossAnnual * FICA
	temp2 = (grossAnnual - 182100) * taxBracket5
	netAnnual = grossAnnual - (temp + temp2 + 37104)
	netWeekly = netAnnual/52
	print("Weekly net income: ", netWeekly)
	print("Annual net income: ", netAnnual)
	print("tax bracket 5")
	pass

elif 231251 <= grossAnnual <=  578125:
	temp = grossAnnual * FICA
	temp2 = (grossAnnual - 231250) * taxBracket6
	netAnnual = grossAnnual - (temp + temp2 + 52832)
	netWeekly = netAnnual/52
	print("Weekly net income: ", netWeekly)
	print("Annual net income: ", netAnnual)
	print("tax bracket 6")
	pass

elif 578125 <= grossAnnual:
	temp = grossAnnual * FICA
	temp2 = grossAnnual * taxBracket7
	netAnnual = (grossAnnual - 578125) - (temp + temp2 + 174238.25)
	netWeekly = netAnnual/52
	print("Weekly net income: ", netWeekly)
	print("Annual net income: ", netAnnual)
	print("tax bracket 7")
	pass

else: 
	print("Error")

print("Does not incorporate state and city taxes. ")


# start the main event loop
root.mainloop()