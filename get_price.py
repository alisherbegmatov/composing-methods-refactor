# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

# TODO: Replace the temporary variable with extracted method/query

# Code snippet. Not runnable.
def get_price():
    base_price = get_quantity() * get_item_price()
    if base_price > 1000:
        adjusted_discount_factor = 0.95
    else:
        adjusted_discount_factor = 0.98

    return base_price * adjusted_discount_factor


def get_quantity():
    return int(input('Enter the quantity: '))


def get_item_price():
    return float(input('Enter the item price: '))


print(get_price())
