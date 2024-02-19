from tkinter import *
from tkinter import filedialog, ttk
from tkinter import Toplevel
from graphviz import Digraph
from tkinter import Toplevel, Canvas
import matplotlib.pyplot as plt
import networkx as nx
import math

# Initialize document variables at a global scope
document1 = ""
document2 = ""

# Create the main window
fenetre = Tk()
fenetre.geometry('600x400')
fenetre.title('Calculer la Similarité ')
fenetre['bg'] = 'beige'  # Set background color

# Label to display results at the bottom
result_label = Label(fenetre, text="", fg="blue")
result_label.pack(side=BOTTOM, pady=100)

# Create a new window to display the steps as a tree
tree_window = Toplevel(fenetre)
tree_window.title('Steps Tree')
tree_window.geometry('800x600')

# Create a Treeview widget
tree = ttk.Treeview(tree_window, columns=('Step', 'Method'), show='headings')
tree.heading('Step', text='Step')
tree.heading('Method', text='Method')
tree.pack(expand=YES, fill=BOTH)

# Variable to keep track of the step number
step_number = 1

# Function to perform the similarity calculation based on the selected method
def perform_similarity_calculation(order, method):
    global step_number

    # Add your similarity calculation code here using document1, document2, order, and method
    result_label.config(text=f"Similarité calculée avec méthode {method} ({order})")

    # Add the step to the tree
    tree.insert('', 'end', values=(f'Step {step_number}', method))
    step_number += 1

# Function to load and read the first document
def Read_Split1():
    global document1
    text1 = filedialog.askopenfilename()
    if text1:
        with open(text1, "r") as file:
            document1 = file.read()

        # Enable the "Calculer Similarité Ascendante" and "Calculer Similarité Descendante" buttons
        btn_similarity_asc.config(state=NORMAL)
        btn_similarity_desc.config(state=NORMAL)
        result_label.config(text="")  # Clear previous results

    else:
        print("Aucun fichier sélectionné.")

# Function to perform ascending similarity calculation
def Calculate_Similarity_Asc():
    show_similarity_menu("ascendant")

# Function to perform descending similarity calculation
def Calculate_Similarity_Desc():
    show_similarity_menu("descendant")

# Function to show the similarity method menu
def show_similarity_menu(order):
    similarity_menu = Menu(fenetre, tearoff=0)

    # Add items to the menu dynamically
    methods = ["Bulle", "selection", "Insertion", "trieRapide", "Fusion", "ABR", "TasMax", "tasmin", "avl", "radix"]
    for method in methods:
        if method == "Insertion" and order == "ascendant":
            similarity_menu.add_command(label=method, command=call_insertion_function_asc)
        elif method == "Insertion" and order == "descendant":
            similarity_menu.add_command(label=method, command=call_insertion_function_desc)
        elif method == "selection" and order == "ascendant":
            similarity_menu.add_command(label=method, command=call_selection_function_asc)
        elif method == "selection" and order == "descendant":
            similarity_menu.add_command(label=method, command=call_selection_function_desc)
        elif method == "Bulle" and order == "ascendant":
            similarity_menu.add_command(label=method, command=call_bubble_function_asc)
        elif method == "Bulle" and order == "descendant":
            similarity_menu.add_command(label=method, command=call_bubble_function_desc)
        elif method == "trieRapide" and order == "ascendant":
            similarity_menu.add_command(label=method, command=call_quick_sort_function_asc)
        elif method == "trieRapide" and order == "descendant":
            similarity_menu.add_command(label=method, command=call_quick_sort_function_desc)
        elif method == "Fusion" and order == "ascendant":
            similarity_menu.add_command(label=method, command=call_merge_sort_function_asc)
        elif method == "Fusion" and order == "descendant":
            similarity_menu.add_command(label=method, command=call_merge_sort_function_desc)
        elif method == "radix" and order == "ascendant":
            similarity_menu.add_command(label=method, command=call_radix_sort_function_asc)
        elif method == "radix" and order == "descendant":
            similarity_menu.add_command(label=method, command=call_radix_sort_function_desc)
        elif method == "tasmin" and order == "ascendant":
            similarity_menu.add_command(label=method, command=call_tasmin_function)
        elif method == "TasMax" and order == "descendant":
            similarity_menu.add_command(label=method, command=call_TasMax_function)    
           
    # Display the menu at the current mouse position
    similarity_menu.post(fenetre.winfo_pointerx(), fenetre.winfo_pointery())

# Function to perform the similarity calculation based on the selected method
def perform_similarity_calculation(order, method):
    global step_number

    # Add your similarity calculation code here using document1, document2, order, and method
    result_label.config(text=f"Similarité calculée avec méthode {method} ({order})")

    # Check if there are children in the tree
    if tree.get_children():
        # If there are children, get the last one
        last_step = tree.get_children()[-1]
        # Extract the step number from the last step
        last_step_number = int(tree.item(last_step, "values")[0].split()[1])
        step_number = last_step_number + 1
    else:
        # If there are no children, start from step 1
        step_number = 1

    # Add the step to the tree
    tree.insert('', 'end', values=(f'Step {step_number}', method))


                 # insertion

# Modify the call_insertion_function_asc function to update the tree with each step
def call_insertion_function_asc():
    global document1, step_number
    # Reset the step_number to 1 for a new sort
    step_number = 1

    if document1:
        # Split the document content into a list of integers
        numbers_list = list(map(int, document1.split()))

        # Display the original list in the result_label
        result_label.config(text=f"Liste originale: {numbers_list}")

        # Update the tree with each step
        for i in range(1, len(numbers_list)):
            cle = numbers_list[i]
            j = i - 1
            while j >= 0 and cle < numbers_list[j]:
                numbers_list[j + 1] = numbers_list[j]
                # Add the step to the tree
                tree.insert('', 'end', values=(f'Step {step_number}', f'Insertion (asc) - Étape {i}: {numbers_list[:]}'))
                step_number += 1
                j -= 1
            numbers_list[j + 1] = cle

        # Display the final sorted list in the result_label
        result_label.config(text=f"Liste triée avec Insertion (asc): {numbers_list}")

    else:
        result_label.config(text="Aucun document chargé.")


# Modify the call_insertion_function_desc function to update the tree with each step
def call_insertion_function_desc():
    global document1, step_number
    # Reset the step_number to 1 for a new sort
    step_number = 1

    if document1:
        # Split the document content into a list of integers
        numbers_list = list(map(int, document1.split()))

        # Display the original list in the result_label
        result_label.config(text=f"Liste originale: {numbers_list}")

        # Update the tree with each step
        for i in range(1, len(numbers_list)):
            cle = numbers_list[i]
            j = i - 1
            while j >= 0 and cle > numbers_list[j]:
                numbers_list[j + 1] = numbers_list[j]
                # Add the step to the tree
                tree.insert('', 'end', values=(f'Step {step_number}', f'Insertion (desc) - Étape {i}: {numbers_list[:]}'))
                step_number += 1
                j -= 1
            numbers_list[j + 1] = cle

        # Display the final sorted list in the result_label
        result_label.config(text=f"Liste triée avec Insertion (desc): {numbers_list}")

    else:
        result_label.config(text="Aucun document chargé.")




           #selection

# Modify the call_selection_function_asc function to update the tree with each step
def call_selection_function_asc():
    global document1, step_number
    # Reset the step_number to 1 for a new sort
    step_number = 1

    if document1:
        # Split the document content into a list of integers
        numbers_list = list(map(int, document1.split()))

        # Display the original list in the result_label
        result_label.config(text=f"Liste originale: {numbers_list}")

        # Update the tree with each step
        for i in range(len(numbers_list)):
            min_index = i
            for j in range(i + 1, len(numbers_list)):
                if numbers_list[j] < numbers_list[min_index]:
                    min_index = j

            # Swap the found minimum element with the first element
            numbers_list[i], numbers_list[min_index] = numbers_list[min_index], numbers_list[i]

            # Add the step to the tree
            tree.insert('', 'end', values=(f'Step {step_number}', f'Selection (asc) - Étape {i + 1}: {numbers_list[:]}'))
            step_number += 1

        # Display the final sorted list in the result_label
        result_label.config(text=f"Liste triée avec Selection (asc): {numbers_list}")

    else:
        result_label.config(text="Aucun document chargé.")


# Modify the call_selection_function_desc function to update the tree with each step
def call_selection_function_desc():
    global document1, step_number
    # Reset the step_number to 1 for a new sort
    step_number = 1

    if document1:
        # Split the document content into a list of integers
        numbers_list = list(map(int, document1.split()))

        # Display the original list in the result_label
        result_label.config(text=f"Liste originale: {numbers_list}")

        # Update the tree with each step
        for i in range(len(numbers_list)):
            max_index = i
            for j in range(i + 1, len(numbers_list)):
                if numbers_list[j] > numbers_list[max_index]:
                    max_index = j

            # Swap the found maximum element with the first element
            numbers_list[i], numbers_list[max_index] = numbers_list[max_index], numbers_list[i]

            # Add the step to the tree
            tree.insert('', 'end', values=(f'Step {step_number}', f'Selection (desc) - Étape {i + 1}: {numbers_list[:]}'))
            step_number += 1

        # Display the final sorted list in the result_label
        result_label.config(text=f"Liste triée avec Selection (desc): {numbers_list}")

    else:
        result_label.config(text="Aucun document chargé.")


                      #bubble sort
                      
 # Modify the call_bubble_function_asc function to update the tree with each step
def call_bubble_function_asc():
    global document1, step_number
    # Reset the step_number to 1 for a new sort
    step_number = 1

    if document1:
        # Split the document content into a list of integers
        numbers_list = list(map(int, document1.split()))

        # Display the original list in the result_label
        result_label.config(text=f"Liste originale: {numbers_list}")

        # Update the tree with each step
        for i in range(len(numbers_list)):
            for j in range(0, len(numbers_list) - i - 1):
                if numbers_list[j] > numbers_list[j + 1]:
                    # Swap if the element found is greater than the next element
                    numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]

                    # Add the step to the tree
                    tree.insert('', 'end', values=(f'Step {step_number}', f'Bubble (asc) - Étape {i + 1}: {numbers_list[:]}'))
                    step_number += 1

        # Display the final sorted list in the result_label
        result_label.config(text=f"Liste triée avec Bubble (asc): {numbers_list}")

    else:
        result_label.config(text="Aucun document chargé.")



# Modify the call_bubble_function_desc function to update the tree with each step
def call_bubble_function_desc():
    global document1, step_number
    # Reset the step_number to 1 for a new sort
    step_number = 1

    if document1:
        # Split the document content into a list of integers
        numbers_list = list(map(int, document1.split()))

        # Display the original list in the result_label
        result_label.config(text=f"Liste originale: {numbers_list}")

        # Update the tree with each step
        for i in range(len(numbers_list)):
            for j in range(0, len(numbers_list) - i - 1):
                if numbers_list[j] < numbers_list[j + 1]:
                    # Swap if the element found is smaller than the next element
                    numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]

                    # Add the step to the tree
                    tree.insert('', 'end', values=(f'Step {step_number}', f'Bubble (desc) - Étape {i + 1}: {numbers_list[:]}'))
                    step_number += 1

        # Display the final sorted list in the result_label
        result_label.config(text=f"Liste triée avec Bubble (desc): {numbers_list}")

    else:
        result_label.config(text="Aucun document chargé.")



        # quick sort

def call_quick_sort_function_asc():
    global document1, step_number

    # Reset the step_number to 1 for a new sort
    step_number = 1

    if document1:
        # Split the document content into a list of integers
        numbers_list = list(map(int, document1.split()))

        # Display the original list in the result_label
        result_label.config(text=f"Liste originale: {numbers_list}")

        # Define the partition function for quick sort (ascending order)
        def partition_asc(arr, low, high, step_number):
            pivot = arr[low]
            left = low + 1
            right = high

            done = False
            while not done:
                while left <= right and arr[left] <= pivot:
                    left = left + 1
                while arr[right] >= pivot and right >= left:
                    right = right - 1
                if right < left:
                    done = True
                else:
                    # Swap elements at left and right
                    arr[left], arr[right] = arr[right], arr[left]

            # Swap the pivot element with the right element
            arr[low], arr[right] = arr[right], arr[low]

            # Add the step to the tree
            tree.insert('', 'end', values=(f'Step {step_number}', f'Quick Sort (asc) - Étape: {arr[:]}'))
            step_number += 1

            return right, step_number

        # Define the quick sort algorithm
        def quick_sort_asc(arr, low, high, step_number):
            if low < high:
                # Partition the array and get the pivot index
                pivot_index, step_number = partition_asc(arr, low, high, step_number)

                # Recursively sort the sub-arrays
                step_number = quick_sort_asc(arr, low, pivot_index, step_number)
                step_number = quick_sort_asc(arr, pivot_index + 1, high, step_number)

            return step_number

        # Call the quick sort algorithm
        step_number = quick_sort_asc(numbers_list, 0, len(numbers_list) - 1, step_number)

        # Display the final sorted list in the result_label
        result_label.config(text=f"Liste triée avec Quick Sort (asc): {numbers_list}")

    else:
        result_label.config(text="Aucun document chargé.")


def call_quick_sort_function_desc():
    global document1, step_number

    # Reset the step_number to 1 for a new sort
    step_number = 1

    if document1:
        # Split the document content into a list of integers
        numbers_list = list(map(int, document1.split()))

        # Display the original list in the result_label
        result_label.config(text=f"Liste originale: {numbers_list}")

        # Define the partition function for quick sort (descending order)
        def partition_desc(arr, low, high, step_number):
            pivot = arr[low]
            left = low + 1
            right = high

            done = False
            while not done:
                while left <= right and arr[left] >= pivot:
                    left = left + 1
                while arr[right] <= pivot and right >= left:
                    right = right - 1
                if right < left:
                    done = True
                else:
                    # Swap elements at left and right
                    arr[left], arr[right] = arr[right], arr[left]

            # Swap the pivot element with the right element
            arr[low], arr[right] = arr[right], arr[low]

            # Add the step to the tree
            tree.insert('', 'end', values=(f'Step {step_number}', f'Quick Sort (desc) - Étape: {arr[:]}'))
            step_number += 1

            return right, step_number

        # Define the quick sort algorithm
        def quick_sort_desc(arr, low, high, step_number):
            if low < high:
                # Partition the array and get the pivot index
                pivot_index, step_number = partition_desc(arr, low, high, step_number)

                # Recursively sort the sub-arrays
                step_number = quick_sort_desc(arr, low, pivot_index, step_number)
                step_number = quick_sort_desc(arr, pivot_index + 1, high, step_number)

            return step_number

        # Call the quick sort algorithm
        step_number = quick_sort_desc(numbers_list, 0, len(numbers_list) - 1, step_number)

        # Display the final sorted list in the result_label
        result_label.config(text=f"Liste triée avec Quick Sort (desc): {numbers_list}")

    else:
        result_label.config(text="Aucun document chargé.")

        # merge sort 
def call_merge_sort_function_asc():
    global document1, step_number

    # Reset the step_number to 1 for a new sort
    step_number = 1

    if document1:
        # Split the document content into a list of integers
        numbers_list = list(map(int, document1.split()))

        # Display the original list in the result_label
        result_label.config(text=f"Liste originale: {numbers_list}")

        # Define the merge sort algorithm
        def merge_sort_asc(arr, step_number):
            if len(arr) > 1:
                mid = len(arr) // 2
                left_half = arr[:mid]
                right_half = arr[mid:]

                merge_sort_asc(left_half, step_number)
                merge_sort_asc(right_half, step_number)

                i = j = k = 0

                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        arr[k] = left_half[i]
                        i += 1
                    else:
                        arr[k] = right_half[j]
                        j += 1
                    k += 1

                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1

                # Add the step to the tree
                tree.insert('', 'end', values=(f'Step {step_number}', f'Merge Sort (asc) - Étape: {arr[:]}'))
                step_number[0] += 1

        # Call the merge sort algorithm
        merge_sort_asc(numbers_list, [step_number])

        # Display the final sorted list in the result_label
        result_label.config(text=f"Liste triée avec Merge Sort (asc): {numbers_list}")

    else:
        result_label.config(text="Aucun document chargé.")


def call_merge_sort_function_desc():
    global document1, step_number

    # Reset the step_number to 1 for a new sort
    step_number = 1

    if document1:
        # Split the document content into a list of integers
        numbers_list = list(map(int, document1.split()))

        # Display the original list in the result_label
        result_label.config(text=f"Liste originale: {numbers_list}")

        # Define the merge sort algorithm
        def merge_sort_desc(arr, step_number):
            if len(arr) > 1:
                mid = len(arr) // 2
                left_half = arr[:mid]
                right_half = arr[mid:]

                merge_sort_desc(left_half, step_number)
                merge_sort_desc(right_half, step_number)

                i = j = k = 0

                while i < len(left_half) and j < len(right_half):
                    if left_half[i] > right_half[j]:
                        arr[k] = left_half[i]
                        i += 1
                    else:
                        arr[k] = right_half[j]
                        j += 1
                    k += 1

                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1

                # Add the step to the tree
                tree.insert('', 'end', values=(f'Step {step_number}', f'Merge Sort (desc) - Étape: {arr[:]}'))
                step_number[0] += 1

        # Call the merge sort algorithm
        merge_sort_desc(numbers_list, [step_number])

        # Display the final sorted list in the result_label
        result_label.config(text=f"Liste triée avec Merge Sort (desc): {numbers_list}")

    else:
        result_label.config(text="Aucun document chargé.")

                   # radix sort 

def call_radix_sort_function_asc():
    global document1, step_number

    # Reset the step_number to 1 for a new sort
    step_number = 1

    if document1:
        # Split the document content into a list of integers
        numbers_list = list(map(int, document1.split()))

        # Display the original list in the result_label
        result_label.config(text=f"Liste originale: {numbers_list}")

        # Define the radix sort algorithm
        def radix_sort_asc(arr):
            # Find the maximum number to know the number of digits
            max_num = max(arr)

            # Do counting sort for every digit
            exp = 1
            while max_num // exp > 0:
                counting_sort_asc(arr, exp, [step_number])
                exp *= 10

        # Define the counting sort function for radix sort (ascending order)
        def counting_sort_asc(arr, exp, step_number):
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            # Store count of occurrences in count[]
            for i in range(n):
                index = arr[i] // exp
                count[index % 10] += 1

            # Change count[i] so that count[i] now contains actual position of this digit in output[]
            for i in range(1, 10):
                count[i] += count[i - 1]

            # Build the output array
            i = n - 1
            while i >= 0:
                index = arr[i] // exp
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1
                i -= 1

            # Copy the output array to arr[] so that arr[] contains sorted numbers according to the current digit
            for i in range(n):
                arr[i] = output[i]

                # Add the step to the tree
                tree.insert('', 'end', values=(f'Step {step_number[0]}', f'Radix Sort (asc) - Étape: {arr[:]}'))
                step_number[0] += 1

        # Call the radix sort algorithm
        radix_sort_asc(numbers_list)

        # Display the final sorted list in the result_label
        result_label.config(text=f"Liste triée avec Radix Sort (asc): {numbers_list}")

    else:
        result_label.config(text="Aucun document chargé.")


def call_radix_sort_function_desc():
    global document1, step_number

    # Reset the step_number to 1 for a new sort
    step_number = 1

    if document1:
        # Split the document content into a list of integers
        numbers_list = list(map(int, document1.split()))

        # Display the original list in the result_label
        result_label.config(text=f"Liste originale: {numbers_list}")

        # Define the radix sort algorithm
        def radix_sort_desc(arr):
            # Find the maximum number to know the number of digits
            max_num = max(arr)

            # Do counting sort for every digit
            exp = 1
            while max_num // exp > 0:
                counting_sort_desc(arr, exp, [step_number])
                exp *= 10

        # Define the counting sort function for radix sort (descending order)
        def counting_sort_desc(arr, exp, step_number):
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            # Store count of occurrences in count[]
            for i in range(n):
                index = arr[i] // exp
                count[index % 10] += 1

            # Change count[i] so that count[i] now contains the actual position of this digit in output[]
            for i in range(1, 10):
                count[i] += count[i - 1]

            # Build the output array
            i = n - 1
            while i >= 0:
                index = arr[i] // exp
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1
                i -= 1

            # Copy the output array to arr[] so that arr[] contains sorted numbers according to the current digit
            for i in range(n):
                arr[i] = output[i]

                # Add the step to the tree
                tree.insert('', 'end', values=(f'Step {step_number[0]}', f'Radix Sort (desc) - Étape: {arr[:]}'))
                step_number[0] += 1

        # Call the radix sort algorithm
        radix_sort_desc(numbers_list)

        # Display the final sorted list in the result_label
        result_label.config(text=f"Liste triée avec Radix Sort (desc): {numbers_list}")

    else:
        result_label.config(text="Aucun document chargé.")

# Function to perform similarity calculation based on the "TasMin" method
def call_tasmin_function():
    global document1, step_number
    # Reset the step_number to 1 for a new sort
    step_number = 1

    if document1:
        # Split the document content into a list of integers
        numbers_list = list(map(int, document1.split()))

        # Display the original list in the result_label
        result_label.config(text=f"Liste originale: {numbers_list}")

        # Call the TasMin sorting algorithm
        tasmin_sort(numbers_list)

        # Display the final sorted list in the result_label
        result_label.config(text=f"Liste triée avec TasMin: {numbers_list}")

    else:
        result_label.config(text="Aucun document chargé.")

#TASMIN
def tasmin_sort(arr, step_number):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        tree.insert('', 'end', values=(f'Step {step_number}', f'TasMin - Étape {n - i}: {arr[:]}'))
        step_number += 1
        heapify(arr, i, 0)
# Function to perform similarity calculation based on the "TasMin" method
def call_tasmin_function():
    global document1, step_number

    # Reset the step_number to 1 for a new sort
    step_number = 1

    if document1:
        # Split the document content into a list of integers
        numbers_list = list(map(int, document1.split()))

        # Display the original list in the result_label
        result_label.config(text=f"Liste originale: {numbers_list}")

        # Call the tasmin sort algorithm
        tasmin_sort(numbers_list, step_number)

        # Display the final sorted list in the result_label
        result_label.config(text=f"Liste triée avec TasMin: {numbers_list}")

        # Draw and display the tree
        dessiner_arbre(numbers_list)

    else:
        result_label.config(text="Aucun document chargé.")

#TASMAX
def tasMax_sort(arr, step_number):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] > arr[left]:
            largest = left

        if right < n and arr[largest] > arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        tree.insert('', 'end', values=(f'Step {step_number}', f'TasMin - Étape {n - i}: {arr[:]}'))
        step_number += 1
        heapify(arr, i, 0)

# Function to perform similarity calculation based on the "TasMin" method
def call_TasMax_function():
    global document1, step_number
    # Reset the step_number to 1 for a new sort
    step_number = 1

    if document1:
        # Split the document content into a list of integers
        numbers_list = list(map(int, document1.split()))

        # Display the original list in the result_label
        result_label.config(text=f"Liste originale: {numbers_list}")

        # Call the TasMax sorting algorithm with the initial step_number value
        tasMax_sort(numbers_list, step_number)
        


        # Display the final sorted list in the result_label
        result_label.config(text=f"Liste triée avec TasMax: {numbers_list}")
        # Draw and display the tree
        dessiner_arbre(numbers_list)

    else:
        result_label.config(text="Aucun document chargé.")




def dessiner_arbre(liste):
    G = nx.Graph()

    for i, valeur in enumerate(liste):
        G.add_node(i, label=str(valeur))
        if i > 0:
            parent = (i - 1) // 2
            G.add_edge(parent, i)

        # Draw and display the tree at each step
        draw_tree_step(G, i)

    plt.show()

def draw_tree_step(G, current_node):
    pos = {}
    max_depth = int(math.log2(current_node + 2)) + 1

    for i in range(current_node + 1):
        depth = int(math.log2(i + 1)) + 1
        pos[i] = ((i + 1) * (1 / (2 ** depth)), -depth)  # Adjust positions based on depth

    labels = nx.get_node_attributes(G, 'label')

    nx.draw(G, pos, with_labels=True, labels=labels, font_weight='bold', node_size=700, node_color="skyblue", font_size=8,
            arrows=False)
    plt.show()

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    def draw_tree(self):
        G = nx.Graph()
        self._add_nodes_edges(G, self.root)
        pos = self._generate_positions(G, self.root)
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        plt.show()

    def _add_nodes_edges(self, G, node):
        if node:
            G.add_node(node.key)
            if node.left:
                G.add_edge(node.key, node.left.key)
                self._add_nodes_edges(G, node.left)
            if node.right:
                G.add_edge(node.key, node.right.key)
                self._add_nodes_edges(G, node.right)

    def _generate_positions(self, G, node, pos=None, x=0, level=1, width=2.0):
        if pos is None:
            pos = {node.key: (x, level)}
        else:
            pos[node.key] = (x, level)

        if node.left:
            dx = width / 2
            nextx = x - width / 2 - dx / 2
            pos = self._generate_positions(G, node.left, pos, nextx, level + 1, width=dx)

        if node.right:
            dx = width / 2
            nextx = x + width / 2 + dx / 2
            pos = self._generate_positions(G, node.right, pos, nextx, level + 1, width=dx)

        return pos
def Read_Split(txt):
    with open(txt, "r") as file:
        text = file.read()
        l1 = [int(x) for x in text.split()]
    return l1

def display_tree():
    bst = BinarySearchTree()
    elements = Read_Split("nmb.txt")
    for element in elements:
        bst.insert(element)
        bst.draw_tree()



# Button to load and read the first document
btn_load_document = Button(fenetre, text="Charger Document", command=Read_Split1)
btn_load_document.place(x=200, y=70)

# Button to perform ascending similarity calculation
btn_similarity_asc = Button(fenetre, text="Calculer Similarité Ascendante", command=Calculate_Similarity_Asc,
                            state=DISABLED)
btn_similarity_asc.place(x=200, y=100)

# Button to perform descending similarity calculation
btn_similarity_desc = Button(fenetre, text="Calculer Similarité Descendante", command=Calculate_Similarity_Desc,
                             state=DISABLED)

btn_similarity_desc.place(x=200, y=130)
# Bouton pour afficher l'arbre
btn_display_treeABR = Button(fenetre, text="Afficher ABR", command=display_tree)
btn_display_treeABR.place(x=200, y=160)
# Start the Tkinter event loop

# Start the Tkinter event loop
fenetre.mainloop()
