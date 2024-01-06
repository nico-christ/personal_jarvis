# personal_jarvis
Personal_Jarvis

**!!! The voice_reg_experimental does not work !!!**
Please use the voice_reg instead.
Working on it.


## Speech Recognition Project

This project utilizes the SpeechRecognition library in Python for speech recognition on audio files. It includes functionality to record audio, recognize speech using different engines, and provides a modular structure for easy customization.

## Getting Started

### Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Install spaCy](#install-spacy)
        - [Download spaCy Models](#download-spacy-models)
        - [Getting Started](#getting-started)
        - [Additional Resources](#additional-resources)
3. [Contributing](#contributing)
4. [License](#license)

### Prerequisites

- Python 3.x
- SpeechRecognition library (`pip install SpeechRecognition`)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://https://github.com/nico-christ/personal_jarvis.git
   cd personal_jarvis
   ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

1. # spaCy Installation Guide

    ### Introduction

    [spaCy](https://spacy.io/) is an open-source natural language processing library for Python designed to be fast and efficient. It provides pre-trained models for various languages and allows for easy integration into natural language processing workflows.

    This guide will walk you through the installation process of spaCy and how to set it up for your Python projects.

    ### Installation

    #### Prerequisites

    Before installing spaCy, make sure you have the following prerequisites:

    - Python (>=3.6)

    #### Install spaCy

    You can install spaCy using `pip`, the Python package installer. Open your terminal or command prompt and run:

    ## spaCy Installation Guide

    1. ### Download spaCy Models

        ```bash
        pip install spacy
        ```


        After installing spaCy, you'll need to download language models for the specific language(s) you intend to work with. spaCy provides various pre-trained models for different languages.

        ```bash
        python -m spacy download <language_model>
        ```

    2. ### To download a model:
        ```bash
        python -m spacy download <language_model>
        ```

        Replace `<language_model>` with the specific model you want to download. For example, we use the english model:

        ```bash
        python -m spacy download en_core_web_md
        ```

    ## Additional Resources

    - [spaCy Documentation](https://spacy.io/usage)
    - [spaCy GitHub Repository](https://github.com/explosion/spaCy)
    - [spaCy Models](https://spacy.io/models)


## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the **LICENSE** file for details
