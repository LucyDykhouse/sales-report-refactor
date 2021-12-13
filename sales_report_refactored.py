def get_info_by_salesperson(filename):
    """Add comment"""

    melons_by_person = {}

    with open(filename, 'r') as sales_data:

        for line in sales_data:
            salesperson_name, _, melons_sold = line.rstrip().split('|')

            if salesperson_name in melons_by_person:
                melons_by_person[salesperson_name] += int(melons_sold)
            else:
                melons_by_person[salesperson_name] = int(melons_sold)

    return melons_by_person


def print_melons_by_person(dict):
    """Add comment here"""

    for salesperson_name, melons_sold in dict.items():
        print(f'{salesperson_name} sold {melons_sold} melons')


def main():
    """Add comment here"""

    sales_data = get_info_by_salesperson('sales-report.txt')

    print_melons_by_person(sales_data)


main()


