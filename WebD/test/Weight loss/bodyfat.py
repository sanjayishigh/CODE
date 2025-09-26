# Let's calculate basic body composition metrics and requirements
weight_kg = 68
height_cm = 173

# Calculate BMI
bmi = weight_kg / (height_cm/100)**2
print(f"Current BMI: {bmi:.1f}")

# Estimate current body fat percentage based on visual assessment
# From the images, appears to be around 15-18% body fat
current_bf_estimate = 16  # percent

# Target body fat for visible abs (men)
target_bf = 10  # percent for clear ab definition

# Calculate fat mass and lean mass
current_fat_mass = weight_kg * (current_bf_estimate / 100)
current_lean_mass = weight_kg - current_fat_mass

print(f"\nCurrent estimated body composition:")
print(f"Body fat: {current_bf_estimate}% ({current_fat_mass:.1f} kg)")
print(f"Lean mass: {current_lean_mass:.1f} kg")

# Target weight calculation
target_weight = current_lean_mass / (1 - target_bf/100)
fat_to_lose = weight_kg - target_weight

print(f"\nTarget body composition for visible abs:")
print(f"Target weight: {target_weight:.1f} kg")
print(f"Fat to lose: {fat_to_lose:.1f} kg")

# 15-day realistic expectations
# Safe fat loss rate: 0.5-1kg per week
max_safe_fat_loss_15days = 2.1  # kg (about 1kg per week)

print(f"\nRealistic 15-day expectations:")
print(f"Maximum safe fat loss: {max_safe_fat_loss_15days:.1f} kg")
print(f"Expected weight after 15 days: {weight_kg - max_safe_fat_loss_15days:.1f} kg")

# Calculate protein needs for muscle preservation
protein_per_kg = 2.2  # grams per kg bodyweight for cutting
daily_protein_need = weight_kg * protein_per_kg

print(f"\nDaily protein requirement: {daily_protein_need:.0f}g")

# Calorie calculations
# Estimated maintenance calories for active male (height 173cm, weight 68kg, age ~20)
bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * 20)  # assuming age 20
maintenance_calories = bmr * 1.6  # moderate activity
cutting_calories = maintenance_calories - 500  # 500 cal deficit

print(f"\nCalorie calculations:")
print(f"Estimated maintenance: {maintenance_calories:.0f} calories")
print(f"Cutting calories: {cutting_calories:.0f} calories")

# Macronutrient breakdown for cutting
protein_calories = daily_protein_need * 4
fat_percentage = 25  # 25% of total calories
fat_calories = cutting_calories * (fat_percentage/100)
fat_grams = fat_calories / 9

carb_calories = cutting_calories - protein_calories - fat_calories
carb_grams = carb_calories / 4

print(f"\nMacronutrient targets:")
print(f"Protein: {daily_protein_need:.0f}g ({protein_calories:.0f} cal)")
print(f"Fat: {fat_grams:.0f}g ({fat_calories:.0f} cal)")
print(f"Carbs: {carb_grams:.0f}g ({carb_calories:.0f} cal)")