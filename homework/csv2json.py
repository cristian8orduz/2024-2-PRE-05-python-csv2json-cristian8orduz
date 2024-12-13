import csv
import json
"""Script para convertir un archivo CSV a JSON"""

from nicegui import ui


def convert_csv_2_json(input_file):
    """Converts a CSV file to a JSON file"""

    output_file = input_file.replace(".csv", ".json")
    data = []

    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f)

    ui.notify("The file was transformed successfully!")


def app():
    """Main function to run the app"""

    ui.label("CSV to JSON Converter").classes("text-4xl font-bold")
    ui.label("")

    filename = ui.input(
        label="CSV file to convert:",
        placeholder="filename",
    )

    ui.label("")

    ui.label("")
    ui.button("Convert", on_click=lambda: convert_csv_2_json(filename.value))
    ui.run()


app()