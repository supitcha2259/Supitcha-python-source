"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the # highest temperature #
- Finds and returns the # lowest temperature #
- # Returns all three values as a tuple #

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""

def get_temperatures():
    temp_list = [22.5, 24.0, 26.5, 23.0, 28.0, 30.4, 19.0] #predefined values
    return temp_list

def analyze_temps(temp_list):
    average = sum(temp_list) / 7

    """หรือ ใช้ loop
    
    for i in range(7):
        sum += temp_list[i]
        
        if temp_list[i] > max:
            max = temp_list[i]
    """

    high = max(temp_list)
    low = min(temp_list)

    return(average,high,low)

def display_analysis(avg, high, low): #avg, high, low คนละตัวกับ def analyze_temps(temp_list)
    print("Temperature Analysis for the week: ")
    print(f"Average: %.1f C" % avg)
    print(f"Highest: %.1f C" % high)
    print(f"Lowest: %.1f C" % low)

temps = get_temperatures()
print(temps)
result = analyze_temps()
print(result)
display_analysis(result[0],result[1],result[2])