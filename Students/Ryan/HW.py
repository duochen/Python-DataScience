# Python code
import pandas as pd

data = {
    'Planet Name': [
        'LHS 1140 c', 'LHS 1140 b', 'LHS 1140 c', 'GJ 486 b', 'LTT 3780 b',
        'GJ 806 b', 'TOI-1685 b', 'TOI-178 b', 'TOI-178 c', 'TOI-824 b',
        'GJ 143 b', 'WASP-132 c', 'TOI-238 b', 'HD 207897 b', 'HD 207897 b',
        'K2-182 b', 'K2-182 b', 'TOI-2076 b', 'TOI-2076 c', 'TOI-2076 d',
        'TOI-1824 b', 'HIP 97166 b', 'K2-263 b', 'TOI-1444 b', 'HD 63433 c',
        'TOI-1753 b', 'TOI-1776 b', 'TOI-2141 b', 'TOI-1669 c', 'TOI-1451 b',
        'HD 93963 A b', 'TOI-1742 b', 'TOI-559 b', 'TOI-1736 b', 'Kepler-1514 b', 
        'HR 858 d', 'TOI-628 b', 'WASP-18 b', 'Kepler-1704 b', 'TOI-480 b', 
        'NGTS-13 b', 'Kepler-21 b', 'TOI-2145 b', 'TOI-2145 b', 'TOI-2497 b'
    ],
    'Semi-Major Axis': [
        0.027, 0.0946, 0.02675, 0.01713, 0.01195, 0.01406, 0.01138, 0.02607,
        0.037, 0.02177, 0.1915, 0.01833, 0.02118, 0.1163, 0.117, 0.05174,
        0.0526, 0.088, 0.142, 0.199, 0.151, 0.091, 0.2573, 0.0116, 0.146,
        0.059, 0.0378, 0.133, 0.0376, 0.127, 0.02061, 0.154, 0.0723, 0.074,
        0.753, 0.1046, 0.0486, 0.02024, 2.027, 0.077, 0.0549, 0.0427172,
        0.1108, 0.111, 0.1166
    ],
    'Stellar Luminosity': [
        -2.42022, -2.42022, -2.35556, -1.9165, -1.78252, -1.58528, -1.51542,
        -0.87943, -0.87943, -0.70997, -0.6862, -0.57512, -0.47083, -0.4437,
        -0.42136, -0.41117, -0.40782, -0.37779, -0.37779, -0.37779, -0.37263,
        -0.32514, -0.25964, -0.17587, -0.11748, -0.06956, -0.05306, -0.05,
        -0.03574, 0.02449, 0.06781, 0.12123, 0.22737, 0.25, 0.32838, 0.36361,
        0.39445, 0.42813, 0.45179, 0.46195, 0.5172, 0.715, 0.99651, 1.00664,
        1.16732
    ],
}

# Sanity check: all columns equal length (should be 45)
assert len(data['Planet Name']) == len(data['Semi-Major Axis']) == len(data['Stellar Luminosity'])

df = pd.DataFrame(data)

# Derived column
df["Luminosity Star"] = 10 * df["Stellar Luminosity"]

def is_in_Habitable_Zone(row):
    L = 10 * row["Stellar Luminosity"]
    a = row["Semi-Major Axis"]
    r_inner = (L * 0.5) * 0.95
    r_outer = (L * 0.5) * 1.37
    return r_inner <= a <= r_outer

df["In Habitable Zone"] = df.apply(is_in_Habitable_Zone, axis=1)

# ---- display options (put before printing) ----
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)        # show all rows
pd.set_option("display.width", None)           # unlimited line width
pd.set_option("display.max_colwidth", None)    # do not truncate cell text
# -----------------------------------------------

# Print the full table (no truncation)
print(df[["Planet Name", "Stellar Luminosity", "Semi-Major Axis", "In Habitable Zone"]].to_string(index=False))