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

### Installing and running the scrapy experiment

<hr>

The following instructions will allow you to replicate the scrapy experiment. These instructions are how I would run this on Linux. A Unix terminal on a Mac should be similar. More modifications may be needed to run this on Windows.



### Research methods

<hr>

* Google Scholar was utilized to perform a literature review on articles regarding Artificial Intelligence (AI) and its use in corporate information infrastructure. Search criteria, search terms and article selection were tailored to focus on the research objectives.

* **scrapy** was used in a proof of concept deployment of a web scraper that could crawl internet search results and collect targeted content. Article meta data was programmatically collected from CODATA.org's *Data Science Journal* (2024) and stored in a local (desktop environment) file as JSON.

### Research results

<hr>

* AI platforms do not, for all intents and purposes, exist independent of the 'big tech' corporate entities that have become synonymous with these technologies (van der Vlist, Helmond and Ferrari 2024). The implications of this is that any new AI or cloud based product is likely to require infrastructure from one of the large firms. This is not an obstacle to technology product development (and in some ways is a catalyst) but must be kept in mind when considering cost, threat of competition and capabilities.

* AI conversational assistants (i.e. "chatbots") represent billions of dollars in cost savings to corporations (Bavaresco et al. 2020). The most popular chatbots include ChatGPT, Laxis, Otter, Fireflies, Siri, Cortana, Alexa and Google Assistant (McFarland 2024). While these tools are already in use in many organizations, including corporations, there are privacy, security and compliance risks that must be considered and mitigated (Bhardwaj et al. 2024). Samsung, for example, experienced multiple leaks of proprietary information within weeks of allowing their engineers to use ChatGPT (Powell 2023). The concerns around ChatGPT's adherence to the European Union's General Data Protection Regulation (*GDPR*) caused the Italian government to ban its use while measures could be put in place to prevent the mining of private data (Ibid). I know from my own work experience that some large companies are hosting their own models, on their own infrastructure, in an attempt to leverage Natural Language Processing (*NLP*) and generative AI techniques while maintaining control over their data. This may address some of the concerns surrounding the use of chatbots in a corporate settings but there are trade offs including cost and performance.

* Financial technology (*fintech*) is incorporating AI with several goals in mind. These include matching products with customers, managing risk and increasing efficiency (Topçu 2023). This is a promising indicator of market opportunities in this sector.

* Financial services providers are already using AI to provide security as well. Ghenescu et al. (2020) describes a system that uses AI to monitor, not only financial transactions for suspicious behavior, but integrates physical systems including on-premises video surveillance to create a comprehensive "Financial Security" (*FINSEC*) gateway. 

* The firms that are taking the lead in this space have technologically "savvy" leadership, up to and including (most importantly) the board of directors (Torre, Teigland, and Engstam 2019). According to U.S. News (Duggan 2024) the top, publicly traded, AI firms include Microsoft, NVIDIA, Alphabet (Google), Amazon and Meta. The conclusions reached by Torre, Teigland and Engstam seem to hold true in the light of actual industry data.

* **scrapy** can be used to extract records from a variety of websites (*"A Fast and Powerful Scraping..."* 2024). There are some caveats however. While experimenting with the package I have discovered:

   * Scraping relies heavily on element and CSS class names. These are not always sufficient to select and extract specific information in a programmatic way. In some cases, websites may randomly/dynamically generate these to prevent scraping. This means there may be websites that are difficult to scrap, requiring more time than available (if we can at all.)
   * This will be nearly impossible to abstract. Each data source (website) will likely need a custom scrapy "spider" tailored to that site's layout. We can overcome this limitation by focusing on a small number of sites with lots of records (journals, Google Scholar, search engines, etc.)
   * The documentation is fairly well written, however they use extremely rosy examples (i.e. websites built with web scraping in mind and very verbose CSS class names that classify the text they wrap very purposefully.) This means implementation details (including required programming time) will not be fully known until we try to deploy this package for our own use case.

### Porter's Five Forces Analysis

A situational analysis of a potential business opportunity, Porter's Five Forces are competition, barriers to entry, supply chain considerations ("supplier power"), customer power and availability of substitutes (Gratton 2024). 

#### Competition

* The management problem described in the prompt indicates our organization is interested in developing new AI based financial products. There has been an explosion in the number and variety of "fintech" products (Nagl 2023). Firms in this space offer digital payment services, mobile banking, financial management platforms (i.e. Copilot, Mint, etc.), AI financial advisors (WealthFront, Betterment, etc.) and digital self-serve insurance applications. This suggests there is much competition in this space.

* The number of competitors should be balanced with the growth of the sector. Market researchers (Podorozhko 2024) point to four main reasons for the surging investment and size of fintech. These include advancing technology, crystallizing government regulations, developing trust from customers and an overall growing maturity of the sector as a whole. 

* In my opinion, a new technology product with a good or novel value proposition will be able to overcome competitive rivals.

#### "Threat of Entry"

* The greatest barriers to entry in the fintech space are government regulations for firms that meet certain criteria ("*Fintech: Strategic Advantages and...*" 2024). Capital startup costs are relatively low given the recent ubiquity of cloud based infrastructure services (Fong et al. 2021).

* Additional factors catalyzing entrants into fintech include "no-code" application development, IoT technologies becoming pervasive, popularity of block chain and the surge of funding for AI tools (Ibid).

#### "Supplier Power"

* As described above, a new technology product will be dependent on a small number of Infrastructure as a Service (IaaS) providers (AWS, Azure, Google Cloud, Rumble Cloud, etc.) 

* As described above, the high potential for new participants means products will have to be unique and/or develop strong branding.

* As cited above, the popularity and importance of these technologies is on the rise, increasing demand and, therefore, the power of individual suppliers.

#### "Customer Power"

* As cited above, the increase in demand represents an influx of customers. This lowers the pull of individual consumers. The small number of providers means rigid prices and less options for customers.

* The trends outlined above (growing numbers of firms, lowering costs, etc) mean customer power could grow in the future as fintech matures.

#### Substitutes

* For our new technology product to be viewed as a viable substitute for our competitor's platforms we need to exploit the price insensitivity described above. 

* A product that is perceived as similar can also be a substitute.

### References

<hr>

<div style="padding-left: 1.5em; text-indent:-1.5em;">

“A Fast and Powerful Scraping and Web Crawling Framework.” Scrapy. Accessed October 8, 2024. https://scrapy.org/. 

Bavaresco, Rodrigo, Diórgenes Silveira, Eduardo Reis, Jorge Barbosa, Rodrigo Righi, Cristiano Costa, Rodolfo Antunes et al. "Conversational agents in business: A systematic literature review and future research directions." Computer Science Review 36 (2020): 100239.

Bhardwaj, Vivek, Balwinder Kaur Dhaliwal, Sanjaya Kumar Sarangi, T. M. Thiyagu, Aruna Patidar, and Divyam Pithawa. "Conversational AI: Introduction to Chatbot's Security Risks, Their Probable Solutions, and the Best Practices to Follow." Conversational Artificial Intelligence (2024): 435-457.

Data Science Journal. Accessed October 8, 2024. https://datascience.codata.org/. 

Duggan, Wayne. Artificial Intelligence Stocks: The 10 best AI companies | investing | U.S. news. Accessed October 8, 2024. https://money.usnews.com/investing/articles/artificial-intelligence-stocks-the-10-best-ai-companies. 

“Fintech: Strategic Advantages and Initial Costs for Entry into Banking.” Deloitte United Kingdom. Accessed October 9, 2024. https://www.deloitte.com/be/en/Industries/financial-services/research/fintech-strategic-advantages-and-initial-costs-for-entry-into-b.html. 

Fong, Dick, Feng Han, Louis Liu, John Qu, and Arthur Shek. “Seven Technologies Shaping the Future of Fintech: Greater China.” McKinsey & Company, November 9, 2021. https://www.mckinsey.com/cn/our-insights/our-insights/seven-technologies-shaping-the-future-of-fintech. 

Ghenescu, Marian, Serban Carata, Roxana Mihaescu, and Sabin Floares. "Artificial Intelligence Gateway for Cyber-physical Security in Critical Infrastructure and Finance." (2020): 53.

Gratton, Peter. “Porter’s Five Forces Explained and How to Use the Model.” Investopedia. Accessed October 9, 2024. https://www.investopedia.com/terms/p/porter.asp. 

McFarland, Alex. “10 Best AI Assistants (October 2024).” Unite.AI, October 3, 2024. https://www.unite.ai/10-best-ai-assistants/. 

Nagl, Steph. “5 Fintech Examples Transforming Everyday Life.” School of Professional Studies at Wake Forest University, December 5, 2023. https://sps.wfu.edu/articles/fintech-examples-transforming-everyday-life/. 

Podorozhko, Yuliia. “Web and Mobile App Development Company.” Madappgang website. Accessed October 9, 2024. https://madappgang.com/blog/why-fintech-is-growing/. 

Powell, Olivia. “Samsung Employees Allegedly Leak Data via CHATGPT.” Cyber Security Hub, August 29, 2023. https://www.cshub.com/data/news/iotw-samsung-employees-allegedly-leak-proprietary-information-via-chatgpt. 

Topçu, Güneş. "Impact of Artificial Intelligence on the Infrastructure of Financial Centers: Transforming Financial Operations with Advanced Technologies." AI Renaissance (2023): 1.

Torre, Fernanda, Robin Teigland, and Liselotte Engstam. "7 AI leadership and the future of corporate governance." The digital transformation of labor (2019): 116.

van der Vlist, F., Helmond, A., & Ferrari, F. (2024). Big AI: Cloud infrastructure dependence and the industrialization of artificial intelligence. Big Data & Society, 11(1). https://doi.org/10.1177/20539517241232630


</div>