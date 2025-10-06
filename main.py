import os, json




def handle_equations():
    try:
        with open('input.json', 'r') as f:
            data = json.load(f)
            data.append(user_input)
            json.dump(data, f)

            print(data)
    except Exception as e:
        print("Error:", e)

while(True):
    print("Enter Equations and Arrays into JSON file. Code will handle the rest.")
    user_input = input("Please enter your equations and arrays then press Enter (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    else:
        handle_equations()