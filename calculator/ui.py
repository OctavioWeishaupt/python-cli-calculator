LEN_LINE = 50


def line():
    """
    -> Write a line of '-'
    """
    print('-' * LEN_LINE)


def title(txt):
    """
    -> Write a title personalized
    :param txt: The text to be printed in the title
    """
    line()
    print(txt.center(LEN_LINE))
    line()