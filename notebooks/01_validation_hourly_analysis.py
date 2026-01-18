import pandas as pd

# Load sample data
df = pd.read_csv("data/sample_validations.csv")

# Parse datetime
df["Date"] = pd.to_datetime(df["Date"])

# Create date column
df["Fecha"] = df["Date"].dt.date

# Create hourly range label
hour = df["Date"].dt.floor("H")
df["Hora_Rango"] = (
    hour.dt.strftime("%H:00") + " a " +
    (hour + pd.Timedelta(hours=1)).dt.strftime("%H:00")
)

# Aggregate validations
summary = (
    df.groupby(["Fecha", "Hora_Rango", "StopPlaceShortName"], as_index=False)
      .size()
      .rename(columns={"size": "Validaciones"})
)

# Save output
summary.to_csv("outputs/hourly_station_counts.csv", index=False)

print(summary)
