# !/bin/sh

# Remove database
rm -f *.db
echo "Database deleted."

# Create database, tables and add mock data
python db_setup.py
python mock_create.py