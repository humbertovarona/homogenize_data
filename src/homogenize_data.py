def homogenize_data(input_csv, output_csv):
    with open(input_csv, 'r', newline='') as inputcsv, open(output_csv, 'w', newline='') as outputcsv:
        in_csv = csv.reader(inputcsv)
        out_csv = csv.writer(outputcsv)
        for datarow in in_csv:
            if not any(col == '' for col in datarow):
                out_csv.writerow(datarow)
