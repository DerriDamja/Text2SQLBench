# Text2SQL Benchmark

**Text2SQL** is an automated benchmarking framework used to evaluate AI-generated SQL queries against a subset of the Spider 1.0 dataset.

## Recommended Setup
To run this on your own machine, it is recommended to use Docker to run the benchmark environment in containers.

Requires Docker Desktop (Windows, MacOS) or Docker Engine w/ Compose (Linux).

```bash
git clone https://github.com/DerriDamja/Text2SQL.git
cd Text2SQL
```

At this point, it is encouraged to copy and modify the **.env.example** file to best fit your needs. Remember to rename your copy to **.env** before continuing.

```bash
docker compose up -d
```

This will pull the required **PostgreSQL** and **Ollama** images, which may require **~9-10 GB** of storage.