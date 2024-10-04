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

### 2. **Download Flight Data from Kaggle**

   *(Note: Data is already included; skip unless necessary.)*

- Steps to download the data:
     1. Create a free [Kaggle account](https://www.kaggle.com/account/login).
     2. In Kaggle's settings, generate an API key and download `kaggle.json`.
     3. Copy `kaggle.json` to the project root and set permissions (Linux/macOS/WSL):

        ```bash
        chmod 600 kaggle/kaggle.json
        ```

     4. Download the dataset:

        ```bash
        kaggle datasets download -d mahoora00135/flights
        ```

     5. Unzip and move the `flights.csv` file to the `data` folder.

### 3. **Install OpenSky API**

- Install OpenSky API dependencies:

     ```bash
     pip install -e src/python3/python
     ```

- If you encounter issues with `python3`, use `python`.

---

## Deployment Workflow

### 1. **Branching and Git Commands**

- Create a new branch for each task.
- If not on `main`, switch to it:

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

- For the first push of a new branch:

     ```bash
     git push --set-upstream origin <branch-name>
     ```

---

## Branch Discipline

- **Protected Branch:** `main` – Managed by the project manager. No direct pushes allowed.
- **Testing Branch:** `stage` – All code contributions are merged into `stage` .
- Once `stage` is stable and conflict-free, it will be merged into `main`.

---
