import datetime

# Function to get yes or no input from user
def get_yes_no_input(question):
    while True:
        answer = input(question + " (Y/N)").strip().lower()
        if answer == "y" or answer == "yes":
            return True
        elif answer == "n" or answer == "no":
            return False
        else:
            print("Invalid input. Please enter Y or N.")

# Open file for writing
with open("dream_journal.txt", "a") as f:

    # Get current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Ask if user remembers any dreams from last night
    if get_yes_no_input("Do you remember any dreams you had from last night?"):
        
        # Ask remaining questions
        who = input("Who was in the dream? ").strip()
        locations = input("Which locations did you visit or see in the dream? ").strip()
        about = input("What was the dream about? ").strip()
        sounds = input("What did you hear during the dream? ").strip()
        feelings = input("How did the dream make you feel? ").strip()
        
        # Ask if any of the dreams were lucid dreams
        lucid = get_yes_no_input("Were any of the dreams lucid dreams?")
        
        # Write entry to file
        f.write(f"{current_date}\nDream:\nWho: {who}\nLocations: {locations}\nWhat was the dream about: {about}\nSounds: {sounds}\nFeelings: {feelings}\nLucid: {lucid}\n\n")
        
    else:
        # Write entry to file if no dreams were remembered
        f.write(f"{current_date}\nNo dreams\n\n")
