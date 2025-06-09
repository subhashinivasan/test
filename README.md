# Cool To-Do List Application

A sleek and modern to-do list application with calendar and date functionalities for each task. Designed to be interactive and visually appealing.

## Features

*   **Add Tasks:** Easily add new tasks to your list.
*   **Set Due Dates:** Assign a due date to each task using an interactive calendar (powered by Flatpickr).
*   **Mark as Complete:** Toggle tasks between complete and incomplete status. Completed tasks are visually distinguished.
*   **Delete Tasks:** Remove tasks from your list with a smooth animation.
*   **Persistent Storage:** Tasks are saved in your browser's local storage, so they persist even after you close the page.
*   **Modern Design:** A clean, modern interface with subtle animations and hover effects.
*   **Responsive:** Adapts to different screen sizes for use on desktop or mobile.

## How to Use

1.  **Open `index.html`:** Simply open the `index.html` file in your web browser.
2.  **Add a Task:**
    *   Type your task description into the input field labeled "Add a new task...".
    *   Optionally, click on the date input field next to it to select a due date from the calendar.
    *   Click the "Add Task" button or press Enter in the task input field.
3.  **Manage Tasks:**
    *   **Complete/Undo:** Click the "Complete" button (or "Undo" if already complete) next to a task to change its status.
    *   **Delete:** Click the "Delete" button to remove a task.
    *   Due dates are displayed alongside each task.

## Technologies Used

*   HTML5
*   CSS3 (with animations and responsive design)
*   JavaScript (ES6+)
*   [Flatpickr](https://flatpickr.js.org/) for the date picker functionality.

## Structure

*   `index.html`: The main HTML file for the application structure.
*   `style.css`: Contains all the styles for the application, including layout, theme, and animations.
*   `script.js`: Handles all the application logic, including task management, date handling, and local storage.

This project was created to demonstrate a modern front-end to-do list implementation.

## Sales Analysis

This project also includes a Python script for basic sales data analysis and visualization.

### `sales_analyzer.py`

The `sales_analyzer.py` script reads sales data from `sales_data.csv`, which should contain 'Year' and 'Sales' columns. It then generates a bar chart visualizing annual sales performance and saves it as `sales_chart.png`.

### How to Run the Script

1.  **Ensure you have Python installed.**
2.  **Navigate to the project directory** in your terminal.
3.  **Install dependencies:** The script requires the `matplotlib` library. You can install it using pip:
    ```bash
    pip install matplotlib
    ```
4.  **Run the script:**
    ```bash
    python sales_analyzer.py
    ```
    This will process `sales_data.csv` (if present and correctly formatted) and generate `sales_chart.png` in the same directory.

### Files

*   `sales_data.csv`: Sample CSV file containing yearly sales data.
*   `sales_analyzer.py`: Python script for reading the CSV and generating the sales chart.
*   `sales_chart.png`: Output image file of the generated sales chart.
