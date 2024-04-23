from datetime import datetime
from journal_data import journal_data
import time

def input_with_message(message):
    while True:
        user_input = input(message)
        if user_input:
            return user_input
        else:
            print("Input cannot be empty. Please enter as instructed.")

def input_integer_with_message(message):
    while True:
        user_input = input_with_message(message)
        try:
            return int(user_input)
        except ValueError:
            print("Input must be an integer! Please enter as instructed.")

def input_valid_date(message):
    while True:
        date_input = input_with_message(message)
        try:
            return datetime.strptime(date_input, '%d-%m-%Y')
        except ValueError:
            print("Invalid date format. Please enter the date in the correct format.")

def add_journal():
    title = input_with_message("Enter journal title: ")
    content = input_with_message("Enter journal content: ")
    date = input_valid_date("Enter journal date (format: DD-MM-YYYY, e.g., 20-04-2024): ")
    location = input_with_message("Enter location visited: ")

    new_journal_entry = {
        "title": title,
        "content": content,
        "date": date.strftime('%d-%m-%Y'),
        "location": location
    }

    journal_data.append(new_journal_entry)
    print("New journal entry has been added!")

def display_journal_details(journal):
    print(f"Title: {journal['title']}")
    print(f"Content: {journal['content']}")
    print(f"Date: {journal['date']}")
    print("-" * 155)
    time.sleep(3)

def search_journal():
    keyword = input_with_message("Enter search keyword: ")
    found_journals = []

    for journal in journal_data:
        if keyword.lower() in journal["title"].lower() or keyword.lower() in journal["content"].lower() or keyword.lower() in journal["date"].lower() or keyword.lower() in journal["location"].lower():
            found_journals.append(journal)

    if found_journals:
        print("Found journals:")
        for idx, journal in enumerate(found_journals):
            print(f"{idx + 1}. {journal['title']}")

        journal_number = input_integer_with_message("Enter the journal number to display details (0 to go back): ")

        if journal_number != 0 and 1 <= journal_number <= len(found_journals):
            display_journal_details(found_journals[journal_number - 1])
    else:
        print("Journal not found.")

def show_journal_titles():
    if not journal_data:
        print("No journal data.")
        return

    print("\nJournal Titles:")
    for idx, journal in enumerate(journal_data):
        print(f"{idx + 1}. {journal['title']}")

def show_journal_details():
    journal_number = input_integer_with_message("Enter the journal number to display details: ")

    if journal_number < 1 or journal_number > len(journal_data):
        print("Invalid journal number.")
        return

    display_journal_details(journal_data[journal_number - 1])

def show_journal():
    show_journal_titles()

    choice = input_with_message("Enter 0 to go back or 1 to view journal details: ")
    if choice == "1":
        show_journal_details()

def edit_journal():
    show_journal_titles()
    journal_number = input_integer_with_message("Enter the journal number to edit: ")

    if journal_number < 1 or journal_number > len(journal_data):
        print("Invalid journal number.")
        return

    old_journal = journal_data[journal_number - 1]
    new_title = old_journal["title"]
    new_content = old_journal["content"]
    new_date = old_journal["date"]
    new_location = old_journal["location"]

    print("Options for editing:")
    print("1. Journal Title")
    print("2. Journal Content")
    print("3. Journal Date")
    print("4. Journal Location")

    edit_choice = input_with_message("Enter the option number: ")

    if edit_choice == "1":
        new_title = input_with_message(f"Edit journal title ({old_journal['title']}): ") or old_journal["title"]
    elif edit_choice == "2":
        new_content = input_with_message(f"Edit journal content ({old_journal['content']}): ") or old_journal["content"]
    elif edit_choice == "3":
        new_date = input_valid_date(f"Edit journal date ({old_journal['date']}, format: DD-MM-YYYY, e.g., 20-04-2024): ").strftime('%d-%m-%Y')
    elif edit_choice == "4":
        new_location = input_with_message(f"Edit location visited ({old_journal['location']}, Format: City, Country, e.g., Batam, Indonesia): ") or old_journal["location"]
    else:
        print("Invalid choice.")
        return

    journal_data[journal_number - 1] = {
        "title": new_title,
        "content": new_content,
        "date": new_date,
        "location": new_location
    }

    print("Journal has been edited!")

def delete_journal():
    show_journal_titles()
    journal_number = input_integer_with_message("Enter the journal number to delete: ")

    if journal_number < 1 or journal_number > len(journal_data):
        print("Invalid journal number.")
        return

    del journal_data[journal_number - 1]
    print("Journal has been deleted!")

def sort_journals_by_date():
    journal_data.sort(key=lambda x: datetime.strptime(x['date'], '%d-%m-%Y'))
    print("Journals have been sorted by date.")

def filter_journals_by_year():
    year = input_valid_date("Enter the year to filter journals (format: YYYY): ").year
    filtered_journals = [journal for journal in journal_data if datetime.strptime(journal['date'], '%d-%m-%Y').year == year]

    if filtered_journals:
        print(f"Journals for the year {year}:")
        for idx, journal in enumerate(filtered_journals):
            print(f"{idx + 1}. {journal['title']}")
            display_journal_details(journal)
    else:
        print(f"No journals for the year {year}.")

def filter_journals_by_year_range():
    start_year = input_valid_date("Enter the start year (format: YYYY): ").year
    end_year = input_valid_date("Enter the end year (format: YYYY): ").year
    filtered_journals = [journal for journal in journal_data if start_year <= datetime.strptime(journal['date'], '%d-%m-%Y').year <= end_year]

    if filtered_journals:
        print(f"Journals within the year range {start_year}-{end_year}:")
        for idx, journal in enumerate(filtered_journals):
            print(f"{idx + 1}. {journal['title']}")
            display_journal_details(journal)
    else:
        print(f"No journals within the year range {start_year}-{end_year}.")

def calculate_travel_summary():
    travel_summary = {}

    for journal in journal_data:
        year = datetime.strptime(journal['date'], '%d-%m-%Y').year
        location = journal["location"]
        if year not in travel_summary:
            travel_summary[year] = {"destinations": {}}
        if location not in travel_summary[year]["destinations"]:
            travel_summary[year]["destinations"][location] = []
        travel_summary[year]["destinations"][location].append(journal['date'])

    return travel_summary

def print_travel_summary():
    travel_summary = calculate_travel_summary()
    summary_text = "\nTravel Summary:\n"
    for year, data in sorted(travel_summary.items()):
        summary_text += f"\nin {year}:\n"
        idx = 1
        for location, dates in (data['destinations'].items()):
            date_info = ', '.join(dates)
            summary_text += f"{idx}. {location} ({date_info})\n"
            idx += 1

    print(summary_text)

def additional_menu():
    while True:
        print("\nAdditional Menu:")
        print("1. Search Journal with Keywords")
        print("2. Sort Journals by Date")
        print("3. Filter Journals by Year")
        print("4. Filter Journals by Year Range")
        print("5. Travel Summary")
        print("6. Back to Main Menu")

        choice = input_with_message("Enter your choice: ")

        if choice == "1":
            search_journal()
        elif choice == "2":
            sort_journals_by_date()
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

while True:
    print("\nTravel Journal Menu")
    print("1. Add Journal")
    print("2. Show Journal")
    print("3. Edit Journal")
    print("4. Delete Journal")
    print("5. Additional Features")
    print("6. Exit")

    choice = input_with_message("Enter your choice: ")

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

print("\nThank you for using the Travel Journal app!")