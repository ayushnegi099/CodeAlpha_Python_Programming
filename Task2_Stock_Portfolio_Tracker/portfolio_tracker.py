import csv
from datetime import datetime

# Hardcoded dictionary defining stock prices (in USD)
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "AMZN": 185.00,
    "GOOGL": 175.00,
    "NVDA": 120.00,
    "META": 480.00,
    "NFLX": 600.00
}

def display_available_stocks():
    print("\n" + "="*40)
    print("      AVAILABLE STOCKS & CURRENT PRICES")
    print("="*40)
    for stock, price in STOCK_PRICES.items():
        print(f"  - {stock:6} : ${price:8.2f}")
    print("="*40)

def save_to_txt(portfolio, total_value):
    filename = "portfolio_report.txt"
    try:
        with open(filename, "w") as f:
            f.write("==================================================\n")
            f.write("             STOCK PORTFOLIO REPORT               \n")
            f.write(f"             Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("==================================================\n")
            f.write(f"{'Stock':<10}{'Quantity':<12}{'Unit Price':<12}{'Total Value':<12}\n")
            f.write("-"*52 + "\n")
            for stock, qty in portfolio.items():
                price = STOCK_PRICES[stock]
                val = qty * price
                f.write(f"{stock:<10}{qty:<12.2f}${price:<11.2f}${val:<11.2f}\n")
            f.write("-"*52 + "\n")
            f.write(f"{'TOTAL PORTFOLIO VALUE:':<34}${total_value:<11.2f}\n")
            f.write("==================================================\n")
        print(f"\n[Success] Portfolio saved successfully to '{filename}'!")
    except Exception as e:
        print(f"\n[Error] Could not save to text file: {e}")

def save_to_csv(portfolio, total_value):
    filename = "portfolio_report.csv"
    try:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock Portfolio Report"])
            writer.writerow(["Date", datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
            writer.writerow([])
            writer.writerow(["Stock", "Quantity", "Unit Price (USD)", "Total Value (USD)"])
            for stock, qty in portfolio.items():
                price = STOCK_PRICES[stock]
                val = qty * price
                writer.writerow([stock, qty, f"{price:.2f}", f"{val:.2f}"])
            writer.writerow([])
            writer.writerow(["Total Portfolio Value", "", "", f"{total_value:.2f}"])
        print(f"\n[Success] Portfolio saved successfully to '{filename}'!")
    except Exception as e:
        print(f"\n[Error] Could not save to CSV file: {e}")

def main():
    print("*" * 50)
    print("Welcome to the Stock Portfolio Tracker!")
    print("*" * 50)
    
    portfolio = {}
    display_available_stocks()
    
    while True:
        stock_input = input("\nEnter stock symbol (or type 'done' to finish, 'list' to view prices): ").strip().upper()
        
        if stock_input == 'DONE':
            break
        elif stock_input == 'LIST':
            display_available_stocks()
            continue
        elif stock_input not in STOCK_PRICES:
            print(f"Error: '{stock_input}' is not in our tracked list. Please select one of the available stocks.")
            continue
        
        # Get quantity
        try:
            qty_input = input(f"Enter quantity of {stock_input} you own: ").strip()
            qty = float(qty_input)
            if qty < 0:
                print("Quantity cannot be negative. Please enter a valid amount.")
                continue
            elif qty == 0:
                if stock_input in portfolio:
                    del portfolio[stock_input]
                    print(f"Removed {stock_input} from your portfolio.")
                else:
                    print("Quantity is zero. Nothing added.")
                continue
        except ValueError:
            print("Invalid input. Quantity must be a number.")
            continue
        
        # Add or update portfolio
        portfolio[stock_input] = portfolio.get(stock_input, 0.0) + qty
        print(f"Updated: {qty} shares of {stock_input} added to portfolio (Total: {portfolio[stock_input]} shares).")

    if not portfolio:
        print("\nYour portfolio is empty. Exiting.")
        return

    # Calculate and Display Results
    print("\n" + "="*55)
    print("                    YOUR PORTFOLIO SUMMARY")
    print("="*55)
    print(f"{'Stock':<10}{'Quantity':<12}{'Unit Price':<12}{'Total Value':<12}{'Weight':<8}")
    print("-"*55)
    
    total_val = 0.0
    portfolio_details = []
    
    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        val = qty * price
        total_val += val
        portfolio_details.append((stock, qty, price, val))
        
    for stock, qty, price, val in portfolio_details:
        weight = (val / total_val) * 100 if total_val > 0 else 0
        print(f"{stock:<10}{qty:<12.2f}${price:<11.2f}${val:<11.2f}{weight:>5.1f}%")
        
    print("-"*55)
    print(f"{'TOTAL INVESTMENT:':<34}${total_val:<11.2f}")
    print("="*55)
    
    # Save Options
    while True:
        save_choice = input("\nWould you like to save this portfolio report? (txt / csv / no): ").strip().lower()
        if save_choice in ['txt', 'text']:
            save_to_txt(portfolio, total_val)
            break
        elif save_choice == 'csv':
            save_to_csv(portfolio, total_val)
            break
        elif save_choice in ['no', 'n', 'exit']:
            print("Portfolio not saved. Thank you for using Stock Portfolio Tracker!")
            break
        else:
            print("Invalid choice. Please enter 'txt', 'csv', or 'no'.")

if __name__ == "__main__":
    main()