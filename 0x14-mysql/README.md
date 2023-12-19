"""
README for MySQL Replication Project

This project aims to implement MySQL replication, which is the process of copying data from one MySQL database to another. The replication process involves a master database that serves as the source of data and one or more slave databases that receive and apply the replicated data.

To get started with this project, follow the steps below:

1. Install MySQL on your machine.
2. Set up a master database by configuring the necessary settings in the MySQL configuration file.
3. Create one or more slave databases by configuring the replication settings in the MySQL configuration file.
4. Start the MySQL server on both the master and slave databases.
5. Test the replication by making changes to the master database and verifying that the changes are replicated to the slave databases.

For more detailed instructions and troubleshooting tips, refer to the project's documentation located in the 'docs' directory.

Author: [Your Name]
Date: [Current Date]
"""
/**
 * This query retrieves all customers from the 'customers' table
 * who have made a purchase in the last 30 days.
 *
 * @return array An array of customer records.
 */
SELECT * FROM customers WHERE purchase_date >= DATE_SUB(NOW(), INTERVAL 30 DAY);
