from datetime import datetime
from journal_data import journal_data
import time

# Function to add a journal entry
def add_journal():
    # Request input from the user
    while True:
        title = input("Enter journal title: ")
        if title:
            break
        else:
            print("Title cannot be empty. Please enter as instructed.")

    while True:
        content = input("Enter journal content: ")
        if content:
            break
        else:
            print("Content cannot be empty. Please enter as instructed.")

    while True:
        date_input = input("Enter journal date (format: DD-MM-YYYY, e.g., 20-04-2024): ")
        try:
            # Convert input date to datetime object
            date = datetime.strptime(date_input, '%d-%m-%Y')
            break
        except ValueError:
            print("Invalid date format. Please enter the date in the correct format.")

    while True:
        location = input("Enter location visited: ")
        if location:
            break
        else:
            print("Location cannot be empty. Please enter as instructed.")

    # Create a new journal entry
    new_journal_entry = {
        "title": title,
        "content": content,
        "date": date.strftime('%d-%m-%Y'),  # Convert date to the desired format
        "location": location
    }

    # Add the new journal entry to the list
    journal_data.append(new_journal_entry)

    # Confirmation message
    print("New journal entry has been added!")

def show_searched_journal_details(journal):
    print(f"Title: {journal['title']}")
    print(f"Content: {journal['content']}")
    print(f"Date: {journal['date']}")
    print("-" * 155)
    time.sleep(3)

# Function to search for a journal
def search_journal():
    
    # Request keyword from the user
    while True:
        keyword = input("Enter search keyword: ")
        if keyword:
            break
        else:
            print("Keyword cannot be empty. Please enter as instructed.")

    # Search for journals that match the keyword
    found_journals = []
    for journal in journal_data:
        if keyword.lower() in journal["title"].lower() or keyword.lower() in journal["content"].lower():
            found_journals.append(journal)

    # Display the titles of the found journals
    if found_journals:
        print("Found journals:")
        for idx, journal in enumerate(found_journals):
            print(f"{idx + 1}. {journal['title']}")
        
        # Request the journal number from the user to display details
        while True:
            journal_number_str = input("Enter the journal number to display details (0 to go back): ")
            if journal_number_str:
                try:
                    journal_number = int(journal_number_str)
                    break
                except ValueError:
                    print("Journal number must be integer! Please enter as instructed.")
            else:
                print("Journal number cannot be empty. Please enter as instructed.")

        if journal_number != 0 and 1 <= journal_number <= len(found_journals):
            show_searched_journal_details(found_journals[journal_number - 1])
    else:
        print("Journal not found.")

# Function to display journal titles
def show_journal_titles():
    # Check if there is journal data
    if not journal_data:
        print("No journal data.")
        return

    # Display journal titles
    print("\nJournal Titles:")
    for idx, journal in enumerate(journal_data):
        print(f"{idx + 1}. {journal['title']}")

# Function to display journal details by title
def show_journal_details():
    # Request journal number from the user
    while True:
        journal_number_str = input("Enter the journal number to display details: ")
        if journal_number_str:
            try:
                journal_number = int(journal_number_str)
                break
            except ValueError:
                print("Journal number must be integer! Please enter as instructed.")
        else:
            print("Journal number cannot be empty. Please enter as instructed.")

    # Check if the journal number is valid
    if journal_number < 1 or journal_number > len(journal_data):
        print("Invalid journal number.")
        return

    # Display journal details
    journal = journal_data[journal_number - 1]
    print(f"Title: {journal['title']}")
    print(f"Content: {journal['content']}")
    print(f"Date: {journal['date']}")
    print(f"Location: {journal['location']}")
    print("-" * 155)
    time.sleep(2)

# Add filter and sort menu to the main menu
def show_journal():
    # Display journal titles
    show_journal_titles()

    while True:
        choice = input("Enter 0 to go back or 1 to view journal details: ")
        if choice == "0":
            return
        elif choice == "1":
            show_journal_details()
            time.sleep(3)
        else:
            print("Please input as instructed.")

# Function to edit journal entry
def edit_journal():
    # Display journal titles
    show_journal_titles()

    # Request journal number from the user
    while True:
        journal_number_str = input("Enter the journal number to edit: ")
        if journal_number_str:
            try:
                journal_number = int(journal_number_str)
                break
            except ValueError:
                print("Journal number must be integer! Please enter as instructed.")
        else:
            print("Journal number cannot be empty. Please enter as instructed.")

    

    # Check if the journal number is valid
    if journal_number < 1 or journal_number > len(journal_data):
        print("Invalid journal number.")
        return

    # Retrieve the journal data to be edited
    old_journal = journal_data[journal_number - 1]

    # Initialize variables to store new values
    new_title = old_journal["title"]
    new_content = old_journal["content"]
    new_date = old_journal["date"]
    new_location = old_journal["location"]

    # Display options to edit title, content, or date
    print("Options for editing:")
    print("1. Journal Title")
    print("2. Journal Content")
    print("3. Journal Date")
    print("4. Journal Location")

    edit_choice = input("Enter the option number: ")

    # Check the edit choice
    if edit_choice == "1":
        new_title = input(f"Edit journal title ({old_journal['title']}): ") or old_journal["title"]
    elif edit_choice == "2":
        new_content = input(f"Edit journal content ({old_journal['content']}): ") or old_journal["content"]
    elif edit_choice == "3":
        # Request a valid date input
        while True:
            date_input = input(f"Edit journal date ({old_journal['date']}, format: DD-MM-YYYY, e.g., 20-04-2024): ")
            try:
                # Convert input date to datetime object
                new_date = datetime.strptime(date_input, '%d-%m-%Y').strftime('%d-%m-%Y')
                break
            except ValueError:
                print("Invalid date format. Please enter the date in the correct format.")
    elif edit_choice == "4":
        new_location = input(f"Edit location visited ({old_journal['location']}, Format: City, Country, e.g., Batam, Indonesia): ") or old_journal["location"]
    else:
        print("Invalid choice.")
        return

    # Update journal data
    journal_data[journal_number - 1] = {
        "title": new_title,
        "content": new_content,
        "date": new_date,
        "location": new_location
    }

    # Confirmation message
    print("Journal has been edited!")

# Function to delete journal entry
def delete_journal():
    # Display journal titles
    show_journal_titles()

    # Request journal number from the user
    while True:
        journal_number_str = input("Enter the journal number to delete: ")
        if journal_number_str:
            try:
                journal_number = int(journal_number_str)
                break
            except ValueError:
                print("Journal number must be integer! Please enter as instructed.")
        else:
            print("Journal number cannot be empty. Please enter as instructed.")

    # Check if the journal number is valid
    if journal_number < 1 or journal_number > len(journal_data):
        print("Invalid journal number.")
        return

    # Delete journal data
    del journal_data[journal_number - 1]

    # Confirmation message
    print("Journal has been deleted!")

# Function to sort journals by date
def sort_journals_by_date():
    journal_data.sort(key=lambda x: datetime.strptime(x['date'], '%d-%m-%Y'))

# Function to filter journals by year
def filter_journals_by_year():
    # Request year from the user
    while True:
        year_input = input("Enter the year to filter journals (format: YYYY): ")
        try:
            year = datetime.strptime(year_input, '%Y').year
            break
        except ValueError:
            print("Invalid year format. Please enter the year in the correct format.")

    # Filter journals by year
    filtered_journals = [journal for journal in journal_data if datetime.strptime(journal['date'], '%d-%m-%Y').year == year]

    # Display filtered journals
    if filtered_journals:
        print(f"Journals for the year {year}:")
        for idx, journal in enumerate(filtered_journals):
            print(f"{idx + 1}. {journal['title']}")
            show_searched_journal_details(journal)
    else:
        print(f"No journals for the year {year}.")

def filter_journals_by_year_range():
    # Request year range from the user
    while True:
        start_year_input = input("Enter the start year (format: YYYY): ")
        end_year_input = input("Enter the end year (format: YYYY): ")
        try:
            start_year = datetime.strptime(start_year_input, '%Y').year
            end_year = datetime.strptime(end_year_input, '%Y').year
            break
        except ValueError:
            print("Invalid year format. Please enter the year in the correct format.")

    # Filter journals by year range
    filtered_journals = [journal for journal in journal_data if start_year <= datetime.strptime(journal['date'], '%d-%m-%Y').year <= end_year]

    # Display filtered journals
    if filtered_journals:
        print(f"Journals within the year range {start_year}-{end_year}:")
        for idx, journal in enumerate(filtered_journals):
            print(f"{idx + 1}. {journal['title']}")
            # Display journal details
            show_searched_journal_details(journal)
    else:
        print(f"No journals within the year range {start_year}-{end_year}.")

def calculate_travel_summary():
    travel_summary = {}

    # Hitung statistik perjalanan pertahun
    for journal in journal_data:
        year = datetime.strptime(journal['date'], '%d-%m-%Y').year
        location = journal["location"]
        if year not in travel_summary:
            travel_summary[year] = {"destinations": {}}
        if location not in travel_summary[year]["destinations"]:
            travel_summary[year]["destinations"][location] = []
        travel_summary[year]["destinations"][location].append(journal['date'])
        # print(travel_summary)

    return travel_summary

def print_travel_summary():
    travel_summary = calculate_travel_summary()
    # print(travel_summary)
    summary_text = "\nTravel Summary:\n"
    for year, data in sorted(travel_summary.items()):
        summary_text += f"\nin {year}:\n"
        idx = 1
        for location, dates in (data['destinations'].items()):
            date_info = ', '.join(dates)
            # print(data)
            summary_text += f"{idx}. {location} ({date_info})\n"
            idx += 1
            
    print(summary_text)

# Filter and sort menu
def additional_menu():
    
    while True:
        print("\nAdditional Menu:")
        print("1. Search Journal with Keywords")
        print("2. Sort Journals by Date")
        print("3. Filter Journals by Year")
        print("4. Filter Journals by Year Range")
        print("5. Travel Summary")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            search_journal()
        elif choice == "2":
            sort_journals_by_date()
            print("Journals have been sorted by date.")
            show_journal()
        elif choice == "3":
            filter_journals_by_year()
        elif choice == "4":
            filter_journals_by_year_range()
        elif choice == "5":
            print_travel_summary()
        elif choice == "6":
            return
        else:
            print("Invalid choice.")

# Main menu
while True:
    print("\nTravel Journal Menu")
    print("1. Add Journal")
    print("2. Show Journal")
    print("3. Edit Journal")
    print("4. Delete Journal")
    print("5. Additional Features")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_journal()
    elif choice == "2":
        show_journal()
    elif choice == "3":
        edit_journal()
    elif choice == "4":
        delete_journal()
    elif choice == "5":
        additional_menu()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")

# Farewell message
print("\nThank you for using the Travel Journal app!")