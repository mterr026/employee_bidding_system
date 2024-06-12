# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.0/containers/python-3/.devcontainer/base.Dockerfile

ARG VARIANT="3.11"
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

ENV POSTGRES_USER=postgres 
ENV POSTGRES_PASSWORD=123
ENV POSTGRES_DB=postgres

# Install PostgreSQL and dependencies
RUN apt-get update && \
    apt-get install -y postgresql postgresql-contrib

# Install the public key for the repository:
    RUN curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg

    # Create the repository configuration file:
    RUN sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
    
    # Install for web mode only: 
    RUN sudo apt install -y pgadmin4-web
    # Start PostgreSQL
    
    RUN service postgresql start
    RUN export PGADMIN_PLATFORM_TYPE=debian
    

    
    #after install of pgadmin4
    RUN export PGADMIN_PLATFORM_TYPE=debian


EXPOSE 8000 5433 5050
