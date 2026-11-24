def daily_sales_report(sales):
    total = 0
    count = 0
    highest = sales[0]
    lowest = sales[0]
    for sale in sales:
        total += sale
        count += 1
        if sale > highest:
            highest = sale
        if sale < lowest:
            lowest = sale
    average = total / count
    spread = highest - lowest
    above = 0
    below = 0
    equal = 0
    for sale in sales:
        if sale > average:
            above += 1
        elif sale < average:
            below += 1
        else:
            equal += 1
    squares = 0
    for sale in sales:
        squares += (sale - average) ** 2
    variance = squares / count
    print("Total sales:", total)
    print("Orders:", count)
    print("Highest sale:", highest)
    print("Lowest sale:", lowest)
    print("Spread:", spread)
    print("Average sale:", average)
    print("Above average:", above)
    print("Below average:", below)
    print("On average:", equal)
    print("Variance:", variance)
    return average


def weekly_sales_report(sales):
    total = 0
    count = 0
    highest = sales[0]
    lowest = sales[0]
    for sale in sales:
        total += sale
        count += 1
        if sale > highest:
            highest = sale
        if sale < lowest:
            lowest = sale
    average = total / count
    spread = highest - lowest
    above = 0
    below = 0
    equal = 0
    for sale in sales:
        if sale > average:
            above += 1
        elif sale < average:
            below += 1
        else:
            equal += 1
    squares = 0
    for sale in sales:
        squares += (sale - average) ** 2
    variance = squares / count
    print("Total sales:", total)
    print("Orders:", count)
    print("Highest sale:", highest)
    print("Lowest sale:", lowest)
    print("Spread:", spread)
    print("Average sale:", average)
    print("Above average:", above)
    print("Below average:", below)
    print("On average:", equal)
    print("Variance:", variance)
    return average


def monthly_sales_report(sales):
    total = 0
    count = 0
    highest = sales[0]
    lowest = sales[0]
    for sale in sales:
        total += sale
        count += 1
        if sale > highest:
            highest = sale
        if sale < lowest:
            lowest = sale
    average = total / count
    spread = highest - lowest
    above = 0
    below = 0
    equal = 0
    for sale in sales:
        if sale > average:
            above += 1
        elif sale < average:
            below += 1
        else:
            equal += 1
    squares = 0
    for sale in sales:
        squares += (sale - average) ** 2
    variance = squares / count
    print("Total sales:", total)
    print("Orders:", count)
    print("Highest sale:", highest)
    print("Lowest sale:", lowest)
    print("Spread:", spread)
    print("Average sale:", average)
    print("Above average:", above)
    print("Below average:", below)
    print("On average:", equal)
    print("Variance:", variance)
    return average


def monthly_sales_report(sales):
    total = 0
    count = 0
    highest = sales[0]
    lowest = sales[0]
    for sale in sales:
        total += sale
        count += 1
        if sale > highest:
            highest = sale
        if sale < lowest:
            lowest = sale
    average = total / count
    spread = highest - lowest
    above = 0
    below = 0
    equal = 0
    for sale in sales:
        if sale > average:
            above += 1
        elif sale < average:
            below += 1
        else:
            equal += 1
    squares = 0
    for sale in sales:
        squares += (sale - average) ** 2
    variance = squares / count
    print("Total sales:", total)
    print("Orders:", count)
    print("Highest sale:", highest)
    print("Lowest sale:", lowest)
    print("Spread:", spread)
    print("Average sale:", average)
    print("Above average:", above)
    print("Below average:", below)
    print("On average:", equal)
    return average
    
def monthly_sales_report(sales):
    total = 0
    count = 0
    highest = sales[0]
    lowest = sales[0]
    for sale in sales:
        total += sale
        count += 1
        if sale > highest:
            highest = sale
        if sale < lowest:
            lowest = sale
    average = total / count
    spread = highest - lowest
    above = 0
    below = 0
    equal = 0
    for sale in sales:
        if sale > average:
            above += 1
        elif sale < average:
            below += 1
        else:
            equal += 1
    squares = 0
    for sale in sales:
        squares += (sale - average) ** 2
    variance = squares / count
    print("Total sales:", total)
    print("Orders:", count)
    print("Highest sale:", highest)
    print("Lowest sale:", lowest)
    print("Spread:", spread)
    print("Average sale:", average)
    print("Above average:", above)
    print("Below average:", below)
    print("On average:", equal)
    return average

   
