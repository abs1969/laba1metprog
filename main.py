import csv
import os
import random
import string
import time
import matplotlib.pyplot as plt


class Employee:
    def __init__(self, full_name: str, position: str, division: str, salary: int):
        # Constructor for the Employee class that takes four arguments:
        # full_name (str), position (str), division (str), and salary (int).
        # Initializes the corresponding fields with the values passed in.
        self._full_name = full_name
        self._position = position
        self._division = division
        self._salary = salary

    @property
    def full_name(self) -> str:
        # Getter method for the full_name field.
        # Returns the value of the private _full_name field.
        return self._full_name

    @property
    def position(self) -> str:
        # Getter method for the position field.
        # Returns the value of the private _position field.
        return self._position

    @property
    def division(self) -> str:
        # Getter method for the division field.
        # Returns the value of the private _division field.
        return self._division

    @property
    def salary(self) -> float:
        # Getter method for the salary field.
        # Returns the value of the private _salary field.
        return self._salary

    def __eq__(self, other):
        # Overloads the equality operator (==) to compare Employee objects
        # first by division, then by full_name, and finally by salary.
        # Returns True if all three fields are equal, False otherwise.
        if isinstance(other, Employee):
            return self.division == other.division and self.full_name == other.full_name and self.salary == other.salary
        return NotImplemented

    def __lt__(self, other):
        # Overloads the less-than operator (<) to compare Employee objects
        # first by division, then by full_name, and finally by salary.
        # Returns True if the current object is less than the other object,
        # False otherwise.
        if isinstance(other, Employee):
            if self.division == other.division:
                if self.full_name == other.full_name:
                    return self.salary < other.salary
                return self.full_name < other.full_name
            return self.division < other.division
        return NotImplemented

    def __le__(self, other):
        # Overloads the less-than-or-equal-to operator (<=) to compare
        # Employee objects first by division, then by full_name, and finally
        # by salary. Returns True if the current object is less than or equal
        # to the other object, False otherwise.
        if isinstance(other, Employee):
            if self.division == other.division:
                if self.full_name == other.full_name:
                    return self.salary <= other.salary
                return self.full_name <= other.full_name
            return self.division <= other.division
        return NotImplemented

    def __gt__(self, other):
        # Overloads the greater-than operator (>) to compare Employee objects
        # first by division, then by full_name, and finally by salary.
        # Returns True if the current object is greater than the other object,
        # False otherwise.
        if isinstance(other, Employee):
            if self.division == other.division:
                if self.full_name == other.full_name:
                    return self.salary > other.salary
                return self.full_name > other.full_name
            return self.division > other.division
        return NotImplemented

    def __ge__(self, other):
        # Overloads the greater-than-or-equal-to operator (=) to compare Employee objects first by division,
        # then by full_name, and finally by salary. Returns True if the current object is greater
        # than or equal to the other object, False otherwise.
        if isinstance(other, Employee):
            if self.division == other.division:
                if self.full_name == other.full_name:
                    return self.salary >= other.salary
                return self.full_name >= other.full_name
            return self.division >= other.division
        return NotImplemented


# Create some Employee objects
employee1 = Employee("John Smith", "Manager", "Marketing", 50000)
employee2 = Employee("Jane Doe", "Assistant Manager", "Marketing", 45000)
employee3 = Employee("Bob Johnson", "Manager", "Sales", 55000)
employee4 = Employee("Samantha Lee", "Assistant Manager", "Sales", 47500)

# Test the comparison operators
print(employee1 > employee2)  # True
print(employee3 < employee4)  # True
print(employee1 == employee3)  # False
print(employee2 >= employee4)  # False
print(employee1 <= employee3)  # True
print("Sales" > "Finance")

def generate_full_name():
    first_name = "".join(random.choice(string.ascii_letters) for i in range(random.randint(3, 10)))
    last_name = "".join(random.choice(string.ascii_letters) for i in range(random.randint(3, 10)))
    return f"{first_name.capitalize()} {last_name.capitalize()}"


def generate_csv_table(rows, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["full_name", "position", "department", "salary"])
        for i in range(rows):
            full_name = generate_full_name()
            position = random.choice(["Manager", "Supervisor", "Assistant", "Director"])
            department = random.choice(["Sales", "Marketing", "Finance", "Operations"])
            salary = random.randint(50000, 100000)
            writer.writerow([full_name, position, department, salary])


size = 100
for i in range(10):
    os.makedirs("files", exist_ok=True)
    filename = f"files/file{size}.csv"
    generate_csv_table(size, filename)
    size += 12000


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        # reset the flag for each iteration
        swapped = False

        # perform a bubble sort from left to right
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # if no swaps were made in the first iteration, the list is already sorted
        if not swapped:
            break

        # reset the flag for the next iteration
        swapped = False

        # perform a bubble sort from right to left
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # move the start index one position to the right
        start += 1

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # divide the list into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # recursively sort each half
    left = merge_sort(left)
    right = merge_sort(right)

    # merge the two sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # append any remaining elements from the left or right list
    result += left[i:]
    result += right[j:]

    return result


insertion_times = []
cocktail_times = []
merge_times = []


def sort_csv_file(filename, sort_func):
    # read the contents of the CSV file into a list
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip the header row
        objects = [Employee(*row) for row in reader]
    start_time = time.time()
    # sort the list using the specified sorting algorithm
    sorted_data = sort_func(objects)
    finish_time = time.time()
    print(f"{filename} sorted in {finish_time - start_time} seconds using {sort_func.__name__}")
    if sort_func.__name__ == "insertion_sort":
        insertion_times.append(finish_time - start_time)
    if sort_func.__name__ == "cocktail_sort":
        cocktail_times.append(finish_time - start_time)
    if sort_func.__name__ == "merge_sort":
        merge_times.append(finish_time - start_time)

    # write the sorted list to a new CSV file in a folder named after the sorting algorithm
    folder_name = f"folder_{sort_func.__name__}"
    os.makedirs(folder_name, exist_ok=True)
    output_filename = os.path.join(folder_name, os.path.basename(filename))
    with open(output_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["full_name", "position", "division", "salary"])
        for person in sorted_data:
            writer.writerow([person.full_name, person.position, person.division, person.salary])


file_list = []
for filename in os.listdir("files"):
    if os.path.isfile(os.path.join("files", filename)) and os.path.join("files", filename) != "files/.DS_Store":
        file_list.append(os.path.join("files", filename))
print(file_list)

sizes = sorted([int(fil.split('files/file')[1].split('.csv')[0]) for fil in file_list])

print(sizes)

print("---")
for siz in sizes:
    sort_csv_file(f"files/file{siz}.csv", insertion_sort)
print("---")
for siz in sizes:
    sort_csv_file(f"files/file{siz}.csv", cocktail_sort)
print("---")
for siz in sizes:
    sort_csv_file(f"files/file{siz}.csv", merge_sort)

plt.plot(sizes, sorted(insertion_times))
plt.title("Insertion Sort O(n^2)")
plt.xlabel("Size")
plt.ylabel("Running time (seconds)")
plt.savefig("quick_sort.png")

plt.clf()

plt.plot(sizes, sorted(cocktail_times))
plt.title("Cocktail Sort O(n^2)")
plt.xlabel("Size")
plt.ylabel("Running time (seconds)")
plt.savefig("cocktail_sort.png")

plt.clf()

plt.plot(sizes, sorted(merge_times))
plt.title("Merge Sort O(nlogn)")
plt.xlabel("Size")
plt.ylabel("Running time (seconds)")
plt.savefig("merge_sort.png")

plt.clf()

plt.plot(sizes, insertion_times, label="Insertion Sort")
plt.plot(sizes, cocktail_times, label="Cocktail Sort")
plt.plot(sizes, merge_times, label="Merge sort")
plt.xlabel("Size of file (strings)")
plt.ylabel("Time (seconds)")
plt.legend()
#plt.show()
plt.savefig("plot_all.png")