
    'tan': math.tan,
    'sqrt': math.sqrt,
    'log': math.log,  # Natural logarithm
    'log10': math.log10,
    'factorial': math.factorial,
    'exp': math.exp,  # Exponential function (e^x)
    'pi': math.pi,
    'e': math.e,
    'radians': math.radians,  # For converting degrees to radians
    'degrees': math.degrees,  # For converting radians to degrees
}
print("Welcome to the Scientific Calculator!")
print("Enter mathematical expressions using functions like sin(), cos(), sqrt(), etc.")
print("Use 'pi' for π and 'e' for e. Type 'quit' to exit.")
while True:
    try:
        expression = input("\nEnter an expression: ").strip()
        
        if expression.lower() == 'quit':
            print("Exiting the calculator. Goodbye!")
            break
        
        if not expression:  # Skip empty input
            continue
        
        # Evaluate the expression safely
        result = eval(expression, {"__builtins__": None}, allowed_names)
        print("Result:", result)
    
    except Exception as e:
        print("Error: Invalid expression. Please check your input and try again.")
        print("Details:", str(e))