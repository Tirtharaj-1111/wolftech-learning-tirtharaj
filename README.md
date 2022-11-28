# wolftech-learning-tirtharaj
<p>1. text-json-csv project shows reading and writing to and from text,json files<br>
<p>2. Currently studying scrapy, venv, postman, web-scraping basics, APIs. My aim is to create a composite multiconceptual project that includes Python concepts, scraping work and also writing the obtained output to a text,json and csv file. I wish to divide this project into 2 parts: html-scraping and api-scraping<br>
  2a. Installed scrapy in virtual env using Anaconda -> python -m venv scrapyvenv (Open Anaconda -> cd directory -> run command)<br>
  2b. scrapyvenv\Scripts\Activate<br>
  2c. scrapyvenv scripts issue: scrapyvenv\Scripts\Activate : File E:\Wolftech\wolftech-learning-tirtharaj\scraping-project\scrapyvenv\Scripts\Activate.ps1 cannot be loaded because running 
scripts is disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
  2d. set-ExecutionPolicy RemoteSigned -Scope CurrentUser -> Get-ExecutionPolicy -> Get-ExecutionPolicy -list <br>
  2e. scrapy startproject onescrape -> cd onescrape -> create spider -> use for loop and return<br>
  2f. use for loop and yield<br>
  2g. use for loop and print a dictionary<br> (similar to 2f but doesnt show response code)
  2h. use items container to store in a better format<br>
  2i. export to json,csv<br>
</p>
<p>3. MySQL Workbench installation and multi-conceptual exercise</p>
<p>4. Scraped usk-wroc.logintrade.net</p>
<p>5. Scraped zsm-czest.logintrade.net but pagination is not working</p>
<p>6. Scraped https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_2?ie=UTF8&pg=1 but pagination is not working</p>
   6b.Scraped https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_2?ie=UTF8&pg=1 with pagination (Reference used: https://www.youtube.com/watch?v=C2w18Wou3aU)
<p>7. data-science-adv-python project to demonstrate pandas features to read, export and deal with datasets.</p>
<p>8. Imported the medical_table made in data-science-adv-python project into SQL and then reimported into Pandas dataframe to be exported as json/csv/xlsx</p>
<p>9. Accessed jsonplaceholder REST API, made GET,POST,PUT requests to the API to get data from the underlying web service. Created a table out of the response json data</p>
