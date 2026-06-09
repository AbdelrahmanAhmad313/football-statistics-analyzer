# Football Statistics Analyzer

A Python and SQLite project that analyzes football team performance using the European Soccer Database.

This project was built to practice software engineering fundamentals, SQL query design, database analysis, and Python application development. It allows users to generate team statistics, build league tables, and filter results by season and league.

---

## Features

### Team Statistics

Generate detailed statistics for any team:

* Wins
* Draws
* Losses
* Goals Scored
* Goals Conceded
* Goal Difference
* Points

Example:

```python
getTeamStats("FC Barcelona", season="2015/2016")
```

Output:

```python
{
    "wins": 29,
    "draws": 4,
    "losses": 5,
    "goals_scored": 112,
    "goals_conceded": 29,
    "goal_difference": 83,
    "points": 91
}
```

---

### Dynamic Filtering

Most statistics functions support optional filtering by:

* Season
* League

Example:

```python
getWins("FC Barcelona")
getWins("FC Barcelona", season="2015/2016")
getWins("FC Barcelona", league_id=21518)
getWins("FC Barcelona", season="2015/2016", league_id=21518)
```

---

### League Table Generation

Generate complete league tables using optimized SQL queries.

The league table calculation includes:

* Points
* Goals Scored
* Goals Conceded
* Goal Difference

Tables are automatically sorted by:

1. Points
2. Goal Difference

---

## Technologies Used

* Python
* SQLite
* SQL
* Git
* GitHub

---

## SQL Concepts Applied

This project applies a wide range of SQL concepts including:

* SELECT
* WHERE
* COUNT
* SUM
* JOIN
* GROUP BY
* ORDER BY
* CASE WHEN
* UNION ALL
* Aggregate Queries
* Derived Tables (Subqueries)
* Dynamic Query Construction
* Parameterized Queries

---

## Project Structure

```text
Football-Statistics-Analyzer/

├── data/
│   └── database.sqlite

├── helpers/

├── src/
│   ├── analyzer.py
│   ├── database.py
│   ├── league_table.py
│   └── stats.py

├── .gitignore
└── README.md
```

---

## Query Optimization

One of the main goals of this project was learning how to move calculations from Python into SQL.

Instead of executing multiple queries for each team, league tables are generated using a single optimized SQL query built with:

* UNION ALL
* CASE WHEN
* GROUP BY
* SUM

This significantly reduces the amount of Python processing required and allows the database engine to perform the heavy calculations.

---

## Database

This project uses the European Soccer Database.

The database file is not included in this repository because of its size.

To run the project:

1. Download the European Soccer Database.
2. Place `database.sqlite` inside the `data/` directory.
3. Run `analyzer.py`.

---

## Learning Objectives

This project was created to practice:

* Python programming
* SQL query development
* Database exploration
* Query optimization
* Code refactoring
* Modular project organization
* Git and GitHub workflows

---

## Future Improvements

Potential future enhancements include:

* Command-line interface (CLI)
* Data visualization
* Player statistics
* League comparison tools
* Web dashboard

---

## Author

Abdelrahman Ahmed

Aspiring Software Engineer / Data Engineer

Focused on building practical projects with Python, SQL, and data-driven applications.
