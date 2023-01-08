import re


def validate_cpf(cpf: str) -> bool:

    """ Validate the CPF, both formatting and verifying digits.

    Parameters:
        cpf (str): CPF to be validated

    Returns:
        bool:
            - False, when the CPF does not have the format 999.999.999-99
            - False, when the CPF does not have 11 numeric characters
            - False, when check digits are invalid
            - True otherwise.

    Examples:

    >>> validate_cpf('52998224725')
    False
    >>> validate_cpf('111.111.111-11')
    False
    >>> validate_cpf('529.982.247-25')
    True
    """

    # Check CPF formatting
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return False

    # Gets only CPF numbers, ignoring scores
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Checks if the CPF has 11 numbers or if they are all the same
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validation of the first check digit
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validation of the second check digit
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True
