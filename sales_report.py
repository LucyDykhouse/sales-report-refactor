"""Generate sales report showing total melons each salesperson sold."""

# Lists for each salesperson and the number of melons that each salesperson sold
# For better correlation between salesperson and melons_sold, should use a dictionary
salespeople = []
melons_sold = []

# Read sales-report.txt
# Should close the file at end of document
# Should be in a function for reproducibility
f = open('sales-report.txt')

# Loop over each line in file object
for line in f:
    line = line.rstrip()    # Remove trailing whitespace
    entries = line.split('|')   # Split line on |, creating a list of data

    salesperson = entries[0]    # From list, get salesperson name at position 0
    melons = int(entries[2])    # From list, get # of melons sold at position 2

    # If the salesperson is in the salespeople list, increment the corresponding melons_sold entry
    # Else, add the salesperson name to the salespeople list and add melons to the melons_sold list
    if salesperson in salespeople:
        position = salespeople.index(salesperson)   # Records index of specific salesperson
        melons_sold[position] += melons             # Uses index to add melons to corresponding melons_sold item
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


# Loop over indices of salespeople and use index to access and print corresponding salespeople, melons_sold items.
# Should print keys, values from dictionary
# Should be in a function for reproducibility
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')


