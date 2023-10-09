"""calc.py"""


def rate_calculating(input_summ, output_summ):
    """The rate calculating."""
    input_summ_float = float(input_summ)
    output_summ_float = float(output_summ)
    if input_summ_float >= output_summ_float:
        rate = input_summ_float / output_summ_float
    else:
        rate = output_summ_float / input_summ_float
    rate = "{:.2f}".format(rate)
    return rate
