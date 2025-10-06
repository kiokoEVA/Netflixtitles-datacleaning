import pandas as pd

# Load the dataset
df = pd.read_csv('netflix_titles.csv')

# --- Helper function for string matching in the 'country' column ---
def filter_country(df, country_name):
    """Filters a DataFrame where the 'country' column contains the specified country name."""
    # Fills NaN values in 'country' with an empty string for reliable string searching
    return df[df['country'].fillna('').str.contains(country_name, na=False)]

# ====================================================================
# A. Dataset Meta-Information Questions
# ====================================================================

print(f"--- Dataset Meta-Information ---")

# 1. How many rows and columns are contained in the dataset?
rows, cols = df.shape
print(f"1. Rows and columns: {rows} rows and {cols} columns.")

# 2. What datatypes are contained in the dataset?
print(f"\n2. Datatypes:")
print(df.info(verbose=False))

# 3. Is the dataset complete? i.e no missing values?
missing_values = df.isnull().sum()
print(f"\n3. Missing values per column (Is the dataset complete?):")
print(missing_values[missing_values > 0])
if missing_values.sum() == 0:
    print("The dataset is complete (no missing values).")
else:
    print("\nNo, the dataset is NOT complete. Missing values are present in the columns listed above.")

# 4. List the number of Movies and TV Shows among the last 20 rows of the dataset.
last_20_rows = df.tail(20)
type_counts_last_20 = last_20_rows['type'].value_counts()
print(f"\n4. Content Type Count in the last 20 rows:")
print(type_counts_last_20)

# ====================================================================
# B. Data-Specific Questions
# ====================================================================

print(f"\n--- Data-Specific Analysis ---")

# 1. Give the number of all Movies originating from South Africa
sa_movies = filter_country(df[df['type'] == 'Movie'], 'South Africa')
num_sa_movies = len(sa_movies)
print(f"1. Number of all Movies originating from South Africa: {num_sa_movies}")

# 2. What is the description of the movie in the 12th row? (Index 11)
# Note: This is the 12th row of the ENTIRE dataset.
row_12 = df.iloc[11]
print(f"\n2. Description of the content in the 12th row (index 11):")
print(f"   Title: {row_12['title']} ({row_12['type']})")
print(f"   Description: '{row_12['description']}'")

# 3. From these South African movies, list only those released in 2021
sa_movies_2021 = sa_movies[sa_movies['release_year'] == 2021]
sa_movies_2021_titles = sa_movies_2021['title'].tolist()
print(f"\n3. South African movies released in 2021:")
if sa_movies_2021_titles:
    print(sa_movies_2021_titles)
else:
    print("No South African movies were found released in 2021 in the dataset.")

# 4. List the entire cast of all movies released in 2021.
movies_2021 = df[(df['type'] == 'Movie') & (df['release_year'] == 2021)].copy()

# Prepare for output, handling missing cast information
movies_2021_cast = movies_2021[['title', 'cast']].fillna({'cast': 'Cast information missing'}).reset_index(drop=True)

print(f"\n4. Entire cast list for all movies released in 2021 ({len(movies_2021)} movies):")
# The detailed list is saved to a CSV file due to its length.
movies_2021_cast.to_csv('movies_2021_cast.csv', index=False)
print("The list of movies and their cast for 2021 has been saved to 'movies_2021_cast.csv'.")