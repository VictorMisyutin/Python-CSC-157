# Variable declarations
purchase = 0.0
stateTax = 0.0
countyTax = 0.0
totalTax = 0.0
totalSale = 0.0

# Constants for the state and county tax rates
STATE_TAX_PERCENT = 0.05
COUNTY_TAX_PERCENT = 0.025
# Get the amount of the purchase.
purchase = float(input("Please enter the purchase amount:\n$"))
# Calculate the state sales tax.
stateTax = purchase*STATE_TAX_PERCENT
# Calculate the county sales tax.
countyTax = purchase*COUNTY_TAX_PERCENT
# Calculate the total tax.
totalTax = stateTax+countyTax
# Calculate the total of the sale.
totalSale = purchase + totalTax
# Print information about the sale.
print(f"The original purchase was ${purchase}\nState Sales Tax was ${stateTax}\nCounty Sales Tax was ${countyTax}\nTotal Sales Tax was ${totalTax}\nThe Total Sale was ${totalSale}")