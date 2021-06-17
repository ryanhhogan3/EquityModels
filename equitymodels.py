### This is the interworkings and mathematics behind some simple equity models

### Gordon (Constant) Growth Model module ###
def Gordongrowth(dividend, costofequity, growthrate):
    price = dividend / (costofequity - growthrate)
    price1 = round(price * .95, 2)
    price2 = round(price * 1.05, 2)
    print(f"Based on the Gordon Growth Model, this stock's price is valued between: {price1} and {price2}.")
    
### One Year Holding Period ###
def oneyearmodel(saleprice, dividend, costofequity):
    price = (dividend + saleprice) / (1 + costofequity)
    price1 = round(price * .95, 2)
    price2 = round(price * 1.05, 2)
    print(f"Based on the One Year Holding Model, this stock's price is valued between: {price1} and {price2}.")

### Multi-Stage (Double Year Holding Period) Dividend Discount Model module ###
def twoyearmodel(saleprice, dividend1, dividend2, costofequity):
    price = (dividend1 / (1 + costofequity)) + (dividend2 / (1 + costofequity)**2) + (saleprice / (1 + costofequity)**2)
    price1 = round(price * .95, 2)
    price2 = round(price * 1.05, 2)
    print(f"Based on the Two Year Holding Model, this stock's price is valued between: {price1} and {price2}.")
    
### Free Cash Flow Model (uses same formula as GordonGrowth, substitutes dividends with Free Cash Flow per share)
def Freecashflowmodel(FCFpershare, costofequity, growthrate):
    price = FCFpershare / (costofequity - growthrate)
    price1 = round(price * .95, 2)
    price2 = round(price * 1.05, 2)
    print(f"Based on the Free Cash Flow Model, this stock's price is valued between: {price1} and {price2}.")