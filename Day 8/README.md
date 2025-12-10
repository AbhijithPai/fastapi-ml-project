# ✅ Day 8 — CI Foundations in MLOps (2 Hours)

Today I implemented **Continuous Integration (CI)** for my ML API using **GitHub Actions**.

The CI pipeline automatically triggers on every push or pull request to the `main` branch and performs the following things:
- Sets up a clean Linux environment
- Installs Python dependencies
- Runs tests
- Builds the Docker image

This ensures my ML system is reproducible, stable, and protected against silent breakages before deployment.  
It moves the project from *local-only validation* to *automated, production-ready checks*.

✅ CI workflow added under `.github/workflows/ci.yml`  
✅ Code quality is now enforced automatically

**Time spent:** ~2 hours

