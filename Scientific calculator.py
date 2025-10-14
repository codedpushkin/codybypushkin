import math

print("=== Scientific Calculator ===")
print("Available operations:")
print("+, -, *, /, ^ (power)")
print("Functions: sqrt(x), sin(x), cos(x), tan(x), asin(x), acos(x), atan(x), log(x), exp(x)")
print("Constants: pi, e")
print("Conversions: deg(x) → convert radians to degrees, rad(x) → convert degrees to radians")
print("Type 'exit' to quit")

while True:
    expr = input("\nEnter expression: ").strip()
    if expr.lower() == "exit":
        print("Calculator closed.")
        break
    try:
        # Replace ^ with ** for power operation
        expr = expr.replace("^", "**")

        # Safe evaluation with math functions
        result = eval(expr, {"__builtins__": None}, {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "asin": math.asin,
            "acos": math.acos,
            "atan": math.atan,
            "log": math.log,
            "exp": math.exp,
            "pi": math.pi,
            "e": math.e,
            "deg": math.degrees,   # radians → degrees
            "rad": math.radians    # degrees → radians
        })
        print("Result:", result)
    except Exception as e:
        print("Error:", e)