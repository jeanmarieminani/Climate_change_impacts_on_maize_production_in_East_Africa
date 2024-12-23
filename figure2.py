import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

# Load datasets
temp_prec_data = pd.read_csv(r"east_africa_annual_temp_precip_1750_2023.csv")
maize_data = pd.read_csv(r"east_africa_maize_yields_tonne_ha_1961_2022.csv")
world_avg = pd.read_csv(r"World_clean_maize_data_1961_2022.csv")

# Adjust column names
temp_prec_data.rename(columns={"YEAR": "Year", "ANN_AVG_TEMP": "Temperature", "ANN_AVG_PREC": "Precipitation"}, inplace=True)
maize_data.rename(columns={"Avg_East_Africa_tonne/ha": "East_Africa_Yield"}, inplace=True)
world_avg.rename(columns={"maize_yields_tonne/ha": "World_Yield"}, inplace=True)

# Convert "Year" columns to datetime
temp_prec_data["Year"] = pd.to_datetime(temp_prec_data["Year"], format='%Y')
maize_data["Year"] = pd.to_datetime(maize_data["Year"], format='%Y')
world_avg["Year"] = pd.to_datetime(world_avg["Year"], format='%Y')

# Group data for temperature and precipitation
temp_annual = temp_prec_data.groupby("Year")["Temperature"].mean().reset_index(name="Temperature")
precip_annual = temp_prec_data.groupby("Year")["Precipitation"].sum().reset_index(name="Precipitation")

# Define events
flood_years = [1997, 1998, 2005, 2006, 2018, 2020]
drought_years = [1972, 1973, 1974, 1982, 1983, 1984, 1988, 1989, 1998, 1999, 2000, 2010, 2011, 2012, 2020, 2021, 2022]
El_Niño_events = [1982, 1983, 1997, 1998, 2015, 2016, 2023]
#1972, 1973,
La_Niña_events = [1973, 1974, 1984, 1989, 1998, 1999, 2000, 2010, 2012, 2020, 2021, 2022]
#1983, 2011,
# Define x-axis limits and ticks
xlim_1750 = (pd.Timestamp('1750-01-01'), pd.Timestamp('2023-12-31'))
xlim_1961 = (pd.Timestamp('1961-01-01'), pd.Timestamp('2022-12-31'))
x_ticks_1750 = pd.date_range(start='1750', end='2026', freq='25YE')
x_ticks_1961 = pd.date_range(start='1960', end='2026', freq='5YE')

# Create subplots
fig, axes = plt.subplots(4, 1, figsize=(12, 20), sharex=False)

# Plot 1: Temperature Trends 1750-2023
axes[0].plot(temp_annual["Year"], temp_annual["Temperature"], color='#FF00FF', marker='o', label='Temperature (°C)')
axes[0].set_title("Annual Mean Temperature in Eastern Africa (1750-2023)", fontsize=14)
axes[0].set_ylabel("Temperature (°C)", fontsize=12)
axes[0].grid()
axes[0].legend()
axes[0].set_xlim(*xlim_1750)
axes[0].set_xticks(x_ticks_1750)
axes[0].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# Plot 2: Precipitation Trends 1750-2023 with El Niño and La Niña events
axes[1].plot(precip_annual["Year"], precip_annual["Precipitation"], color='#0000FF', marker='o', label='Precipitation (mm)')
for year in El_Niño_events:
    year_datetime = pd.Timestamp(f"{year}-01-01")
    axes[1].scatter(year_datetime,
                    precip_annual.loc[precip_annual["Year"] == year_datetime, "Precipitation"],
                    color='blue', s=200, label='El Niño' if year == El_Niño_events[0] else "")
for year in La_Niña_events:
    year_datetime = pd.Timestamp(f"{year}-01-01")
    axes[1].scatter(year_datetime,
                    precip_annual.loc[precip_annual["Year"] == year_datetime, "Precipitation"],
                    color='orange', s=200, label='La Niña' if year == La_Niña_events[0] else "")
axes[1].set_title("Annual Precipitation in Eastern Africa (1750-2023) and El Niño/La Niña Events (1961-2023)", fontsize=14)
axes[1].set_ylabel("Precipitation (mm)", fontsize=12)
axes[1].grid()
axes[1].legend()
axes[1].set_xlim(*xlim_1750)
axes[1].set_xticks(x_ticks_1750)
axes[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# Plot 3: Maize Yield with Floods and Droughts 1961-2022
axes[2].plot(maize_data["Year"], maize_data["East_Africa_Yield"], color='#FF7F00', marker='o', label='Maize Yield (tonne/ha)')
for year in flood_years:
    year_datetime = pd.Timestamp(f"{year}-01-01")
    axes[2].scatter(year_datetime,
                    maize_data.loc[maize_data["Year"] == year_datetime, "East_Africa_Yield"],
                    color='blue', s=200, label='Severe Floods' if year == flood_years[0] else "")
for year in drought_years:
    year_datetime = pd.Timestamp(f"{year}-01-01")
    axes[2].scatter(year_datetime,
                    maize_data.loc[maize_data["Year"] == year_datetime, "East_Africa_Yield"],
                    color='red', s=200, label='Severe Droughts' if year == drought_years[0] else "")
axes[2].set_title("Maize Yield in East Africa with Floods and Droughts (1961-2022)", fontsize=14)
axes[2].set_ylabel("Yield (tonne/ha)", fontsize=12)
axes[2].grid()
axes[2].legend()
axes[2].set_xlim(*xlim_1961)
axes[2].set_xticks(x_ticks_1961)
axes[2].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# Plot 4: East Africa vs World Maize Yield 1961-2022
axes[3].plot(maize_data["Year"], maize_data["East_Africa_Yield"], color='magenta', linewidth=3, label='East Africa Average')
axes[3].plot(world_avg["Year"], world_avg["World_Yield"], color='red', linewidth=3, label='World Average')
axes[3].set_title("Maize Yield Trends: East Africa vs World (1961-2022)", fontsize=14)
axes[3].set_ylabel("Yield (tonne/ha)", fontsize=12)
axes[3].set_xlabel("Year", fontsize=12)
axes[3].grid()
axes[3].legend()
axes[3].set_xlim(*xlim_1961)
axes[3].set_xticks(x_ticks_1961)
axes[3].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))


# Add Data source
fig.text(0.05, 0.01, "Data compiled by the authors from various organizations:\n"
         "Temperature and Precipitation: NASA-POWER, NASA-GISS, NOAA, and Berkeley Earth.\n"
         "Maize Yield: FAOSTAT", ha="left", fontsize=10, color="blue")

# Save the figure to a file
fig.savefig("Figure2.png", dpi=300, bbox_inches='tight')

# Adjust layout and avoid overlap
plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.show()
