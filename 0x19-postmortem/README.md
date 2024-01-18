# Postmortem

**Postmortem: Web Stack Outage on January 18, 2024**

**Issue Summary:**

- **Duration:**
    - Start Time: January 18, 2024, 10:15 AM (UTC)
    - End Time: January 18, 2024, 2:45 PM (UTC)

- **Impact:**
    - Web application downtime, affecting 30% of users.
    - Users experienced slow response times and intermittent errors during the outage.

- **Root Cause:**
    - A database connection pool exhaustion due to a misconfigured database query.

**Timeline:**

- **Detection Time:**
    - January 18, 2024, 10:15 AM (UTC)

- **Detection Method:**
    - Monitoring alert triggered due to an increased number of HTTP 500 errors.

- **Actions Taken:**
    - Investigated server logs and identified a surge in database connections.
    - Assumed a potential database overload and investigated the database server.
    - Analyzed query performance and suspected inefficient queries.

- **Misleading Paths:**
    - Initially focused on network issues, but no anomalies were found.
    - Explored potential DDoS attacks, but traffic patterns were normal.
    - Considered server hardware failure, but all system metrics were stable.

- **Escalation:**
    - Escalated the incident to the Database Operations team.
    - Engaged with the Development team to review and optimize database queries.

- **Resolution:**
    - Temporarily increased the database connection pool limit to restore service.
    - Identified and optimized poorly performing database queries.
    - Implemented a code fix to prevent similar queries from causing future connection pool exhaustion.

**Root Cause and Resolution:**

- **Root Cause:**
    - A misconfigured database query caused an excessive number of open connections to the database server. The
      connection pool was exhausted, leading to a service outage.

- **Resolution:**
    - Temporarily increased the database connection pool limit to mitigate the immediate impact.
    - Identified and optimized the problematic database queries to reduce resource consumption.
    - Deployed a code fix to prevent the misconfiguration of queries and implemented query caching for improved
      performance.

**Corrective and Preventative Measures:**

- **Improvements/Fixes:**
    - Conduct a thorough review of all database queries to identify and optimize potential performance bottlenecks.
    - Implement stricter monitoring thresholds for database connection pool usage.
    - Enhance logging and alerting mechanisms to quickly detect and respond to similar issues in the future.

- **Tasks to Address the Issue:**
    - Patch the application codebase to include the query optimization and caching changes.
    - Conduct a comprehensive review of the database schema and indexing to ensure optimal query execution.
    - Update the monitoring system to provide more granular insights into database performance.
    - Schedule a team-wide training session on best practices for database query optimization and connection management.

This postmortem serves as a valuable learning experience, highlighting the importance of continuous monitoring,
efficient query optimization, and collaborative troubleshooting. The implemented measures aim to prevent similar
incidents, ensuring a more resilient and performant web stack in the future.
