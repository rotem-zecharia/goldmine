# Wisser/Jailer

Database Subsetting and Relational Data Browsing Tool.

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

## installation

Use the installation file "Jailer-database-tools-n.n.n.msi" (for Windows) or "jailer-database-tools_n.n.n-x64.deb" (for Linux).

Unless you want to use your own Java installation. Or also if you want to use the command line interface (CLI). In this cases unzip the file "jailer_n.n.n.zip". See also <a href="https://wisser.github.io/Jailer/faq.html#multiuser">https://wisser.github.io/Jailer/faq.html#multiuser</a>

To start the tool from the unpacked zip:

  - On windows platform execute "Jailer.exe". You can also start "jailerGUI.bat".
  - On Unix/Linux/macOS platform execute the script "jailerGUI.sh" or use "java -jar jailer.jar"
