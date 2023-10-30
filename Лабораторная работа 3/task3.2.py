def find_common_participants(first_str, second_str, separator=','):
    common_set = set(first_str.split(separator)).intersection(second_str.split(separator))
    return sorted(list(common_set))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, '|'))

