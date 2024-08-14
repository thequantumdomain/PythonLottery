Python Lottery <br>

Explanation<br>
fetch_random_users(size): Fetches random users from the API given in task.<br>
init_db(): Initializes the SQLite database and creates the winner table (id, email, state) if it doesn't already exist.<br>
update_winner(conn, user_data): Inserts or replaces a winner entry in the database.<br>
main(): Main function that runs the lottery system until 25 unique state winners are found. It fetches random users every 10 seconds and updates the database accordingly.<br>

Running the Script<br>
Ensure the virtual environment is activated.<br>
Run the script by executing <br>
-- python3 lottery.py<br>

Output
<br>
Final Winners:<br>
(6, 'whitney.howell@email.com', 'South Dakota')<br>
(830, "margarito.o'conner@email.com", 'Pennsylvania')<br>
(1118, 'santos.frami@email.com', 'South Carolina')<br>
(1122, 'rusty.nitzsche@email.com', 'Massachusetts')<br>
(1170, 'moises.heaney@email.com', 'Idaho')<br>
(3485, 'denver.jaskolski@email.com', 'Connecticut')<br>
(3953, 'michel.daniel@email.com', 'Maryland')<br>
(4495, 'landon.waelchi@email.com', 'Arizona')<br>
(4814, 'raymundo.braun@email.com', 'Oregon')<br>
(4824, 'wanetta.hettinger@email.com', 'New Mexico')<br>
(5169, 'selena.reichel@email.com', 'Michigan')<br>
(5594, 'marianna.rohan@email.com', 'Missouri')<br>
(6027, 'ezekiel.herzog@email.com', 'Delaware')<br>
(6171, 'nickie.treutel@email.com', 'Minnesota')<br>
(6505, 'tiesha.cole@email.com', 'Maine')<br>
(7133, 'adolfo.feil@email.com', 'Kentucky')<br>
(7360, 'raymond.hyatt@email.com', 'North Dakota')<br>
(7680, 'charlena.wintheiser@email.com', 'North Carolina')<br>
(7976, 'cheryle.steuber@email.com', 'Illinois')<br>
(8222, 'tim.pagac@email.com', 'New York')<br>
(8403, 'billie.cremin@email.com', 'Louisiana')<br>
(8420, 'rigoberto.roberts@email.com', 'Georgia')<br>
(9702, 'fay.kautzer@email.com', 'California')<br>
(9944, 'elijah.kreiger@email.com', 'Alaska')<br>
(9967, 'meryl.kirlin@email.com', 'New Hampshire')<br>

Testing<br>
To test the functionality, run the script and observe the output.<br>
Ensure the database is being updated correctly and that the final output displays 25 unique winners from different states.<br>

Code Review<br>
Using a venv keeps dependencies required by different projects separate.<br>
Modularizing the code into functions optimizes readability and maintainability.<br>
Handling database operations carefully to avoid SQL injection attacks (though not demonstrated in this simple script).<br>
Regularly committing changes to the database to ensure data integrity.<br>
This script provides the basic framework for a lottery system.<br>
Depending on the exact requirements and constraints, further refinements and error handling may be necessary.<br>

Key Iterations<br>
Logging Changes: Added a print statement in the update_winner function to log whenever a new winner is added or an existing winner is replaced. This provides clear logs indicating changes in the table.<br>
Loop Continuation: The loop in the main function continues fetching random users every 10 seconds until there are 25 unique state winners. This is ensured by checking the length of the states_won dictionary, which tracks the count of unique states with winners.<br>

Testing and Validation<br>
Observe the terminal output to ensure that the script runs continuously, fetching new users every 10 seconds.<br>
- To improve we can implement a time-stamp log which displays the time of each selection (+10s).<br>
Verify that the logs clearly indicate additions or replacements in the winner table.<br>
Once 25 unique state winners are identified, the script should terminate and print the final list of winners.<br>

Run tests by<br>
-- python3 -m unittest discover -s tests<br>

Output of Tests 14.08.2024 09:30<br>
----------------------------------------------------------------------
Ran 4 tests in 50.105s<br>

OK<br>

Notes<br>
OpenSSL warning - common situation for MacOS users due to Python being compiled with LibreSSL instead of OpenSSL. Informational warning - indicates that urllib3 v2.x supports OpenSSL 1.1.1+ but detects LibreSSL 2.8.3, which can lead to untested configurations.<br>
Since the tests are passing and the warning does not impact functionality, we opt to ignore it.<br>
If issues related to SSL/TLS connections in the application that could be attributed to the LibreSSL configuration we can address directly.<br>

Terome J. Mensah
