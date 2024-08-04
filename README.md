<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vibrato Recharge Plugin</title>
</head>
<body>
    <h1>Vibrato Recharge Plugin</h1>
    <p>A simple Python-based plugin to manage shaking currency, handle purchases, and maintain a balance history for a user. This plugin is designed for real-time interaction and allows for user-specific management of shaking currency and transactions.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Recharge Shaking Currency</strong>: Add shaking currency to the user's account.</li>
        <li><strong>Purchase Items</strong>: Make purchases with shaking currency, with a limit of 99 transactions.</li>
        <li><strong>Balance History</strong>: View the balance history for the last 9 days.</li>
    </ul>

    <h2>Installation</h2>
    <ol>
        <li><strong>Clone the Repository</strong>
            <pre><code>git clone https://github.com/yourusername/vibrato-recharge-plugin.git
cd vibrato-recharge-plugin</code></pre>
        </li>
        <li><strong>Ensure Python is Installed</strong>
            <p>This script requires Python 3.x. You can download Python from <a href="https://www.python.org/">python.org</a>.</p>
        </li>
        <li><strong>Run the Script</strong>
            <p>The script can be executed directly with Python. You do not need to make it executable.</p>
            <pre><code>python myplugin.py &lt;user_id&gt;</code></pre>
            <p>Replace &lt;user_id&gt; with the desired user ID. For example:</p>
            <pre><code>python myplugin.py user123</code></pre>
        </li>
    </ol>

    <h2>Usage</h2>
    <p>Once you run the script, you'll see a menu with the following options:</p>
    <ol>
        <li><strong>Recharge Shaking Currency</strong>: Add a specified amount of shaking currency to the user's account.</li>
        <li><strong>Purchase Item</strong>: Deduct an amount of shaking currency for purchasing an item. The maximum number of purchases is 99.</li>
        <li><strong>View Balance History</strong>: Display the balance changes over the last 9 days.</li>
        <li><strong>Exit</strong>: Exit the application.</li>
    </ol>

    <h3>Example Interaction</h3>
    <pre><code>Options:
1. Recharge Shaking Currency
2. Purchase Item
3. View Balance History
4. Exit
Select an option: 1
Enter amount to recharge: 100
Recharged 100 shaking currency. Current balance: 100

Options:
1. Recharge Shaking Currency
2. Purchase Item
3. View Balance History
4. Exit
Select an option: 2
Enter item cost: 10
Purchased item for 10. Remaining balance: 90

Options:
1. Recharge Shaking Currency
2. Purchase Item
3. View Balance History
4. Exit
Select an option: 3
Date: 2024-08-04, Amount: 100
Date: 2024-08-04, Amount: -10

Options:
1. Recharge Shaking Currency
2. Purchase Item
3. View Balance History
4. Exit
Select an option: 4
Exiting...</code></pre>

    <h2>Contributing</h2>
    <p>Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code follows the style guidelines and includes appropriate tests.</p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

    <h2>Contact</h2>
    <p>For any questions or suggestions, please open an issue on the GitHub repository or contact me at <a href="mailto:mwangeamusa@gmail.com">mwangeamusa@gmail.com</a>.</p>
</body>
</html>
