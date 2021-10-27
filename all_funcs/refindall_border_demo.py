# %%
#######################################
def refindall_border_demo():
    import re

    example1 = "987!5887315075505 963273979167!1792 424 8829428 758423813480156538725 80338918230792#82063912 *891"
    example2 = "823!03270182 997 868!465#891*0105#46535832231!296!2364#1903 406333702!355536717 1204!827205710879978416468!3357 *711"

    print(
        r'For the first example I will take the string and isolate each sequence of 3 digits surrounded by a "border character" or "\b"',
        "\n",
    )
    print(f"Example1 String: {example1}\n")

    # Here we are specifying each group of 3 digits surrounded by a "border character" or "\b"
    match_syntax1 = re.compile(r"\b\d{3}\b")
    print(f"Using the match syntax: {match_syntax1}")

    result1 = re.findall(match_syntax1, example1)
    print(f"Result for Example #1: {result1}")
    # Output:   Result for Example #1: ['987', '424', '891']

    print("\n\n")

    print(
        r'For the second example I will take the string and isolate each sequence of 4 digits surrounded by a "border character" or "\b"',
        "\n",
    )
    print(f"Example2 String: {example2}\n")

    # Here we are specifying each group of 4 digits surrounded by a "border character" or "\b"
    match_syntax2 = re.compile(r"\b\d{4}\b")
    print(f"Using the match syntax: {match_syntax2}")

    result2 = re.findall(match_syntax2, example2)
    print(f"Result for Example #2: {result2}")
    # Output:   Result for Example #2: ['0105', '2364', '1903', '1204', '3357']

