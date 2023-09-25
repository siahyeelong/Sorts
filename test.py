import pandas as pd

merge_sort_df = pd.DataFrame(
    {
        "Merge_Sort_Keycomp": [],
        "Merge_Sort_Elapsed_Time": [],
    }
)

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]

merge_sort_df.append(arr1)

print(merge_sort_df)
