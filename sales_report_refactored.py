"""Generate sales report showing the total number of melons each salesperson sold"""


def get_info_by_salesperson(filename):
    """Return a dictionary of salesperson_name: melons_sold

    Arguments:
        filename (str) - the path to a sales report log file

    Return:
        melons_by_person (dict)
    """

    melons_by_person = {}

    with open(filename, 'r') as sales_data:
        for line in sales_data:

            # Create a list of data and unpack values
            salesperson_name, _, melons_sold = line.rstrip().split('|')

            # Set or update the salesperson's total number of melons sold
            if salesperson_name in melons_by_person:
                melons_by_person[salesperson_name] += int(melons_sold)
            else:
                melons_by_person[salesperson_name] = int(melons_sold)

    return melons_by_person


def print_melons_by_person(dict):
    """Print a report of salespeople and the amount of melons they sold

    Arguments:
        dict (dictionary): dictionary containing keys and values of salesperson: melons_sold
    """

    for salesperson_name, melons_sold in dict.items():
        print(f'{salesperson_name} sold {melons_sold} melons')


def main():
    """Body of script"""

    # Invoke info function
    sales_data = get_info_by_salesperson('sales-report.txt')

    # Using dictionary returned above, invoke printing function
    print_melons_by_person(sales_data)


# Invoke body
main()


