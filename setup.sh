# !/bin/sh

# Remove database
rm -f *.db
echo "Database deleted."

# Create database and tables
python tests/db_setup.py