def count_vo_c(s):
    vowels = 'aeiouAEIOU'
    v_count = sum(1 for c in s if c.isalpha() and c in vowels)
    c_count = sum(1 for c in s if c.isalpha() and c not in vowels)
    print(f"Vowels: {v_count}, Consonants: {c_count}")
count_vo_c("Sameer Kumar Narasimha")
