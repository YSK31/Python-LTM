class EmployeeSalaryAnalyzer:
    def __init__(self):
        pass

    def build_salary_dict(self, records):
        salary_dict = {}
        for line in records.splitlines():
            parts = line.split(",")
            if len(parts) == 2:
                try:
                    name = parts[0].strip()
                    salary = float(parts[1].strip())
                    salary_dict[name] = salary
                except ValueError:
                    pass
        return salary_dict

    def total_salary(self, salary_dict):
        return sum(salary_dict.values())

    def give_raise(self, salary_dict, percent):
        res = {}
        for key,val in salary_dict.items():
            res[key] = round(val * (1 + percent / 100), 2)
        return res

    def top_n_earners(self, salary_dict, n):
        if n <= 0:
            return []
        res = sorted(salary_dict.items(), key=lambda x: (-x[1], x[0]))
        return res[:n]
