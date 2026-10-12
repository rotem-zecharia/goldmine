# Wisser/Jailer

Database Subsetting and Relational Data Browsing Tool.

## installation

1. Download the installer for Windows (`.msi`) or Linux (`.deb`) from the [latest release](https://github.com/Wisser/Jailer/releases/latest), or the zip for any platform with Java (see [Installation](#installation)).
2. Start Jailer and open the included **demo database**. No configuration needed.
3. Connect to your own database and start the **Data Browser** or the **Subsetter**.

## features

- Exports consistent and referentially intact row-sets from your productive database
   and imports the data into your development and test environment.
 - Improves database performance by removing and archiving obsolete data without violating integrity.
 - Generates topologically sorted SQL-DML, hierarchically structured JSON, YAML, XML and DbUnit datasets.
 - Data Browsing. Navigate bidirectionally through the database by following foreign-key-based or user-defined relationships.
 - SQL Console with code completion, syntax highlighting, charts and database metadata visualization.
 - AI Subsetting Assistant. Describe in natural language what data to subset. The AI generates the subject table, WHERE condition, and association restrictions.
 - AI Query Assistant and Advisor. Generate SQL from natural language questions using Anthropic or OpenAI-compatible APIs with smart table selection for large schemas. Analyze, explain, and refactor existing SQL queries with AI assistance.
 - A demo database is included with which you can get a first impression without any configuration effort.

## Supported Databases

Thanks to the JDBC technology used, any DMBS is in principle supported. For best results, specific additional support features are useful, however. These are available for:

 - PostgreSQL
 - Oracle
 - MySQL
 - MariaDB
 - Microsoft SQL Server
 - IBM Db2
 - SQLite
 - Sybase
 - Amazon Redshift
 - Firebird
 - Informix Dynamic Server
 - H2
 - Exasol

## News

 - 2026-06-25    AI Subsetting Assistant: Describe in natural language what data to subset. The AI generates the subject table, WHERE condition, and association restrictions.
 - 2026-05-31    SQL Advisor: Analyze, explain, and refactor existing SQL queries with AI assistance. A suggestions menu covers the most common tasks (explain, optimize, rewrite as CTEs, find NULL issues, and more). Results are shown as a split view with the revised SQL on the left and a formatted explanation on the right. An inline diff toggle highlights removed and added lines directly in the SQL area.
 - 2026-05-15    AI Query Assistant: Generate SQL from natural language questions using Anthropic or OpenAI-compatible APIs (OpenAI, Azure, Groq, Ollama, OpenRouter, etc.) with smart table selection for large schemas.
 - 2024-07-04    Data can now also be exported as structured JSON and YAML files.
 - 2024-06-26    A dark UI theme has been introduced that improves readability in low light environments.
 - 2024-04-18    DDL scripts for creating database objects can now be generated thanks to an integration of the [Liquibase](https://www.liquibase.com) tool. This makes it possible to create subset databases from scratch using only on-board means.
 - 2023-02-03    Thanks to deep analysis of statements, the SQL console can now relate the result of queries to the source tables and display them accordingly. In addition, this technique also allows filter conditions to be dynamically added to arbitrary SQL queries.
 - 2022-01-01    Comprehensive redesign and modernization of the entire user interface. New Look & Feel [FlatLaf](https://github.com/JFormDesigner/FlatLaf). 
 - 2021-02-04    Cycles in parent-child relationships will be detected and broken. Thus, such data can be exported by deferring the insertion of nullable foreign keys.
 - 2020-02-04    The Jailer engine is published in Maven repository. https://mvnrepository.com/artifact/io.github.wisser/jailer-engine
 - 2019-02-01    The new "Model Migration Tool" allows you to easily find and edit the newly added associations if the data model has been extended after the last change to this extraction model.
 - 2018-04-26    The new feature "Analyze SQL" analyzes SQL statements and proposes association definitions. This allows to reverse-engineer the data model based on existing SQL queries.
 - 2018-03-06    SQL Console with code completion, syntax highlighting and database metadata visualization.
 - 2017-05-10    New API provides programmatic access to the data
