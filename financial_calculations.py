def calculate_compound_interest(principal, rate, time, compound_frequency=1):
    result = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
    return result


if __name__ == "__main__":
    # Basic demo
    result = calculate_compound_interest(1000, 0.05, 2, 4)
    print(f"Compound interest result: {result}")
