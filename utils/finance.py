def calculate_net_profit(total_income, total_costs, tax_rate=0.09):
    tax = total_income * tax_rate
    profit = total_income - total_costs - tax
    return {
        "gross": total_income,
        "costs": total_costs,
        "tax": tax,
        "net_profit": profit
    }
