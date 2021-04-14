import random
import requests
import bs4

class Games:

    def __init__(self):
        #initialization
        a=0

    def guess_number(self, min_range, max_range):
        #range = (1,max_range)
        n = random.randint(min_range, max_range)
        print("This is number guessing game.  User has 6 chances to guess the number. \nAfter each wrong guess, user looses the 20 points")
        count = 5
        bool_guess = bool(0)
        points = 100
        pt_val = {5:100, 4:80, 3:60, 2:40, 1:20, 0:0}

        try:
            guess = int(input("Enter an integer from {} to {}: ".format(min_range, max_range)))
            if guess < min_range or guess > max_range:
        	    raise ValueError("Invalid number is entered.  Please enter input in the range 1 to 199")

            while count > 0:
                if guess < n:
                    print ("guess is low")
                    guess = int(input("Enter an integer from {} to {}: ".format(min_range, max_range)))
                    if guess < min_range or guess > max_range:
	                    raise ValueError("Invalid number is entered.  Please enter input in the range 1 to 199")
                elif guess > n:
                    print ("guess is high")
                    guess = int(input("Enter an integer from {} to {}: ".format(min_range, max_range)))
                    if guess < min_range or guess > max_range:
	                    raise ValueError("Invalid number is entered.  Please enter input in the range 1 to 199")
                else:
                    print ("you guessed it!")
                    bool_guess = bool(10)
                    break
                count-=1

            if bool_guess:
                print("You earned ", pt_val[count],  " points")
            else:
                print("The number was : ", n)
                print("You earned ", pt_val[count], " points and lost the game")
        except ValueError as ve:
            print(ve)
        except:
            print("Invalid input")


    def find_temp_city(self, city):
        url = "https://www.google.com/search?q=temperature+in+"+city
        
        #Get request to read current temperature
        result = requests.get(url)
        
        #Read HTTP data from the google page
        http_data = bs4.BeautifulSoup(result.text,"html.parser")
        #print(http_data)

        #Read temperature
        temp = http_data.find( "div" , class_='BNeawe' ).text
        #print(temp)
        return temp


    def block_unblock_url(self, action, url):
        #host_file = r"C:\Windows\System32\drivers\etc\hosts"
        host_file = r"C:\Users\Dell\Desktop\Axis_Debit_card.txt"
        redirected_to = "127.0.0.1"

        with open(host_file,"r+") as file_handle:
            try:
                host_lines = file_handle.readlines()
                file_handle.seek(0)
                content = file_handle.read()
                
				if action.lower() == 'block':
                    #Write url
                    if url in content:
                        print("Website is already blocked")
                    else:
                        file_handle.write(redirected_to +"    "+ url +"\n")
                elif action.lower() == 'unblock':
                    if url in content:
                        #Remove url
                        file_handle.seek(0)
                        for line in host_lines:
                            if not url in line:
                                file_handle.write(line)
                        file_handle.truncate()
                    else:
                        print("Website was not blocked")
            except EOFError as eof:
                print(eof)
            except FileNotFoundError as fnf:
                print(fnf)
            finally:
                #close opened files   
                file_handle.close()   