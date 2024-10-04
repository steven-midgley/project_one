# project_one

**Flight Tracker and Flight Delay Predictor**

## API References

- [Kaggle Dataset](https://www.kaggle.com/datasets/mahoora00135/flights)
- [OpenSky API](https://github.com/openskynetwork/opensky-api)

---

## Quickstart Guide

### 1. **Install Project Dependencies**

- Open the terminal (VS Code terminal shortcut: macOS `Control + tilde` | Windows `Ctrl + backtick`).
- Ensure you are in the project root directory, then run:

     ```bash
     pip install -r requirements.txt
     ```

### 2. **Downloading Flight Data from Kaggle** (Already Included — *Skip Unless Necessary*)

- If you need to download fresh data:
     1. Create a free [Kaggle account](https://www.kaggle.com/account/login).
     2. In Kaggle's settings, create an API key and download `kaggle.json`.
     3. Copy `kaggle.json` to the project root.
     4. Set permissions (Linux/macOS/WSL):

        ```bash
        chmod 600 kaggle/kaggle.json
        ```

     5. Run the Kaggle download command:

        ```bash
        kaggle datasets download -d mahoora00135/flights
        ```

     6. Unzip and place `flights.csv` in the `data` folder.

### 3. **Install OpenSky API**

- Install OpenSky API dependencies:

     ```bash
     pip install -e src/python3/python
     ```

- If there is an issue with `python3`, use `python`.

---

## Deployment Workflow

### **Branching and Git Commands**

- Always create a new branch for each task.
- If not on `main`:

     ```bash
     git switch main
     git pull origin main
     git checkout -b <branch-name>
     ```

- Commit and push frequently:

     ```bash
     git status
     git add .
     git commit -m 'commit message'
     git push
     ```

- For first-time branch pushes:

     ```bash
     git push --set-upstream origin <branch-name>
     ```

---

## Branch Discipline

- **Sacred Branch:** `main` – Managed by the project manager. No direct pushes.
- **Testing Branch:** `stage` – All new code goes through `stage` for review.
  - At least **two reviewers** must approve before merging into `stage`.
  - Once `stage` is stable and conflict-free, it will be merged into `main`.

---
