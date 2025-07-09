def count_co_e(list1, list2):
    common = set(list1).intersection(set(list2))
    print(f"Common Elements: {common}")
    print(f"Number of Common Elements: {len(common)}")
count_co_e([1, 2, 3, 4], [3, 4, 5, 6])
