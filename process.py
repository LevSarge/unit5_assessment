#We are going to be opening "um-server-01.txt" file and save it into the variable 'log_file'
log_file = open("um-server-01.txt")

#Function named 'sales_reports' is declared and 'log_file' will be passed into it as an argument
def sales_reports(log_file):
    #Running a for-in loop for 'log_file' as the function combs through the text
    for line in log_file:
        #Each line will be looped through and have its trailing characters removed with the '.rstrip' method
        line = line.rstrip()
        #accessing the list, we're going to slice, or accessing a specific range using the colon operator starting at the beginning and stopping at third specified day
        day = line[0:3]
        #using an "if" statement, if the text matches the day (Tuesday), the lines in the file will be printed
        if day == "Mon":
            print(line)

#Calling the 'sales_reports' function while passing 'log_file' in as an argument
sales_reports(log_file)
