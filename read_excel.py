from openpyxl import load_workbook, Workbook

class Read_Data():

    def __init__(self):

        self.NULL = {None, "=""", ""}
        self.WORKFILE = "data_file.xlsx"
        self.SHEET_NAMES = ["Equipment Details", "Worker Details", "Facility Details", "Work Order Examples"]
        self.wb = load_workbook(self.WORKFILE)

        self.EQUIPMENT_FIELDS = ["failure", "fix", "fac1", "fac2", "fac3", "fac4", "fac5"]
        self.WORKER_FIELDS = ["certifications", "shifts", "latitude", "longitude"]
        self.FACILITY_FIELDS = ["latitude", "longitude", "occupancy"]
        self.ORDER_FIELDS = ["facility", "type", "id", "priority", "completion_time", "submission_time"]

        self.EQUIPMENT = self.read_sheet(self.SHEET_NAMES[0], 3, 2, self.EQUIPMENT_FIELDS)
        self.WORKER = self.read_sheet(self.SHEET_NAMES[1], 2, 2, self.WORKER_FIELDS)
        self.FACILITY = self.read_sheet(self.SHEET_NAMES[2], 3, 2, self.FACILITY_FIELDS)
        self.ORDER = self.read_sheet(self.SHEET_NAMES[3], 3, 2, self.ORDER_FIELDS)


    def read_sheet(self, sheetname, start_row, start_col, fields):

        data = dict()
        ws = self.wb[sheetname]
        row = start_row

        while True:
            key = ws.cell(row, start_col).value
            if key in self.NULL:
                break
            field_dict = dict()
            col = start_col + 1
            for index, field in enumerate(fields):
                field_dict[field] = str(ws.cell(row, col + index).value)
            data[key] = field_dict

            row += 1

        return data

    def get_equipment(self):
        return self.EQUIPMENT

    def get_worker(self):
        return self.WORKER

    def get_facility(self):
        return self.FACILITY

    def get_order(self):
        return self.ORDER



def run():
    data = Read_Data()

    print(data.get_equipment()["Pump"]["failure"])
    print(data.get_order()[1001])

if __name__ == '__main__':
    run()
