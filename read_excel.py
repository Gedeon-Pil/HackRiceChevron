from openpyxl import load_workbook, Workbook
import math

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

        self.DISTANCE_MATRIX = self.generate_distance_matrix()


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

    def generate_distance_matrix(self):

        n = len(self.FACILITY)
        coordinates = list()
        for fields in self.FACILITY.values():
            pair = (float(fields["latitude"]), float(fields["longitude"]))
            coordinates.append(pair)

        matrix = list()
        for index1 in range(n):
            distance = list()
            latitude1 = coordinates[index1][0]
            longitude1 = coordinates[index1][1]
            for index2 in range(n):
                latitude2 = coordinates[index2][0]
                longitude2 = coordinates[index2][1]
                distance.append(math.sqrt((latitude2 - latitude1) ** 2 + (longitude2 - longitude1) ** 2))

            matrix.append(distance)

        return matrix


    def get_equipment(self):
        return self.EQUIPMENT

    def get_worker(self):
        return self.WORKER

    def get_facility(self):
        return self.FACILITY

    def get_order(self):
        return self.ORDER


class Equipment():

    def __init__(self, key, equipment_fields):

        self.key = key
        self.failure = equipment_fields["failure"]
        self.fix = equipment_fields["fix"]
        self.fac1 = equipment_fields["fac1"]
        self.fac2 = equipment_fields["fac2"]
        self.fac3 = equipment_fields["fac3"]
        self.fac4 = equipment_fields["fac4"]
        self.fac5 = equipment_fields["fac5"]

    def get_key(self):
        return self.key

    def get_failure(self):
        return self.failure

    def get_fix(self):
        return self.fix

    def get_fac1(self):
        return self.fac1

    def get_fac2(self):
        return self.fac2

    def get_fac3(self):
        return self.fac3

    def get_fac4(self):
        return self.fac4

    def get_fac5(self):
        return self.fac5


class Worker():

    def __init__(self, key, worker_fields):

        self.key = key
        self.certifications = worker_fields["certifications"]
        self.shifts = worker_fields["shifts"]
        self.latitude = worker_fields["latitude"]
        self.longitude = worker_fields["longitude"]

    def get_key(self):
        return self.key

    def get_certifications(self):
        return self.certifications

    def get_shifts(self):
        return self.shifts

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude


class Facility():

    def __init__(self, key, facility_fields):

        self.key = key
        self.latitude = facility_fields["latitude"]
        self.longitude = facility_fields["longitude"]
        self.occupancy = facility_fields["occupancy"]

        def get_key(self):
            return self.key

        def get_latitude(self):
            return self.latitude

        def get_longitude(self):
            return self.longitude

        def get_occupancy(self):
            return self.occupancy


class Order():

    def __init__(self, key, order_fields):

        self.key = key
        self.facility = order_fields["facility"]
        self.type = order_fields["type"]
        self.id = order_fields["id"]
        self.priority = order_fields["priority"]
        self.completion_time = order_fields["completion_time"]
        self.submission_time = order_fields["submission_time"]

        def get_key(self):
            return self.key

        def get_facility(self):
            return self.facility

        def get_type(self):
            return self.type

        def get_id(self):
            return self.id

        def get_priority(self):
            return self.priority

        def get_completion_time(self):
            return self.completion_time

        def get_submission_time(self):
            return self.submission_time



class Data():

    def __init__(self):

        self.data = Read_Data()
        self.equipment_data = self.data.get_equipment()
        self.worker_data = self.data.get_worker()
        self.facility_data = self.data.get_facility()
        self.order_data = self.data.get_order()

        self.equipment_objs = dict()
        self.worker_objs = dict()
        self.facility_objs = dict()
        self.order_objs = dict()

        for key, equipment_fields in self.equipment_data.items():
            self.equipment_objs[key] = Equipment(key, equipment_fields)

        for key, worker_fields in self.worker_data.items():
            self.worker_objs[key] = Worker(key, worker_fields)

        for key, facility_fields in self.facility_data.items():
            self.facility_objs[key] = Facility(key, facility_fields)

        for key, order_fields in self.order_data.items():
            self.order_objs[key] = Order(key, order_fields)

    def get_equipment(self, name):
        if name in self.equipment_objs:
            return self.equipment_objs[name]
        return None

    def get_worker(self, name):
        if name in self.worker_objs:
            return self.worker_objs[name]
        return None

    def get_facility(self, name):
        if name in self.facility_objs:
            return self.facility_objs[name]
        return None

    def get_order(self, name):
        if name in self.order_objs:
            return self.order_objs[name]
        return None


def main():
    data = Data()
    bob = data.get_worker("Bob")
    print(bob.get_shifts())

if __name__ == '__main__':
    main()
