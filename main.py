"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    total_class_days = CLASS_DAYS_PER_SEMESTER * SEMESTERS_PER_YEAR
    return annual_cost / total_class_days


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    semester_cost = cost_per_semester(annual_cost)
    return semester_cost / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    one_credit_cost = cost_per_credit(annual_cost, credits)
    semester_course_cost = one_credit_cost * CS1430_CREDITS
    return semester_course_cost / CS1430_MEETINGS_PER_SEMESTER


def cost_of_skipped_classes(annual_cost, credits, classes_skipped):
    """Calculate how much money is represented by skipped CS 1430 meetings."""
    one_class_cost = cost_per_class(annual_cost, credits)
    return one_class_cost * classes_skipped


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here, then credits this semester
    annual_cost = float(input("Enter the total cost for one year of college: $"))
    credits = int(input("Enter the number of credits you are taking this semester: "))

    
    while True:
        print("\n===== THE COST OF COLLEGE =====")
        print("1. Cost per semester")
        print("2. Cost per month of the academic year")
        print("3. Cost per class day")
        print("4. Cost per credit")
        print("5. Cost per CS 1430 class meeting")
        print("6. Cost of skipped CS 1430 classes (Worth It?)")
        print("Q. Quit")

        choice = input("Choose an option: ").strip().upper()

        if choice == "Q":
            print("Thanks for using The Cost of College")
            break

        elif choice == "1":
            result = cost_per_semester(annual_cost)
            print(f"One semester costs: ${result:,.2f}")

        elif choice == "2":
            result = cost_per_month(annual_cost)
            print(f"One academic month costs: ${result:,.2f}")

        elif choice == "3":
            result = cost_per_day(annual_cost)
            print(f"One class day costs: ${result:,.2f}")

        elif choice == "4":
            result = cost_per_credit(annual_cost, credits)
            print(f"One credit costs: ${result:,.2f}")

        elif choice == "5":
            result = cost_per_class(annual_cost, credits)
            print(f"One CS 1430 class meeting costs: ${result:,.2f}")

        elif choice == "6":
            classes_skipped = int(input("How many CS 1430 classes would you skip? "))
            result = cost_of_skipped_classes(annual_cost, credits, classes_skipped)
            print(f"The cost represented by skipping "f"{classes_skipped} class(es) is ${result:,.2f}")

        if result > 0:
            print("Is skipping worth it? Consider what you miss in class, too.")


        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or Q.")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
