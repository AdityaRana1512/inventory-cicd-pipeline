def calculate_stock(current_stock, sold):
    return current_stock - sold

if __name__ == "__main__":
    print("Inventory CI/CD Pipeline Demo")
    print("Remaining Stock:", calculate_stock(100, 20))
