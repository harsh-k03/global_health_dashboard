from sklearn.cluster import KMeans

def cluster_countries(df):
    # Select features
    features = df[["Life Expectancy", "Health Expenditure", "Infant Mortality"]]

    # Train model
    kmeans = KMeans(n_clusters=3, random_state=42)
    df["Cluster"] = kmeans.fit_predict(features)

    return df