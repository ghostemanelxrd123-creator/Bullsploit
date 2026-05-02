<div align="center">
  <h1 align="center">Bullsploit Framework</h1>
</div>

<p align="center">
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
  [![Python 3.14](https://img.shields.io/badge/python-3.14-3776ab.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
  [![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json&style=for-the-badge)](https://github.com/astral-sh/uv)
  [![Tested with Pytest](https://img.shields.io/badge/testing-Pytest-00c0ff.svg?style=for-the-badge)](https://github.com/Alishahryar1/free-claude-code/actions/workflows/tests.yml)
  [![Type checking: Ty](https://img.shields.io/badge/type%20checking-ty-ffcc00.svg?style=for-the-badge)](https://pypi.org/project/ty/)
  [![Code style: Ruff](https://img.shields.io/badge/code%20formatting-ruff-f5a623.svg?style=for-the-badge)](https://github.com/astral-sh/ruff)
  [![Logging: Loguru](https://img.shields.io/badge/logging-loguru-4ecdc4.svg?style=for-the-badge)](https://github.com/Delgan/loguru)
</p>


<img width="1188" height="393" alt="photo_2026-04-25_15-35-52" src="https://github.com/user-attachments/assets/41f8e638-69f9-4de2-87f8-243017fbee36" />



BullSploit is a modular, high-performance penetration testing ecosystem designed for automated network reconnaissance and security research. The framework provides a robust environment for developing, managing, and executing security-centric modules.

### 🏗 Technical Architecture

The framework is built upon a modular micro-kernel design, prioritizing scalability and runtime stability.

•  Dynamic Module Introspection: Implements importlib for runtime dependency injection and module management.

•  AST-based Validation: Utilizes the Abstract Syntax Tree (AST) library for pre-execution syntax verification, ensuring core stability against malformed module code.

•  Concurrency Engine: Optimized for I/O-bound tasks using the threading library, supporting high-concurrency network operations (3000+ threads).

•  Unified Argument Parser: A specialized parameter management system providing strict type validation for user-defined inputs.

### 📂 Module Classification

Functional units are categorized into three distinct domains:
## 🛠 Installation & Deployment

The framework requires an isolated Python environment. An automated deployment script is provided for Linux-based systems.

 Automated Setup
### Clone the repository
```
git clone https://github.com/ghostemanelxrd123-creator/BullSploit.git
```

### Execute the deployment script
```
chmod +x Setup.sh
```
```
./Setup.sh
```

### Manual Launch
```
sudo BullsploitFramework.py
```

## ⚖️ Legal Disclaimer

This software is intended for authorized security auditing and educational purposes only. The developer assumes no liability for misuse or illicit activity. Unauthorized access to computer systems is illegal and strictly prohibited.

## 📝 Information

•   Lead Developer: Rapid
•   Language: Python 3.13
•   License: [MIT](LICENSE)
