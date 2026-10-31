from decimal import Decimal, InvalidOperation


#region Decimal calculators

def decimal_sum(decimal_numbers: list[Decimal] | tuple[Decimal]) -> Decimal:
    if not decimal_numbers:
        raise ValueError

    decimal_sum = Decimal("0")

    for decimal_number in decimal_numbers:
        decimal_sum += decimal_number

    return decimal_sum


def decimal_product(decimal_numbers: list[Decimal] | tuple[Decimal]) -> Decimal:
    if not decimal_numbers:
        raise ValueError
    
    decimal_product = Decimal("1")

    for decimal_number in decimal_numbers:
        decimal_product *= decimal_number

    return decimal_product


def decimal_logarithm(decimal_value: Decimal, decimal_base: Decimal) -> Decimal:
    decimal_logarithm: Decimal = (decimal_value.ln() / decimal_base.ln()).quantize(Decimal("1"))
    return decimal_logarithm


def decimal_scalar(decimal_numbers: list[Decimal] | tuple[Decimal], scalar_value: Decimal) -> list[Decimal]:
    if not decimal_numbers:
        raise ValueError
    
    decimal_scalar: list[Decimal] = [decimal_number * scalar_value for decimal_number in decimal_numbers]
    return decimal_scalar


def decimal_factorial(decimal_number: Decimal) -> Decimal:
    decimal_number_is_not_natural: bool = decimal_number < Decimal("1") or decimal_number % Decimal("1") != Decimal("0")

    if decimal_number_is_not_natural:
        raise ValueError

    decimal_factorial: Decimal = Decimal("1")

    for decimal_multiplier in range(1, int(str(decimal_number)) + 1):
        decimal_factorial *= decimal_multiplier

    return decimal_factorial


def decimal_back_factorial(decimal_number: Decimal) -> Decimal:
    decimal_number_is_not_natural: bool = decimal_number < Decimal("1") or decimal_number % Decimal("1") != Decimal("0")
    
    if decimal_number_is_not_natural:
        raise ValueError

    back_factorial = Decimal("0")
    decimal_divisor = Decimal("1")
    decimal_number_is_one: bool = decimal_number == Decimal("1")
    
    if decimal_number_is_one:
        return Decimal("1")

    while not decimal_number_is_one:
        decimal_number /= decimal_divisor

        decimal_number_is_not_whole: bool = decimal_number % Decimal("1") != Decimal("0")

        if decimal_number_is_not_whole:
            raise ValueError
        else:
            back_factorial += Decimal("1")
            decimal_divisor += Decimal("1")

        decimal_number_is_one: bool = decimal_number == Decimal("1")

    return back_factorial


def decimal_expected_value(decimal_x: list[Decimal], decimal_p: list[Decimal]) -> Decimal:
    decimal_x_length: int = len(decimal_x)
    decimal_p_length: int = len(decimal_p)
    probabilties_sum: Decimal = sum(decimal_p, Decimal("0"))

    lengths_are_mismatched: bool = decimal_x_length != decimal_p_length
    probabilities_sum_is_invalid: bool = probabilties_sum != Decimal("1")

    if lengths_are_mismatched or probabilities_sum_is_invalid:
        raise ValueError

    expected_value: Decimal = Decimal("0")

    for x, p in zip(decimal_x, decimal_p):
        expected_value += x * p

    return expected_value


def get_quadratic_equation_roots(
    *,
    a: Decimal,
    b: Decimal,
    c: Decimal,
    mode: str | None = None,
) -> list[Decimal]:

    D: Decimal = ((b ** Decimal("2")) - ((Decimal("4") * a * c))).sqrt()

    x1: Decimal = (-b - D) / (Decimal("2") * a)
    x2: Decimal = (-b + D) / (Decimal("2") * a)

    quadratic_equation_roots: list[Decimal] = [x1, x2]

    modified_quadratic_equation_roots_map: dict = {
        "POSITIVE": [x for x in quadratic_equation_roots if x > Decimal("0")],
        "NEGATIVE": [x for x in quadratic_equation_roots if x < Decimal("0")],
    }

    roots_are_equal: bool = x1 == x2

    if roots_are_equal:
        quadratic_equation_roots = [x1]

    quadratic_equation_solution: list[Decimal] = modified_quadratic_equation_roots_map.get(mode, quadratic_equation_roots)
    there_ate_no_solutions: bool = not quadratic_equation_solution

    if there_ate_no_solutions:
        raise ValueError
    else:
        return quadratic_equation_solution

#endregion


#region Decimal parsers

def clean_decimal_number(
    *,
    decimal_number: Decimal,
    format_mode: str = "f",
) -> Decimal:

    cleaned_decimal_number: Decimal = Decimal(format(decimal_number.normalize(), format_mode))
    return cleaned_decimal_number


def decimal_zip(list1: list[Decimal], list2: list[Decimal]) -> list:
    list1_length: int = len(list1)
    list2_length: int = len(list2)

    both_lists_are_empty: bool = not list1 and not list2
    lengths_are_mismached: bool = list1_length != list2_length

    if both_lists_are_empty or lengths_are_mismached:
        raise ValueError
    else:
        lists_zip: list = list(zip(list1, list2))
        return lists_zip


def get_decimal_numbers_from_user_input(
    *,
    user_input: str,
    valid_characters: str = "0123456789-.",
) -> list[Decimal]:

    valid_characters_matrix: list[list[str]] = []
    valid_characters_list: list[str] = []

    user_input_length: int = len(user_input)

    for index, character in enumerate(user_input):
        character_is_valid: bool = character in valid_characters

        if character_is_valid:
            valid_characters_list.append(character)
            cycle_is_over: bool = index == user_input_length - 1

            if cycle_is_over:
                valid_characters_matrix.append(valid_characters_list)
                valid_characters_list: list[str] = []

        else:
            valid_characters_list_is_empty: bool = not valid_characters_list

            if valid_characters_list_is_empty:
                continue

            valid_characters_matrix.append(valid_characters_list)
            valid_characters_list: list[str] = []

    decimal_numbers: list[Decimal] = []

    for valid_characters_list in valid_characters_matrix:
        potential_decimal_number: str = "".join(valid_characters_list)
    
        try:
            raw_decimal_number: Decimal = Decimal(potential_decimal_number)
            cleaned_decimal_number: Decimal = clean_decimal_number(decimal_number=raw_decimal_number)
            decimal_numbers.append(cleaned_decimal_number)
        except InvalidOperation:
            continue

    return decimal_numbers

#endregion
