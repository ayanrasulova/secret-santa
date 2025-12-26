import random
import os # saves to folder

# include all the names of who will be in this current secret santa
names = ["name1", "name2", "name3", "name4", "name5"]

prev_pairings = { 
"""include who each santa has already given a gift to """
# format: { "santa": {"person_who_recieved_gift_already", "another_person_who_already_got_a_gift"}, .... }
                "name1": {"name2", "name3"},
                "name2": {"name3", "name4"},
                "name3": {"name4", "name5"},
                "name4": {"name5", "name1"},
                "name5": {"name1", "name2"}
                }

new_pairings = {}
reciever = []


def assign_for_each(): # run for each santa
    for i in range(len(names)):
        assigner(i)

def assigner(i):

    name = names[i]
    random_assignment = random.randint(0, 8)
    while random_assignment == i: # cant be own santa
        random_assignment = random.randint(0, 8)
    
    if (names[random_assignment] not in reciever): # plus cant give gift to someone who already has a santa
        if name not in prev_pairings:
            new_pairings[name] = names[random_assignment]
            reciever.append(names[random_assignment])  # add as reciever
        
        elif name in prev_pairings:
            if names[random_assignment] not in prev_pairings[name]:  # if prev year reciever of that name isn't the new reciever 
                new_pairings[name] = names[random_assignment]
                reciever.append(names[random_assignment]) # add as reciever
        
    if name not in new_pairings: # recursively run again if santa not assigned
        assigner(i) 

def run():
    new_pairings.clear() # clears list to restart
    reciever.clear()
    assign_for_each()

def write_to_file(): 
    """saves a .txt file for each santa with their pairing inside! """ 
    directory = "Documents/secret-santa" # update with your directory!

    for santa, receiver in new_pairings.items(): # returns dict items as tuple
        path = os.path.join(directory, f"{santa}.txt") # directory + individual document name

        with open(path, "w", encoding="utf-8") as file:
            file.write(receiver)

def main():
    while True:
        try: 
            run()
            print((new_pairings))
            write_to_file()
            break # if successful... break 
        except RecursionError:
            continue # redo the loop

main()