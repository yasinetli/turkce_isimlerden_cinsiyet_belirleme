from data import name_dict
from test import test_list


def gender_counter():
    test_processed_dict = {}
    for item in test_list:
        if item in name_dict:
            test_processed_dict[item] = name_dict[item]
        else:
            test_processed_dict[item] = 4
    print(test_processed_dict)
    gender_dict = {"1": 0, "2": 0, "3": 0, "4": 0}
    for i in test_list:
        if i in name_dict:
            gender = name_dict[i]
            gender_dict[f"{gender}"] += 1
        else:
            gender_dict["4"] += 1
    print(gender_dict)
    estimated_dict = {}
    unknown = gender_dict["3"] + gender_dict["4"]
    estimated_dict["1"] = gender_dict["1"] + round(unknown * (gender_dict["1"]/(gender_dict["1"] + gender_dict["2"])))
    estimated_dict["2"] = gender_dict["2"] + (unknown - (estimated_dict["1"] - gender_dict["1"]))
    print(estimated_dict)


gender_counter()
