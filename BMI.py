def compute_bmi(weight, height):
    """
    Function to compute BMI based on weight (kg) and height (m).
    """
    bmi_value = weight / (height ** 2)
    return bmi_value

def categorize_bmi(bmi_value):
    """
    Function to categorize BMI into groups (underweight, normal weight, overweight).
    """
    if bmi_value < 18.5:
        return "Underweight"
    elif 18.5 <= bmi_value < 24.9:
        return "Normal Weight"
    else:
        return "Overweight"

def run_bmi_calculator():
    """
    Main function to run the BMI calculator.
    """
    print("Body Mass Index (BMI) Calculator")

    # Obtain weight and height input from the user
    try:
        user_weight = float(input("Please enter your weight in kilograms: "))
        user_height = float(input("Please enter your height in meters: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")
        return

    # Check if weight and height are non-negative
    if user_weight <= 0 or user_height <= 0:
        print("Invalid input. Please enter positive values for weight and height.")
        return

    # Calculate BMI
    bmi_result = compute_bmi(user_weight, user_height)

    # Categorize BMI
    bmi_category = categorize_bmi(bmi_result)

    # Display the results
    print(f"\nYour BMI is: {bmi_result:.2f}")
    print(f"You are categorized as: {bmi_category}")

if __name__ == "__main__":
    run_bmi_calculator()
