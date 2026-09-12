import pandas as pd

df = pd.read_csv("startup_funding.csv")

print(df.head())
print(df.columns)
print(df.shape)
print(df.info())
print(df.isnull().sum())

print("\n--- CITY VALUES ---")
print(df['City  Location'].value_counts(dropna=False))

print("\nNumber of unique city values:")
print(df['City  Location'].nunique(dropna=True))

print(df['City  Location'].value_counts(dropna=False).to_string())
print("\n--- MULTIPLE / COMPLEX CITY VALUES ---")

city_values = df['City  Location'].dropna().unique()

for city in sorted(city_values):
    if '/' in city:
        print(city)

#City names changed

city_mapping = {
    'Bangalore': 'Bengaluru',
    'Gurgaon': 'Gurugram',
    'Ahemadabad': 'Ahmedabad',
    'Ahemdabad': 'Ahmedabad',
    'Kolkatta': 'Kolkata',
    'Bhubneswar': 'Bhubaneswar',
    'Nw Delhi': 'New Delhi',
    'Kormangala': 'Bengaluru',
    'Andheri': 'Mumbai',
    'Chembur': 'Mumbai',
    'Taramani': 'Chennai',
    'Delhi': 'New Delhi'
}

df['City  Location'] = df['City  Location'].replace(city_mapping)
print(df['City  Location'].value_counts(dropna=False).to_string())

complex_cities = [
    'Mumbai/Bengaluru',
    'India/US',
    'Bangalore/ Bangkok',
    'Bangalore / SFO',
    'New Delhi / US',
    'Bengaluru and Gurugram',
    'India/Singapore',
    'New York, Bengaluru',
    'Delhi & Cambridge',
    'SFO / Bangalore',
    'Seattle / Bangalore',
    'Pune/Seattle',
    'Pune / Dubai',
    'Mumbai / UK',
    'Hyderabad/USA',
    'Bangalore / Palo Alto',
    'Mumbai / NY',
    'USA/India',
    'Goa/Hyderabad',
    'Noida / Singapore',
    'Chennai/ Singapore',
    'Pune / Singapore',
    'Bangalore / San Mateo',
    'New York/ India',
    'US/India',
    'Gurgaon / SFO',
    'Bangalore / USA',
    'New Delhi/ Houston',
    'Mumbai / Global',
    'India / US',
    'New Delhi / California',
    'Dallas / Hyderabad'
]

print(df[df['City  Location'].isin(complex_cities)][
    ['Startup Name', 'City  Location', 'Industry Vertical', 'Amount in USD']
].to_string(index=False))



# Create a cleaned city column
df['City_Clean'] = df['City  Location']

# Standardize obvious spelling/name variations
city_mapping = {
    'Bangalore': 'Bengaluru',
    'Gurgaon': 'Gurugram',
    'Ahemadabad': 'Ahmedabad',
    'Ahemdabad': 'Ahmedabad',
    'Kolkatta': 'Kolkata',
    'Bhubneswar': 'Bhubaneswar',
    'Delhi': 'New Delhi',
    'Nw Delhi': 'New Delhi',
    'Kormangala': 'Bengaluru',
    'Andheri': 'Mumbai',
    'Chembur': 'Mumbai',
    'Taramani': 'Chennai'
}

df['City_Clean'] = df['City_Clean'].replace(city_mapping)
complex_city_mapping = {
    'Mumbai/Bengaluru': 'Mumbai',
    'Bengaluru and Gurugram': 'Bengaluru',
    'New York, Bengaluru': 'Bengaluru',

    'Bangalore/ Bangkok': 'Bengaluru',
    'Bangalore / SFO': 'Bengaluru',
    'SFO / Bangalore': 'Bengaluru',
    'Seattle / Bangalore': 'Bengaluru',
    'Bangalore / Palo Alto': 'Bengaluru',
    'Bangalore / San Mateo': 'Bengaluru',
    'Bangalore / USA': 'Bengaluru',

    'New Delhi / US': 'New Delhi',
    'New Delhi/ Houston': 'New Delhi',
    'New Delhi / California': 'New Delhi',

    'Gurgaon / SFO': 'Gurugram',

    'Hyderabad/USA': 'Hyderabad',
    'Goa/Hyderabad': 'Goa',
    'Dallas / Hyderabad': 'Hyderabad',

    'Noida / Singapore': 'Noida',

    'Pune / US': 'Pune',
    'Pune/Seattle': 'Pune',
    'Pune / Dubai': 'Pune',
    'Pune / Singapore': 'Pune',

    'Mumbai / UK': 'Mumbai',
    'Mumbai / NY': 'Mumbai',
    'Mumbai / Global': 'Mumbai',

    'Chennai/ Singapore': 'Chennai',

    'India/US': 'Unknown',
    'India / US': 'Unknown',
    'India/Singapore': 'Unknown',
    'USA/India': 'Unknown',
    'US/India': 'Unknown',
    'New York/ India': 'Unknown'
}

df['City_Clean'] = df['City_Clean'].replace(complex_city_mapping)

non_city_mapping = {
    'Haryana': 'Unknown',
    'Karnataka': 'Unknown',
    'Kerala': 'Unknown',
    'Uttar Pradesh': 'Unknown',
    'India': 'Unknown',
    'US': 'Unknown',
    'USA': 'Unknown',
    'California': 'Unknown'
}

df['City_Clean'] = df['City_Clean'].replace(non_city_mapping)

# Missing city values
df['City_Clean'] = df['City_Clean'].fillna('Unknown')

print("\n--- CLEANED CITY VALUES ---")
print(df['City_Clean'].value_counts().to_string())

print("\nOriginal city column:")
print(df['City  Location'].head(20))

print("\nClean city column:")
print(df['City_Clean'].head(20))

print(df['City_Clean'].value_counts().to_string())
print("\n--- VALUES STILL CONTAINING / ---")
print(df[df['City_Clean'].astype(str).str.contains('/', regex=False)]['City_Clean'].value_counts())
print("\nMissing values in City_Clean:")
print(df['City_Clean'].isnull().sum())



# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r'\s+', '_', regex=True)
)

# Rename columns with clearer names / fix typos
df.rename(columns={
    'date_dd/mm/yyyy': 'date',
    'investmentntype': 'investment_type'
}, inplace=True)

# Check cleaned column names
print(df.columns.tolist())

#INDUSTRY VERTICAL VALUES

print("\n--- INDUSTRY VERTICAL VALUES ---")
print(df['industry_vertical'].value_counts(dropna=False).to_string())

print("\nNumber of unique Industry Verticals:")
print(df['industry_vertical'].nunique(dropna=True))

print("\nMissing Industry Verticals:")
print(df['industry_vertical'].isnull().sum())

# Create a cleaned industry column
df['industry_clean'] = df['industry_vertical'].astype('string')

# Remove leading and trailing spaces
df['industry_clean'] = df['industry_clean'].str.strip()

# Replace multiple spaces with one space
df['industry_clean'] = df['industry_clean'].str.replace(
    r'\s+', ' ', regex=True
)

# Check the result
print("\n--- CLEANED INDUSTRY VALUES ---")
print(df['industry_clean'].value_counts(dropna=False).to_string())

print("\nNumber of unique industries:")
print(df['industry_clean'].nunique(dropna=True))

print("\nMissing industries:")
print(df['industry_clean'].isna().sum())




# ==========================================
# STEP 4 - INDUSTRY VERTICAL CLEANING
# ==========================================

# Create a separate cleaned column
df['industry_clean'] = df['industry_vertical'].astype('string')

# ------------------------------------------
# 1. Basic text cleaning
# ------------------------------------------

# Remove leading/trailing spaces
df['industry_clean'] = df['industry_clean'].str.strip()

# Replace multiple spaces with one space
df['industry_clean'] = df['industry_clean'].str.replace(
    r'\s+', ' ', regex=True
)

# Remove unwanted non-breaking space characters
df['industry_clean'] = df['industry_clean'].str.replace(
    r'\\xc2\\xa0', ' ', regex=True
)

# Remove unwanted newline characters
df['industry_clean'] = df['industry_clean'].str.replace(
    '\n', ' ', regex=False
)

# Remove extra spaces again
df['industry_clean'] = df['industry_clean'].str.replace(
    r'\s+', ' ', regex=True
).str.strip()


# ------------------------------------------
# 2. Standardize obvious industry variations
# ------------------------------------------

industry_mapping = {

    # E-Commerce variations
    'eCommerce': 'E-Commerce',
    'ECommerce': 'E-Commerce',
    'E-Commerce': 'E-Commerce',
    'E-commerce': 'E-Commerce',
    'Ecommerce': 'E-Commerce',
    'ecommerce': 'E-Commerce',
    'eCommece': 'E-Commerce',

    # EdTech variations
    'Ed-Tech': 'EdTech',
    'E-tech': 'EdTech',
    'Edtech': 'EdTech',
    'Ed-tech': 'EdTech',
    'Ed-Tech Platform': 'EdTech',

    # FinTech variations
    'FinTech': 'FinTech',
    'Fintech': 'FinTech',
    'Fin-Tech': 'FinTech',
    'Financial Tech': 'FinTech',

    # IT variations
    'IT': 'Information Technology',
    'Information Technology': 'Information Technology',

    # SaaS variations
    'SaaS': 'SaaS',
    'Saas': 'SaaS',

    # Healthcare variations
    'Healthcare': 'Healthcare',
    'healthcare': 'Healthcare',
    'Health Care': 'Healthcare',

    # Consumer Internet variations
    'Consumer Internet': 'Consumer Internet',
    'Consumer internet': 'Consumer Internet',
    'Consumer Interne': 'Consumer Internet',

    # Food & Beverage variations
    'Food & Beverage': 'Food & Beverage',
    'Food and Beverage': 'Food & Beverage',
    'Food & Beverages': 'Food & Beverage',
    'Food and Beverages': 'Food & Beverage',

    # Transportation variations
    'Transportation': 'Transportation',
    'Transport': 'Transportation',

    # Automobile variations
    'Automobile': 'Automobile',
    'Automotive': 'Automobile',
    'Auto': 'Automobile',

    # Logistics
    'Logistics': 'Logistics',

    # Fintech spelling
    'Fiinance': 'Finance'
}

df['industry_clean'] = df['industry_clean'].replace(industry_mapping)


# ------------------------------------------
# 3. Handle missing industry values
# ------------------------------------------

df['industry_clean'] = df['industry_clean'].fillna('Unknown')


# ------------------------------------------
# 4. Display results
# ------------------------------------------

print("\n--- CLEANED INDUSTRY VALUES ---")
print(
    df['industry_clean']
    .value_counts(dropna=False)
    .to_string()
)

print("\nNumber of unique industries after cleaning:")
print(df['industry_clean'].nunique())

print("\nMissing values in industry_clean:")
print(df['industry_clean'].isna().sum())


# ==========================================
# STEP 5 - CLEAN INVESTMENT AMOUNT
# ==========================================

# Create a separate cleaned amount column
df['amount_clean'] = df['amount_in_usd'].astype('string')

# Remove commas
df['amount_clean'] = df['amount_clean'].str.replace(',', '', regex=False)

# Remove leading/trailing spaces
df['amount_clean'] = df['amount_clean'].str.strip()

# Convert to numeric
# Invalid values will become NaN
df['amount_clean'] = pd.to_numeric(
    df['amount_clean'],
    errors='coerce'
)

# Check the result
print("\n--- AMOUNT CLEANING ---")
print(df[['amount_in_usd', 'amount_clean']].head(20).to_string())

print("\nAmount data type:")
print(df['amount_clean'].dtype)

print("\nMissing amounts:")
print(df['amount_clean'].isna().sum())

# Find original amount values that could not be converted to numbers
invalid_amounts = df[
    df['amount_in_usd'].notna() & df['amount_clean'].isna()
]

print("\n--- INVALID AMOUNT VALUES ---")
print(invalid_amounts['amount_in_usd'].value_counts(dropna=False).to_string())

print("\nNumber of invalid amount entries:")
print(len(invalid_amounts))


# ==========================================
# STEP 5 - CLEAN INVESTMENT AMOUNT
# ==========================================

# Create a separate cleaned amount column
df['amount_clean'] = df['amount_in_usd'].astype('string')

# Remove unwanted encoded characters
df['amount_clean'] = (
    df['amount_clean']
    .str.replace(r'\\xc2\\xa0', '', regex=True)
    .str.replace(r'\xc2\xa0', '', regex=True)
)

# Remove commas
df['amount_clean'] = df['amount_clean'].str.replace(',', '', regex=False)

# Remove leading/trailing spaces
df['amount_clean'] = df['amount_clean'].str.strip()

# Remove + sign from values such as 14,342,000+
df['amount_clean'] = df['amount_clean'].str.replace(
    '+', '', regex=False
)

# Convert to numeric
# N/A, undisclosed and unknown will become NaN
df['amount_clean'] = pd.to_numeric(
    df['amount_clean'],
    errors='coerce'
)

# Check the result
print("\n--- AMOUNT CLEANING ---")

print("\nOriginal vs Cleaned:")
print(
    df[['amount_in_usd', 'amount_clean']]
    .head(20)
    .to_string(index=False)
)

print("\nAmount data type:")
print(df['amount_clean'].dtype)

print("\nMissing amounts:")
print(df['amount_clean'].isna().sum())

print("\nInvalid/unconverted original values:")
print(
    df[
        df['amount_in_usd'].notna() &
        df['amount_clean'].isna()
    ]['amount_in_usd']
    .value_counts()
    .to_string()
)




# ==========================================
# STEP 5 - FINAL AMOUNT CLEANING
# ==========================================

# Create cleaned amount column
df['amount_clean'] = df['amount_in_usd'].astype('string')

# Remove literal encoded characters
df['amount_clean'] = (
    df['amount_clean']
    .str.replace(r'\\x[a-fA-F0-9]{2}', '', regex=True)
)

# Remove commas
df['amount_clean'] = df['amount_clean'].str.replace(
    ',', '', regex=False
)

# Remove + sign
df['amount_clean'] = df['amount_clean'].str.replace(
    '+', '', regex=False
)

# Remove leading/trailing spaces
df['amount_clean'] = df['amount_clean'].str.strip()

# Convert to numeric
df['amount_clean'] = pd.to_numeric(
    df['amount_clean'],
    errors='coerce'
)

# ------------------------------------------
# Validation
# ------------------------------------------

# ==========================================
# STEP 5 - FINAL AMOUNT CLEANING
# ==========================================

# Create cleaned amount column
df['amount_clean'] = df['amount_in_usd'].astype('string')

# Extract only the numeric characters
# This handles:
# 20,00,00,000
# \xc2\xa020,000,000
# 14,342,000+
# etc.

df['amount_clean'] = (
    df['amount_clean']
    .str.replace(',', '', regex=False)
    .str.extract(r'(\d+(?:\.\d+)?)', expand=False)
)

# Convert to numeric
df['amount_clean'] = pd.to_numeric(
    df['amount_clean'],
    errors='coerce'
)

# ==========================================
# VALIDATION
# ==========================================

print("\n--- FINAL AMOUNT CLEANING ---")

print("\nData type:")
print(df['amount_clean'].dtype)

print("\nMissing amounts:")
print(df['amount_clean'].isna().sum())

print("\nRemaining invalid values:")
print(
    df[
        df['amount_in_usd'].notna() &
        df['amount_clean'].isna()
    ]['amount_in_usd']
    .value_counts()
    .to_string()
)

print("\nPreviously invalid numeric values:")
print(
    df[
        df['amount_in_usd'].astype('string').str.contains(
            r'\\x|\\xc2',
            regex=True,
            na=False
        )
    ][['amount_in_usd', 'amount_clean']]
    .to_string(index=False)
)




# ==========================================
# STEP 5 - CORRECT AMOUNT CLEANING
# ==========================================

# Create cleaned amount column
df['amount_clean'] = df['amount_in_usd'].astype('string')

# Remove the literal encoded characters
df['amount_clean'] = df['amount_clean'].str.replace(
    r'\\x[cC]2\\x[aA]0',
    '',
    regex=True
)

# Remove commas
df['amount_clean'] = df['amount_clean'].str.replace(
    ',',
    '',
    regex=False
)

# Remove + sign
df['amount_clean'] = df['amount_clean'].str.replace(
    '+',
    '',
    regex=False
)

# Remove spaces
df['amount_clean'] = df['amount_clean'].str.strip()

# Convert to numeric
df['amount_clean'] = pd.to_numeric(
    df['amount_clean'],
    errors='coerce'
)

# ==========================================
# VALIDATION
# ==========================================

print("\n--- FINAL AMOUNT CLEANING ---")

print("\nPreviously problematic values:")
print(
    df[
        df['amount_in_usd'].astype('string').str.contains(
            r'\\x[cC]2\\x[aA]0',
            regex=True,
            na=False
        )
    ][['amount_in_usd', 'amount_clean']]
    .to_string(index=False)
)

print("\nRemaining invalid values:")
print(
    df[
        df['amount_in_usd'].notna() &
        df['amount_clean'].isna()
    ]['amount_in_usd']
    .value_counts()
    .to_string()
)

print("\nMissing amounts:")
print(df['amount_clean'].isna().sum())

print("\nData type:")
print(df['amount_clean'].dtype)




# ==========================================
# STEP 6 - DATE CLEANING
# ==========================================

# Convert date column to datetime
df['date_clean'] = pd.to_datetime(
    df['date'],
    dayfirst=True,
    errors='coerce'
)

print("\n--- DATE CLEANING ---")

print("\nOriginal vs Cleaned:")
print(
    df[['date', 'date_clean']]
    .head(20)
    .to_string(index=False)
)

print("\nDate data type:")
print(df['date_clean'].dtype)

print("\nInvalid/missing dates:")
print(df['date_clean'].isna().sum())



# ==========================================
# CHECK INVALID DATES
# ==========================================

invalid_dates = df[
    df['date'].notna() & df['date_clean'].isna()
]

print("\n--- INVALID DATE VALUES ---")
print(
    invalid_dates['date']
    .value_counts(dropna=False)
    .to_string()
)

print("\nNumber of invalid date entries:")
print(len(invalid_dates))

print("\nRows with invalid dates:")
print(
    invalid_dates[
        ['sr_no', 'startup_name', 'date']
    ].to_string(index=False)
)

print("\n--- MISSING DATE VALUES ---")
print("Missing original dates:", df['date'].isna().sum())




# ==========================================
# STEP 6.2 - FIX INVALID DATES
# ==========================================

date_corrections = {
    '05/072018': '05/07/2018',
    '01/07/015': '01/07/2015',
    '12/05.2015': '12/05/2015',
    '13/04.2015': '13/04/2015',
    '15/01.2015': '15/01/2015',
    '22/01//2015': '22/01/2015'
}

# Correct the original date values
df['date_fixed'] = df['date'].replace(date_corrections)

# Convert corrected dates to datetime
df['date_clean'] = pd.to_datetime(
    df['date_fixed'],
    dayfirst=True,
    errors='coerce'
)

# ==========================================
# VALIDATION
# ==========================================

print("\n--- DATE VALIDATION ---")

print("\nCorrected dates:")
print(
    df[
        df['date'].isin(date_corrections.keys())
    ][['sr_no', 'startup_name', 'date', 'date_fixed', 'date_clean']]
    .to_string(index=False)
)

print("\nInvalid dates remaining:")
print(df['date_clean'].isna().sum())

print("\nDate data type:")
print(df['date_clean'].dtype)





# ==========================================
# STEP 7 - MISSING VALUE ANALYSIS
# ==========================================

print("\n--- MISSING VALUES ---")

missing_count = df.isna().sum()
missing_percent = (df.isna().sum() / len(df)) * 100

missing_summary = pd.DataFrame({
    'Missing_Count': missing_count,
    'Missing_Percentage': missing_percent.round(2)
})

print(missing_summary)

print("\n--- CLEANED COLUMN MISSING VALUES ---")

print("city_clean:", df['city_clean'].isna().sum())
print("industry_clean:", df['industry_clean'].isna().sum())
print("amount_clean:", df['amount_clean'].isna().sum())
print("date_clean:", df['date_clean'].isna().sum())


# ==========================================
# STEP 7 - HANDLE MISSING VALUES
# ==========================================

# Fill categorical fields where "Unknown" is meaningful
df['subvertical'] = df['subvertical'].fillna('Unknown')

df['investors_name'] = df['investors_name'].fillna('Unknown')

df['investment_type'] = df['investment_type'].fillna('Unknown')

# Keep amount_clean as NaN
# Missing investment amount should NOT be treated as zero

# Keep remarks as NaN
# Remarks are optional descriptive information

# ==========================================
# VALIDATION
# ==========================================

print("\n--- MISSING VALUES AFTER CLEANING ---")

missing_count = df.isna().sum()
missing_percent = (missing_count / len(df)) * 100

missing_summary = pd.DataFrame({
    'Missing_Count': missing_count,
    'Missing_Percentage': missing_percent.round(2)
})

print(missing_summary.to_string())



# ==========================================
# STEP 8 - DUPLICATE CHECK
# ==========================================

# Check completely identical rows
duplicate_rows = df.duplicated().sum()

print("\n--- DUPLICATE CHECK ---")
print("Completely duplicate rows:", duplicate_rows)

# Show duplicate rows if any
if duplicate_rows > 0:
    print("\nDuplicate rows:")
    print(
        df[df.duplicated(keep=False)]
        .sort_values('sr_no')
        .to_string(index=False)
    )
else:
    print("No completely identical duplicate rows found.")


# Check duplicate Startup + Date combinations
startup_date_duplicates = df.duplicated(
    subset=['startup_name', 'date_clean'],
    keep=False
).sum()

print("\nDuplicate Startup + Date combinations:",
      startup_date_duplicates)



# ==========================================
# STEP 9 - FINAL DATA QUALITY VALIDATION
# ==========================================

print("\n========================================")
print("       FINAL DATA QUALITY REPORT")
print("========================================")

# Dataset shape
print("\nDataset shape:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Duplicate check
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Missing values
print("\nMissing values:")
print(df.isna().sum().to_string())

# Data types
print("\nData types:")
print(df.dtypes.to_string())

# Unique values
print("\nUnique values:")
print(df.nunique().to_string())

# Cleaned city check
print("\nTop cleaned cities:")
print(df['city_clean'].value_counts().head(15).to_string())

# Cleaned industry check
print("\nTop cleaned industries:")
print(df['industry_clean'].value_counts().head(15).to_string())

# Amount summary
print("\nInvestment amount summary:")
print(df['amount_clean'].describe())

# Date range
print("\nDate range:")
print("Earliest:", df['date_clean'].min())
print("Latest:", df['date_clean'].max())

print("\n========================================")
print("       VALIDATION COMPLETE")
print("========================================")



# ==========================================
# STEP 10 - CREATE FINAL CLEANED DATASET
# ==========================================

# Remove only temporary helper column
df_clean = df.drop(columns=['date_fixed'])

# Reorder columns for easier analysis
df_clean = df_clean[
    [
        'sr_no',
        'date_clean',
        'startup_name',
        'industry_clean',
        'subvertical',
        'city_clean',
        'investors_name',
        'investment_type',
        'amount_clean',
        'remarks',
        'date',
        'industry_vertical',
        'city_location',
        'amount_in_usd'
    ]
]

# Save cleaned dataset
output_file = 'startup_funding_cleaned.csv'

df_clean.to_csv(
    output_file,
    index=False
)

print("\n========================================")
print("FINAL CLEANED DATASET CREATED")
print("========================================")

print("\nFile:", output_file)
print("Rows:", df_clean.shape[0])
print("Columns:", df_clean.shape[1])

print("\nColumns:")
print(df_clean.columns.tolist())

print("\nFirst 5 rows:")
print(df_clean.head().to_string(index=False))





# ==========================================
# CHECK INDUSTRY VALUES
# ==========================================

print("\n--- ALL INDUSTRY VALUES ---")

industry_counts = (
    df['industry_clean']
    .value_counts(dropna=False)
)

print(industry_counts.to_string())

print("\nNumber of unique industries:")
print(df['industry_clean'].nunique())



# ==========================================
# CHECK INDUSTRY VALUES
# ==========================================

industry_counts = df['industry_clean'].value_counts(dropna=False)

print("\n--- ALL INDUSTRY VALUES ---")
print(industry_counts.to_string())

print("\nNumber of unique industries:")
print(df['industry_clean'].nunique())


# Show industries that occur only once
rare_industries = df['industry_clean'].value_counts()

print("\n--- INDUSTRIES WITH ONLY 1 RECORD ---")
print(rare_industries[rare_industries == 1].to_string())

print("\nNumber of single-occurrence industries:")
print((rare_industries == 1).sum())




# ==========================================
# STEP 11 - FINAL CLEAN DATASET
# ==========================================

# Remove temporary/original helper columns
final_df = df.drop(columns=[
    'date_fixed'
])

# Make sure cleaned columns are in the correct format
final_df['date_clean'] = pd.to_datetime(
    final_df['date_clean'],
    errors='coerce'
)

final_df['amount_clean'] = pd.to_numeric(
    final_df['amount_clean'],
    errors='coerce'
)

# Final duplicate check
print("\n--- FINAL CHECK ---")
print("Rows:", len(final_df))
print("Columns:", len(final_df.columns))
print("Duplicate rows:", final_df.duplicated().sum())
print("Missing dates:", final_df['date_clean'].isna().sum())
print("Missing cities:", final_df['city_clean'].isna().sum())
print("Missing industries:", final_df['industry_clean'].isna().sum())

# Save final dataset
final_df.to_csv(
    'startup_funding_cleaned_final.csv',
    index=False
)

print("\n========================================")
print("PART A CLEANING COMPLETE")
print("========================================")
print("Saved as: startup_funding_cleaned_final.csv")





# ==========================================
# STEP 11 - FINAL CLEAN DATASET
# ==========================================

# Remove temporary/original helper columns
final_df = df.drop(columns=[
    'date_fixed'
])

# Make sure cleaned columns are in the correct format
final_df['date_clean'] = pd.to_datetime(
    final_df['date_clean'],
    errors='coerce'
)

final_df['amount_clean'] = pd.to_numeric(
    final_df['amount_clean'],
    errors='coerce'
)

# Final duplicate check
print("\n--- FINAL CHECK ---")
print("Rows:", len(final_df))
print("Columns:", len(final_df.columns))
print("Duplicate rows:", final_df.duplicated().sum())
print("Missing dates:", final_df['date_clean'].isna().sum())
print("Missing cities:", final_df['city_clean'].isna().sum())
print("Missing industries:", final_df['industry_clean'].isna().sum())

# Save final dataset
final_df.to_csv(
    'startup_funding_cleaned_final.csv',
    index=False
)

print("\n========================================")
print("PART A CLEANING COMPLETE")
print("========================================")
print("Saved as: startup_funding_cleaned_final.csv")