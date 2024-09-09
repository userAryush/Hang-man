from words import word
import random 

def random_words(word):
    word = random.choice(word)
    return word.upper()


def hangman(word):
    print("\n\nTO SAVE THE MAN FROM HANGING GUESS THE CORRECT WORD!")
    lives = 6
    letter=""
    
    current_word = "-"*len(word)
    while lives>0:
        print(f"You have {lives} lives :: Letter used: {letter} ")
        
        print(f"Current-Word:: {current_word}\n")
        
        guess = input(f"Guess a letter: ").upper()
        letter= letter+" "+ guess
        idx=0
        if guess in word:
            print(f"{guess} is in the word")
            for i in range(len(word)):
                idx = word.find(guess,idx)
                if idx == -1:
                    break
                else:
                    
                    x=list(current_word)
                
                    x[idx] = guess
                    current_word="".join(x)
                    idx+=1
                
                
        else:
            print(f"{guess} is not in the word")
            
            lives-=1
        if word == current_word:
            print("Man lives!!\nYou have matched the word")
            return
    print("Man died!!!\nYou have 0 lives. You lost!! ")
        
    
hang_word=random_words(word)
hangman(hang_word)