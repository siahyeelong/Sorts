import random
import time
import pandas as pd

time_check = time.time()  # global variable for time tracking
keycomp = 0


def insertion_sort(arr):
    global keycomp
    for a in range(1, len(arr)):
        for b in range(a, 0, -1):
            keycomp += 1
            if arr[b] < arr[b - 1]:
                arr[b], arr[b - 1] = arr[b - 1], arr[a]


def merge_sort(arr, S):
    global keycomp

    if len(arr) > S:
        # split part
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, S)
        merge_sort(R, S)

        # merge part
        l_counter = r_counter = arr_counter = 0

        while l_counter < len(L) and r_counter < len(R):
            keycomp += 1

            if L[l_counter] <= R[r_counter]:
                arr[arr_counter] = L[l_counter]
                l_counter += 1
            else:
                arr[arr_counter] = R[r_counter]
                r_counter += 1

            arr_counter += 1

        # clean up the remaining values
        while l_counter < len(L):
            arr[arr_counter] = L[l_counter]
            l_counter += 1
            arr_counter += 1

        while r_counter < len(R):
            arr[arr_counter] = R[r_counter]
            r_counter += 1
            arr_counter += 1

    else:
        insertion_sort(arr)

    return


# generate random array of length N
def generate_random(N):
    return random.sample(range(N), N)


# function to trigger start of program (1) and end of program (0)
def logtime(trigger):
    global time_check
    if trigger:
        time_check = time.time()
    else:
        return time.time() - time_check


# main code here ###########################################


test = generate_random(100)
keycomp = 0

logtime(1)
merge_sort(test, 12)
print(logtime(0), "seconds elapsed")

print("Keycomps:", keycomp)

# Create an empty DataFrame to store results
keycomps_df = pd.DataFrame(columns=range(1, 60))
runtime_df = pd.DataFrame(columns=range(1, 60))


# def runtest():
#     global keycomp
#     global runtime_df
#     global keycomps_df
#     for N in [1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]:
#         random_array = generate_random(N)

#         # create a dictionary to store results for the current N
#         keycomps_dict = {"N": N}
#         runtime_dict = {"N": N}

#         for S in range(1, 60):
#             test_array = random_array.copy()
#             keycomp = 0

#             logtime(1)
#             merge_sort(test_array, S)
#             elapsed_time = logtime(0)

#             # add keycomps as a result for the current S value
#             keycomps_dict[S] = keycomp
#             # add runtime as a result for the current S value
#             runtime_dict[S] = elapsed_time

#             print("S:", S, "N:", N, "Keycomps:", keycomp, "Time taken:", elapsed_time)

#         # append the keycomps_df to the DataFrame
#         keycomps_df = keycomps_df.append(keycomps_dict, ignore_index=True)
#         keycomps_df.to_excel("KeyComps.xlsx")
#         # append the keycomps_df to the DataFrame
#         runtime_df = runtime_df.append(runtime_dict, ignore_index=True)
#         runtime_df.to_excel("Runtime.xlsx")

#     return


# runtest()

# keycomps_df.to_excel("KeyComps.xlsx")
# runtime_df.to_excel("Runtime.xlsx")


# Create empty DataFrames to store keycomp and elapsed_time values
merge_sort_keycomp_values = []
merge_sort_elapsed_time_values = []
insertion_sort_keycomp_values = []
insertion_sort_elapsed_time_values = []


def base_performance():
    global keycomp
    i = 0

    for S in range(1, 100, 1):
        random_arr = generate_random(1_000)

        # Merge sort base performance
        test_arr = random_arr.copy()
        keycomp = 0
        logtime(1)
        merge_sort(test_arr, S)
        elapsed_time = logtime(0)

        # Append keycomp and elapsed_time values for Merge Sort
        merge_sort_keycomp_values.append(keycomp)
        merge_sort_elapsed_time_values.append(elapsed_time)

        # Insertion sort base performance
        test_arr = random_arr.copy()
        keycomp = 0
        logtime(1)
        insertion_sort(test_arr)
        elapsed_time = logtime(0)

        # Append keycomp and elapsed_time values for Insertion Sort
        insertion_sort_keycomp_values.append(keycomp)
        insertion_sort_elapsed_time_values.append(elapsed_time)

        print(
            "Merge sort performance, S:",
            S,
            "--",
            merge_sort_keycomp_values[i],
            merge_sort_elapsed_time_values[i],
        )
        print(
            "Insertion sort performance",
            "--",
            insertion_sort_keycomp_values[i],
            insertion_sort_elapsed_time_values[i],
        )

        # saving values into excel every 10 iterations
        if i % 10 == 0:
            # Create DataFrames from the lists of values
            merge_sort_df = pd.DataFrame(
                {
                    "Merge_Sort_Keycomp": merge_sort_keycomp_values,
                    "Merge_Sort_Elapsed_Time": merge_sort_elapsed_time_values,
                }
            )

            insertion_sort_df = pd.DataFrame(
                {
                    "Insertion_Sort_Keycomp": insertion_sort_keycomp_values,
                    "Insertion_Sort_Elapsed_Time": insertion_sort_elapsed_time_values,
                }
            )

            # Concatenate DataFrames to get the final result
            performance_df = pd.concat([merge_sort_df, insertion_sort_df], axis=1)

            # Export the DataFrame to an Excel file
            performance_df.to_excel("sorting_performance_small.xlsx", index=False)
            print("export no.:", i / 10)

        i += 1


base_performance()
