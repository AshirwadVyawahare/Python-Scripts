from Games_Pkg import Games 

g1 = Games()
#### Start: Guess number game ####
#g1.guess_number(1,50)
##### End: Guess number game #####

#### Start: Find Temperature ####
#city = input("Enter the name of city: ")
#get_temp = g1.find_temp_city(city)
#print("Temperature of city {} is {}".format(city,get_temp))
##### End: Find Temperature #####

#### Start: Block/Unblock site ####
action = input("Select the action on site (Block/Unblock): ")
while not (action.lower() == "block" or action.lower() == "unblock"):
    action = input("Input was invalid.  Provide input as block or unblock. \n\nSelect the action on site (Block/Unblock): ")

url = input("Enter site excluding \'http://\' : ")
g1.block_unblock_url(action, url)
