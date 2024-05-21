<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
 

  <h3 align="center">Edmonton Property Valuation</h3>

  <p align="center">
    An advanced project for predicting property prices in Edmonton, AB.
    <br />
    <a href="https://github.com/OgSamu/Edmonton-Property-Valuation"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="[https://github.com/OgSamu/Edmonton-Property-Valuation](https://youtu.be/3_5aeFjkNSw)">View Demo</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project


I designed this project to help predict house prices in Edmonton, by leveraging historical data and machine learning techniques, more specifically a ridge regression model . 

The primary objectives was to forecast house future prices through historical features and inflation adjustments. 
To better improve this model, I could add more features such as proximity to school parks etc and add some interaction features that could show show a more complex relationship and effect on house prices. Furthermore, with more features, I could utilize Gradient Boosting Machines to capture more complex relationships.  
## Built With

This section lists the major frameworks and libraries used to bootstrap the project. Here are the ones used in this project:

* [![Python][Python]][Python-url]
* [![Flask][Flask]][Flask-url]
* [![Scikit-learn][Scikit-learn]][Scikit-learn-url]
* [![Pandas][Pandas]][Pandas-url]
* [![Next.js][Next.js]][Next-url]
* [![Tailwind CSS][Tailwind]][Tailwind-url]

[Python]: https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/
[Scikit-learn]: https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white
[Scikit-learn-url]: https://scikit-learn.org/
[Pandas]: https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[Tailwind]: https://img.shields.io/badge/TailwindCSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white
[Tailwind-url]: https://tailwindcss.com/


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 3.9+
* npm
  ```sh
  npm install npm@latest -g

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/OgSamu/Edmonton-Property-Valuation.git
   ```
2. Set up the virtual environment
   ```sh
   python -m venv .venv
   source .venv/bin/activate   # On Windows, use `.venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Run the Flask app
   ```sh
   flask run
   ```
4. Navigate to the `frontend` directory and install NPM packages
   ```sh
   cd frontend
   npm install
   ```
5. Run the Next.js development server
   ```sh
   npm run dev
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

To use the application, navigate to the front-end interface and enter the required property details to get the predicted price. The back-end Flask API processes the input data, performs the prediction, and adjusts the price for inflation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Adjust predictions for inflation
- [ ] Incorporate additional data sources
- [ ] Explore advanced models like Random Forests and Gradient Boosting
- [ ] Integrate real-time data feeds

See the [open issues](https://github.com/OgSamu/Edmonton-Property-Valuation/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Ogo Samuel - [LinkedIn](https://www.linkedin.com/in/ogo-samuel/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/OgSamu/Edmonton-Property-Valuation/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/OgSamu/Edmonton-Property-Valuation/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/OgSamu/Edmonton-Property-Valuation/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/OgSamu/Edmonton-Property-Valuation/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/OgSamu/Edmonton-Property-Valuation/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ogo-samuel
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Flask]: https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=fl
