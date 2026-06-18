# kaun banega crorepati game

print("Welcome to Kaun Banega Crorepati!")


questions_and_answers = [
    ["What is the capital of India?", "New Delhi", "Patna", "Mumbai", "Chandigarh", 1],

    ["What is the largest planet in our solar system?", "Saturn", "Jupiter", "Earth", "Mars", 2],

    ["Who is the current president of the United States?", "Joe Biden", "Donald Trump", "Barack Obama", "George Bush", 1],

    ["What is the chemical symbol for water?", "NaCl", "CO2", "O2", "H20", 4],

    ["Who wrote the play 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain", 2],

    ["What is the largest mammal?", "Blue Whale", "Elephant", "Giraffe", "Hippopotamus", 1],

    ["What is the currency of Japan?", "Dollar", "Euro", "Yen","Pound", 3]
    ]

Prizes = [10000, 50000, 100000 ]

for question in questions_and_answers:
    print(question[0])
    print("1.", question[1])
    print("2.", question[2])
    print("3.", question[3])
    print("4.", question[4])
 
    answer = int(input("Enter your answer (1/2/3/4): "))

    if answer == question[5]:
        print("Correct!")
    else:
        print("Wrong! The correct answer is:", question[5])
        print("Game Over!")
        break

print("Thank you for playing Kaun Banega Crorepati!")
print("Aap jeet chuke hain 7 crore rupaye!")