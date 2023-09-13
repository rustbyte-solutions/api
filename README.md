# api 🌐
An internal API we use for safe communication with our database at rustbyte.
Currently only being used for fetching avatars from a database to use on [our website](https://github.com/rustbyte-solutions/rustbyte-website).

## Installing & Running 📥
We do no recommend running this API, but here are the instructions anyways.
1. Setup a PostgreSQL database with the [`data/schema.sql`](https://github.com/rustbyte-solutions/api/data/schema.sql) schema.
2. Rename `config.toml.example` to `config.toml` and fill in the required credentials.
3. Create a virtual environment (optional) and install the requirements from the `requirements.txt` file.
4. Run the project using uvicorn: `uvicorn main:app --reload`
Don't expect us to help you with running it.