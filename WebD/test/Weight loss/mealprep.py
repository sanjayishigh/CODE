# Create a detailed meal plan using college mess menu and additional foods
import pandas as pd

# Mess menu items with estimated nutritional values (per serving)
mess_items = {
    'Food Item': [
        'Idli (2 pieces)', 'Uttapam', 'Sambhar (1 bowl)', 'Coconut Chutney', 'Poori (2 pieces)',
        'Veg Kofta', 'Gobi Semi Gravy', 'Majjige Rice', 'Brinjal Curry', 'Green Moong Curry',
        'Chapathi (1 piece)', 'Rasam (1 bowl)', 'Rice (1 bowl)', 'Dal (1 bowl)', 'Rajma Curry',
        'Paneer Curry', 'Chicken Curry', 'Egg (1 boiled)', 'Milk (1 glass)', 'Banana (1 medium)',
        'Apple (1 medium)', 'Whey Protein (1 scoop)'
    ],
    'Calories': [
        160, 200, 80, 60, 280, 150, 120, 250, 100, 140,
        80, 60, 180, 120, 160, 180, 200, 70, 150, 105,
        80, 100
    ],
    'Protein_g': [
        6, 8, 4, 1, 8, 8, 6, 8, 4, 10,
        3, 2, 4, 8, 12, 15, 25, 6, 8, 1,
        0, 20
    ],
    'Carbs_g': [
        30, 35, 12, 3, 35, 15, 12, 45, 12, 20,
        15, 10, 40, 18, 20, 8, 5, 1, 12, 27,
        21, 2
    ],
    'Fat_g': [
        2, 3, 2, 5, 12, 8, 4, 6, 4, 2,
        1, 1, 1, 2, 4, 8, 8, 5, 8, 0,
        0, 1
    ]
}

mess_df = pd.DataFrame(mess_items)

# Create 15-day meal plan
meal_plan_data = []

# Day 1-5 meal plan
for day in range(1, 6):
    # Early Morning (6:00 AM)
    meal_plan_data.append({
        'Day': day,
        'Meal': 'Early Morning',
        'Time': '6:00 AM',
        'Food': 'Water (2 glasses)',
        'Calories': 0,
        'Protein': 0,
        'Carbs': 0,
        'Fat': 0
    })
    
    # Breakfast (8:00 AM)
    if day % 2 == 1:  # Odd days
        meal_plan_data.append({
            'Day': day,
            'Meal': 'Breakfast',
            'Time': '8:00 AM',
            'Food': '2 Idli + Sambhar + Coconut Chutney',
            'Calories': 300,
            'Protein': 11,
            'Carbs': 45,
            'Fat': 9
        })
    else:  # Even days
        meal_plan_data.append({
            'Day': day,
            'Meal': 'Breakfast',
            'Time': '8:00 AM',
            'Food': '2 Boiled Eggs + 1 Chapathi',
            'Calories': 220,
            'Protein': 15,
            'Carbs': 16,
            'Fat': 11
        })
    
    # Mid-Morning Snack (10:30 AM)
    meal_plan_data.append({
        'Day': day,
        'Meal': 'Mid-Morning',
        'Time': '10:30 AM',
        'Food': 'Whey Protein + Banana',
        'Calories': 205,
        'Protein': 21,
        'Carbs': 29,
        'Fat': 1
    })
    
    # Lunch (1:00 PM)
    lunch_options = [
        {'Food': 'Dal + Rice (1/2 bowl) + Veg Curry + Salad', 'Calories': 400, 'Protein': 18, 'Carbs': 62, 'Fat': 8},
        {'Food': 'Rajma + 2 Chapathi + Salad', 'Calories': 320, 'Protein': 18, 'Carbs': 50, 'Fat': 6},
        {'Food': 'Chicken Curry + 1 Chapathi + Salad', 'Calories': 280, 'Protein': 28, 'Carbs': 20, 'Fat': 9}
    ]
    lunch = lunch_options[day % 3]
    meal_plan_data.append({
        'Day': day,
        'Meal': 'Lunch',
        'Time': '1:00 PM',
        'Food': lunch['Food'],
        'Calories': lunch['Calories'],
        'Protein': lunch['Protein'],
        'Carbs': lunch['Carbs'],
        'Fat': lunch['Fat']
    })
    
    # Evening Snack (4:00 PM)
    meal_plan_data.append({
        'Day': day,
        'Meal': 'Evening',
        'Time': '4:00 PM',
        'Food': '1 Apple + Green Tea',
        'Calories': 80,
        'Protein': 0,
        'Carbs': 21,
        'Fat': 0
    })
    
    # Dinner (8:00 PM)
    dinner_options = [
        {'Food': 'Paneer Curry + 1 Chapathi + Salad', 'Calories': 260, 'Protein': 18, 'Carbs': 23, 'Fat': 9},
        {'Food': 'Dal + 1 Chapathi + Veg Curry + Salad', 'Calories': 280, 'Protein': 14, 'Carbs': 39, 'Fat': 7},
        {'Food': 'Chicken Curry + Salad (no rice/chapathi)', 'Calories': 200, 'Protein': 25, 'Carbs': 5, 'Fat': 8}
    ]
    dinner = dinner_options[day % 3]
    meal_plan_data.append({
        'Day': day,
        'Meal': 'Dinner',
        'Time': '8:00 PM',
        'Food': dinner['Food'],
        'Calories': dinner['Calories'],
        'Protein': dinner['Protein'],
        'Carbs': dinner['Carbs'],
        'Fat': dinner['Fat']
    })
    
    # Pre-bed (10:00 PM)
    meal_plan_data.append({
        'Day': day,
        'Meal': 'Pre-bed',
        'Time': '10:00 PM',
        'Food': '1 Glass Milk (low fat) OR Casein protein',
        'Calories': 120,
        'Protein': 8,
        'Carbs': 12,
        'Fat': 4
    })

# Continue for days 6-15 with similar pattern
for day in range(6, 16):
    # Similar structure but with variations
    # Early Morning
    meal_plan_data.append({
        'Day': day,
        'Meal': 'Early Morning',
        'Time': '6:00 AM',
        'Food': 'Water (2 glasses)',
        'Calories': 0,
        'Protein': 0,
        'Carbs': 0,
        'Fat': 0
    })
    
    # Breakfast variations
    breakfast_options = [
        {'Food': 'Uttapam + Sambhar', 'Calories': 280, 'Protein': 12, 'Carbs': 47, 'Fat': 5},
        {'Food': '2 Egg Omelette + 1 Chapathi', 'Calories': 220, 'Protein': 15, 'Carbs': 16, 'Fat': 11},
        {'Food': 'Oats with milk + fruits', 'Calories': 250, 'Protein': 10, 'Carbs': 35, 'Fat': 6}
    ]
    breakfast = breakfast_options[(day-6) % 3]
    meal_plan_data.append({
        'Day': day,
        'Meal': 'Breakfast',
        'Time': '8:00 AM',
        'Food': breakfast['Food'],
        'Calories': breakfast['Calories'],
        'Protein': breakfast['Protein'],
        'Carbs': breakfast['Carbs'],
        'Fat': breakfast['Fat']
    })
    
    # Mid-morning (only whey for first 10 days as mentioned)
    if day <= 10:
        meal_plan_data.append({
            'Day': day,
            'Meal': 'Mid-Morning',
            'Time': '10:30 AM',
            'Food': 'Whey Protein + Banana',
            'Calories': 205,
            'Protein': 21,
            'Carbs': 29,
            'Fat': 1
        })
    else:
        meal_plan_data.append({
            'Day': day,
            'Meal': 'Mid-Morning',
            'Time': '10:30 AM',
            'Food': '1 Boiled Egg + Green Tea',
            'Calories': 70,
            'Protein': 6,
            'Carbs': 1,
            'Fat': 5
        })
    
    # Continue with lunch, evening, dinner similar to above pattern...
    lunch_options = [
        {'Food': 'Green Moong + Rice (1/2 bowl) + Salad', 'Calories': 320, 'Protein': 14, 'Carbs': 60, 'Fat': 3},
        {'Food': 'Brinjal Curry + 2 Chapathi + Dal', 'Calories': 360, 'Protein': 13, 'Carbs': 57, 'Fat': 7},
        {'Food': 'Chicken Curry + 1 Chapathi + Salad', 'Calories': 280, 'Protein': 28, 'Carbs': 20, 'Fat': 9}
    ]
    lunch = lunch_options[(day-6) % 3]
    meal_plan_data.append({
        'Day': day,
        'Meal': 'Lunch',
        'Time': '1:00 PM',
        'Food': lunch['Food'],
        'Calories': lunch['Calories'],
        'Protein': lunch['Protein'],
        'Carbs': lunch['Carbs'],
        'Fat': lunch['Fat']
    })
    
    # Evening snack
    meal_plan_data.append({
        'Day': day,
        'Meal': 'Evening',
        'Time': '4:00 PM',
        'Food': '1 Apple OR Green Tea',
        'Calories': 80,
        'Protein': 0,
        'Carbs': 21,
        'Fat': 0
    })
    
    # Dinner
    dinner_options = [
        {'Food': 'Dal + Veg Curry + Salad (no chapathi)', 'Calories': 200, 'Protein': 12, 'Carbs': 24, 'Fat': 6},
        {'Food': 'Paneer Curry + Salad (no chapathi)', 'Calories': 180, 'Protein': 15, 'Carbs': 8, 'Fat': 8},
        {'Food': 'Chicken Curry + Salad (no carbs)', 'Calories': 200, 'Protein': 25, 'Carbs': 5, 'Fat': 8}
    ]
    dinner = dinner_options[(day-6) % 3]
    meal_plan_data.append({
        'Day': day,
        'Meal': 'Dinner',
        'Time': '8:00 PM',
        'Food': dinner['Food'],
        'Calories': dinner['Calories'],
        'Protein': dinner['Protein'],
        'Carbs': dinner['Carbs'],
        'Fat': dinner['Fat']
    })
    
    # Pre-bed
    meal_plan_data.append({
        'Day': day,
        'Meal': 'Pre-bed',
        'Time': '10:00 PM',
        'Food': '1 Glass Milk (low fat)',
        'Calories': 120,
        'Protein': 8,
        'Carbs': 12,
        'Fat': 4
    })

# Create DataFrame
meal_plan_df = pd.DataFrame(meal_plan_data)

# Calculate daily totals for first 5 days
daily_totals = []
for day in range(1, 16):
    day_data = meal_plan_df[meal_plan_df['Day'] == day]
    total_calories = day_data['Calories'].sum()
    total_protein = day_data['Protein'].sum()
    total_carbs = day_data['Carbs'].sum()
    total_fat = day_data['Fat'].sum()
    
    daily_totals.append({
        'Day': day,
        'Total_Calories': total_calories,
        'Total_Protein': total_protein,
        'Total_Carbs': total_carbs,
        'Total_Fat': total_fat
    })

daily_totals_df = pd.DataFrame(daily_totals)

print("Daily Nutritional Totals for 15-Day Plan:")
print(daily_totals_df.head(10))

print("\nAverage daily nutrition:")
print(f"Calories: {daily_totals_df['Total_Calories'].mean():.0f}")
print(f"Protein: {daily_totals_df['Total_Protein'].mean():.0f}g")
print(f"Carbs: {daily_totals_df['Total_Carbs'].mean():.0f}g") 
print(f"Fat: {daily_totals_df['Total_Fat'].mean():.0f}g")

# Save to CSV
meal_plan_df.to_csv('15_day_meal_plan.csv', index=False)
daily_totals_df.to_csv('daily_nutrition_totals.csv', index=False)

print("\nMeal plan saved to CSV files!")