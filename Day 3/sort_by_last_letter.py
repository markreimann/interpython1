store = []


def sort_by_last_letter(string):
    """
    Task define a function that takes a string as input parameter.
       Defines a local function that returns the last letter of the string
    Your main function returns a sorted list  based on the last letter.
    Sort string by last leter
    :param string: list of strings
    :return: sorted list of imput string
    """
    #local function
    def last_letter(s):
        return s[-1]

    store.append((last_letter))
    print(last_letter)

    # Hint: use the local functiona as lambda to the sorted built in function
    return sorted(string, key=last_letter)


def logger(msg):
    def log_message():
        print("Log: ", msg)
    return log_message


def html_tag(tag):
    """
    Crfeates a heml tag based on input
    :param tab: Tag
    :return: a callable function
    """
    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))
    return wrap_text


def main():
    names = ["huga", "mara", "peter", "Mario", "Luegi"]
    print(sort_by_last_letter(names))
    pass


if __name__ == '__main__':
    main()
    exit(0)