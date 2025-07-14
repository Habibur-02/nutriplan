def recommend_food(df, cond, top_n=10):
    df = df.copy()

    cond = cond.lower()

    if cond == "obesity":
        df["score"] = (1 - df["calories"]) + (1 - df["saturated_fatty_acids"]) + (1 - df["sugars"]) + df["fiber"] + df["protein"]

    elif cond == "type 2 diabetes":
        df["score"] = (1 - df["sugars"]) + (1 - df["carbohydrate"]) + (1 - df["saturated_fat"]) + df["fiber"] + df["protein"]

    elif cond == "high cholesterol (hyperlipidemia)":
        df["score"] = (1 - df["saturated_fat"]) + (1 - df["fatty_acids_total_trans"]) + df["fiber"] + df["protein"]

    elif cond == "hypertension (high blood pressure)":
        df["score"] = (1 - df["sodium"]) + (1 - df["saturated_fat"]) + df["potassium"] + df["magnesium"] + df["calcium"] + df["fiber"]

    elif cond == "non-alcoholic fatty liver disease (nafld)":
        df["score"] = (1 - df["fructose"]) + (1 - df["saturated_fat"]) + df["fiber"] + df["protein"]

    elif cond == "coronary artery disease (heart disease)":
        df["score"] = (1 - df["saturated_fat"]) + (1 - df["fatty_acids_total_trans"]) + df["fiber"] + df["potassium"] + df["vitamin_c"] + df["vitamin_e"]

    elif cond == "stroke":
        df["score"] = (1 - df["sodium"]) + (1 - df["saturated_fat"]) + df["fiber"] + df["potassium"] + df["vitamin_c"] + df["vitamin_e"]

    elif cond == "metabolic syndrome":
        df["score"] = (1 - df["sugars"]) + (1 - df["carbohydrate"]) + (1 - df["saturated_fat"]) + df["fiber"] + df["protein"]

    elif cond == "chronic kidney disease (early stage)":
        df["score"] = (1 - df["sodium"]) + (1 - df["phosphorous"]) + (1 - df["potassium"]) + (1 - df["protein"]) + df["fiber"]

    elif cond == "gastroesophageal reflux disease (gerd)":
        df["score"] = (1 - df["saturated_fat"]) + (1 - df["caffeine"]) + df["fiber"]

    elif cond == "fatty liver (alcoholic / non-alcoholic)":
        df["score"] = (1 - df["alcohol"]) + (1 - df["sugars"]) + (1 - df["saturated_fat"]) + df["fiber"] + df["protein"]

    elif cond == "gout":
        df["score"] = (1 - df["protein"]) + df["water"] + df["fiber"]  # purine proxy

    elif cond == "osteoporosis":
        df["score"] = df["calcium"] + df["vitamin_d"] + df["magnesium"] + df["vitamin_k"] + df["protein"]

    elif cond == "pcos (polycystic ovary syndrome)":
        df["score"] = (1 - df["carbohydrate"]) + (1 - df["saturated_fat"]) + df["fiber"] + df["protein"]

    elif cond == "sleep apnea":
        df["score"] = (1 - df["calories"]) + df["fiber"] + df["protein"]

    elif cond == "fatigue / chronic fatigue syndrome":
        df["score"] = df["iron"] + df["vitamin_b12"] + df["thiamin"] + df["carbohydrate"] + df["water"] + df["protein"]

    elif cond == "depression & anxiety":
        df["score"] = df["vitamin_b12"] + df["folate"] + df["vitamin_c"] + df["vitamin_e"] + df["magnesium"] + df["protein"]

    else:
        raise ValueError(f"Condition '{cond}' not recognized.")

    return df.sort_values("score", ascending=False)[["name", "score"]].head(top_n)
