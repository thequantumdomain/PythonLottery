Python Lottery 

Explanation
fetch_random_users(size): Fetches random users from the API given in task.
init_db(): Initializes the SQLite database and creates the winner table (id, email, state) if it doesn't already exist.
update_winner(conn, user_data): Inserts or replaces a winner entry in the database.
main(): Main function that runs the lottery system until 25 unique state winners are found. It fetches random users every 10 seconds and updates the database accordingly.

Running the Script
Ensure the virtual environment is activated.
Run the script by executing 
-- python3 lottery.py

Output

Final Winners:
(6, 'whitney.howell@email.com', 'South Dakota')
(830, "margarito.o'conner@email.com", 'Pennsylvania')
(1118, 'santos.frami@email.com', 'South Carolina')
(1122, 'rusty.nitzsche@email.com', 'Massachusetts')
(1170, 'moises.heaney@email.com', 'Idaho')
(3485, 'denver.jaskolski@email.com', 'Connecticut')
(3953, 'michel.daniel@email.com', 'Maryland')
(4495, 'landon.waelchi@email.com', 'Arizona')
(4814, 'raymundo.braun@email.com', 'Oregon')
(4824, 'wanetta.hettinger@email.com', 'New Mexico')
(5169, 'selena.reichel@email.com', 'Michigan')
(5594, 'marianna.rohan@email.com', 'Missouri')
(6027, 'ezekiel.herzog@email.com', 'Delaware')
(6171, 'nickie.treutel@email.com', 'Minnesota')
(6505, 'tiesha.cole@email.com', 'Maine')
(7133, 'adolfo.feil@email.com', 'Kentucky')
(7360, 'raymond.hyatt@email.com', 'North Dakota')
(7680, 'charlena.wintheiser@email.com', 'North Carolina')
(7976, 'cheryle.steuber@email.com', 'Illinois')
(8222, 'tim.pagac@email.com', 'New York')
(8403, 'billie.cremin@email.com', 'Louisiana')
(8420, 'rigoberto.roberts@email.com', 'Georgia')
(9702, 'fay.kautzer@email.com', 'California')
(9944, 'elijah.kreiger@email.com', 'Alaska')
(9967, 'meryl.kirlin@email.com', 'New Hampshire')

Testing
To test the functionality, run the script and observe the output.
Ensure the database is being updated correctly and that the final output displays 25 unique winners from different states.

Code Review
Using a venv keeps dependencies required by different projects separate.
Modularizing the code into functions optimizes readability and maintainability.
Handling database operations carefully to avoid SQL injection attacks (though not demonstrated in this simple script).
Regularly committing changes to the database to ensure data integrity.
This script provides the basic framework for a lottery system.
Depending on the exact requirements and constraints, further refinements and error handling may be necessary.

Key Iterations
Logging Changes: Added a print statement in the update_winner function to log whenever a new winner is added or an existing winner is replaced. This provides clear logs indicating changes in the table.
Loop Continuation: The loop in the main function continues fetching random users every 10 seconds until there are 25 unique state winners. This is ensured by checking the length of the states_won dictionary, which tracks the count of unique states with winners.

Testing and Validation
Observe the terminal output to ensure that the script runs continuously, fetching new users every 10 seconds.
- To improve we can implement a time-stamp log which displays the time of each selection (+10s).
Verify that the logs clearly indicate additions or replacements in the winner table.
Once 25 unique state winners are identified, the script should terminate and print the final list of winners.

Run tests by
-- python3 -m unittest discover -s tests

Output of Tests 14.08.2024 09:30
----------------------------------------------------------------------
Ran 4 tests in 50.105s

OK

Notes
OpenSSL warning - common situation for MacOS users due to Python being compiled with LibreSSL instead of OpenSSL. Informational warning - indicates that urllib3 v2.x supports OpenSSL 1.1.1+ but detects LibreSSL 2.8.3, which can lead to untested configurations.
Since the tests are passing and the warning does not impact functionality, we opt to ignore it.
If issues related to SSL/TLS connections in the application that could be attributed to the LibreSSL configuration we can address directly.

Terome J. Mensah