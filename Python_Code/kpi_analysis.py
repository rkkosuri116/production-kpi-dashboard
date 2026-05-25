import pandas as pd
import matplotlib.pyplot as plt

# Load CSV dataset

df = pd.read_csv('Data/production_data.csv')

print("\n=== Production Dataset ===")
print(df)

# =========================
# KPI CALCULATIONS
# =========================

total_production = df['Production_Count'].sum()

total_defects = df['Defects'].sum()

total_downtime = df['Downtime_Minutes'].sum()

defect_rate = (total_defects / total_production) * 100

average_production = df['Production_Count'].mean()

average_downtime = df['Downtime_Minutes'].mean()

machine_efficiency = (
    df['Production_Count'] /
    (df['Production_Count'] + df['Downtime_Minutes'])
) * 100

print("\n=== KPI SUMMARY ===")

print(f"Total Production: {total_production}")

print(f"Total Defects: {total_defects}")

print(f"Total Downtime: {total_downtime} minutes")

print(f"Defect Rate: {defect_rate:.2f}%")

print(f"Average Production: {average_production:.2f}")

print(f"Average Downtime: {average_downtime:.2f} minutes")

print("\n=== Machine Efficiency ===")
print(machine_efficiency)

# =========================
# MACHINE-WISE ANALYSIS
# =========================

machine_production = df.groupby('Machine_ID')['Production_Count'].sum()

print("\n=== Production by Machine ===")
print(machine_production)

# =========================
# ANOMALY DETECTION
# =========================

print("\n=== Anomaly Detection ===")

# High downtime detection

high_downtime = df[df['Downtime_Minutes'] > 40]

high_downtime.to_csv(
    'Data/high_downtime_events.csv',
    index=False
)

print("\nMachines with High Downtime:")
print(high_downtime)

# High defect detection

high_defects = df[df['Defects'] > 15]

high_defects.to_csv(
    'Data/high_defect_events.csv',
    index=False
)

print("\nMachines with High Defects:")
print(high_defects)

# =========================
# SHIFT-WISE ANALYSIS
# =========================

shift_production = df.groupby('Shift')['Production_Count'].sum()

print("\n=== Shift-wise Production ===")
print(shift_production)

shift_downtime = df.groupby('Shift')['Downtime_Minutes'].sum()

print("\n=== Shift-wise Downtime ===")
print(shift_downtime)

shift_defects = df.groupby('Shift')['Defects'].sum()

print("\n=== Shift-wise Defects ===")
print(shift_defects)

# =========================
# EXPORT KPI SUMMARY
# =========================

summary = pd.DataFrame({
    'Total Production': [total_production],
    'Total Defects': [total_defects],
    'Total Downtime': [total_downtime],
    'Defect Rate': [defect_rate]
})

summary.to_csv('Data/kpi_summary.csv', index=False)

print("\nCSV export successful")

# =========================
# VISUALIZATIONS
# =========================

# Production by Machine

plt.figure()

machine_production.plot(kind='bar')

plt.title('Production by Machine')

plt.xlabel('Machine ID')

plt.ylabel('Production Count')

# Defects by Machine

plt.figure()

defects_by_machine = df.groupby('Machine_ID')['Defects'].sum()

defects_by_machine.plot(kind='bar')

plt.title('Defects by Machine')

plt.xlabel('Machine ID')

plt.ylabel('Defect Count')

# Downtime by Machine

plt.figure()

downtime_by_machine = df.groupby('Machine_ID')['Downtime_Minutes'].sum()

downtime_by_machine.plot(kind='bar')

plt.title('Downtime by Machine')

plt.xlabel('Machine ID')

plt.ylabel('Downtime (minutes)')

# Shift-wise Production

plt.figure()

shift_production.plot(kind='bar')

plt.title('Shift-wise Production')

plt.xlabel('Shift')

plt.ylabel('Production Count')

# Show all plots together

plt.show()