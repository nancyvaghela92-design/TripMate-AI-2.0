from openpyxl import Workbook


def create_excel(trips):

    wb = Workbook()

    ws = wb.active

    ws.title = "Saved Trips"

    ws.append([
        "ID",
        "Destination",
        "Budget",
        "Travelers",
        "Travel Type",
        "Itinerary"
    ])

    for trip in trips:

        ws.append(trip)

    filename = "TripMate_Saved_Trips.xlsx"

    wb.save(filename)

    return filename
    