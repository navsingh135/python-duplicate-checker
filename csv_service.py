import pandas as pd

def findDuplicateRows(file):
    file.seek(0)  # Move to the beginning of the file

    # Open the tempfile with pandas
    df = pd.read_csv(file, on_bad_lines='skip')

    names = {}

    for index, row in df.iterrows():
        name = row["Names"]
        if name in names:
            names[name] = names[name] + 1
        else:
            names[name] = 1

    print(names)

    duplicates = {key: value for key, value in names.items() if value > 1}
    # Close the temporary file
    file.close()
    return duplicates
