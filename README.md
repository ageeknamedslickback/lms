<!-- Improved compatibility of back to top link -->

<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->

[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Smart Maktaba Library Management System</h3>

  <p align="center">
    A library management system is software built to handle the primary housekeeping functions of a library. The purpose of a library management system is to operate 
    a library with efficiency and at reduced costs. Library activities include 
    purchasing books, cataloguing, indexing books, recording books in circulation and 
    stock checking, which when done by automated software eliminates the need for 
    repetitive manual work and minimizes the chances of errors. Smart Maktaba LMS is such a system.
    <br />
    <a href="https://github.com/ageeknamedslickback/smart-maktaba-lms"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/ageeknamedslickback/smart-maktaba-lms/issues">Report Bug</a>
    ·
    <a href="https://github.com/ageeknamedslickback/smart-maktaba-lms/issues">Request Feature</a>
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
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

The project is a simple Custom Odoo Library Management System module, that is not only a POC on the
capabilities of the Odoo Framework but a simple, fun and functional project to work on and use.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [![Odoo][odoo-python]][odoo-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Here is a list things you need to use the software and how to install them.

- git

  ```sh
  sudo apt install git
  ```

- odoo

  ```sh
  mkdir -p $HOME/src
  cd $HOME/src
  git clone git@github.com:odoo/odoo.git
  ```

- postgresql
  ```sh
  sudo apt install postgresql postgresql-client
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/ageeknamedslickback/smart-maktaba-lms.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = "ENTER YOUR API";
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

The project can be used as a school project or a POC to a production grade custom LMS.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [x] Library managment and multi-tenancy
- [x] Books and book-items management
- [x] Library members management

See the [open issues](https://github.com/ageeknamedslickback/smart-maktaba-lms/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

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

Kenneth Mathenge - [Email Me](ken.mathenge@gmail.com)

Project Link: [https://github.com/ageeknamedslickback/smart-maktaba-lms](https://github.com/ageeknamedslickback/smart-maktaba-lms)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- [Odoo Official Documentation](https://www.odoo.com/documentation/16.0/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/ageeknamedslickback/smart-maktaba-lms/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/ageeknamedslickback/smart-maktaba-lms/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/kenmathenge
[product-screenshot]: images/screenshot.png
[odoo-python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[odoo-url]: https://www.odoo.com/documentation/16.0/
