# %%
#######################################
def floor_division(dividend: int, divisor: int):
    """Describes and gives an example of how floor division and the "//" symbols are used in Python.

    Examples:
        >>> floor_division(15, 6)\n
        Floor division returns the nearest whole number as the quotient, rounding down when there is a remainder.\n
          dividend // divisor\n
          15 // 6\n

        2

    Args:
        dividend (int): Supply a dividend
        divisor (int): Supply a divisor

    Returns:
        int: Returns the quotient of the floor division operation
    """
    print(
        "Floor division returns the nearest whole number as the quotient, rounding down when there is a remainder."
    )
    print("  dividend // divisor ")
    print(f"  {dividend} // {divisor}")
    print("")
    return dividend // divisor

