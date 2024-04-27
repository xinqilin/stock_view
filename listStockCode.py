import twstock

# twstock.__update_codes()
codes = twstock.codes

for k, v in codes.items():
    print(f"code: {k}, value: {v}")
