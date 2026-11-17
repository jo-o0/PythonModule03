import sys


class DuplicateItem(Exception):
    def __init__(self, message: str =
                 "Duplicated item...Discarding...") -> None:
        super().__init__(message)


class NotAnItem(Exception):
    def __init__(self, message: str = "Not an item...Discarding..."):
        super().__init__(message)

class NotANum(Exception):
    def __init__(self, message: str = "One item's quantity is not a number... discarding..."):
        super().__init__(message)


def ft_inventory_logic(inventory: dict) -> None:
    ft_key: int = len(inventory.keys())
    total: int = sum(inventory.values())
    print(f"Inventory: {inventory}\n")
    print(f"Total quantity of the {ft_key} items: {total}")
    for item, qnty in inventory.items():
        percentaje: float = qnty / total * 100
        print(f"{item} represents: {percentaje:.1f}%")
    most_item, most_qty = max(inventory.items(), key=lambda x: x[1])
    min_item, min_qty = min(inventory.items(), key=lambda x: x[1])
    print(f"The most abundant item is {most_item} "
          f"with a total quantity of {most_qty} ")
    print(f"The least abundant item is {min_item}"
          f"with a total quantity of {min_qty}")


def arg_pars(arg: str, inventory: dict) -> dict:
    item: str
    quantity: str
    if ':' not in arg:
        raise NotAnItem()
    item, quantity = arg.split(":", 1)
    if not quantity.isdigit():
        raise NotANum()
    qnty: int = int(quantity)
    if item in inventory:
        raise DuplicateItem()
    inventory.update({item: qnty})
    return inventory


def ft_inventory(args: list) -> None:
    inventory: dict = {}
    for arg in args:
        try:
            inventory = arg_pars(arg, inventory)
        except (Exception, ValueError, NotAnItem, DuplicateItem) as err:
            print(f"Found Error: {err}")
    ft_inventory_logic(inventory)
    new_item: str = input("\nPlease introduce a new item: ")
    try:
        arg_pars(new_item, inventory)
    except (Exception, ValueError, NotAnItem, DuplicateItem) as err:
        print(f"Found Error: {err}")
    print(f"Updated Inventory: {inventory}\n")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===\n")
    nArgs: int = len(sys.argv)
    if nArgs == 1:
        print("No inventory provided... Please make sure"
              "you provide the items in the format 'item:quantity'")
    else:
        ft_inventory(sys.argv[1:])
    print("=== End of program ===")
