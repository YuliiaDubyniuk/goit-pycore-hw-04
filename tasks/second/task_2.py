def get_cats_info(path):
    try:
        with open(path, mode="r", encoding="utf-8", errors="strict") as f:
            f_content = f.readlines()
    except FileNotFoundError as e:
        print("File not found:", e)
        return []
    except UnicodeDecodeError as e:
        print("Can not decode file content:", e)
        return []
    except Exception as e:
        print("Unexpected error while opening/reading file:", e)
        return []

    cats_list = []

    if f_content:
        for line in f_content:
            if not line.strip():
                continue
            cats_data = line.strip().split(",")
            if len(cats_data) != 3:
                print(f"Missing/invalid data in line: {line}")
                continue
            cat = {"id": cats_data[0],
                   "name": cats_data[1],
                   "age": cats_data[2]}
            cats_list.append(cat)

    return cats_list


cats_info = get_cats_info("tasks/second/cats.txt")
print(cats_info)
