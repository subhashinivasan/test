import csv
import matplotlib
matplotlib.use('Agg') # Use a non-interactive backend for environments without a display
import matplotlib.pyplot as plt

def read_sales_data(filepath):
    """
    Reads sales data from a CSV file.

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        tuple: A tuple containing two lists (years, sales).
               Returns (None, None) if an error occurs.
    """
    years = []
    sales = []
    try:
        with open(filepath, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            if 'Year' not in reader.fieldnames or 'Sales' not in reader.fieldnames:
                print(f"Error: CSV file '{filepath}' must contain 'Year' and 'Sales' columns.")
                return None, None
            for row in reader:
                try:
                    years.append(int(row['Year']))
                    sales.append(int(row['Sales']))
                except ValueError:
                    print(f"Warning: Skipping row with invalid data: {row}")
                    continue
        if not years or not sales:
            print(f"Warning: No valid data found in '{filepath}'.")
            return None, None
        return years, sales
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'.")
        return None, None
    except IOError as e:
        print(f"Error reading file '{filepath}': {e}")
        return None, None

def generate_sales_chart(years, sales, output_filepath='sales_chart.png'):
    """
    Generates and saves a bar chart of sales per year.

    Args:
        years (list): A list of years.
        sales (list): A list of sales figures corresponding to the years.
        output_filepath (str): The path to save the generated chart.
    """
    if not years or not sales or len(years) != len(sales):
        print("Error: Invalid data provided for chart generation.")
        return

    try:
        plt.figure(figsize=(10, 6))
        plt.bar(years, sales, color='skyblue')
        plt.xlabel('Year')
        plt.ylabel('Sales')
        plt.title('Annual Sales Performance')
        plt.xticks(years) # Ensure all years are displayed as ticks
        plt.tight_layout() # Adjust layout to prevent labels from being cut off
        plt.savefig(output_filepath)
        print(f"Chart saved as '{output_filepath}'")
        # plt.show() # Typically, plt.show() would be here, but it's problematic in non-GUI environments.
                     # Saving the file is the primary goal for automated scripts.
    except Exception as e:
        print(f"Error generating chart: {e}")

def main():
    """
    Main function to execute the sales analysis and chart generation.
    """
    csv_filepath = 'sales_data.csv'
    years, sales = read_sales_data(csv_filepath)

    if years and sales:
        generate_sales_chart(years, sales)
    else:
        print("Sales analysis could not be performed due to data reading errors.")

if __name__ == '__main__':
    main()
