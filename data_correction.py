import csv

csv_file_path = "../muser-firebase-export/music-analysis.csv"  # CSV data export file path

csv_corrected_file = []

# Try different encodings and error handling strategies until one works
encoding = 'utf-8'  # utf-8 works, ascii does not

flag = 0
with open(csv_file_path, mode='r', encoding=encoding) as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        indices_to_remove = [7, 8, 9, 11, 13, 14, 15, 17, 18, 22, 24, 25, 27, 28, 30, 33, 37, 38, 39, 40, 41, 42, 43,
                             44, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]  # unnecessary items
        indices_to_remove.sort(reverse=True)  # revert indices to avoid index shifting
        for index in indices_to_remove:
            del row[index]
        csv_corrected_file.append(row)

for item in csv_corrected_file:
    print(item)

corrected_file_path = 'corrected_data.csv'
with open(corrected_file_path, mode='w', newline='', encoding=encoding) as file:
    csv_writer = csv.writer(file)
    for row in csv_corrected_file:
        csv_writer.writerow(row)

print("Write successful")

