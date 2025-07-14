from sklearn.cluster import KMeans

def cluster_foods(df, n_clusters=6):
    
    nutrient_cols = df.select_dtypes(include=['number']).columns.tolist()
    X = df[nutrient_cols]

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(X)

    return df

def get_similar_foods(df, food_name, top_n=5):
    food_name = food_name.lower()
    target = df[df['name'].str.lower().str.contains(food_name)]
    if target.empty:
        return f"❌ '{food_name}' not found"
    target_cluster = target['cluster'].values[0]
    similar = df[(df['cluster'] == target_cluster) & (~df['name'].str.lower().str.contains(food_name))]
    return similar[['name', 'calories', 'protein', 'fat']].head(top_n)
