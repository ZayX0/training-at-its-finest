word = "bottles"

# Create a range from 99 to 1 and loop over it with the iteration variable beer_num
for beer_num in range(99, 0, -1):
    # The print calls for each line of the song
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    # When the loop iteration variable reaches 1 do this if statement
    if beer_num == 1:
        # Print no more bottles
        print("No more bottles of beer on the wall.")
    # If beer_num (iteration variable) does not equal one, do this
    else:
        # Subtract one from the beer number and put it in new variable new_num
        new_num = beer_num - 1
        # If new_num equals one run the below indednted code
        if new_num == 1:
            # Assign the string bottle to the variable 'word'
            word = "bottle"
            # Print new_num variable, word variable, and rest of string
        print(new_num, word, "of beer on the wall.")
    print()
