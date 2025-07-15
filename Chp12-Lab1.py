#Jackie-Merritt_Chp12-1_7/11/2025

states = {"Ohio": "Columbus", "Washington": "Olympia",
          "North Carolina": "Raleigh", "North Dakota": "Bismarck",
          "New Mexico": "Santa Fe"}

correct = []
incorrect = []

def main():
    print("State Capital's Game\n")
    for code in states:
        print(f'What is the capital of {code}?')
        y = input('Type your answer here: ')
        x = y.title()
        if x == states[code]:
            print("Good Job!\n")
            correct.append('.')
        else:
            print(f'Sorry the answer is {states[code]}\n')
            incorrect.append('.')
    print(f'You answered {len(correct)} correctly and {len(incorrect)} incorrectly.')

if __name__ == '__main__':
    main()
    
