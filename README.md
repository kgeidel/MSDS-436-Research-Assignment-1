<div align=center>
RESEARCH ASSIGNMENT #1:  <br>
A COMPETITIVE REVIEW OF AI IN THE MARKETPLACE
</div>
<br>

<div align=center>

Kevin Geidel <br>
MSDS 436: Analytics Systems Engineering <br>
Northwestern University <br>
October 13, 2024 <br>
</div>
<br>
</p>

### Research objectives

<hr>

* *"...learn more about the application of AI within corporate information infrastructure, specifically focusing on leaders and emerging players in this field."*
* *...the current landscape, emerging technologies, and new growth opportunities, with a focus on financial services."* 
* *"...to what extent other financial services firms utilize AI.* 
* *"...insights into existing players, emerging technologies, and potential growth areas in AI for financial services."*

### Installing/replication/running analysis

<hr>

Must include instructions for forking, setting up and running any examples, demos, experiments, etc...

### Research methods

<hr>

* Google Scholar was utilized to perform a literature review on articles regarding Artificial Intelligence (AI) and its use in corporate information infrastructure. Search criteria, search terms and article selection were tailored to focus on the research objectives.

* **scrapy** was used in a proof of concept deployment of a web scraper that could crawl internet search results and collect targeted content. Article meta data was programmatically collected from CODATA.org's *Data Science Journal* (2024) and stored in a local (desktop environment) file as JSON.

### Research results

<hr>

* AI platforms do not, for all intents and purposes, exist independent of the 'big tech' corporate entities that have become synonymous with these technologies (van der Vlist, Helmond and Ferrari 2024). The implications of this is that any new AI or cloud based product is likely to require infrastructure from one of the large firms. This is not an obstacle to technology product development (and in some ways is a catalyst) but must be kept in mind when considering cost, threat of competition and capabilities.

* AI conversational assistants (i.e. "chatbots") represent billions of dollars in cost savings to corporations (Bavaresco et al. 2020). The most popular chatbots include ChatGPT, Laxis, Otter, Fireflies, Siri, Cortana, Alexa and Google Assistant (McFarland 2024). While these tools are already in use in many organizations, including corporations, there are privacy, security and compliance risks that must be considered and mitigated (Bhardwaj et al. 2024). Samsung, for example, experienced multiple leaks of proprietary information within weeks of allowing their engineers to use ChatGPT (Powell 2023). The concerns around ChatGPT's adherence to the European Union's General Data Protection Regulation (*GDPR*) caused the Italian government to ban its use while measures can be put in place to prevent the mining of private data (Ibid). I know from my own work experience that some large companies are hosting their own models, on their own infrastructure, in an attempt to leverage Natural Language Processing (*NLP*) and generative AI techniques while maintaining control over their data. This may address some of the concerns surrounding the use of chatbots in a corporate settings but there are trade offs including cost and performance.

* Financial technology (*fintech*) is incorporating AI with several goals in mind. These include matching products with customers, managing risk and increasing efficiency (Topçu 2023). This is a promising indicator of market opportunities in this sector.

* Financial services providers are already using AI to provide security as well. Ghenescu et al. (2020) describes a system that uses AI to monitor, not only financial transactions for suspicious behavior, but integrates physical systems including on-premises video surveillance to create a comprehensive "Financial Security" (*FINSEC*) gateway. 

* The firms that are taking the lead in this space have technologically "savvy" leadership, up to and including (most importantly) the board of directors (Torre, Teigland, and Engstam 2019). According to U.S. News (Duggan 2024) the top, publicly traded, AI firms include Microsoft, NVIDIA, Alphabet (Google), Amazon and Meta. The conclusions reached by Torre, Teigland and Engstam seem to hold true in the light of actual industry data.

* **scrapy** can be used to extract records from a variety of websites (*"A Fast and Powerful Scraping..."* 2024). There are some caveats however. While experimenting with the package I have discovered:

   * Scraping relies heavily on element and CSS class names. These are not always sufficient to select and extract specific information in a programmatic way. In some cases, websites may randomly/dynamically generate these to prevent scraping. This means there may be websites that are difficult to scrap, requiring more time than available (if we can at all.)
   * This will be nearly impossible to abstract. Each data source (website) will likely need a custom scrapy "spider" tailored to that site's layout. We can overcome this limitation by focusing on a small number of sites with lots of records (journals, Google Scholar, search engines, etc.)
   * The documentation is fairly well written, however they use extremely rosy examples (i.e. websites built with web scraping in mind and very verbose CSS class names that classify the text they wrap very purposefully.) This means implementation details (including required programming time) will not be fully known until we try to deploy this package for our own use case.

#### Porter's Five Forces

Relevant market factors...

#### "Supplier Power"

Software dependencies, etc...

#### "Threat of Entry"

Particularly the double edge sword of ubiquitous, affordable cloud resources...

#### Substitutes

AI and conventional replacements/alternatives...

### References

<hr>

<div style="padding-left: 1.5em; text-indent:-1.5em;">

“A Fast and Powerful Scraping and Web Crawling Framework.” Scrapy. Accessed October 8, 2024. https://scrapy.org/. 

Bavaresco, Rodrigo, Diórgenes Silveira, Eduardo Reis, Jorge Barbosa, Rodrigo Righi, Cristiano Costa, Rodolfo Antunes et al. "Conversational agents in business: A systematic literature review and future research directions." Computer Science Review 36 (2020): 100239.

Bhardwaj, Vivek, Balwinder Kaur Dhaliwal, Sanjaya Kumar Sarangi, T. M. Thiyagu, Aruna Patidar, and Divyam Pithawa. "Conversational AI: Introduction to Chatbot's Security Risks, Their Probable Solutions, and the Best Practices to Follow." Conversational Artificial Intelligence (2024): 435-457.

Data Science Journal. Accessed October 8, 2024. https://datascience.codata.org/. 

Duggan, Wayne. Artificial Intelligence Stocks: The 10 best AI companies | investing | U.S. news. Accessed October 8, 2024. https://money.usnews.com/investing/articles/artificial-intelligence-stocks-the-10-best-ai-companies. 

Ghenescu, Marian, Serban Carata, Roxana Mihaescu, and Sabin Floares. "Artificial Intelligence Gateway for Cyber-physical Security in Critical Infrastructure and Finance." (2020): 53.

McFarland, Alex. “10 Best AI Assistants (October 2024).” Unite.AI, October 3, 2024. https://www.unite.ai/10-best-ai-assistants/. 

Powell, Olivia. “Samsung Employees Allegedly Leak Data via CHATGPT.” Cyber Security Hub, August 29, 2023. https://www.cshub.com/data/news/iotw-samsung-employees-allegedly-leak-proprietary-information-via-chatgpt. 

Topçu, Güneş. "Impact of Artificial Intelligence on the Infrastructure of Financial Centers: Transforming Financial Operations with Advanced Technologies." AI Renaissance (2023): 1.

Torre, Fernanda, Robin Teigland, and Liselotte Engstam. "7 AI leadership and the future of corporate governance." The digital transformation of labor (2019): 116.

van der Vlist, F., Helmond, A., & Ferrari, F. (2024). Big AI: Cloud infrastructure dependence and the industrialization of artificial intelligence. Big Data & Society, 11(1). https://doi.org/10.1177/20539517241232630


</div>