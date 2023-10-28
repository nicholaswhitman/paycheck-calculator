# paycheck calculator
# Nicholas W
# 20 May 2023


def main():

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

	quit = False

	while quit == False:

		grossWeekly = grossAnnual = 0.0
		userJobs = int(input("How many jobs do you have? "))
	
		for i in range(0, userJobs, 1):
			grossHourly   = float(input("What is your hourly pay? "))
			hoursPerWeek  = float(input("How many hours a week do you work? "))
			hoursOvertime =  float(input("How many overtime hours? "))
			overtime = (grossHourly * 1.5) * hoursOvertime

			tempGrossWeekly = grossHourly * hoursPerWeek + overtime
			tempGrossAnnual = ((grossHourly * hoursPerWeek) + overtime) * 52 

			grossWeekly += tempGrossWeekly
			grossAnnual += tempGrossAnnual 

			print("Weekly gross income for job",i+1, f": {tempGrossWeekly:,}")
			print("Annual gross income for job",i+1, f": {tempGrossAnnual:,}")
			print("-----------------------------------------")

		if userJobs > 1:
			print(f"Total weekly gross income: {grossWeekly:,}")
			print(f"Total annual gross income: {grossAnnual:,}")

		if grossAnnual <= 11000:
			temp = grossAnnual * (FICA + taxBracket1)
			netAnnual = grossAnnual - temp
			netWeekly = netAnnual/52

			output(userJobs, netWeekly, netAnnual)
			print("Tax bracket 1")

		elif 11001 <= grossAnnual <=  44725:
			temp = grossAnnual * FICA
			temp2 = (grossAnnual - 11000) * taxBracket2
			netAnnual = grossAnnual - (temp + temp2 + 1100)
			netWeekly = netAnnual/52

			output(userJobs, netWeekly, netAnnual)
			print("Tax bracket 2")	

		elif 44756 <= grossAnnual <=  95375:
			temp = grossAnnual * FICA
			temp2 = (grossAnnual - 44725) * taxBracket3
			netAnnual = grossAnnual - (temp + temp2 + 5127)
			netWeekly = netAnnual/52

			output(userJobs, netWeekly, netAnnual)
			print("Tax bracket 3")	

		elif 95376 <= grossAnnual <=  182100:
			temp = grossAnnual * FICA
			temp2 = (grossAnnual - 95375) * taxBracket4
			netAnnual = grossAnnual - (temp + temp2 + 16290)
			netWeekly = netAnnual/52

			output(userJobs, netWeekly, netAnnual)
			print("Tax bracket 4")

		elif 182101 <= grossAnnual <=  231250:
			temp = grossAnnual * FICA
			temp2 = (grossAnnual - 182100) * taxBracket5
			netAnnual = grossAnnual - (temp + temp2 + 37104)
			netWeekly = netAnnual/52

			output(userJobs, netWeekly, netAnnual)
			print("Tax bracket 5")

		elif 231251 <= grossAnnual <=  578125:
			temp = grossAnnual * FICA
			temp2 = (grossAnnual - 231250) * taxBracket6
			netAnnual = grossAnnual - (temp + temp2 + 52832)
			netWeekly = netAnnual/52

			output(userJobs, netWeekly, netAnnual)
			print("Tax bracket 6")

		elif 578125 <= grossAnnual:
			temp = grossAnnual * FICA
			temp2 = grossAnnual * taxBracket7
			netAnnual = (grossAnnual - 578125) - (temp + temp2 + 174238.25)
			netWeekly = netAnnual/52

			output(userJobs, netWeekly, netAnnual)
			print("Tax bracket 7")

		else: 
			print("Error ")

		print("Does not incorporate state and city taxes. ")

		# end condition for while loop
		userInput = input("Do you want to quit? ").strip().lower()
		if userInput == 'no' or userInput == 'n':
			print("-----------------------------------------")
			quit = False
		else: 
			print("Now exiting.")
			quit = True	




#print function that puts commas 
def output(userJobs, netWeekly, netAnnual):
	if userJobs == 1:
		print(f"Weekly net income: {netWeekly:,}")
		print(f"Annual net income: {netAnnual:,}")
	else: 
		print(f"Total Weekly net income:  {netWeekly:,}")
		print(f"Total Annual net income:  {netAnnual:,}")



main()