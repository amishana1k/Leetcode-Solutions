class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        count = 0
        
        # Loop through all possible substrings
        for i in range(len(word)):
            seen_vowels = set()
            for j in range(i, len(word)):
                if word[j] in vowels:
                    seen_vowels.add(word[j])
                    # Check if all vowels are present
                    if len(seen_vowels) == 5:
                        count += 1
                else:
                    break  # Stop if we encounter a non-vowel character
        
        return count
