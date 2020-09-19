from read_excel import *
import heapq
from random import randrange


class Delegate_Tasks:

    def __init__(self):

        self.data = Data()
        self.daily_orders = self.data.get_all_orders()
        self.heap = list()
        self.workers = self.data.get_all_workers()


    def generate_schedule(self):
        current_day = 0

        while True:

            available_workers = {key : worker for key, worker in self.workers.items() if worker.get_schedule().is_available()]
            new_orders = self.daily_orders[cuurent_day]
            new_order_priorities = [(order.get_priority(), key) for key, order in new_orders.items()]
            for order in new_order_priorities:
                heapq.heappush(self.heap, order)

            employee_capabilites = dict()
            for key in available_workers():
                employee_capabilites[key] = set()
            order_capabilities = dict()

            temp_heap = self.heap.copy()
            while temp_heap:
                qualified_workers = set()
                priority, order_key = heapq.heappop(temp_heap)
                order = data.get_order(order_key)
                order_type = order.get_type()
                for key, worker in available_workers.items():
                    if order_type in worker.get_certifications():
                        qualified_workers.add(key)
                        employee_capabilites[key].add((priority, order_key))

                order_capabilities[order_key] = qualified_workers

            while True:

                # if facility is full, move on

                priority, order_key = heapq.heappop(self.heap)
                order = data.get_order(order_key)
                qualified_workers = order_capabilities[order_key]
                candidate = None
                max_time_remaining = 0
                min_max_priority_alternate = -1
                for key in qualified_workers:
                    worker = data.get_worker(key)
                    if len(employee_capabilites[worker]) == 1:
                        time_remaining = worker.get_schedule().get_time_remaining()
                        if time_remaining > max_time_remaining:
                            candidate = key
                            max_time_remaining = time_remaining
                    else if not max_time_remaining:
                        other_tasks = employee_capabilites[key] - {(priority, order_key)}
                        max_priority_alternate = max(other_tasks)[0]
                        if max_priority_alternate < min_max_priority_alternate or min_max_priority_alternate == -1:
                            candidate = key
                            min_max_priority_alternate = max_priority_alternate

                if candidate:
                    worker = data.get_worker(candidate)
                    schedule = worker.get_schedule()
                    if schedule.add_task(order_key, Time(order.get_completion_time(), 0), (worker.get_latitude(), worker.get_longitude()), (order.get_latitude(), order.get_longitude())):

                        if not schedule.is_available():
                            if candidate in employee_capabilites:
                                employee_capabilites.remove(candidate)

                    else:
                        heapq.heappush(self.heap, (priority, order_key))

                else:
                    heapq.heappush(self.heap, (priority, order_key))

                if order_key in order_capabilities:
                    order_capabilities.remove(order_key)

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

            # Update schedules at the end of each day

            for worker in self.workers.values():
                worker.get_schedule().update()

            current_day += 1
