import random

def meal_plan(df, target_calories, meals):
    df = df.copy()
    plan = []
    total_cal = 0

    for _ in range(meals * 10):  # Try multiple times
        sample = df.sample(meals)
        cal = sample['calories'].sum()

        if abs(cal - target_calories) <= 300:
            plan = sample
            total_cal = cal
            break

    if len(plan) == 0:
        return f"😢 No combination is found {target_calories}±100 Calories"

    return plan[['name', 'calories', 'protein', 'carbohydrate', 'fat']]
