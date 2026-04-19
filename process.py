import csv
import datetime

input_file = "Estados.txt"
output_file = "resultado.txt"
log_file = "backup.log"

count = 0
results = []

with open(input_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        temp = int(row["Temperatura"])
        humidity = int(row["Humedad"])
        cost = int(row["Costo_Alojamiento"]) + int(row["Costo_Transporte"])

        if 20 <= temp <= 28 and humidity <= 70 and cost <= 2000:
            results.append(f"{row['Estado']} | Temp:{temp}°C | Hum:{humidity}% | Cost:{cost}")
            count += 1

with open(output_file, "w", encoding='utf-8') as f:
    f.write("\n".join(results))

with open(log_file, "a", encoding='utf-8') as log:
    log.write(f"{datetime.datetime.now()} | {input_file} | {count} results\n")

print(f"Filtered {count} states")