# MLOps ETL Lab

## Pipeline Steps
1. Load CSV data
2. Clean: remove missing rows
3. Feature Engineering: added tip percentage

## Tools Used
- Python (pandas)
- Git (code versioning)
- DVC (data versioning)

## File Structure
- data/raw/tips.csv — Raw data
- data/processed/tips_clean.csv — Cleaned data
- etl.py — ETL script

## 🧠 Reflection: Version Control in MLOps

### Data, Code, and Model Versioning
- I used Git to version the ETL script (`etl.py`)
- I used DVC to version both raw and processed data (`tips.csv` and `tips_clean.csv`)
- This setup allows me to go back in time and reproduce any previous pipeline state

### 🔄 Example of Reproducibility
- I updated the raw CSV by adding a new row
- Then I ran `python -m dvc add`, followed by a Git commit
- Later, I used `git checkout <old_commit>` + `dvc checkout` to revert the data back
- This shows how easily experiments can be reproduced and undone

### 🧪 Experimentation
- I created a new branch and modified the ETL script to add a new feature
- The change was isolated and testable
- I could merge this later without affecting the main pipeline

---

## 📘 Discussion

**Q: How might this workflow change if the dataset were very large (GBs or TBs) and updated daily?**  
A: I would store data remotely using DVC remotes (e.g., S3, Google Drive) and automate DVC pipelines using `dvc.yaml` and CI/CD tools like GitHub Actions.

**Q: What additional steps could you include to check data quality before adding new data to the pipeline?**  
A: Use data validation tools like [Great Expectations](https://greatexpectations.io/) to create rules for missing values, data types, or valid ranges before accepting new data.

**Q: How would you handle conflicting changes if multiple collaborators updated the data or ETL script simultaneously?**  
A: I would use Git branches for each collaborator, ensure changes are tested, and resolve merge conflicts before pushing to `main`. For data, I’d use DVC locks or merge metadata carefully.
