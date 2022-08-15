import json

with open("5.7_source.txt", "r", encoding="utf-8") as f:
    data = [l.strip().split() for l in f.readlines()]
    result = []
    all_profit = []
    org_dict = {}

    for name, property_type, earnings, costs in data:
        profit = int(earnings) - int(costs)
        org_dict[name] = profit
        if profit > 0:
            all_profit.append(profit)

    result.append(org_dict)
    result.append({"average_profit": round(sum(all_profit) / len(all_profit))})

    with open("5.7_result.txt", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
