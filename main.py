import SOPModel

def main():
    f_name = input(f"Your first name\n")
    # l_name = input(f"Your last name\n")
    # f_name = "majid"
    # l_name = "majidi"
    university_name = input(f"University for your SOP\n")
    study_field = input(f"Field of study\n")
    # university_name = "Adelaide"
    # study_field = "Mining Engineering"
    print("Now enter any key words or additional information you want")
    print("To quit write 'LEAVE'")

    key_words = []
    while True:
        k = input()
        if (k == 'LEAVE'): break
        key_words.append(k)

    model = SOPModel.SOPModel(f_name + " " + l_name, university_name, study_field, key_words, './201709301651_masters_portal.csv')
    model.preprocess()
    model.get_sop(f_name, l_name)
if __name__ == "__main__":
    main()