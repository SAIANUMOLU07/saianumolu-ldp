def determine_winner(sequence):
    
    odd_count = 0
    even_count = 0
    
    for number in sequence:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    if odd_count % 2 == 0:
        return "Alice"  
    else:
        return "Bob"    


user_input = input("Enter a sequence of numbers separated by spaces: ")
sequence = list(map(int, user_input.split()))
winner = determine_winner(sequence)
print(f"The winner is: {winner}")
