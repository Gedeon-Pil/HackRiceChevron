from read_excel import *
from random import randrange
import heapq
import math


class Delegate_Tasks:

    def __init__(self):

        self.data = Data()
        self.daily_orders = self.data.get_all_daily_orders()
        self.heap = list()
        self.workers = self.data.get_all_workers()
        self.facilities = self.data.get_all_facilities()


    def generate_schedule(self):

        current_day = 0

        while current_day < len(self.daily_orders):

            print("DAY ", current_day)

            available_workers = {key : worker for key, worker in self.workers.items() if worker.get_schedule().is_available()}
            new_orders = self.daily_orders[current_day]
            new_order_priorities = [(order.get_priority(), key) for key, order in new_orders.items()]
            for priority, order in new_order_priorities:
                heapq.heappush(self.heap, (-1 * priority, order))

            print("Orders at beginning of day: %d" % len(self.heap))
            print(self.heap)

            employee_capabilites = dict()
            for key in available_workers:
                employee_capabilites[key] = set()
            order_capabilities = dict()

            temp_heap = self.heap.copy()
            while temp_heap:
                qualified_workers = set()
                priority, order_key = heapq.heappop(temp_heap)
                priority *= -1

                order = self.data.get_order(order_key)
                order_type = order.get_type()
                for key, worker in available_workers.items():
                    if order_type in worker.get_certifications():
                        qualified_workers.add(key)
                        employee_capabilites[key].add((priority, order_key))

                order_capabilities[order_key] = qualified_workers

            unclaimed_orders = list()

            while True:

                print(order_key)
                priority, order_key = heapq.heappop(self.heap)
                priority *= -1

                order = self.data.get_order(order_key)
                completion_time = Time(order.get_completion_time(), 0)

                facility = self.data.get_facility(order.get_facility())
                facility_schedule = facility.get_schedule()
                start_times = facility_schedule.get_start_times(completion_time)

                qualified_workers = order_capabilities[order_key]
                candidate = None
                max_time_remaining = ZERO_TIME
                min_max_priority_alternate = float('inf')

                for key in qualified_workers:
                    worker = self.data.get_worker(key)
                    if len(employee_capabilites[key]) == 1:
                        time_remaining = worker.get_schedule().get_time_remaining()
                        if time_remaining.greater(max_time_remaining):
                            candidate = key
                            max_time_remaining = time_remaining
                    elif max_time_remaining.equals(ZERO_TIME):

                        other_tasks = employee_capabilites[key] - {(priority, order_key)}

                        max_priority_alternate = max(other_tasks)[0]

                        if max_priority_alternate < min_max_priority_alternate or min_max_priority_alternate == -1:
                            candidate = key
                            min_max_priority_alternate = max_priority_alternate

                if candidate:
                    worker = self.data.get_worker(candidate)
                    schedule = worker.get_schedule()
                    next_available_time = schedule.get_next_start_time(worker.get_location(), facility.get_location())

                    under_capacity = False

                    for start_time in start_times:

                        if start_time[0].get_time() <= next_available_time.get_time() <= start_time[1].get_time():
                            under_capacity = True
                            break

                    if under_capacity and schedule.add_task(order, completion_time, facility.get_location()):

                        if not schedule.is_available():
                            if candidate in employee_capabilites:
                                employee_capabilites.remove(candidate)

                    else:
                        unclaimed_orders.append((-1 * priority, order_key))

                else:
                    unclaimed_orders.append((-1 * priority, order_key))


                order_capabilities.pop(order_key, None)

                for key, tasks in employee_capabilites.items():
                    if (priority, order_key) in tasks:
                        tasks.remove((priority, order_key))


                no_capabilites = True
                for key, tasks in employee_capabilites.items():
                    if tasks:
                        no_capabilites = False
                        break

                if no_capabilites:
                    break

            for order in unclaimed_orders:
                    heapq.heappush(self.heap, order)

            for worker in self.workers.values():
                print(worker.get_key())
                schedule = worker.get_schedule()
                schedule.print_today()
                worker.get_schedule().update()
                print("")

            for facility in self.facilities.values():
                facility_schedule = facility.get_schedule()
                facility_schedule.update()

            current_day += 1

            print("Orders at end of day: %d" % len(self.heap))
            print(self.heap)


    def daily_schedule(self, greedy):
            pass

    def get_all_schedules(self):
        master_dict = dict()
        for worker in self.workers.values():
            schedule = worker.get_schedule()
            master_dict[worker.get_key()] = schedule.get_running_schedule()

        return master_dict


def main():
    framework = Delegate_Tasks()
    framework.generate_schedule()
    master_scheduler = framework.get_all_schedules()

if __name__ == '__main__':
    main()
