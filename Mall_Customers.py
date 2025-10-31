import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
df = pd.read_csv('Mall_Customers.csv')  
# Exploratory Data Analysis
print("=== EDA INSIGHTS ===")
print(f"1. Dataset shape: {df.shape}")
print(f"2. Age groups: Young(20-35): {len(df[df['Age'] <= 35])}, Middle(35-50): {len(df[(df['Age'] > 35) & (df['Age'] <= 50)])}, Senior(50+): {len(df[df['Age'] > 50])}")
print(f"3. Gender distribution: Female: {len(df[df['Gender'] == 'Female'])}, Male: {len(df[df['Gender'] == 'Male'])}")

#  Single feature clustering (Annual Income)
X1 = df[['Annual Income (k$)']]


wcss1, sil_scores1 = [], []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X1)
    wcss1.append(kmeans.inertia_)
    sil_scores1.append(silhouette_score(X1, labels))

optimal_k1 = 3  # Based on elbow and silhouette

kmeans1 = KMeans(n_clusters=optimal_k1, random_state=42)
df['Cluster_Income'] = kmeans1.fit_predict(X1)

# (Income + Spending)
X2 = df[['Annual Income (k$)', 'Spending Score (1-100)']]

wcss2, sil_scores2 = [], []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X2)
    wcss2.append(kmeans.inertia_)
    sil_scores2.append(silhouette_score(X2, labels))

optimal_k2 = 5
kmeans2 = KMeans(n_clusters=optimal_k2, random_state=42)
df['Cluster_Income_Spending'] = kmeans2.fit_predict(X2)

fig, axes = plt.subplots(2, 2, figsize=(15, 10))
# Elbow Method plots
axes[0,0].plot(range(2, 11), wcss1, marker='o')
axes[0,0].set_title('Elbow Method - Income Only')
axes[0,1].plot(range(2, 11), wcss2, marker='o')
axes[0,1].set_title('Elbow Method - Income + Spending')

# Cluster results
axes[1,0].scatter(df['Annual Income (k$)'], [1]*len(df), c=df['Cluster_Income'], cmap='viridis')
axes[1,0].set_title('Single Feature Clustering')
axes[1,1].scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=df['Cluster_Income_Spending'], cmap='viridis')
axes[1,1].set_title('Two Feature Clustering')

plt.tight_layout()
plt.show()

print(f"\nOptimal clusters - Single feature: {optimal_k1}, Two features: {optimal_k2}")
print("\n=== CLUSTER PROFILES ===")
cluster_profile = df.groupby('Cluster_Income_Spending')[['Annual Income (k$)', 'Spending Score (1-100)']].mean()
print(cluster_profile)