def count_vowels(word):
    vowel=['a','e','i','o','u']
    count=0
    for i in range(0,len(word)):
        if(word[i].lower() in vowel):
            count+=1
    return count

if __name__=="__main__":
    word="DatascienceBootcamp"
    print(count_vowels(word))