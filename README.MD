# Web scraper TopLearn

 A web scraper using BeautifulSoup and request to scrap [TopLearn](https://toplearn.com/) and save lectur titles of a course to a txt file.
 # Description
In this project,I used request library to get the data from the site,then use the BeautifulSoup library to use the html data of site.Next using html tags and classes find the data that I want,wich in this case is the title of lecturs.

Finaly store the titles in a list and write them in a txt file to save the data.

### Dependencies
 * bs4
 * requests

### Executing program
Copy the link of cours and paste it to variable 'url' and than run the program.after scraping the page the result will save in a txt file.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.

*  Fork the repository. Create your feature branch:
    ```
    git checkout -b feature/YourFeature
    ```
*  Commit your changes:
    ```
    git commit -m 'Add some feature'
    ```

*  Push to the branch:
    ```
    git push origin feature/YourFeature
    ```
Open a pull request. And done :)
