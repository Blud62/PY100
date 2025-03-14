import json

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    
    return False

def messages(message):
    return MESSAGES[message]

with open('mortgage_calc_messages.json', 'r') as file:
    MESSAGES = json.load(file)
def main():
    while True:
        # Get the loan amount
        prompt(messages("loan_amount_prompt"))  # Display the prompt
        loan_amount_str = input()  # Get user input
        
        # Validate the input
        if not invalid_number(loan_amount_str):
            loan_amount = float(loan_amount_str)  # Convert to float
            prompt(f"Valid loan amount: {loan_amount}")
            break  # Exit the loop
        else:
            prompt(messages("invalid_input"))  # Display error message

if __name__ == "__main__":
    main()