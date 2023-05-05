import csv

with open('input.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    with open('output.csv', 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        for row in reader:
            if row[1] == '':
                url_parts = row[4].split('/')
                if len(url_parts) >= 3:
                    domain = url_parts[2]
                    row[1] = domain
            writer.writerow(row)
