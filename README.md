<p align="center">
  <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="100" />
</p>
<p align="center">
    <h1 align="center">SCRAPY</h1>
</p>
<p align="center">
    <em>Scrape Smarter, Not Harder-Your Career Catalyst</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/shivatmax/Scrapy?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/shivatmax/Scrapy?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/shivatmax/Scrapy?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/shivatmax/Scrapy?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat&logo=Streamlit&logoColor=white" alt="Streamlit">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat&logo=Pydantic&logoColor=white" alt="Pydantic">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
</p>
<hr>

## 🔗 Quick Links

> - [📍 Overview](#-overview)
> - [📦 Features](#-features)
> - [📂 Repository Structure](#-repository-structure)
> - [🧩 Modules](#-modules)
> - [🚀 Getting Started](#-getting-started)
>   - [⚙️ Installation](#️-installation)
>   - [🤖 Running Scrapy](#-running-Scrapy)
>   - [🧪 Tests](#-tests)
> - [🛠 Project Roadmap](#-project-roadmap)
> - [🤝 Contributing](#-contributing)
> - [📄 License](#-license)
> - [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

Scrapy is a streamlined job scraping framework that systematically compiles listings from multiple job platforms, excluding Indeed, into a single CSV file for efficient job searches. It utilizes an interactive Streamlit front-end for parameter input, fostering user accessibility. By incorporating custom exceptions and advanced utility functions, Scrapy enhances data processing, facilitates error handling across different job sites, and offers unique features such as urgency detection and precise currency parsing. This amalgamation maximizes job seekers' efficiency and effectiveness in their employment quest.

---

## 📦 Features

|    | Feature            | Description                                                                                           |
|----|--------------------|-------------------------------------------------------------------------------------------------------|
| ⚙️  | **Architecture**   | Scrapy utilizes Streamlit for the interactive UI and employs Beautiful Soup for HTML content parsing. |
| 🔩 | **Code Quality**   | Code adheres to standard Python conventions, though specific style checks and linting are not evident. |
| 📄 | **Documentation**  | `requirements.txt` and repository content describe the purpose, but in-code commenting is limited.     |
| 🔌 | **Integrations**   | Integrates Streamlit for UI and Beautiful Soup for scraping, apart from core Python libraries.        |
| 🧩 | **Modularity**     | The codebase contains utility functions and custom exceptions, suggesting modular design practices.    |
| 🧪 | **Testing**        | Testing frameworks and tools are not explicitly mentioned, so test infrastructure remains unclear.    |
| ⚡️ | **Performance**    | Performance insight is limited without benchmarks, but reliance on Beautiful Soup may affect it.       |
| 🛡️ | **Security**       | No explicit security measures or data protection practices are documented in the codebase.             |
| 📦 | **Dependencies**   | Dependencies include Streamlit, Pydantic, Pandas, Beautiful Soup, and several Python standard libraries.|
| 🚀 | **Scalability**    | Scalability is unclear from the repository's documentation; tailored for small to medium-scale scraping.|


---

## 📂 Repository Structure

```sh
└── Scrapy/
    ├── README.md
    ├── Scrappy
    │   ├── __init__.py
    │   ├── jobs
    │   │   └── __init__.py
    │   └── scrapers
    │       ├── __init__.py
    │       ├── exceptions.py
    │       ├── glassdoor
    │       │   └── __init__.py
    │       ├── indeed
    │       │   └── __init__.py
    │       ├── linkedin
    │       │   └── __init__.py
    │       ├── utils.py
    │       └── ziprecruiter
    │           └── __init__.py
    ├── requirements.txt
    └── scrapy.py
```

---

## 🧩 Modules

<details closed><summary>.</summary>

| File                                                                                 | Summary                                                                                                                                                                                                                            |
| ---                                                                                  | ---                                                                                                                                                                                                                                |
| [scrapy.py](https://github.com/shivatmax/Scrapy/blob/master/scrapy.py)               | This script is Scrapy's interactive front-end, using Streamlit to input job search parameters and trigger a scraping process, which aggregates job listings from multiple sites (excluding Indeed) and outputs them to a CSV file. |
| [requirements.txt](https://github.com/shivatmax/Scrapy/blob/master/requirements.txt) | This `requirements.txt` defines dependencies for a web scraping application within the Scrapy repository, ensuring the necessary libraries are installed for parsing HTML, data manipulation, and web interaction.                 |

</details>

<details closed><summary>Scrappy.scrapers</summary>

| File                                                                                            | Summary                                                                                                                                                                                                                                                                     |
| ---                                                                                             | ---                                                                                                                                                                                                                                                                         |
| [exceptions.py](https://github.com/shivatmax/Scrapy/blob/master/Scrappy/scrapers/exceptions.py) | Defines custom exceptions for each scraper module within the Scrapy framework, handling errors specific to LinkedIn, Indeed, ZipRecruiter, and Glassdoor integrations.                                                                                                      |
| [utils.py](https://github.com/shivatmax/Scrapy/blob/master/Scrappy/scrapers/utils.py)           | This code provides utility functions supporting text processing for a web scraper module, designed to accommodate features like urgency detection in job descriptions, email extraction, network session customization, job type enumeration, and precise currency parsing. |

</details>

---

## 🚀 Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

### ⚙️ Installation

1. Clone the Scrapy repository:

```sh
git clone https://github.com/shivatmax/Scrapy
```

2. Change to the project directory:

```sh
cd Scrapy
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

### 🤖 Running Scrapy

Use the following command to run Scrapy:

```sh
streamlit run main.py
```


---


## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/shivatmax/Scrapy/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/shivatmax/Scrapy/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/shivatmax/Scrapy/issues)**: Submit bugs found or log feature requests for Scrapy.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/shivatmax/Scrapy
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

---
