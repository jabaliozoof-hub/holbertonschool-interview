# Algorithmic Interview Preparation & Technical Challenges 🧠🐍

Welcome to my **Algorithmic Interview Preparation** repository completed at **Holberton School**. This repository features rigorous algorithmic problem-solving, data structures, and optimization tasks implemented cleanly in **Python 3**, focusing on time/space complexity and PEP 8 compliance.

---

## 📌 Topics Covered & Solutions

| Directory / Problem | Description & Core Concepts | Complexity Focus |
| :--- | :--- | :--- |
| `lockboxes` | Key-unlock graph traversal problem | Breadth-First / Depth-First Search |
| `log_parsing` | Real-time log data filtering and metrics computation | String Parsing, Stream Processing |
| `minimum_operations` | Optimal character duplication sequences (H-Index style) | Dynamic Programming / Greedy |
| `nqueens` | Classic chess backtracking problem | Recursion, Backtracking, State Space Trees |
| `pascal_triangle` | Mathematical triangle generation | Matrix generation, List comprehensions |
| `rotate_2d_matrix` | In-place 2D matrix manipulation | Matrix traversal, Space optimization ($O(1)$) |
| `utf8_validation` | Bitwise operations and byte validation | Bit manipulation, Protocol parsing |

---

## 🛠️ Environment & Standards

- **Language:** Python 3.8+
- **Style Guidelines:** PEP 8 (checked via `pycodestyle`)
- **Execution:** All scripts are tested and executable under Linux / WSL2 environments.

---

## 🚀 How to Run Any Script

To test any individual script or module:

```bash
python3 -m <directory_name>.<script_name>
# Example for lockboxes:
python3 -c 'from lockboxes.0-lockboxes import canUnlockAll; print(canUnlockAll([[1], [2], [3], [4], []]))'
