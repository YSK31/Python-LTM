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


if __name__ == "__main__":
    analyzer = EmployeeSalaryAnalyzer()
    records = "Alice,50000\nBob,60000\nCharlie,70000\nBadRecord\nDiana,not-a-number"
    salary_dict = analyzer.build_salary_dict(records)

    print("Salary dictionary:", salary_dict)
    print("Total salary:", analyzer.total_salary(salary_dict))
    print("10% raise:", analyzer.give_raise(salary_dict, 10))
    print("Top 2 earners:", analyzer.top_n_earners(salary_dict, 2))
    print("Top 0 earners:", analyzer.top_n_earners(salary_dict, 0))
    print("Tie handling:", analyzer.top_n_earners({"Zara": 70000, "Arun": 70000, "Maya": 65000}, 2))
