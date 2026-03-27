def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    aux = {
        "packets": "available",
        "grams": "total",
    }
    if (unit == "area"):
        print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
        return
    elif (unit in aux):
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} {aux[unit]}")
    else:
        print("Unknown unit type")

# ft_seed_inventory("tomato", 15, "packets")
# ft_seed_inventory("carrot", 8, "grams")
# ft_seed_inventory("lettuce", 12, "area")
# ft_seed_inventory("lettuce", 12, "areaa")