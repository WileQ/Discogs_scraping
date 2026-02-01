def split_file(input_file, n):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total_lines = len(lines)
    base = total_lines // n
    extra = total_lines % n

    print(total_lines)
    start = 0
    for i in range(n):
        end = start + base + (1 if i < extra else 0)
        with open(f"ids_todo_worker{i+1}.txt", "w", encoding="utf-8") as out:
            out.writelines(lines[start:end])
        start = end


# usage
split_file("ids_todo_wiktor.txt", 2)
