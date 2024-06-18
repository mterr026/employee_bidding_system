#!/bin/bash
# Start PostgreSQL service
service postgresql start

# Start pgAdmin4 service
service apache2 start

# Keep the container running
tail -f /dev/null
