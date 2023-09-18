# paycheck calculator
# Nicholas W
# 20 May 2023

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

userJobs = int(input("How many jobs do you have? "))


for i in range(0, userJobs, 1):
	grossHourly = float(input("What is your hourly pay? "))
	hoursPerWeek = float(input("How many hours a week do you work? "))

	tempGrossWeekly = grossHourly * hoursPerWeek
	tempGrossAnnual = grossHourly * hoursPerWeek * 52

	grossWeekly += tempGrossWeekly
	grossAnnual += tempGrossAnnual

	print("Weekly gross income for job",i+1,":", tempGrossWeekly)
	print("Annual gross income for job",i+1,":", tempGrossAnnual)
	print("-----------------------------------------")


if userJobs > 1 :
	print("Total weekly gross income: ", grossWeekly)
	print("Total annual gross income: ", grossAnnual)


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



