"""
Created on Mon Dec  8 15:45:41 2025

@author: Raphael Jaydrek, CY/L4
"""

"""
Dictionary made to store all the available items in the shop.
The shop has 4 categories the user can select, with each category having 5 items.
"""
ShopItems = {
"Weapons" : 
    {
    "1A":("Steel Sword",10),
    "1B":("Steel Spear",12),
    "1C":("Longbow",15),
    "1D":("Slingshot",7),
    "1E":("Glock 19",100)
    },
"Armor":
    {
    "2A":("Padded Armor",12),
    "2B":("Leather/Hide Armor",17),
    "2C":("Chainmail Armor",22),
    "2D":("Plate Armor",27),
    "2E":("Forbidden Armor",40)
    },
"Miscellaneous Items" : 
    {
    "3A":("Health Potion",7),
    "3B":("Mana Potion",7),
    "3C":("Recall Potion",7),
    "3D":("A pack of Beef Jerky",5),
    "3E":("A bundle of Torches",5)
    },
"Materials" : 
    {
    "4A":("Slime Gel",1),
    "4B":("Ancient Cloth",2),
    "4C":("Feather",2),
    "4D":("Black Lens",5),
    "4E":("Bezoar",10)
    }
}

TotalItems = [] #Stores the items the user selects to be displayed later.

def ShowCategories(): #Displays every category inside the shop.
    print("\n□====== OUR CATEGORIES ======□\n")
    for num, Category in enumerate(ShopItems.keys(), start=1):
        print(f"{num}. {Category}")
    print("\n□============================□")

def ShowItems(Category): #Displays items that belong to the user-selected category.
    print(f"\n□========== OUR SELECTION OF {Category.upper()} ==========□\n")
    for num, (item, price) in ShopItems[Category].items():
        print(f"{num}. {item} - {price}g")
    print("\n□==============================================□")
    
def UsersItems(TotalGold): #Shows the user all their selected items alongside the total amount.
    print("\n□========== YOUR CART ==========□\n")
    for num, (item, price) in enumerate(TotalItems, start=1):
        print(f"{num}. {item} - {price}g")
    print(f"\nYour total is: {TotalGold}g")
    print("\n□===============================□")

def TheTravellingMerchant():
    TotalGold = 0 #The total amount of all the users items
    GoldOwed = 0 #The amount the user needs to pay
    Phase = 1 #The main function is split into 4 phases, they'll be explained at their corresponding phase number.
    
    while True:
        while Phase == 1: #This is the 1st phase. The user is asked to choose among the displayed categories.
            ShowCategories()
            try:
                print("Please choose something from our given categories!")
                ChosenCategory=int(input("Type in a number from 1 - 4 (Choices displayed on the side): "))
                if ChosenCategory == 0: #A makeshift fix because frankly I want to finish this already. It works though.
                    print("We don't have that category here.")
                    Phase = 1 #Keeps this on Phase 1.
                else:
                    Shop2List = list(ShopItems.keys()) #Converts the users choice into a list so that the chosen category can be indexed and called properly.
                    Category = Shop2List[ChosenCategory - 1] #Converts this list into its own variable so that it can be referenced by the dictionary.
                    Phase = 2 #Switches to Phase 2.
            except KeyboardInterrupt: #You'll be seeing this a lot, so I'll comment on this once. Basically ends the process.
                Phase = 4
                break
            except: #Shows up when the user types in something that isn't shown. This is also something you'll see a lot.
                print("We don't have that category here.")
                
        while Phase == 2: #This is the 2nd phase. It's the same process as the 1st but the user selects an item instead.
            ShowItems(Category)
            try:
                print("Please choose an item on this list!")
                ItemNumber=str(input(f"Type in a code number displayed from {ChosenCategory}A - {ChosenCategory}E (Choices displayed on the side.): ").upper())
                item, price = ShopItems[Category][ItemNumber] #Stores the users selected item into two separate variables that'll be stored into a list for future referencing.
                print(f"\nYou have selected: {ItemNumber}. {item} - {price}g")
                TotalItems.append((item,price)) #Stores both item and price variables into their own tuple then adds it inside the list.
                TotalGold += price #Adds the price of the users item onto their total.
                Phase = 3 #Switches to Phase 3.
            except KeyboardInterrupt:
                Phase = 4
                break
            except:
                print("We don't have that item on our list.")
        
        while Phase == 3: #This is the 3rd and final phase. It is the checkout/refund phase, by far the most complicated of the three.
            try:
                UsersItems(TotalGold) #Displays all the items the user has in their cart (Also shows the user their updated cart after they remove an item.)
                print("Would you like to buy another item or would you like to take an item off your cart?")
                print("1. Continue Buying. \n2. Take an item off your cart. \n3. Pay.")
                UserConfirmation = input("Type in a number from 1 - 3 (Choices displayed on the side): ")
                if UserConfirmation == "3": #If the user enters 'N', they'll be asked to pay.
                    while GoldOwed < TotalGold: #This loop persists until the user has paid/overpaid the amount needed.
                        try:
                            Gold = int(input(f"Your total is {TotalGold}g (You've given {GoldOwed}g so far...): ")) #Shows the total and how much they've paid so far.
                            if Gold <= 0: #Happens if the user tries to give 0 or a negative number of gold.
                                print("Please give me something of value.\n")
                                continue 
                            GoldOwed += Gold #Adds the gold entered into the amount the user needs to pay.
                        except ValueError: #Triggers when the user tries to type in something that isn't a number (floats don't work either)...
                            print("You can't pay with that. Please give me something actually valid.!\n")
                            continue
               
                    GoldOwed -= TotalGold #Subtracts the total from the amount the user paid.
                    ItemList = [x[0] for x in TotalItems] #Converts all the items in the list into a str (Tuple -> String).
                    ItemListStr = ", ".join(ItemList) #Allows all the items in the list to be automatically listed with a comma inbetween without any of the brackets on the end and start.
    
                    if len(ItemListStr) == 0: #Happens if the users cart has no items inside.
                        print("\nGiving... Nothing? What a waste of time! Buy something next time!")
                        Phase = 4
                        break
                    else: #Should happen mostly.
                        print(f"\nGiving {ItemListStr}...") #Prints out a list of all the items the user bought.
    
                    if GoldOwed == 0: #Happens if the money the user gave out is exact with the price.
                        print("\nThanks for the business! \nStay safe out there!")
                        Phase = 4
                        break
                    else: #Happens if the user has change left over from the purchase. It shows the extra change you gave and gives it back.
                        print(f"\nThanks for the business! \nBut you gave me a little extra change, so I'm giving it back. It should be {GoldOwed}g. \nStay safe out there!")
                        Phase = 4
                        break
    
                elif UserConfirmation == "2": #If the user enters 'Q', they'll be asked to remove something.
                    if len(TotalItems) == 0: #Happens if there isn't anything in the users cart.
                        print("You don't have anything in your cart to remove!")
                        continue
                    try:
                        print("\nSelect an item to remove from your cart!")
                        Remove=int(input("Type in the number related to the item you want to remove: "))
                        TotalGold -= TotalItems[Remove - 1][1] #Removes the price associated with that item.
                        TotalItems.pop(Remove - 1) #Removes the item that the user selected.
                    except: #Triggers if the user enters something unrelated to their cart.
                        print("Hey! That isn't in your cart!\n")
                
                elif UserConfirmation == "1": #Resets the whole process again, back to Phase 1.
                    Phase = 1
                
                else:
                    print("Please answer me properly!")
            except KeyboardInterrupt:
                Phase = 4
                break
        
        if Phase == 4: #Phase 4 is only here to end the process, either when the user is finished or wants to quit midway.
            break
        
# Runs our "vending machine" function. It doesn't look like a vending machine app but trust me, it works like one.
if __name__ == "__main__":
    TheTravellingMerchant()