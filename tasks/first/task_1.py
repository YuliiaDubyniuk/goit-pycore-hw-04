
def total_salary(path: str) -> tuple[int]:
    """Calculate total and average salary"""
    try:
        with open(path, mode="r", encoding="utf-8", errors="strict") as f:
            f_content = f.readlines()
    except FileNotFoundError as e:
        print("File not found:", e)
        return 0, 0
    except UnicodeDecodeError as e:
        print("Can not decode file content:", e)
        return 0, 0
    except Exception as e:
        print("Unexpected error while opening/reading file:", e)
        return 0, 0

    total_s = 0
    average_s = 0

    if f_content:
        for line in f_content:
            if not line.strip():
                continue
            employee_data = line.strip().split(",")
            salary = employee_data[1] if len(employee_data) == 2 else 0
            total_s += int(salary)

        average_s = total_s / len(f_content)
    else:
        print("File is empty.")

    return total_s, average_s


total, average = total_salary("tasks/first/salaries.txt")
print(
    f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
