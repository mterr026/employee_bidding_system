# Use the official Python image from Microsoft
ARG VARIANT="3.12"
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}

# Environment variables for PostgreSQL
ENV POSTGRES_USER=postgres 
ENV POSTGRES_PASSWORD=123
ENV POSTGRES_DB=postgres

# Install PostgreSQL and dependencies
RUN apt-get update && \
    apt-get install -y postgresql postgresql-contrib curl sudo gnupg

# Install the public key for the repository
RUN curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg

# Create the repository configuration file
RUN sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list' && \
    apt-get update

# Install pgAdmin4 in web mode
RUN apt-get install -y pgadmin4-web

# Configure pgAdmin4
#RUN /usr/pgadmin4/bin/setup-web.sh --yes

# Expose the ports for PostgreSQL and pgAdmin4
EXPOSE 5432 80 8000 8080

# Script to start PostgreSQL and pgAdmin4
COPY scripts/startup.sh /usr/local/bin/startup.sh
RUN chmod +x /usr/local/bin/startup.sh

# Command to run the startup script
CMD ["/usr/local/bin/startup.sh"]