# Beregningsprogram for årlige kostnader ved elbil vs. bensinbil

# Antall kilometer kjørt per år
km_per_aar = 10000  # Antatt årlig kjørelengde

# forsikringskostnader
forsikring_elbil = 5000  # kr/år
forsikring_bensinbil = 7500  # kr/år

# trafikkforsikringsavgift (felles for elbil og bensinbil)
trafikkforsikringsavgift = 8.38 * 365  # kr/år

# Drivstoffkostnader
drivstoffbruk_elbil = 0.2  # kwh/km
strompris = 2.00  # kr/kwh
drivstoffkostnad_elbil = drivstoffbruk_elbil *strompris * km_per_aar

drivstoffkostnad_bensinbil = 1.0 * km_per_aar  # kr/år (1 kr/km for bensinbil)

# Bomavgift
bomavgift_elbil = 0.1 * km_per_aar  # kr/år
bomavgift_bensinbil = 0.3 * km_per_aar  # kr/år

# Totale kostnader per år
totalkostnad_elbil = (forsikring_elbil + trafikkforsikringsavgift + drivstoffkostnad_elbil + bomavgift_elbil) 

totalkostnad_bensinbil = (forsikring_bensinbil + trafikkforsikringsavgift + drivstoffkostnad_bensinbil + bomavgift_bensinbil)

# Kostnadsdifferanse 
kostnadsdifferanse = totalkostnad_bensinbil - totalkostnad_elbil

# Utskrift av resultater
print("Årlige kostnader for elbil:", round(totalkostnad_elbil, 2), "kr")
print("Årlige kostnader for bensinbil:", round(totalkostnad_bensinbil, 2), "kr" )
print("Årlig kostnaddifferanse:", round(kostnadsdifferanse, 2), "kr")